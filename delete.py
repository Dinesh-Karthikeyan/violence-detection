import os
import argparse

def deleteFiles(folderName, prefix):
    filesList = os.listdir(path=folderName)
    for fileName in filesList:
        if fileName[:2] == '._':
            os.remove(os.path.join(folderName, fileName))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='to delete all the files starting with particular prefix')
    parser.add_argument('folder_name', type=str, help='Enter the name of the folder')
    parser.add_argument('--prefix', type=str, help='Enter the prefix of the filename', default='')
    args = parser.parse_args()

    deleteFiles(args.folder_name, args.prefix)