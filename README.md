# bitnami-wordpress-backup-to-dropbox
A python program that backs up a bitnami wordpress instance and sends it to your drop box account

## Install python pip and dropbox for Python
```
sudo apt-get install python-pip
```
```
sudo pip install dropbox
```
## Install Dropbox API
Head over to Dropbox and create an app using the App Console (Dropbox API APP with data access as files and datastores).
```
https://www.dropbox.com/developers/apps/create
```
Click the "generate access token" button and past it into the driver.py file where it says "asdf"

## Create mysqldump credentials
Add the following to the 
```
/opt/bitnami/mysql/bitnami/my.cnf
```
file (make that the username and password you use actually have the ability to back up the database, try it out manually first using a mysqldump command)

```
[mysqldump]
user=asdf
password=asdf
```

Download the Python file called driver.py and run it from the users home directory
```
sudo python driver.py
```

## I decided to add this to the system cron
```
sudo crontab -e
```
```
01 01 * * * /usr/bin/python /home/bitnami/backup_wordpress_to_dropbox.py > /tmp/wordpress_backup_script.py.log 2>&1
```
Make sure that you have the right permissions and test each command seperately, also go to the backup area and restore the entire system at least once to ensure success. For example open the sql file and read it to make sure that it worked and open the content file and make sure that it worked; don't go by file size alone TEST!!!

