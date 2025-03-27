import os
import gdown
import zipfile

def download_dataset(file_id, output_path):
    """
    Downloads the dataset zip file from Google Drive.
    
    Parameters:
    - file_id (str): The Google Drive file ID.
    - output_path (str): The local file path to save the downloaded file.
    """
    # Construct the download URL
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, output_path, quiet=False)

def unzip_dataset(zip_path, extract_to):
    """
    Unzips the downloaded dataset.
    
    Parameters:
    - zip_path (str): The path to the zip file.
    - extract_to (str): The directory to extract the contents.
    """
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def main():
    # Create the /data folder if it doesn't exist
    data_dir = "data"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    # Define the path for the downloaded zip file
    zip_file_path = os.path.join(data_dir, "dataset.zip")
    
    file_id = "1CSE8i-0ICeb9g3Dro5fumqik-rai3x99"
    
    # Download the dataset only if it doesn't already exist
    if not os.path.exists(zip_file_path):
        print("Downloading dataset...")
        download_dataset(file_id, zip_file_path)
    else:
        print("Dataset already downloaded.")
    
    # Optionally, unzip the dataset if it's not already extracted
    extracted_folder = os.path.join(data_dir, "dataset")
    if not os.path.exists(extracted_folder):
        print("Unzipping dataset...")
        unzip_dataset(zip_file_path, data_dir)
        print("Dataset unzipped.")
    else:
        print("Dataset already extracted.")

if __name__ == "__main__":
    main()
