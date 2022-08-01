# FTP uplaod test

import ftplib


file_name = '/home/bastichjones/2022-07-27 18-43-06.mkv'

HOSTNAME = 'ftp.cloudvideo.tv' # ftp target
USERNAME = 'PATRICKBATEMAN'
PASSWORD = 'a2xxrxcpgx'



session = ftplib.FTP(HOSTNAME,USERNAME,PASSWORD)

with open(file_name,'rb') as upload_file:               # file to send
    session.storbinary('STOR {FILENAME}', file)     # send the file                                        # close file and FTP
    session.quit()