import os
from kaggle.api.kaggle_api_extended import KaggleApi



def download_kaggle_dataset(dataset_name, destination_folder):
    """
    Download a Kaggle dataset to the specified destination folder.
    
    :param dataset_name: The name of the Kaggle dataset (e.g., 'zillow/zecon').
    :param destination_folder: The folder where the dataset will be downloaded.
    """
    api = KaggleApi()
    api.authenticate()
    
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    api.dataset_download_files(dataset_name, path=destination_folder, unzip=True)
    print(f"Dataset {dataset_name} downloaded and extracted to {destination_folder}.")


