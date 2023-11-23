import pandas as pd
import requests

proxies = {
    'https': 'http://host:179.108.169.20:8080'
}


def get_category():
    url = 'https://catalog.wb.ru/catalog/gift11/catalog?TestGroup=no_test&TestID=no_test&appType=1&cat=130603&curr=rub&dest=-1257786&sort=popular&spp=28'
    headers = {
        "Accept": "*/*",
        "Accept-Language": "ru-RU,ru;q=0.9,en-RU;q=0.8,en;q=0.7,en-US;q=0.6,uk;q=0.5,ka;q=0.4,be;q=0.3,ar;q=0.2",
        "Connection": "keep-alive",
        "DNT": "1",
        "Origin": "https://www.wildberries.ru",
        "Referer": "https://www.wildberries.ru/catalog/podarki/detyam/igrushki",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "sec-ch-ua": "^\^",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "^\^"
    }
    response = requests.get(url=url, headers=headers, proxies=proxies)
    return response.json()


def prepare_items(response):
    products = []

    products_raw = response.get('data', {}).get('products', None)

    if products_raw != None and len(products_raw) > 0:
        for product in products_raw:
            products.append({
                'brand': product.get('brand', None),
                'name': product.get('name', None),
                'sale': product.get('sale', None),
                'priceU': float(product.get('priceU', None)) / 100 if product.get('priceU', None) != None else None,
                'salePriceU': float(product.get('salePriceU', None)) / 100 if product.get('salePriceU',
                                                                                          None) != None else None,
            })

    return products


def main():
    response = get_category()
    products = prepare_items(response)
    print(products)


if __name__ == '__main__':
    main()
