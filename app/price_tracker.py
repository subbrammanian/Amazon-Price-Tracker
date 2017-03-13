from lxml import html
import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}


def validateLink(product_link):
    page_content = requests.get(product_link, headers=headers)
    return page_content.status_code == 200


def getProductDetails(product_link):
    page_content = requests.get(product_link, headers=headers)
    if page_content.status_code >= 400:
        return -1

    tree = html.fromstring(page_content.content)

    # Find the price (handling different types of display)
    price = None
    price = tree.xpath('//span[@id="priceblock_saleprice"]/text()')
    if not price:
        price = tree.xpath('//span[@id="priceblock_ourprice"]/text()')

    if not price:
        price = tree.xpath('//span[@id="priceblock_dealprice"]/text()')    	
    if not price:
        price = tree.xpath(
            '//span[@class="a-size-medium a-color-price header-price"]/text()')
    if not price:
        price = tree.xpath(
            '//span[@class="a-size-medium a-color-price offer-price a-text-normal"]/text()')

    title = tree.xpath('//title/text()')
    prod_details = title[0].split(':')[0:2]
    if not price: price = None
    prod_details.append(str(min(price)))
    prod_details = map(str.strip, prod_details)
    print prod_details
    return prod_details


if __name__ == "__main__":
    product_link='https://www.amazon.com/Mcoplus-Portable-Aluminium-88522441&sr=8-2-spons&keywords=sony+head&psc=1'
    print getProductDetails(product_link)
