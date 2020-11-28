from chatbot import *
from google_authentication import *
from coronabot import *
from webbrowsers import *

def mainbot():
    WAKE = "joy"
    SERVICE = authenticate_google()
    print("Start")
    greetings = ["hey, how can i help you?", "hello, how can i help you?", "yes, what can i do for you?"]

    flag = True
    HELP = ["hey your name please", "hey this joy your name please","hello am joy and you are",
    "hi this is joy i would love to know your name"]
    reply = random.choice(HELP)
    speak(reply)
    replyget = get_audio()
    speak(replyget)
    speak("what can i do for you?")


    while (flag == True):
        print("Listening")
        text = get_audio()
        if text.count(WAKE) > 0:
            random_greetings = random.choice(greetings)
            speak(random_greetings)
            text = get_audio()
         
        botques = ["what is your name", "your name","who are you", "your name please", "tell me your name",]
        botname = ["my name is joy", "i am joy", "joy", "joy is my name"]
        for phrase in botques:
            if phrase in text:
                nameb = random.choice(botname)
                speak(nameb)               

        botanswerwhen =["i was create in 2020 during the final project at Dmi st Eugene University Zambia", "2020 from august to december at dim st eugene university zambia"]
        boqueswhen = ["when were you created", "in which year whare you created", "where were you created"]
        for phrase in boqueswhen:
            if phrase in text:
                whenbot = random.choice(botanswerwhen)
                speak(whenbot)
                
        createdbot = ["mwansa", "mwansa created me right in this computer"]
        createdques = ["who created you", "who made you","who is your creater", "who programed you"]
        for phrase in createdques:
            if phrase in text:
                creater = random.choice(createdbot)
                speak(creater)
                


        #the word that can be used to ask for events fromthe calender.
        CALENDAR_STRS = ["what do i have next month", "do i have plans", "do i have anything to do today", "what is there on", "when is my birthday?",
        "what do i have on monday","what do i have on friday", "what do i have on sunday", "whats on my calender today",
        "any plans tomorrow","when is my presatation", "any plans today"]
        for phrase in CALENDAR_STRS:
            if phrase in text:
                date = get_date(text)
                if date:
                    get_events(date, SERVICE)
                else:
                    speak("I don't understand")                  

        #words that you can use to tell the bot to take notes                    
        NOTE_STRS = ["make a note", "write this down", "remember this", "take a note", "write this for me",
         "make some points for me", "notes","put this down",]
        for phrase in NOTE_STRS:
            if phrase in text:
                speak("What would you like me to write down")
                note_text =  get_audio()
                note(note_text)
                speak("I've made a note of that.")
               
       
        response = k.respond(text)
        speak(response)


        WEB_REQUEST = ["open the browser","open the webbrowser", "open google for me", "search for me"]
        for phrase in WEB_REQUEST:
            if phrase in text:
                driver=webdriver.Chrome("chromedriver.exe")
                driver.maximize_window()
                data = driver.get("http://www.google.com")
                speak("the browser is open what do you what me to search for you")
                speak ("what do you want to search?")
                searchword = get_audio() 
                search=driver.find_element_by_name(searchword)
                for item in search:
                    textdata = item.text
                    speak(textdata)
                




        # TIME = ["what's is the time", "time", "what time is it"]       
        # for phrase in TIME:
        #     for phrase in text:
        #         cur_time = curenttime()
        #         speak(cur_time)
        #         get_audio()	
        
        # DATE = ["what's the date today", "the date" "todays date",]
        # for phrase in DATE:
        #     if phrase in text:
        #         cur_date = todaydate()
        #         speak(cur_date)
        #         get_audio()

    

