import requests
from bs4 import BeautifulSoup

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
                print(x.text.strip())
                flag+=1
        else:
            break  

international_news()
def indian_news():
    url = 'https://www.indiatoday.in/india'
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find('body').find_all('h2')
    
    flag=0
    for x in list(dict.fromkeys(headlines)):
        if flag<5: 
            print(x.text.strip())
            flag+=1
        else:
            break  
# indian_news()
