import pyttsx3
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
from tkinter import *
import mysql.connector

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

print('S for signup')
print('L for login')
l = input('ENTER YOUR CHOICE:\n')
l = l.lower()
conn = mysql.connector.connect(user='root',passwd='regal', host='localhost',database='hello')
cursor = conn.cursor()
def signup(username, email, password, book):
  query = "INSERT INTO users (name, email, password, book) VALUES (%s, %s, %s, %s)"
  values = (u, e, p, b)
  cursor.execute(query, values)
 
  conn.commit()
  conn.close()
def login(u,p):
    # op999=""Select * from users where name=:username and password=:password""
    # cursor.execute(op999)
    cursor.execute("SELECT * FROM users WHERE name=%s AND password=%s", (u, p))
    result = cursor.fetchone()
    # cursor.close()
    # conn.close()
 
    return result
 
def change():
    sql = "UPDATE users SET password = %s WHERE name = %s"
    val = ("new_password", "username")
    cursor.execute(sql, val)
    conn.commit()
    cursor.close()
    conn.close()
 
if 's' in l:
    u = input('ENTER YOUR USERNAME:\n')
    e = input('ENTER YOUR EMAIL: \n')
    p = input('ENTER YOUR PASSWORD: \n')
    b = input('WHAT IS THE NAME OF YOUR FAVOURITE BOOK: \n')
    signup("u", "e", "p", "b")
