import dropbox
import tarfile
import os
import time

#functions
def addContentToDropbox(compressedFile):
  client = dropbox.client.DropboxClient("asdf")
  print 'linked account: ', client.account_info()
  f = open(compressedFile, 'rb')
  response = client.put_file(compressedFile, f)
  print 'uploaded: ', response


#back up the content
dateOfBackup = time.strftime("%Y-%m-%d") 
compressedFile = "content" + dateOfBackup + ".tar.gz"
tar = tarfile.open(compressedFile, "w:gz")
tar.add("/home/bitnami/apps/wordpress/htdocs/wp-content/")
tar.close()
#add the content to dropbox
addContentToDropbox(compressedFile)
#clean up
os.remove(compressedFile)

#back up the database
sqlCommand = """mysqldump --add-drop-table > database.sql"""
os.system(sqlCommand)
compressedFile = "database" + dateOfBackup + ".tar.gz"
tar = tarfile.open(compressedFile, "w:gz")
tar.add("asdf" + ".sql")
tar.close()
#add the database to dropbox
addContentToDropbox(compressedFile)
#clean up
os.remove(compressedFile)
