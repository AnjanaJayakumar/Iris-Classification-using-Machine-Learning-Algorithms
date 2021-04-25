# Import OS for navigation and environment set up
import os
from zipfile import ZipFile

import subprocess

def download_and_unzip(drive_path, extract_path, kaggle_api, folder_name):
    # Navigate into Drive where you want to store your Kaggle data
    os.chdir(drive_path)

    # Extract the dataset information from the kaggle api
    kaggle_data = kaggle_api.split(' ')[-1]

    # get the name of the zip file and the new folder to be created
    zip_name = kaggle_data.split('/')[-1] + '.zip'

    # check if the zip file exists before downloading the data
    if (os.path.exists(zip_name)):
        print('[INFO]: The file "', zip_name, '" already exists in the given folder.')
        print('Would you like to force download the file again?')
        print('[NOTE]: Force download will replace the existing zipfile in your folder. ')
        print('(Y / N) : ', end='')
        ans = input().upper()
        if (ans == 'Y'):
            # Run the copied API command. The dataset will be downloaded to the specified directory
            subprocess.call(['kaggle','datasets','download','-d',kaggle_data,'--force'], shell=True)
            print('Downloaded the dataset from Kaggle and replaced the file in the destination...')
        else:
            print('Skipped download from Kaggle...')
    else:
        # Run the copied API command. The dataset will be downloaded to the specified directory
        subprocess.call(['kaggle','datasets','download','-d',kaggle_data], shell=True)
        print('Downloaded the dataset from Kaggle...')


    # Extract the contents
    with ZipFile(zip_name, 'r') as zipObj:
        # specify the path
        dir_name = extract_path + '/' + folder_name.capitalize()
        # check if the folder exists or create a new folder
        if os.path.exists(dir_name):
            # check if it contains the same files as the ones to be extracted
            listOfFiles = zipObj.namelist()
            duplicateCount = 0
            for fileName in listOfFiles:
                if os.path.exists(dir_name + '/'+ fileName):
                    duplicateCount += 1
            if (duplicateCount == len(listOfFiles)):
                print('\n[NOTE]: The file(s) to be extracted already exists in the destination folder')
                print('Would you like to replace them? ')
                print('(Y / N): ', end='')
                ans = input().upper()
                if (ans == 'Y'):
                    # Extract the contents of zip file in different directory
                    fileExtract(dir_name, zipObj)
            else:
                # Extract the contents of zip file in different directory
                fileExtract(dir_name, zipObj)
        else: 
            os.mkdir(dir_name)
            # Extract the contents of zip file in different directory
            fileExtract(dir_name, zipObj)
    print('ALL DONE!')
        

        
def fileExtract(extract_path, zipObj):
    zipObj.extractall(extract_path+'/')
    print('Extracted successfully.')

