import pyttsx3 # type: ignore #pip install pyttsx3 (For Speak)
import datetime 
import speech_recognition as sr # pip install speech_recognition
import wikipedia # pip install wikipedia
import smtplib
import webbrowser as wb 
import psutil #pip install psutil
import pyjokes #pip install pyjokes 
import os
import pyautogui  #pip install pyautogui
import random
import wolframalpha
import json
from urllib.request import urlopen
import requests
import time
import winshell
import google.generativeai as genai  # Gemini API
import pywhatkit as kit 
import cv2
from requests import get
import webbrowser
# Google Gemini API configuration
genai.configure(api_key="AIzaSyBOAkMv-bxYz6RsQewoZ7DcOGBDCFFUsOo")
model = genai.GenerativeModel("gemini-1.5-flash")

engine = pyttsx3.init()
wolframalpha_app_id = 'J7WW76-LGHLU775E6'
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    time = datetime.datetime.now().strftime("%I:%M:%S")  # for 12-hour clock
    speak("The current time is")
    print(time)
    speak(time)

def date():
    year = (datetime.datetime.now().year)
    month = (datetime.datetime.now().month)
    date = (datetime.datetime.now().day)
    speak("The current date is")
    print(date)
    print(month)
    print(year)
    speak(date)
    speak(month)
    speak(year)

def wishme():
    print("Welcome Mam")
    speak("Welcome Mam")
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        print("Good Morning!")
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        print("Good Afternoon!")
        speak("Good Afternoon!")
    elif hour >= 18 and hour < 24:
        print("Good Evening!")
        speak("Good Evening!")
    else:
        print("Good Night!")
        speak("Good Night!")
    print("Nexy at your service. Please tell me how can I help you?")
    speak("Nexy at your service. Please tell me how can I help you?")

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-pk')
        print(query)
    except Exception as e:
        print(e)
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    return query

def generate_ai_content(prompt):
    try:
        print("Thinking..")
        speak("Thinking..")  
        response = model.generate_content(prompt)
        answer = response.text
        source = "Source: gemini-1.5-flash"
        print(f"According to {source}")
        speak(f"According to {source}") 
        print("AI Response:", answer)
        speak(answer)
    except Exception as e:
        print("Error:", e)
        speak("Sorry, I could not generate a response.")


def sendEmail(to, subject, content):
    sender_email = 'myjarvis6464@gmail.com'  # my email
    app_password = 'xasu itoz wiaj cfes'  # my App Password

    try:
        # Setup the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(sender_email, app_password)

        # Prepare the email content
        email_message = f"Subject: {subject}\n\n{content}"

        # Send the email
        server.sendmail(sender_email, to, email_message)
        server.quit()  # Close the connection
        print(f"Email sent successfully to {to}")
        speak(f"Email sent successfully to {to}")
    except Exception as e:
        print(f"Error: {e}")
        print("Unable to send the email. Please check the details and try again.")
        speak("Unable to send the email. Please check the details and try again.")

def cpu():
    usage=str(psutil.cpu_percent())
    print('CPU is at'+ usage)
    speak('CPU is at'+ usage)
    battery = psutil.sensors_battery()
    print("Battery is at")
    speak("Battery is at")
    print(battery.percent)
    speak(battery.percent)
 
def jokes():
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke)
def Introduction():
    print("I am Nexy 1.0 , Personal AI assistant . "
    "I am created by Bisma Razzaq. "
    "I can help you in various regards . "
    "In layman terms , I can try to make your life a bed of roses , "
    "Where you just have to command me , and I will do it for you . ")
    speak("I am Nexy 1.0 , Personal AI assistant . "
    "I am created by Bisma Razzaq. "
    "I can help you in various regards . "
    "In layman terms , I can try to make your life a bed of roses , "
    "Where you just have to command me , and I will do it for you . ")

def Creator():
    print("Bisma Razzq is currently studying in BS Computer Science at University Of Education . "
    "She has a deep interest in Robotics, Artificial Intelligence and Machine Learning .  "
    "If you are facing any problem regarding the 'Nexy', She will be glad to help you. ")
    speak("Bisma Razzq is currently studying in BS Computer Science at University Of Education . "
    "She has a deep interest in Robotics, Artificial Intelligence and Machine Learning . "
    "If you are facing any problem regarding the 'Nexy', She will be glad to help you ")


