import pyttsx3
# import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import requests
from bs4 import BeautifulSoup
import playsound
import time
# import pygame
engine = pyttsx3.init() 
voices = engine.getProperty('voices')
r = 145
engine.setProperty('rate',r)
 
engine.setProperty('voice', voices[1].id)
 
 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak('what is your name')
print( '----------------')
print('|               |')
print('|      HI       |')
print('|  What is your |')
print('|     Name      |')
print('|               |')
print(' ---------------- ')
name = input('Enter your name:\n')
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(f'Good..Mornning!..{name}')
    elif hour>=12 and hour<16:
        speak(f'Good..afternoon!..{name}')
    else:
        speak(f'Good..evening!..{name}')  
    speak('I am your assistant how can i help you')
if __name__ == "__main__":
    wishMe()
 
 
 
        
    
 
 
    query = None
    while True:
        query=input('What do you want to search:\n')
        query = query.lower()    
        print('TYPE exit TO EXIT THE CODE')
        if 'wikipedia' in query:
            speak('searching wikipedia.....')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences=3)
            speak('according to wikipedia')
            print(results)
            speak(results) 
        
        elif 'exit' in query:
            speak('ok..... closing.... bye..')
            break
        elif 'open google' in query:
            speak('opening google')
            webbrowser.open("google.com")
        elif 'open youtube' in query:
            speak('opening youtube.')
            webbrowser.open("youtube.com")
        elif 'open' in query:
            query = query.replace('open ','')
            webbrowser.open(f'www.{query}.com')
        elif 'play music' in query:
            music_dir = 'C:\\Users\\Princee\\OneDrive\\Desktop\\prajwal\\songs'
            print('playing sound using  playsound')
            pygame.init()
            songs = os.listdir(music_dir)
            n = random.randint(0,35)
 
            sound = pygame.mixer.Sound(os.path.join(music_dir, songs[n]))
 
            sound.play()
 
            pygame.time.delay(30000)
            sound.stop()
            pygame.quit()
        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f'{name}....the time is{strTime}')
        elif 'joke' in query:
            def jokes1():
                f=open('E:\Class- 12\Computer Project\Jokes.txt','r',)
                open('Jokes.txt','r')
                lines=f.read()
                read1=lines.splitlines()
                print(random.choice(read1))
            jokes1()
        elif '.in' in query:
            webbrowser.open(f'www.{query}')
        elif 'international news' in query:
            def international_news():
                url = 'https://www.bbc.com/news'
                response = requests.get(url)
                
                soup = BeautifulSoup(response.text, 'html.parser')
                headlines = soup.find('body').find_all('h3')
                unwanted = ['BBC World News TV', 'BBC World Service Radio',
                            'News daily newsletter', 'Mobile app', 'Get in touch']
                
                flag=0
                for x in list(dict.fromkeys(headlines)):
                    if flag<5: 
                        if x.text.strip() not in unwanted:
                            h = (x.text.strip())
                            print(h)
                            speak(h)
                            
                            flag+=1
                    else:
                        break  
            international_news()
        elif 'national news' in query:
            def indian_news():
                url = 'https://www.indiatoday.in/india'
                response = requests.get(url)
                
                soup = BeautifulSoup(response.text, 'html.parser')
                headlines = soup.find('body').find_all('h2')
                
                flag=0
                for x in list(dict.fromkeys(headlines)):
                    if flag<5: 
                        h = (x.text.strip())
                        print(h)
                        speak(h)
                        flag+=1
                    else:
                        break  
            indian_news()
        elif 'play game' in query:
            speak('okk....starting....the....game')
            import random
            def gamewin(comp,B):
                if comp == B:
                    return None
                elif comp == 'r':
                    if B == 'p':
                        return True
                    elif B == 's':
                        return False    
                
                elif comp == 'p':
                    if B == 's':
                        return True
                    elif B == 'r':
                        return False 
 
                    elif comp == 's':
                        if B == 'r':
                            return True 
                    elif B == 'p':
                        return False 
            hi = 0
            hii = 0
            count2 = int(input('Enter no. of times you want to play this game:\n'))
            while count2!=0:
 
                n = random.randint(1, 3)
                if n == 1:
                    comp = 'r'
                elif n == 2:
                    comp = 'p'
                elif n == 3:
                    comp = 's'
                print('PLAYER A TURN: ')  
                print('press (r) for rock, (p) for paper, (s) for scissor')   
                B = input('YOUR TURN: ')
 
                print(f"Player A chose  {comp}")
                print(f"You chose {B}")
                a = gamewin(comp,B)
                if a == None:
                    print('TIE')
                elif a == True:
                    print('You win this round')
                    hi = hi+1
                
                elif a == False:
                    print('PLAYER A WIN THIS ROUND') 
                    hii = hii+1
                print(f'Player A = {hii}       You = {hi} ')
                count2 = count2-1
            if (hi>hii):
                    print('-------------')
                    print('|             |')
                    print('|     YOU     |')
                    print('|    WIN      |')
                    print('|             |')
                    print(' -------------')
                    g = True
            elif (hi<hii):
                print('Player A win this game')
                g = False
            else:
                print('Game is Tie')
                g = None
            if g == True:
                print('H m m m, so you won this game ')
                print('it was a good game')
                R11 = input(R)
                print('do you want to play another game')
                R12 = input(R)
 
                if('yes' in R12):
                    o = True
                elif('no' in R12):
                    o = False    
                if (o):
                    print('Alright I have started a game \n In this game i will guess left or right \n And you will also guess the same \n if you guessed what I chose you get a point \n Else I get a point')
                    print('Should I start the Game')
                    R13 = input(R)
                        
                    if('yes' in R13):
                        t = True
                    else:
                        t = False
                    if(t):
                        print('I have startd the game \n choose no. of times you want to play')
                        d = int(input('Enter no. of times you want to play game: \n '))
                        y = int(0)
                        def gamewin2(q,w):
                            if q == B:
                                return True
                            elif q == 'l':
                                if w == 'r':
                                    return False
                            elif q == 'r':
                                if w == 'l':
                                    return False
                        q = None
 
                        v = 0
                        h = 0    
                        while y!=d: 
                        
                            n = random.randint(1,2)
                            if n == 1: 
                                q = 'l' 
                            elif n == 2:
                                q = 'r'
                            print('       Player 1  turn: ')
 
                
 
                            print('Choose (l) for left and (r) for right')
 
                            w= input('Enter l or r:  ')
                            print(f'Player1  chose    {q} '  )
                            print(f'You chose {B} ')
                            l = gamewin(q,w)
                            if l == True:
                                print(' YOU guessed it right: You got 1 POINT  ')
                                v = v+1
                            elif l == False:
                                print(' YOU did not guessed it Player 1 GOT A POINT :) ')
                                h = h+1    
                            print('Player 1 score =  ' +str(v)+  '\n Your score =  '+str(h))
 
                            y = y+1
                        x = int((v/d)*100)
                        z = int((h/d)*100)
                        if h > v:
                            print('            ------------------'          )
                            print('           | You won the Game |         ')
                            print('            ------------------          ')
                        print(         f' You Scored  {v}  POINTS    ')
 
 
    else:
        speak('this language is not yet available')
        print('This Language is not yet available')
 

