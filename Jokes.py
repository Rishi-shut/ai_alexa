import random

def jokes1():
    # f=open('E:\Class- 12\Computer Project\Jokes.txt','r')
    f=open('Jokes.txt','r',encoding='utf-8')
    lines=f.read()
    read1=lines.splitlines()
    print(random.choice(read1))

jokes1()
