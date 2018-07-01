import textract
import os
import io
from apiclient.http import MediaIoBaseDownload
from apiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

def service_setup():
    SCOPES = 'https://www.googleapis.com/auth/drive'
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('drive', 'v3', http=creds.authorize(Http()))
    return service

def folderid_from_foldername(foldername, service):
    page_token = None
    results = service.files().list(
        q="name='{}'".format(foldername),
        spaces="drive",
        fields="nextPageToken, files(id, name)",
        pageToken=page_token).execute()

    items = results.get('files', [])
    if not items:
        print('Folder not found!')
        raise Exception
    else:
        if len(items) > 1:
            print("Too many folders called {}!".format(foldername))
            raise Exception
        return items[0]["id"]

def files_from_folderid(folderid, service):
    # Return a list of all (filename, fileid) pairs in the specified folderid
    page_token = None
    results = service.files().list(
        q="'{}' in parents and ".format(folderid) + 
            "mimeType!='application/vnd.google-apps.folder'",
        spaces="drive",
        fields="nextPageToken, files(id, name)",
        pageToken=page_token).execute()

    items = results.get('files', [])
    if not items:
        print('No files found.')
        return -1
    else:
        return [(item["name"], item["id"]) for item in items]

def create_output_folder(folderid, files, service):
    if "Textified Documents"  in [x[0] for x in files]:
        return
    out_folder_metadata = {
        "name": "Textified GOVREPORTs",
        "parents": [folderid],
        "mimeType": "application/vnd.google-apps.folder"
    }
    output_folder = service.files().create(
        body=out_folder_metadata,
        fields="id").execute()
    return output_folder

def create_intermediate_working_folder():
    if not os.path.exists("workingdir"):
        os.makedirs("workingdir")

def download_file_from_id(fileid, filename, service):
    request = service.files().get_media(fileId=fileid)
    fh = io.FileIO("workingdir/{}".format(filename), "wb")
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()

def upload_text_from_file(filename, output_folderid, service,
                          segment=0):
    if "GOVREPORT" not in filename.split("_"):
        return
    text = textract.process("workingdir/{}".format(filename))
    text = text.decode("utf-8").split()

    if segment:
        text = [text[i:i+segment] for i in (
          range(0, len(text), segment))]
    else:
        text = [text]

    for ix, seg in enumerate(text):
        new_filename = filename.replace(".pdf", ".txt")
        new_filename = new_filename.replace(
          ".txt", "_{}_{}.txt".format(ix+1, len(text)))
        out = open("workingdir/{}".format(new_filename), "w+")
        out.write(" ".join(seg))
        out.close()

        file_metadata = {
            "name": new_filename,
            "parents": [output_folderid]
        }
        media = MediaFileUpload("workingdir/" + new_filename,
                                mimetype="text/plain",
                                resumable=True)
        upfile = service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields="id").execute()
        print("File {}: {}".format(new_filename, upfile.get("id")))

def remove_intermediate_working_folder():
    for to_remove in os.listdir("workingdir"):
        file_path = os.path.join("workingdir/{}".format(to_remove))
        if os.path.isfile(file_path):
            os.remove(file_path)
    os.rmdir("workingdir")

def main():
    service = service_setup()
    folderid = folderid_from_foldername("toTextifyy", service)
    files = files_from_folderid(folderid, service)
    output_folder = create_output_folder(folderid, files, service)
    create_intermediate_working_folder()
    for filename, fileid in files:
        if "GOVREPORT" in filename.split("_"):
            print("Now processing file {}, id {}".format(filename, fileid))
            try:
                download_file_from_id(fileid, filename, service)
                print("Uploading...")
                upload_text_from_file(filename, output_folder["id"], service, segment=600)
            except (HttpError, TypeError, UnicodeDecodeError):
                print("Error. Ignoring...")
    print("Cleaning up...")
    remove_intermediate_working_folder()
    print("Done!")

if __name__ == "__main__":
    main()