elif 'l' in l:
    username = input('ENTER YOUR USERNAME: \n')
    password = input('ENTER THE PASSWORD: \n')
    login(username, password)

    if login(username,password):
        print("Login successful")
 
        engine = pyttsx3.init() 
        voices = engine.getProperty('voices')
        r = 145
        engine.setProperty('rate',r)
 
        engine.setProperty('voice', voices[1].id)
 
 
 
        
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
 
 
 
        if __name__ == "__main__":
            wishMe()
            print('')
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
                    speak(f'ok opening {query}')
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
                elif 'profile' in query:
                    p = input('Do you want to change password')
                    speak('Do you want to change password')
                    if 'y' in p:
                        change()
                    else:
                        print('Ok no problem')
                        speak('Ok no problem')
 
                elif 'what is the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    print(strTime)
                    speak(f'{name}....the time is{strTime}')
                elif 'joke' in query:
                    def jokes1():
                        f=open('E:\Class- 12\Computer Project\Jokes.txt','r')
                        open('Jokes.txt','r')
                        lines=f.read()
                        read1=lines.splitlines()
                        p = random.choice(read1)
                        print(p)
                        speak(p)
 
                    jokes1()
                elif '.in' in query:
                    webbrowser.open(f'www.{query}')
                elif 'news' in query:
                    print('1. International news')
                    print('2. Indian news')
                    o = input('Enter you choice:\n')
                    if o == '1':
                        international_news()
                    elif 0 == '2':
                        indian_news()
                elif 'international news' in query:
                    international_news()
                elif 'national news' in query:
                    indian_news()
                elif 'weather' in query:
                    import requests
                    city = input('Enter the city name:')
                    print(city)
                    speak(f'Showing weather report for {city}')
                    url = 'https://wttr.in/{}'.format(city)
                    res = requests.get(url)
                    print(res.text)
                elif 'calculator' in query:
        
                    cal = Tk()
                    cal.title("Calculator")
                    
                    expression = "" 
                    
                    def press(num):  
                        global expression 
                        expression = expression + str(num) 
                        equation.set(expression) 
                    
                    def equalpress():
                        try: 
                            global expression 
                            total = str(eval(expression)) 
                            equation.set(total)
                            expression = ""
                        except: 
                            equation.set(" error ") 
                            expression = "" 
                    
                    def clear(): 
                        global expression 
                        expression = "" 
                        equation.set("") 
                    
                    equation = StringVar() 
                    
                    expression_field = Entry(cal, textvariable=equation)
                    expression_field.grid(columnspan=4, ipadx=70) 
                    equation.set('enter your expression') 
                    
                    button1 = Button(cal, text=' 1 ', fg='black', bg='cyan', 
                                    command=lambda: press(1), height=1, width=7) 
                    button1.grid(row=2, column=0) 
                    
                    button2 = Button(cal, text=' 2 ', fg='black', bg='cyan', 
                                    command=lambda: press(2), height=1, width=7) 
                    button2.grid(row=2, column=1) 
                    
                    button3 = Button(cal, text=' 3 ', fg='black', bg='cyan', 
                                    command=lambda: press(3), height=1, width=7) 
                    button3.grid(row=2, column=2) 
                    
                    button4 = Button(cal, text=' 4 ', fg='black', bg='cyan', 
                                    command=lambda: press(4), height=1, width=7) 
                    button4.grid(row=3, column=0) 
                    
                    button5 = Button(cal, text=' 5 ', fg='black', bg='cyan', 
                                    command=lambda: press(5), height=1, width=7) 
                    button5.grid(row=3, column=1) 
                    
                    button6 = Button(cal, text=' 6 ', fg='black', bg='cyan', 
                                    command=lambda: press(6), height=1, width=7) 
                    button6.grid(row=3, column=2) 
                    
                    button7 = Button(cal, text=' 7 ', fg='black', bg='cyan', 
                                    command=lambda: press(7), height=1, width=7) 
                    button7.grid(row=4, column=0) 
                    
                    button8 = Button(cal, text=' 8 ', fg='black', bg='cyan', 
                                    command=lambda: press(8), height=1, width=7) 
                    button8.grid(row=4, column=1) 
                    
                    button9 = Button(cal, text=' 9 ', fg='black', bg='cyan', 
                                    command=lambda: press(9), height=1, width=7) 
                    button9.grid(row=4, column=2) 
                    
                    button0 = Button(cal, text=' 0 ', fg='black', bg='cyan', 
                                    command=lambda: press(0), height=1, width=7) 
                    button0.grid(row=5, column=0) 
                    
                    plus = Button(cal, text=' + ', fg='black', bg='cyan', 
                                command=lambda: press("+"), height=1, width=7) 
                    plus.grid(row=2, column=3) 
                    
                    minus = Button(cal, text=' - ', fg='black', bg='cyan', 
                                command=lambda: press("-"), height=1, width=7) 
                    minus.grid(row=3, column=3) 
                    
                    multiply = Button(cal, text=' * ', fg='black', bg='cyan', 
                                    command=lambda: press("*"), height=1, width=7) 
                    multiply.grid(row=4, column=3) 
                    
                    divide = Button(cal, text=' / ', fg='black', bg='cyan', 
                                    command=lambda: press("/"), height=1, width=7) 
                    divide.grid(row=5, column=3) 
                    
                    equal = Button(cal, text=' = ', fg='black', bg='cyan', 
                                command=equalpress, height=1, width=7) 
                    equal.grid(row=5, column=2) 
                    
                    clear = Button(cal, text='Clear', fg='black', bg='cyan', 
                                command=clear, height=1, width=7) 
                    clear.grid(row=5, column='1') 
                    
                    cal.mainloop()
        
                elif 'play game' in query:
                    print('1. HANGMAN')
                    print('2. TAMBOLA')
                    print('3. ROCK,PAPER AND SCISSOR')
                    print('4. RANDOM CHOICE')
                    speak('Enter your choice')
                    z = input('Enter your choice: \n')
                    if z == '1':
                        def hangman():
                            ans=input('Welcome to Hangman! All the best! Input start to start:')
                            if (ans=='start'):
                                words= ('majestic', 'tremendous', 'righteous', 'knowledgeable', 'flabbergasting', 'arbitrary', 'incomprehensibilities', 'hypothetically', 'subsequently', 'nauseous')
                                sel_word=random.choice(words)
                                print ('RULE: \n1. You have 7 wrong guesses.')
                                for i in sel_word:
                                    print ('_', end=' ')
                                    letters=list(sel_word)
                                    wrong_guesses=0
                                    t=0
                                    d=0
                                    guessed_letters=''
                                    HANGMAN = {1:
                            """
                            ------
                            |    |
                            |    O
                            |
                            |
                            |
                            |
                            |
                            |
                            ----------
                            """,
                            2:
                            """
                            ------
                            |    |
                            |    O
                            |   -+-
                            | 
                            |   
                            |   
                            |   
                            |   
                            ----------
                            """,
                            3:
                            """
                            ------
                            |    |
                            |    O
                            |  /-+-
                            |   
                            |   
                            |   
                            |   
                            |   
                            ----------
                            """,
                            4:
                            """
                            ------
                            |    |
                            |    O
                            |  /-+-/
                            |   
                            |   
                            |   
                            |   
                            |   
                            ----------
                            """,
                            5:
                            """
                            ------
                            |    |
                            |    O
                            |  /-+-/
                            |    |
                            |   
                            |   
                            |   
                            |   
                            ----------
                            """,
                            6:
                            """
                            ------
                            |    |
                            |    O
                            |  /-+-/
                            |    |
                            |    |
                            |   | 
                            |   | 
                            |   
                            ----------
                            """,
                            7:
                            """
                            ------
                            |    |
                            |    O
                            |  /-+-/
                            |    |
                            |    |
                            |   | |
                            |   | |
                            |  
                            ----------
                            """}
                                while (wrong_guesses<7):
                                    guess=input('Enter a letter.')
                                    if guess in guessed_letters:
                                        print ('Please input another letter.')
                                    guessed_letters=guessed_letters+guess
                                    if guess in letters:
                                        print ('Correct guess!\n')
                                        d=0
                                        for q in sel_word:
                                            if q in guessed_letters:
                                                print (q, end=' ')
                                            else:
                                                print ('_', end=' ')
                                                d=100
                                        if d==0:
                                            print ('\nCongratulations! You won the game!')
                                            break
                                    else:
                                        wrong_guesses=wrong_guesses+1
                                        print ('Wrong guess!\n')
                                        print(HANGMAN[wrong_guesses])
                                    print ('\n', guessed_letters)
                                    for q in sel_word:
                                            if q in guessed_letters:
                                                print (q, end=' ')
                                            else:
                                                print ('_', end=' ')
                                if wrong_guesses==7:
                                    print ('Woops! You have been hanged!')      
                            else:
                                print ("Do you want to start or no? \'_\'")
                        hangman()
                    elif z == '2':
                        def tambola():
                            import random as rd
 
                            a=[]
 
 
                            bot = Tk()
                            bot.title('BOT')
                            bot.configure(bg="red")
                            bot.geometry("700x500")
                            bot_tit=Label(text="Hello I am a Tambola Bot\n^_^",fg="white",padx=50,pady=70,
                                        font="algerian 28 bold",bg="orange",borderwidth=10,relief=SUNKEN)
                            bot_tit.pack(fill=X,padx=50,pady=50)
 
                            bot.mainloop()
 
 
                            ask=str(input("When You Want to Start Plz Press Enter."))
 
                            if ask=="":
                                while len(a)<90:    
                                    r=rd.randrange(1,91)   
                                    if r not in a:
                                        a.append(r)
                            elif ask!="" :
                                print("Plz Enter A right Comand") 
 
 
                            print("\n\nHere are your tickets:\n")
 
                            for i in range(90):
                                print("%7d"%(a[i]),end=" ")
                                if (i+1)%5==0:
                                    print()
                                if (i+1)%15==0:
                                    print()
 
                            win = Tk()
                            win.title("Random Number generator")
                            win.configure(bg="black")
                            win.geometry('600x400+200+100')
                            win.minsize(600,400)
                            win.maxsize(600,400)
 
                            def rnum():
                                n = rd.choice(a)
                                l = Label(win , text=f"---->>>>The number is : {n} <<<<----" ,
                                        width=30 , height=5 ,
                                        bg='white', fg='red' ,
                                        font="Blackletter 15"  )
                                l.place(x=130,y=100)
 
                                p = a.index(n)
                                a.pop(p)
                                try:
                                    n = rd.choice(a)
                                    pass
                                except IndexError:
                                    l = Label(win , text="<<<<<---- The Game is Finished ---->>>>>" , width=30 , height=5,
                                    bg='white', fg='red' , font="Blackletter 15" )
                                    l.place(x=130,y=100)
 
                            h = Button(win , text='Next' , command=rnum , bd=8 , bg='white' ,
                                            fg='black',
                                        highlightbackground='navy', height=2 ,
                                        width=10 , font='Blackletter 15' ,
                                        activebackground='black',activeforeground= 'white' )
                            h.pack(pady=10)
 
                            def QUIT():
                                win.destroy()
 
 
 
                            q = Button(win , text='Quit' , command=QUIT , bd=8 , bg='white' ,
                                        fg='black',
                                        highlightbackground='grey', height=2 ,
                                        width=10 , font= "Blackletter 15" ,
                                        activebackground='black',activeforeground= 'white' )
                            q.place(x=232,y=270)
 
 
                            mainloop()
 
 
                            print("Thanks for playing")
                        tambola()
                    elif z == '3':
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
                                R11 = input('')
                                print('do you want to play another game')
                                R12 = input('')
 
                                if('yes' in R12):
                                    o = True
                                elif('no' in R12):
                                    o = False    
                                if (o):
                                    print('Alright I have started a game \n In this game i will guess left or right \n And you will also guess the same \n if you guessed what I chose you get a point \n Else I get a point')
                                    print('Should I start the Game')
                                    R13 = input('')
                                        
                                    if('yes' in R13):
                                        R13 = True
                                    else:
                                        t = False
                        gamewin()
                    elif z == '4':
                        def choice(q,w):
                            if q == B:
                                return True
                            elif q == 'l':
                                if w == 'r':
                                    return False
                            elif q == 'r':
                                if w == 'l':
                                    return False
                            q = None
                            y = 0
 
                            v = 0
                            h = 0  
                            d = int(input('ENTER NO. OF TIMES YOU WANT TO PLAY'))  
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
                        choice()
    else:
        print("Login failed")
        p = input('Forgot password')
        p = p.lower()
        if p == 'yes':
            r = input('Enter your favourite book name')
            if login(use,r):
                def hh():
                    cursor.execute("SELECT * FROM users WHERE name=%s AND book=%s", (use, r))
                    result = cursor.fetchone()
                    cursor.close()
                    conn.close()
                    return result
                hh()
            else:
                pass
                
 
        elif p == 'no':
            print('OK try again login in')
            # speak('OK try again login in')
 
 
 
    '''COPYRIGHTED BY EXAMBLASTERS'''
 

