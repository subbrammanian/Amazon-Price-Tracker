from lxml import html
import requests

product_link = 'https://www.amazon.com/Philips-Bikini-Trimmer-Shaving-Head/dp/B00TYSQXIC/ref=sr_1_1_s_it?s=beauty&ie=UTF8&qid=1488499777&sr=1-1&keywords=trimmer+for+women'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}



page_content = requests.get(product_link,headers=headers)
tree = html.fromstring(page_content.content)
price = tree.xpath('//span[@id="priceblock_saleprice"]/text()')

#Find the price (different types of display)
if not price:
	price = tree.xpath('//span[@id="priceblock_ourprice"]/text()')
if not price:
	price = tree.xpath('//span[@class="a-size-medium a-color-price header-price"]/text()')
if not price:
	price = tree.xpath('//span[@class="a-size-medium a-color-price offer-price a-text-normal"]/text()')

price = map(str.strip,price)

for v in price:
	print v

