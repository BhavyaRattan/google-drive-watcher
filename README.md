# google-drive-watcher
watch google drive file modifications

## Prerequisites
To run this script, you'll need:

* Python 2.6 or greater
* The [pip](https://pypi.python.org/pypi/pip) package management tool
* A Google account with Google Drive enabled

## How To Use
1) Setup Python on your system
2) Create a google project, enable drive api and get `client_secret.json` for `OAuth 2.0 Client IDs` (Detailed steps to do this provided in the end)  
3) Rename `client_secret.json` file to `credentials.json` 
4) Move `drive-watcher.py` , `requirements.txt` from this repo and the `credentials.json` file to a single directory
5) Open `drive-watcher.py` and replace `enter_file _id_here` with the file ID you want to watch
6) You can also modify `duration_in_hours` value if you want more frequent updates, the current default is set to 3 hours
7) Run `pip install -r requirements.txt`
8) Save and run `drive-watcher.py`
9) If you are running the script for the first time, it will open your browser window and ask you to grant permissions to you app. Proceed to grant the permission and then close that window.
10) Bingo! you are all set now. You will receive a system notification whenever the watched file gets modified. Clicking on the notification will open the file link in your default web browser.

## How to get client_secret.json
1) Go to the [Google API console](https://console.developers.google.com/projectselector/apis/library) and create a new project
2) Now in the `API Library` section serach for `Google Drive API` and `Enable` it
3) Now from the side menu, navigate to `credentials` and tap on `Configure Consent Screen` button
4) Select `User Type` as `External` and tap on `CREATE` button, you will see `OAuth consent screen` open up
5) Just fill in the Application name column with any name of your choice that you want to use for this script and tap on `Save` button at the bottom of the page
6) Navigate to the `Credentials` section from side menu, tap on `+ Create Credentials` button and select `OAuth client ID` option
7) Select `Desktop app` as the `Application Type` and tap on `CREATE` button, you will see a `OAuth client created` pop up, tap `OK`
8) Now from `OAuth 2.0 Client IDs` download the `client_secret.json` you just created 
9) Note : It might take a few minutes for the drive API to get enabled on your account so sit back and relax