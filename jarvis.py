import pyttsx3 #pip install pyttsx3 (For Speak)
import datetime 
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui #pip install pyautogui (For Screenshot)
import psutil #pip install pustil
import pyjokes #pip install pyjokes
import random
import operator
import json
import wolframalpha
import time
from urllib.request import urlopen
import requests
from os import walk







engine =pyttsx3.init()




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("the time is ")
    speak(Time)
def date_():
    year=datetime.datetime.now().year
    mon=datetime.datetime.now().month
    date=datetime.datetime.now().day
    speak("the date is ")

    speak(date)
    speak(mon)
    speak(year)
    

def wishme():
    
    speak("hello sairam!")

    hour=datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good morning ")
    elif hour>=12 and hour<18:
        speak("good afternoon ")
    elif hour>=18 and hour<24:
        speak("good evening ")
    else:
        speak("good night ")

   
    speak("jarvis  at your service. Please tell me how can i help you!!!!")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold =1
        audio=r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-US')
        print(query)
    except Exception as e:
        print(e)
        print("Say again please....")
        return "None"
    return query

def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('saairaamprasad@gmail.com','Konduru27',initial_response_ok=True)
    server.sendmail('saairaamprasad@gmail.com',to,content)
    server.close()

def cpu():
    usage= str(psutil.cpu_percent())
    speak('cpu is at'+usage )
    battery=str(psutil.sensors_battery())
    speak("battery is at"+ battery)

def joke():
    speak(pyjokes.get_joke())

def screenshot():
    img = pyautogui.screenshot()
    speak("what is name of this screenshot sir")
    name=takecommand()
    img.save("c:/Users/saairaam prasad/Desktop/New folder/"+name+".png")
    speak("screenshot taken sir")


if __name__ == "__main__":
    
    wishme()
    
    while True:
        query = takecommand().lower()



        if  'time'  in query:
            time_()

        if  'date' in query:
            date_()

        elif  'hello jarvis' in query:
            wishme()
        
        elif 'wikipedia' in query:
            speak("searching")
            query= query.replace('wikipedia'," ")
            result=wikipedia.summary(query,sentences=3)
            speak('According to wikipedia')
            print(result)
            speak(result)
        
        elif 'send email' in query:
            try:
                speak("what should i say?")
                content=takecommand()
                speak("to whom should i send this mail")
                reciever=input('Email:')
                to=reciever
                speak('check your content')
                speak(content)
                sendemail(to,content)
                speak('email has been sent ')
            except Exception as e:
                print(e)
                speak("Unable to send email")

        elif 'search in chrome' in query:
            speak("what should I search?")
            chromepath ="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search=takecommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
        elif 'search in youtube' in query:
            speak("what should I search?")
            search_term=takecommand().lower()
            speak("here you go in youtube ")
            wb.open('https://www.youtube.com/results?search_query='+search_term)
        elif 'search in google' in query:
            speak("what should I search?")
            search_Term =takecommand().lower()
            speak('Searching please wait ')
            wb.open('https://www.google.com/search?q='+search_Term)
        elif 'cpu' in query:
            cpu()
        elif 'joke' in query:
            joke()
        elif 'goodbye jarvis' in query:
            speak("going offline ")
            speak("goodbye sir")
            quit()
        elif 'write a note' in query:
            speak("what to write")
            notes=takecommand()
            file=open('notes.txt','w')
            speak("sir shall i add date and time?")
            ans =takecommand().lower()
            if 'yes' in ans or 'sure' in ans:
                strtime=datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strtime)
                file.write(":-")
                file.write(notes)
                speak('Done taking notes')
            else:
                file.write(notes)
        elif 'show notes' in query:
            speak("showing notes")
            file=open('notes.txt','r')
            print(file.read())
            speak(file.read())
        elif 'screenshot' in query:
            screenshot()
        elif 'what is love' and 'tell me about love' in query:
            speak("It is 7th sense that destroy all other senses , "
            "And I think it is just a mere illusion , "
            "It is waste of time")
        elif "who am i" in query:
            speak("If you can talk, then definitely you are a human")
        elif "how did  you come to this world" in query:
            speak("Thanks to sairam i was created by him.")
        elif "what is your purpose" in query:
            speak("Its a secret and it is only  by a very few people")

        elif 'play music' in query:
            s_dir="F:/songs"
            music=os.listdir(s_dir)
            speak("what should i play sir?")
            speak("select a number...")
            _, _, filenames = next(walk(s_dir))
            print(filenames)
            ans= takecommand().lower()
            
            if 'number' in ans:
                no=int(ans.replace('number',''))
                
            if 'random' or 'your choice' or ' mood' or 'just play something' in ans:
                no = random.randint(0,12)
            os.startfile(os.path.join(s_dir,music[no]))
        
        elif 'remember this' in query:
            speak('what should i remember')
            memory=takecommand().lower()
            speak("you asked to remember that"+memory)
            remember=open('mem.txt','w')
            remember.write(memory)
            remember.close()
        elif 'do you remember anything' in query:
            remember =open('mem.txt','r')
            speak("you asked me to remember"+remember.read())
        elif 'where is' in query:
            query=query.replace("where is","")
            location =query
            speak("user asked to locate"+location)
            wb.open_new_tab("https://www.google.com/maps/place/"+location)

        elif 'news' in query:
            
            try:

                jsonObj = urlopen('http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=fc5b3a3ed4ac4712a53e787a9c7cece5')
                data = json.load(jsonObj)
                i = 1
                
                speak('here are some top news from the times of india')
                print('''=============== TOP HEADLINES ============'''+ '\n')
                
                for item in data['articles']:
                    
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
                    
            except Exception as e:
                print(str(e)) 
        elif "weather" in query: 
			
			# Google Open weather website 
			# to get API of Open weather
            api_key = "4f322d40a0d93662a669ff24f19355f6"
            base_url = "http://api.openweathermap.org/data/2.5/weather?q="
            speak(" City name ")
            print("City name : ")
            city_name = takecommand()
            complete_url = base_url + city_name  + "APPID=" + api_key 
            response = requests.get(complete_url)
            x = response.json()
            
            if x["cod"] != "404":
                current_temperature = x["main"]["temp"]
                current_pressure = x["main"]["pressure"]
                current_humidiy = x["main"]["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
                
            else:
                speak(" City Not Found ") 

        elif 'stop listening' in query:
            speak("for how many seconds")
            ans =int(takecommand())
            time.sleep(ans)
            print(ans)
        
        elif "calculate" in query:
            
            app_id = "wolfram alpha api"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer) 

        



        #General Questions
        elif "what is" in query or "who is" in query: 
			
			# Use the same API key 
			# that we have generated earlier
            client = wolframalpha.Client("wolfram alpha api")
            res = client.query(query)
            
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results") 

        elif 'log out' in query:
            os.system('shutdown -l')
        elif 'restart' in query:
            os.system('shutdown /r /t 1') 
        elif 'shutdown' in query:
            os.system('shutdown /s /t 1')

class Main(MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_jarvisUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("E:/wallpaper/jar/iron.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("E:/wallpaper/jar/intial.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)



app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())

    
        



        


        




           





        
        







        
    

