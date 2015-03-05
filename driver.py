import dropbox
import tarfile
import os
import time
#back up the content
dateOfBackup = time.strftime("%Y-%m-%d") 
compressedFile = "content" + dateOfBackup + ".tar.gz"
tar = tarfile.open(compressedFile, "w:gz")
tar.add("/home/bitnami/apps/wordpress/htdocs/wp-content/")
tar.close()
#add the content to dropbox
client = dropbox.client.DropboxClient("asdf")
print 'linked account: ', client.account_info()

f = open(compressedFile, 'rb')
response = client.put_file(compressedFile, f)
print 'uploaded: ', response
#clean up
os.remove(compressedFile)

#back up the database
DB_HOST = "localhost"
DB_USER = "asdf"
DB_USER_PASSWORD = "asdf"
DB_NAME = "asdf"
os.system("mysqldump --add-drop-table -c -u " + str(DB_USER) + " -p " + str(DB_USER_PASSWORD) + str(DB_NAME) + ";" > "asdf" + ".sql")
compressedFile = "database" + dateOfBackup + ".tar.gz"
tar = tarfile.open(compressedFile, "w:gz")
tar.add("asdf" + ".sql")
tar.close()
#add the database to dropbox
client = dropbox.client.DropboxClient("asdf")
print 'linked account: ', client.account_info()

f = open(compressedFile, 'rb')
response = client.put_file(compressedFile, f)
print 'uploaded: ', response
#clean up
os.remove(compressedFile)
