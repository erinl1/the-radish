#!/usr/bin/python3
print('Content-type: text/html\n')
import random
print('''
<html>
<head>
  <title>The Radish</title>
  <link rel="icon" href="radish.png">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
  <!-- Latest compiled and minified JavaScript -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">
  <link rel="stylesheet" type="text/css"
  href="https://fonts.googleapis.com/css?family=Abril+Fatface">
  <link rel="stylesheet" type="text/css"
  href="https://fonts.googleapis.com/css?family=Forum">
  <link rel="stylesheet" type="text/css"
  href="https://fonts.googleapis.com/css?family=Merriweather">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">
  <link rel="stylesheet" type="text/css" href="radish.css">
</head>

<body>
  <div class = 'flex-container header'><br>

<form action = 'radish.py' method = "GET">
  <div class = 'flex-container title' style = 'width: 100%'>
    <a href = 'home.py'><img src = 'title.png' style = 'height: 75px'></a>
    <hr>
<div class = 'row flex-container top'>
<div class = 'col-sm-1'>
<h5> <input class = 'link' name = 'page' type = 'submit' value = 'World'></h5>
</div>
<div class = 'col-sm-1'>
<h5><input class = 'link' name = 'page' type = 'submit' value = 'US'></h5>
</div>
<div class = 'col-sm-1'>
<h5><input class = 'link' name = 'page' type = 'submit' value = 'Politics'></h5>
</div>
<div class = 'col-sm-1'>
<h5><input class = 'link' name = 'page' type = 'submit' value = 'N.Y.'></h5>
</div>
<div class = 'col-sm-1'>
<h5><input class = 'link' name = 'page' type = 'submit' value = 'Business'></h5>
</div>
<div class = 'col-sm-1'>
<h5><input class = 'link' name = 'page' type = 'submit' value = 'Opinion'></h5>
</div>
<div class = 'col-sm-1'>
<h5><input class = 'link' name = 'page' type = 'submit' value = 'Tech'></h5>
</div>
<div class = 'col-sm-1'>
<h5><input class = 'link' name = 'page' type = 'submit' value = 'Science'></h5>
</div>
<div class = 'col-sm-1'>
<h5><input class = 'link' name = 'page' type = 'submit' value = 'Health'></h5>
</div>
<div class = 'col-sm-1'>
<h5><input class = 'link' name = 'page' type = 'submit' value = 'Sports'></h5>
</div>
<div class = 'col-sm-1'>
<h5><input class = 'link' name = 'page' type = 'submit' value = 'Arts'></h5>
</div>
<div class = 'col-sm-1'>
<h5><input class = 'link' name = 'page' type = 'submit' value = 'Books'></h5>
</div>
</div>
</form>
</div>
  <hr style = 'margin-top: -16px'>
''')
def web_print(name):
  master_ary = []
  pic_ary = []
  nopic_ary = []
  file = name
  s = open(file + '.txt', encoding='utf-8').read()
  s = s.encode('ascii', 'xmlcharrefreplace').decode()
  articles = s.split('\n')
  for article in articles:
    sections = article.split("\t")
    if len(sections) > 3:
      dict = {}
      dict["title"] = sections[0]
      dict["description"] = sections[1]
      dict["link"] = sections[2]
      dict["photo"] = sections[3]
      dict["author"] = sections[4] 
      master_ary.append(dict)
      if dict['photo'] == 'NO-IMG':
        nopic_ary.append(dict)
      else: 
        pic_ary.append(dict)
  return [master_ary, pic_ary, nopic_ary]
arys = web_print('home')
print('''
    <div class = 'row'style = 'border-bottom: grey solid thin'>
      <div class = 'col-md-8 rightB'>
''')
i = 0
while i < 2:
  pic_a = arys[1][random.randrange(len(arys[1]))]
  photo = pic_a["photo"]
  title = pic_a["title"]
  description = pic_a["description"]
  description = description.split("'")
  des = ''
  if description[1] != 'NO-DESCRIPTION':
    for d in description:
      if d != '' and d != "":
        des+= d + "<br>" 
  link = pic_a["link"]
  author = pic_a["author"]
  print('''<div class = 'right row flex-container'>
          <div class = 'col-md-8'> 
          <img src = ''' + photo +
        '''>
        </div>
      <div class = 'col-md-4'>
        <h4><a href = ' ''' + link + 
    ''' '> ''' + title +
         '''</a></h4><h5>''' +
      des + "<br>"
      + ''' </h5><p style = "color: #c14441">'''
 + author +   '''</p></div></div>''')
  i+=1
