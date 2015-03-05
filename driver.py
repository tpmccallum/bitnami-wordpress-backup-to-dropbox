import dropbox
import tarfile
import os
import time

dateOfBackup = time.strftime("%Y-%m-%d") 
compressedFile = dateOfBackup + ".tar.gz"
tar = tarfile.open(compressedFile, "w:gz")
tar.add("/home/bitnami/apps/wordpress/htdocs/wp-content/")
tar.close()

client = dropbox.client.DropboxClient("your_dropbox_api_key")
print 'linked account: ', client.account_info()

f = open(compressedFile, 'rb')
response = client.put_file(compressedFile, f)
print 'uploaded: ', response

os.remove(compressedFile)
