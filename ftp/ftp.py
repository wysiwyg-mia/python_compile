from ftplib import FTP, all_errors
import os

def upload(path):
    try:
        with FTP(host='', user='', passwd='') as ftp:
            print(ftp.getwelcome())

            with open(path, 'rb') as text_file:
                ftp.storbinary('STOR ' + os.path.basename(text_file.name), text_file)
    except all_errors as error:
        print(f"Error checking text file size: {error}")