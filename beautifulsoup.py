from urllib.request import urlopen
import random
from bs4 import BeautifulSoup
import inflect
import  nltk
from nltk.tokenize import word_tokenize
p = inflect.engine()
text = word_tokenize("And now for something completely different")
def load(link):
    if link.split("/")[3] == "":
        file = "home"
    elif link.split("/")[3] == "section":
        file = link.split("/")[4]
    csv = ''
    html_1 = urlopen(link)
    soup = BeautifulSoup(html_1, features = 'html.parser')
    articles = soup.find_all('article')
    for article in articles:
        title = article.find("h2").text.strip()
        if article.find("a").get('href')[0] == "/":
           href = 'https://www.nytimes.com' + article.find("a").get('href')
        else:
           href = article.find("a").get('href')
        img = "NO-IMG"
        description = "NO-DESCRIPTION"
        if article.find("img"):
            img = article.find("img").get('src')
        if article.find('p'):
            description = article.find('p')
            if article.find("li"):
                descriptions = article.find_all('li')
                description = '['
                for d in descriptions:
                    description+="'" + d.text.strip() + "',"
                description+=']'
            else:
                description = description.text.strip()
        if article.find(attrs={"itemprop": "author"}):
            authors = article.find(attrs={"itemprop": "author"}).text.strip()
        csv+=title + '\t' + "'" + description + "'" + '\t' + href + '\t' + img + '\t' + authors + '\n'
    articles = csv.split("\n")
    converted = ""
    nouns = open('nounlist.txt').read()
    noun_list = nouns.split()
    nlen= len(noun_list) - 1
    for article in articles:
        title = article.split("\t")[0]
        words = title.split(" ")
        new_ary =  []
       # words_array = nltk.pos_tag(word_tokenize(title))
        for word in words:
            new = ''
            words_array = nltk.pos_tag(word_tokenize(word))
            if len(words_array) == 3 and (words_array[0][0] == "'" or words_array[2][0] == "'"):
               new+="'"
               if word_array[1][1] == 'NN' or word[1] == 'NNP' and len(word[0]) > 2:
                  if random.random() < 0.4:
                     new+= str(noun_list[random.randrange(0, nlen)]).capitalize()
                  else:
                     new+=word[0]
               elif word[1] == 'NNS' or word[1] == 'NNPS':
                  if random.random() < 0.4: 
                     new+=p.plural(str(noun_list[random.randrange(0, nlen)])).capitalize()
                  else:
                     new+=word[0]
               else:
                  new+=word[0]
               new+="'"
            else:
               for w in words_array:
                  if len(w[0]) < 3:
                     new+=w[0]
                  elif w[1] == 'NN' or w[1] == 'NNP' and w[0] != "'" and len(w[0]) > 2:
                     if random.random() < 0.4:
                        new+=str(noun_list[random.randrange(0, nlen)]).capitalize()
                     else:
                        new+=w[0]
                  elif w[1] == 'NNS' or w[1] == 'NNPS':
                     if random.random() < 0.4: 
                        new+=p.plural(str(noun_list[random.randrange(0, nlen)])).capitalize()
                     else:
                        new+=w[0]
                  else:
                     new+=w[0]
            new_ary.append(new)
        etc = ("\t").join(article.split("\t")[1:])
        new_t = " ".join(new_ary)
        converted +=  new_t + "\t" + etc + "\n"
    f = open("text/" + file + ".txt", "w").write(converted)
