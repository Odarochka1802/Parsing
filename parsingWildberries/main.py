import pandas as pd
import requests

proxies = {
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
    response = requests.get(url, headers=headers, proxies=proxies)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")


def prepare_items(response):
    products = []

    products_raw = response.get('data', {}).get('products')

    if products_raw and len(products_raw) > 0:
        for product in products_raw:
            products.append({
                'brand': product.get('brand'),
                'name': product.get('name'),
                'sale': product.get('sale'),
                'priceU': float(product.get('priceU', 0)) / 100,
                'salePriceU': float(product.get('salePriceU', 0)) / 100,
            })

    return products


def main():
    response = get_category()
    products = prepare_items(response)
    df = pd.DataFrame(products)
    print(df)


if __name__ == '__main__':
    main()
