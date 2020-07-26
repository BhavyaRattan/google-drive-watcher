from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from datetime import datetime
from dateutil.parser import parse
import pytz
import os
import time
import sys
from pync import Notifier

file_id = 'enter_file_id_here'
duration_in_minutes = 180

SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
drive_url = 'https://drive.google.com/file/d/' + file_id + '/view?usp=sharing'
duration_in_seconds = duration_in_minutes * 60


def notify(title, text):
    Notifier.notify(text, title=title, open=drive_url)


def do_every(period, f, *args):
    def g_tick():
        t = time.time()
        count = 0
        while True:
            count += 1
            yield max(t + count * period - time.time(), 0)

    g = g_tick()
    while True:
        time.sleep(next(g))
        f(*args)


def getFileDetails(service, first_time=False):
    # Call the Drive v3 API
    item = service.files().get(fileId=file_id, fields='name, id, modifiedTime').execute()

    if not item:
        print('No files found.')
    else:
        modified_date = parse(item['modifiedTime'])
        last_checked = modified_date if first_time else datetime.utcnow().replace(tzinfo=pytz.utc)
        difference = modified_date - last_checked
        drive_name = item['name']
        if difference.total_seconds() + duration_in_seconds > 0 or first_time:
            notify("Drive Watcher",
                   '{0} was last modified at {1}'.format(drive_name, modified_date.strftime("%I:%M %p on %b %d, %Y")))


def main():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token) if sys.version_info[0] < 3 else pickle.load(token, encoding='bytes')
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)
    print("Bingo! We are all set. just sit back and relax, Drive Watcher will notify you! Closing this window will "
          "terminate the script. ")

    getFileDetails(service=service, first_time=True)
    do_every(duration_in_seconds, getFileDetails, service)


if __name__ == '__main__':
    main()
