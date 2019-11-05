import bs4 as bs
import urllib.request
import threading


Results = []
def reddit_headings(_input):
    reddit = urllib.request.urlopen('https://www.reddit.com/r/programming/').read()
    soup = bs.BeautifulSoup(reddit,'lxml')
    for h in soup.find_all('h3'):
        if (_input in h.string):
            Results.append(h.string + '  https://www.reddit.com/r/programming/')

def ycombninator_headings(_input):
    ycombninator = urllib.request.urlopen('http://news.ycombinator.com/').read()
    soup = bs.BeautifulSoup(ycombninator, 'lxml')
    for a in soup.find_all('a'):
        if (_input in a.text):
            Results.append(a.text + '  http://news.ycombinator.com/')

def theguardian_headings(_input):
    theguardian = urllib.request.urlopen('http://www.theguardian.com/us/technology').read()
    soup = bs.BeautifulSoup(theguardian, 'lxml')
    for a in soup.find_all('a'):
        if (_input in a.text):
            Results.append(a.text + '  http://www.theguardian.com/us/technology')

def nytimes_headings(_input):
    nytimes = urllib.request.urlopen('http://www.nytimes.com/pages/technology/index.html').read()
    soup = bs.BeautifulSoup(nytimes, 'lxml')
    for a in soup.find_all('a'):
        if (_input in a.text):
            Results.append(a.text + '  http://www.nytimes.com/pages/technology/index.html')


word = input("Enter the word: ")
reddit_thread = threading.Thread(target=reddit_headings, args= [word])
ycombninator_thread = threading.Thread(target=ycombninator_headings, args= [word])
theguardian_thread = threading.Thread(target=theguardian_headings, args= [word])
nytimes_thread = threading.Thread(target=nytimes_headings, args= [word])
reddit_thread.start()
ycombninator_thread.start()
theguardian_thread.start()
nytimes_thread.start()
reddit_thread.join()
ycombninator_thread.join()
theguardian_thread.join()
nytimes_thread.join()
for result in Results:
    print(result)