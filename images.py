import os
import zipfile
from google.oauth2 import service_account  # type: ignore
from googleapiclient.discovery import build  # type: ignore
from googleapiclient.http import MediaFileUpload  # type: ignore


SERVICE_ACCOUNT_FILE = 'service_account.json'
SCOPES = ['https://www.googleapis.com/auth/drive']
PARENT_FOLDER_ID = "1HCRaO8H9gDNkjE1zFU-3GqGohm3HLSlA"

def compress_files_to_zip(input_folder, output_folder):
    """Compress each file in the input folder into a separate zip file in the output folder."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        if os.path.isfile(file_path):
            zip_file_path = os.path.join(output_folder, f"{filename}.zip")
            with zipfile.ZipFile(zip_file_path, 'w') as zipf:
                zipf.write(file_path, arcname=filename)
            print(f"Compressed {filename} into {zip_file_path}")
        else:
            print(f"Skipping {file_path}, not a file.")

def authenticate():
    """Authenticate and return the Google Drive service."""
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds

def upload_to_drive(file_path):
    """Upload a file to Google Drive."""
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {
        'name': os.path.basename(file_path),
        'parents': [PARENT_FOLDER_ID]
    }
    media = MediaFileUpload(file_path, resumable=True)
    file = service.files().create(
        body=file_metadata,
        media_body=media
    ).execute()
    print(f"Uploaded {file_path} to Google Drive")
if __name__ == '__main__':

    input_folder = r'E:\Pictures 1-1000\Images'
    output_folder = r'C:\Users\dell\Desktop\Zipfile\ZipFile'
    
   
    
    compress_files_to_zip(input_folder, output_folder)
    
  
    for filename in os.listdir(output_folder):
        file_path = os.path.join(output_folder, filename)
        if os.path.isfile(file_path):
            upload_to_drive(file_path)