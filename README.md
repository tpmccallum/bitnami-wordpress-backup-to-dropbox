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
Click the "generate access token" button and past it into the driver.py file where it says "asdf"

## Create mysqldump credentials 
Make a file called .my.cnf in your home directory and add the following lines (also make sure permissions are set correctly)
```
[mysqldump]
user=asdf
password=asdf
```

Download the Python file called driver.py and run it from the users home directory