def screenshot():
    # Take a screenshot
    img = pyautogui.screenshot()
    
    # Define a valid file path and name with an extension
    save_path = r"C:\pics\screenshot.png"  # Use raw string to handle backslashes
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    # Save the screenshot
    img.save(save_path)
    print(f"Screenshot saved at {save_path}")


if __name__ == '__main__':
    wishme()
    while True:
        query = TakeCommand().lower()

        if 'time' in query:
            time_()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            print("Searching...")
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=3)
            print("According to Wikipedia")
            speak("According to Wikipedia")
            print(result)
            speak(result)
        elif 'ask ai' in query or 'explain' in query or 'how' in query or 'what' in query:
            print("What would you like to know?")
            speak("What would you like to know?")
            prompt = TakeCommand()
            generate_ai_content(prompt)    
        elif 'send email' in query:
            try:
                print("What should I say?")
                speak("What should I say?")
                content = TakeCommand()
                print("What is the subject of the email?")
                speak("What is the subject of the email?")
                subject = TakeCommand()
                print("Who is the recipient?")
                speak("Who is the recipient?")
                recipient = input("Enter recipient's email address: ")
                sendEmail(recipient, subject, content)
                print("The email has been sent successfully.")
                speak("The email has been sent successfully.")
            except Exception as e:
                print(e)
                print("Unable to send the email.")
                speak("Unable to send the email.")
        elif 'open youtube' in query:
            print("What should I search?")
            speak("What should I search?")
            Search_term = TakeCommand().lower()
            print("Here we go to Youtube\n")
            speak("Here we go to Youtube\n")
            wb.open("https://www.youtube.com/results?search_query=" + Search_term)
        elif 'search google' in query:
            print("What should I search?")
            speak("What should I search?")
            Search_term = TakeCommand().lower()
            wb.open('https://www.google.com/search?q=' + Search_term)
        elif 'cpu' in query:
            cpu()
        elif 'joke' in query:
            jokes()
        elif 'go offline' in query:
            print("going Offline mam!")
            speak("going Offline mam!")
            quit() 
        elif 'take screenshot' in query:
            screenshot()
            speak("Screenshot taken and saved!") 

        elif "write note" in query:
            print("What should I write, ma'am?")
            speak("What should I write, ma'am?")
            note = TakeCommand()
          # Ensure the directory exists
            save_path = r"E:\Note\notes.txt"  # Raw string for correct path handling
            os.makedirs(os.path.dirname(save_path), exist_ok=True)

            try:
                # Open the file in write mode
                with open(save_path, 'w') as file:
                    print("Ma'am, should I include the date and time?")
                    speak("Ma'am, should I include the date and time?")
                    dt = TakeCommand()

                    if 'yes' in dt or 'sure' in dt:
                        # Add date and time
                        strTime = datetime.datetime.now().strftime("%H:%M:%S")
                        file.write(strTime + " :- " + note + "\n")
                        print("Done! Note with date and time is saved.")
                        speak("Done! Note with date and time is saved.")
                    else:
                        file.write(note + "\n")
                        print("Done! Note is saved without date and time.")
                        speak("Done! Note is saved without date and time.")
            except Exception as e:
                print(f"Error writing the note: {e}")
                print("Sorry, I couldn't write the note. Please try again.")
                speak("Sorry, I couldn't write the note. Please try again.")       
 
        elif 'play songs' in query:
            songs_dir = 'E:\songs'
            music = os.listdir(songs_dir)
            print("What should i play? ")
            speak("What should i play? ")
            print('Select a number...')
            speak('Select a number...')
            ans = (TakeCommand().lower())
            while('number' not in ans and ans != 'random' and ans != 'you choose'):
              print('I could not understand you. Please Try again.')
              speak('I could not understand you. Please Try again.')
              ans = (TakeCommand().lower())
            if 'number' in ans:
             no = int(ans.replace('number',''))
            if 'random' or 'you choose' in ans:
                no = random.randint(1,6)
            os.startfile(os.path.join(songs_dir, music[no]))

        elif "calculate" in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            source = "Source: WolframAlpha"
            print(f"According to  {source}" )
            speak(f"According to  {source}"  )
            print("The answer is " + answer)
            speak("The answer is " + answer) 
        elif 'remember that' in query:
            print("What should I remember ?")
            speak("What should I remember ?")
            memory = TakeCommand()
            print("You asked me to remember that"+memory)
            speak("You asked me to remember that"+memory)
            remember = open(r'C:\Users\PMLS\Desktop\memory.txt', 'w') 
            remember.write(memory)
            remember.close()
        elif 'do you remember anything' in query:
           try:
             # Read the memory from the text file
            with open(r'C:\Users\PMLS\Desktop\memory.txt', 'r') as remember:
              remembered_text = remember.read()
              # Speak and print the remembered text
              print("You asked me to remember that: " + remembered_text)
              speak("You asked me to remember that " + remembered_text)
           except FileNotFoundError:
              print("I don't have any memories saved.")
              speak("I don't have any memories saved.")
        elif "where is" in query:
         location = query.replace("where is", "").strip()
         if location:
          print(f"Locating {location}")
          speak(f"Locating {location}")
          url = f"https://www.google.com/maps/place/{location}"
          print(f"Opening URL: {url}")  # Debug: Print the URL
          wb.open(url)
         else:
          print("I couldn't understand the location. Please try again.")
          speak("I couldn't understand the location. Please try again.")
        elif 'news' in query:
            try:
                jsonObj = urlopen(' https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=600438076054440da76533f261acb728')
                data = json.load(jsonObj)
                i = 1
                print('here are some top news')
                speak('here are some top news')
                print('''=============== TOP HEADLINES ============'''+ '\n')
                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                print(str(e)) 
        elif 'log out' in query:
            print("Logging out... ")
            speak("Logging out... ")
            os.system("shutdown -l")
        elif 'restart' in query:
            print("Restarting... ")
            speak("Restarting... ")
            os.system("shutdown /r /t 1")
        elif 'shutdown' in query:
            print("Shutting down... ")
            speak("Shutting down... ")
            os.system("shutdown /s /t 1")
        elif 'how are you' in query:
         print("I am fine. Thanks for asking.")
         speak("I am fine. Thanks for asking.")
         print("How are you?")
         speak("How are you?")
         # Capture the user's response
         ans = TakeCommand()  # Replace `take_command()` with your voice input function
         if 'fine' in ans or 'good' in ans:
          print("It's good to know that you're fine.")
          speak("It's good to know that you're fine.")
         else:
           print("God bless you.")
           speak("God bless you.")
        elif "who am i" in query:
            print("If you can talk, then definitely you are a human")
            speak("If you can talk, then definitely you are a human")
        elif "why you came to this world" in query:
            print("I came to this world for human ease. ")
            speak("I came to this world for human ease. ")
        elif "define love" in query or "tell me about love" in query:
            print("It is 7th sense that destroy all other senses ")
            speak("It is 7th sense that destroy all other senses ")
        elif "empty recycle bin" in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            print("Recycle Bin Recycled") 
            speak("Recycle Bin Recycled") 
        elif "tell me about yourself" in query or "who are you" in query:
            Introduction()
        elif "tell me about your developer" in query:
            Creator()
        elif "will you be my girlfriend" in query or "will you be my boyfriend" in query:
            print("No. I don't want to waste my precious time in such poor things. ")
            speak("No. I don't want to waste my precious time in such poor things. ")
            
        elif "i love you" in query or "do you love me" in query:
            print("I think you are an extreme single person and you could not find love in humans ")
            speak("I think you are an extreme single person and you could not find love in humans ")
            print("That's why you are talking with an assistant about love")
            speak("That's why you are talking with an assistant about love")
            print("But sorry i have to focus on work to make my developer happy")
            speak("But sorry i have to focus on work to make my developer happy")
        elif "weather" in query:
         api_key = "c3d9dcd557a55f5f1122d13730edfc24"  # Replace this with your actual API key
         base_url = "http://api.openweathermap.org/data/2.5/weather?"
         print("Please tell me the city name.")
         speak("Please tell me the city name.")
         print("City name: ")
         city_name = TakeCommand()
         # Construct the complete API URL
         complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric"
         try:
           # Make a request to the API
           response = requests.get(complete_url)
           x = response.json()  # Get JSON response
           # Print the entire response for debugging
           print("API Response:", x)
           # Check if city is found
           if x["cod"] == 200:  # If the response code is 200 (OK)
             y = x["main"]
             current_temperature = y["temp"]
             current_pressure = y["pressure"]
             current_humidity = y["humidity"]
             z = x["weather"]
             weather_description = z[0]["description"]
             # Output and speak the weather information
             weather_info = (
                f"Temperature: {current_temperature}°C\n"
                f"Atmospheric pressure: {current_pressure} hPa\n"
                f"Humidity: {current_humidity}%\n"
                f"Description: {weather_description}"
            )
             print(weather_info)
             speak(weather_info)

           else:
             # Handle the case where city is not found
             print("City not found, error code:", x["cod"])
             speak("City not found.")

         except requests.exceptions.RequestException as e:
          print("Network error:", e)
          speak("There was a network error. Please try again later.")
         except KeyError as e:
          print(f"Unexpected response format. Missing key: {e}")
          speak("There was an error processing the weather information.")
        elif "don't listen" in query or "stop listening" in query:
          print("For how many seconds should I stop listening?")
          speak("For how many seconds should I stop listening?")
          try:
           ans = TakeCommand()
           if ans:
            # Convert spoken text to a number
            ans = int(ans)
            print(f"Okay, I will stop listening for {ans} seconds.")
            speak(f"Okay, I will stop listening for {ans} seconds.")
            time.sleep(ans)
            print("I am back and listening now.")
            speak("I am back and listening now.")
           else:
              print("I couldn't understand the duration.")
              speak("I couldn't understand the duration.")
          except ValueError:
              print("Please say a valid number.")
              speak("Please say a valid number.")
          except Exception as e:
               print(f"An error occurred: {str(e)}")
               speak(f"An error occurred: {str(e)}")

        elif 'open ms word' in query:
            print("Opening Word")
            speak("Opening Word")
            try:
                os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

            except Exception as e:
                print(f"An error occurred: {str(e)}")
                speak(f"An error occurred: {str(e)}")

        elif "display note" in query:
            save_path = r"E:\Note\notes.txt"
            try:
                print(f"Attempting to open file: {save_path}")  # Debug message
                with open(save_path, 'r') as file:
                    notes = file.read().strip()
                    print(f"File Content: {notes}")  # Show content for debugging
                    if notes:
                        print("Here are your notes:")
                        speak("Here are your notes:")
                        print("Your Notes:\n", notes)
                        speak(notes)
                    else:
                        print("The notes file is empty.")
                        speak("The notes file is empty.")
            except FileNotFoundError:
                print("Sorry, the notes file does not exist.")
                speak("Sorry, the notes file does not exist.")
            except Exception as e:
                print(f"Error: {e}")
                speak(f"An error occurred: {str(e)}")
        elif 'open command prompt' in query:
            print("Opening command prompt")
            speak("Opening command prompt")
            try:
                os.startfile(r"C:\Users\PMLS\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools\Command Prompt")

            except Exception as e:
                print(f"An error occurred: {str(e)}")
                speak(f"An error occurred: {str(e)}")
        elif 'open notepad' in query:
            print("Opening Notepad")
            speak("Opening Notepad")
            try:
                os.startfile(r"C:\Windows\notepad.exe")

            except Exception as e:
                print(f"An error occurred: {str(e)}")
                speak(f"An error occurred: {str(e)}")
        elif 'open github' in query:
            print("Opening GitHub")
            speak("Opening GitHub")
            try:
                os.startfile(r"C:\Users\PMLS\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\GitHub, Inc\GitHub Desktop.lnk")

            except Exception as e:
                print(f"An error occurred: {str(e)}")
                speak(f"An error occurred: {str(e)}")
        elif 'open camera' in query:
          print("Opening camera")
          speak("Opening camera")
          cap = cv2.VideoCapture(0)
          # Check if the camera opened successfully
          if not cap.isOpened():
            print("Error: Could not open camera.")
            speak("Error: Could not open camera.")
            # Set a flag to indicate that the camera cannot be opened
            camera_error = True
          else:
             camera_error = False
          if camera_error:
            # If camera failed to open, skip to the next part of the code
            pass
          else:
            while True:
              ret, img = cap.read()
              # If frame is read correctly, ret is True
              if not ret:
                print("Failed to grab frame.")
                break

              cv2.imshow('webcam', img)
              # Wait for 1 ms for a key press (0 for indefinite)
              k = cv2.waitKey(1)
              # Escape key to break the loop
              if k == 27:  
                break
             # Release the camera and close all windows when done
          cap.release()
          cv2.destroyAllWindows()

        elif 'tell my ip address' in query:
            ip =  get('https://api.ipify.org').text
            print(f'your ip address is {ip}')
            speak(f'your ip address is {ip}')
        elif 'open facebook' in query:
             print("opening facebook")
             speak("opening facebook")
             webbrowser.open('www.facebook.com')
        elif 'send message' in query:
            print("Sending WhatsApp message")
            speak("Sending WhatsApp message")
            # Specify the time directly
            hour = 0
            minute = 0
             #Send the WhatsApp message
            kit.sendwhatmsg('+923477681780', 'this is testing protocol', hour, minute)
        
        
           