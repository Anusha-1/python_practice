import requests
link="https://dataquestio.github.io/web-scraping-pages/simple.html"
page=requests.get(link)
print(page)
print(page.content)

#pip install bs4

from bs4 import BeautifulSoup
soup=BeautifulSoup(page.content,"html.parser")
#print(soup.prettify()) #nice format
#print(list(soup.children))

#data =[type(item) for item in list(soup.children)]
#html =list(soup.children)[2]
#print(list(html.children))


#print(soup.find_all('p'))
