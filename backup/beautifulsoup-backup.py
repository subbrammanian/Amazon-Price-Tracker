import urllib2
from bs4 import BeautifulSoup


link = "http://www.amazon.com/Sony-Dynamic-Headphones-MDR-XB50-B-Black/dp/B00HZD3VGU/ref=s9u_simh_gw_i1?_encoding=UTF8&fpl=fresh&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=&pf_rd_r=PW3DN1C5PSX8AA2AY4TR&pf_rd_t=36701&pf_rd_p=1cded295-23b4-40b1-8da6-7c1c9eb81d33&pf_rd_i=desktop"
headers = "'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'"

request = urllib2.Request(link)
request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36')

page = urllib2.urlopen(request)
soup = BeautifulSoup(page,"lxml")

f = open("pricehtm.html","w")

for line in soup.prettify():
	f.write(line.encode('ascii', 'ignore'))

f.close()

# To identify product category and type
# product_title = soup.title.string.split(':')
# print product_title
# product_title = [x.strip() for x in product_title]
# print product_title
# print "Category: ",product_title[2]
# print "Product: ",product_title[1]

# #Finding price

# # price = soup.find_all('span', class_="a-size-medium a-color-price")



# price = soup.find_all("span", attrs={"class": "a-size-medium a-color-price"})
# print type(price)
# print price
# for v in price:
# 	print v