print("</div><div class = 'col-md-4'><div class = 'row flex-container'>")
i = 2
while i < 5 and i < len(arys[0]):
  ary = arys[0][i]
  author = ary["author"]
  title = ary["title"]
  description = ary["description"]
  description = description.split("'")
  des = ''
  if description[1] == 'NO-DESCRIPTION':
    des = ''  
  for d in description:
      if d != '' and d != "":
        des+= d + "<br>"
  link = ary["link"]
  print('''<div class = 'article' style="width: 95%; padding-left: 10px; border-bottom: grey solid thin"><h4 class = 'article'><a href = ' ''' + link + 
''' '><br> ''' + title +
       '''</a></h4><h5>''' +
    des + "</h5><p style = 'color: #c14441'>"
 + author +   "</p><br> </div><br><br>")
  i +=1
if 5 < len(arys[0]):
  ary = arys[0][5]
  author = ary["author"]
  title = ary["title"]
  description = ary["description"]
  description = description.split("'")
  des = ''
  if description[1] == 'NO-DESCRIPTION':
    des = ''  
  for d in description:
      if d != '' and d != "":
        des+= d + "<br>"
  link = ary["link"]
  print('''<div class = 'article' style="width: 95%; padding-left: 10px;"><h4 class = 'article'><a href = ' ''' + link +
''' '><br> ''' + title +
       '''</a></h4><h5>''' +
    des + "</h5><p style = 'color: #c14441'>"
 + author +   "</p><br> </div><br><br>")

print('''</div></div></div><div class = 'row flex-container bottom' style="border-bottom: grey solid thin">''')

i = 0
while i < 2 and i < len(arys[1]):
  ary = arys[1][random.randrange(len(arys[1]))]
  title = ary["title"]
  description = ary["description"]
  photo = ary['photo']
  author = ary['author']
  description = description.split("'")
  des = ''
  if description[1] == 'NO-DESCRIPTION':
    des = ''  
  for d in description:
      if d != '' and d != "":
        des+= d + "<br>"
  link = ary["link"]

  print('''
<div class = 'col-md-6'><div class = 'row flex-container'>
<div class = 'col-md-5'>''' + '''
<h4 class = 'article'><a href = ' ''' + link + 
''' '> ''' + title +
       '''</a></h4><h5>''' +
    des + "</h5><p style = 'color: #c14441'>"
 + author +
   "</p><br>")
  print('''</div><div class = 'col-md-7'><img src =' ''' + photo +
        ''' '></div></div></div>''')
  i+=1
print(''' </div></div>
 ''')
ary = arys[1][random.randrange(len(arys[1]))]
title = ary["title"]
author = ary["author"]
description = ary["description"]
photo = ary['photo']
description = description.split("'")
des = ''
if description[1] == 'NO-DESCRIPTION':
  des = ''  
for d in description:
   if d != '' and d != "":
      des+= d + "<br>"
link = ary["link"]
print('''<br>
<div class="flex-container" style="border-bottom: grey solid thin"><img src =' '''
 + photo +  ''' '><br><br><h4 class = 'article'><a href = ' ''' + link + 
''' '> ''' + title +
       '''</a></h4><h5>''' +
    des + "</h5><p style = 'color: #c14441'>"
 + author +   "</p><br>" + 
'''</div>
''')
if len(arys[2]) > 0:
  ary = arys[2][random.randrange(len(arys[2]))]
  title = ary["title"]
  author = ary["author"]
  description = ary["description"]
  description = description.split("'")
  des = ''
  if description[1] == 'NO-DESCRIPTION':
    des = ''  
  for d in description:   
    if d != '' and d != "":
      des+= d + "<br>"
  link = ary["link"]
  print('''<br><div class = 'row flex-container'>
<br><div class="col-md-6 right"><h4 class = 'article'><a href = ' ''' + link + 
''' '> ''' + title +
       '''</a></h4><h5>''' +
    des + "</h5><p style = 'color: #c14441'>"
 + author +   "</p><br></div>")
if len(arys[1]) > 0:
  ary = arys[1][random.randrange(len(arys[1]))]
  title = ary["title"]
  author = ary["author"]
  description = ary["description"]
  photo = ary['photo']
  description = description.split("'")
  des = ''
  if description[1] == 'NO-DESCRIPTION':
    des = ''  
  for d in description:
     if d != '' and d != "":
        des+= d + "<br>"
  link = ary["link"]
  print('''<div class="col-md-6"><br><img src =' '''
 + photo +  ''' '><br><br><h4 class = 'article'><a href = ' ''' + link + 
''' '> ''' + title +
       '''</a></h4><h5>''' +
    des + "</h5><p style = 'color: #c14441'>"
 + author +   "</p><br></div></div>" + 
'''
''')

#print("</div>")

print('''
  </div>
</body>
</html>
''')
