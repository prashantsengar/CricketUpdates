import requests
import time
from bs4 import BeautifulSoup as bs
import notify

last_over = 0.0
shout = {'4':'That\'s a four', '6':'Huge SIX', 'W':'A wicket fell down', '2' : 'That\'s a double', '1':'Single'}

def get_score(url):

    page = requests.get(url).text
    soup = bs(page, 'html.parser')

    cl = soup.find_all('div', {'class' : 'cb-min-bat-rw'})
    overs = cl[0].text.find('Ovs')
    

    overs = cl[0].text[overs-6: overs-1]
    try:
        overs = float(overs)
    except ValueError:
        try:
            overs = float(overs[1:])
        except:
            overs = overs.split('(')[1].split(')')
            overs = float(overs[0])
    
    urll = url.replace('scores','scorecard')
    print(urll)
    new_page = requests.get(urll).text
    soupp = bs(new_page, 'html.parser')
    card=soup.find_all('div', {'class' : 'cb-col cb-col-100 cb-scrd-hdr-rw'})
    card = card[0].find_all('span', {'class': 'pull-right'})
    card = card[0].text
    print(card)

    global last_over
    if last_over==overs or last_over==0.0:
    	last_over = (overs)
    	return

    	
    

    text = soup.find(text='Recent: ')
    recent_span = text.parent
    next_span = recent_span.findNext('span')

    score = next_span.text
    print(score)
    i = (float(overs) - float(last_over))*10

    last_over = (overs)
    if i==5:
    	i=1

    i = round(i)
    

    global shout
    for item in shout:
    	if item in score[-1-i:-1]:
            notify.notify(msg=shout[item])
            notify.notify(msg=card)

