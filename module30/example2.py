from bs4 import BeautifulSoup

html_content ="""
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>Welcome to bs4</h1>
 <p class="intro">Beautiful soup makes web scraping easy</p>
<div id="content">
    <p>Here are some links</p>
    <a href="http://example.com/page1">Link 1</a>
    <a href="http://example.com/page2">Link 2</a>
    <a href="http://example.com/page3">Link 3</a>
    
</div>
</body>
</html>
 
 
 
 """

soup =BeautifulSoup(html_content, 'html.parser')
print("Title of the page:", soup.title.text)

intro_text=soup.find('p', class_='intro').text
print("Intro Text:", intro_text)

div_content =soup.find('div', id='content')
links =div_content.find_all('a')
for link in links:
    print("Link:", link['href'])

first_link= soup.find('a')
print("First link text :", first_link.text)
print("Next sibling of the first link:", first_link.next_siblingp)


paragraphs = soup.select('div#content p')
for paragraph in paragraphs:
    print("Paragraph inside content:", paragraph.text)


    new_tag = soup.new_tag('b')
    new_tag.string ="Important"
    soup.h1.append(new_tag)
    print("Modified h1 tag:", soup.h1)
