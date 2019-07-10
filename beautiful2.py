import beautifulsoup
import schedule
import time

def job():
  beautifulsoup.load('https://www.nytimes.com/section/world')
  beautifulsoup.load('https://www.nytimes.com/section/us')
  beautifulsoup.load('https://www.nytimes.com/section/politics')
  beautifulsoup.load('https://www.nytimes.com/section/opinion')
  beautifulsoup.load('https://www.nytimes.com/section/nyregion')
  beautifulsoup.load('https://www.nytimes.com/section/business')
  beautifulsoup.load('https://www.nytimes.com/section/technology')
  beautifulsoup.load('https://www.nytimes.com/section/science')
  beautifulsoup.load('https://www.nytimes.com/section/health')
  beautifulsoup.load('https://www.nytimes.com/section/sports')
  beautifulsoup.load('https://www.nytimes.com/section/arts')
  beautifulsoup.load('https://www.nytimes.com/section/books')
  filenames = ['world.txt', 'us.txt', 'politics.txt', 'opinion.txt', 'nyregion.txt', 'business.txt', 'technology.txt', 'science.txt', 'health.txt', 'sports.txt','arts.txt', 'books.txt']
  with open('home.txt', 'w') as outfile:
      for fname in filenames:
          with open(fname) as infile:
              outfile.write(infile.read())
job()
schedule.every(2).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
