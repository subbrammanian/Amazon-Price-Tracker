from lxml import html
import requests



headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

def validateLink(product_link):
	page_content = requests.get(product_link,headers=headers)
	return page_content.status_code==200

def getPrice(product_link):
	page_content = requests.get(product_link,headers=headers)
	if page_content.status_code>=400:
		return -1
	
	tree = html.fromstring(page_content.content)
	
	#Find the price (handling different types of display)
	price = tree.xpath('//span[@id="priceblock_saleprice"]/text()')
	if not price:
		price = tree.xpath('//span[@id="priceblock_ourprice"]/text()')
	if not price:
		price = tree.xpath('//span[@class="a-size-medium a-color-price header-price"]/text()')
	if not price:
		price = tree.xpath('//span[@class="a-size-medium a-color-price offer-price a-text-normal"]/text()')

	price = map(str.strip,price)

	if price:
		return min(price)
	else:
		return None

if __name__=="__main__":
	product_link = 'https://www.amazon.com/Mcoplus-Portable-Aluminium-Panasonic-Camcorders/dp/B0156BE9JK/ref=sr_1_2?ie=UTF8&qid=1488522441&sr=8-2-spons&keywords=sony+head&psc=1'
	print getPrice(product_link)