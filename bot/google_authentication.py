from chatbot import *

def authenticate_google():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build('calendar', 'v3', credentials=creds)
    return service
# the function for getting events from google acount and Call the Calendar API
def get_events(day, service):
    date = datetime.datetime.combine(day, datetime.datetime.min.time())
    end_date = datetime.datetime.combine(day, datetime.datetime.max.time())
    utc = pytz.UTC
    date = date.astimezone(utc)
    end_date = end_date.astimezone(utc)
    events_result = service.events().list(calendarId='primary', timeMin=date.isoformat(), timeMax=end_date.isoformat(),
                                    singleEvents=True,
                                    orderBy='startTime').execute()
    events = events_result.get('items', [])
    if not events:
        speak('No upcoming events found.')
    else:
        speak(f"you have {len(events)} events on this day.")    
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])
        start_time = str(start.split("T")[1].split("-")[0])
        if int(start_time.split(":")[0]) < 12:
            start_time = start_time + "am"
        else:
            start_time = str(int(start_time.split(":")[0])-12) + start_time.split(":")[1]
            start_time = start_time + "pm"
        speak(event["summary"] + "at" + start_time)
            
#how to call days and day month and year
def get_date(text):
    text = text.lower()
    today = datetime.date.today()
    if text.count("today") > 0:
        return today
    day = -1
    day_of_week = -1
    month = -1
    year = today.year
    for word in text.split():
        if word in MONTHS:
            month = MONTHS.index(word) + 1
        elif  word in DAYS:
            day_of_week = DAYS.index(word)
        elif word.isdigit():
            day = int(word)
        else:
            for ext in DAY_EXTENTIONS:
                found = word.find(ext)
                if found > 0:
                    try:
                        day = int(word[:found])
                    except:
                        pass           
    if month < today.month and month != -1:
        year = year + 1
    if day < today.day and month == -1 and day != -1:
        month = month + 1
    if month ==-1 and day == -1 and day_of_week != -1:
        current_day_of_week = today.weekday()
        dif = day_of_week - current_day_of_week
        if dif < 0:
            dif +=7
            if text.count("next") >= 1:
                dif += 7
        return today + datetime.timedelta(dif)
    if month == -1 or day == -1:
        return None
    return datetime.date(month=month, day=day,year=year)

#The function to open the notepad and take note of what the user wants to take note.
def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)
    subprocess.Popen(["notepad.exe", file_name])

