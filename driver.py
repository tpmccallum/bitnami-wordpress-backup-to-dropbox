import dropbox
import tarfile
import os
import time

#functions
def addContentToDropbox(compressedFile):
  client = dropbox.client.DropboxClient("_GSRrTwYHmEAAAAAAAAABW3vaBdS5B9bYSkBgnO0MJsGFihL0GAa2Zao2icFQiuu")
  print 'linked account: ', client.account_info()
  f = open(compressedFile, 'rb')
  response = client.put_file(compressedFile, f)
  print 'uploaded: ', response

#get the date
dateOfBackup = time.strftime("%Y-%m-%d")
#back up the content
compressedFileC = "content" + dateOfBackup + ".tar.gz"
tar = tarfile.open(compressedFileC, "w:gz")
tar.add("/home/bitnami/apps/wordpress/htdocs/wp-content/")
tar.close()
#add the content to dropbox
addContentToDropbox(compressedFileC)
#clean up
os.remove(compressedFileC)

#back up the database
sqlCommand = """/opt/bitnami/mysql/bin/mysqldump --add-drop-table > database.sql"""
os.system(sqlCommand)
compressedFileD = "database" + dateOfBackup + ".tar.gz"
tar = tarfile.open(compressedFileD, "w:gz")
tar.add("database.sql")
tar.close()
#add the database to dropbox
addContentToDropbox(compressedFileD)
#clean up
os.remove(compressedFileD)
