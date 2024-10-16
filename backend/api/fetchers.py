import requests
from .models import WHThings


class ProductFetcher:
    def __init__(self, articules):
        self.articules = articules
        self.products = []

    def fetch_data(self):
        try:
            response = requests.get(
                f'https://card.wb.ru/cards/v2/detail?appType=1&'
                f'curr=rub&dest=-59202&'
                f'spp=30&ab_testing=false&nm={self.articules}',
                timeout=10
            )
            response.raise_for_status()
            data = response.json().get('data', {})
            self.products = data.get('products', [])
        except requests.exceptions.RequestException as req_err:
            print(f"Ошибка запроса: {req_err}")
        except ValueError:
            print("Ошибка при обработке JSON ответа")

    def get_product_info(self):
        if not self.products:
            return {"error": "Товар не найден или нет данных"}

        product_info_list = []
        for product in self.products:
            brand = product.get('brand', "Нет данных")
            colors = product.get('colors', [])
            color = colors[0].get('name', "Нет данных") if colors else "Нет данных"
            entity = product.get('entity', "Нет данных")
            name = product.get('name', "Нет данных")
            reviewRating = product.get('reviewRating', None)
            supplier = product.get('supplier', "Нет данных")
            supplierId = product.get('supplierId', None)
            supplierRating = product.get('supplierRating', None)

            sizes = product.get('sizes', [{}])
            qty = sizes[0].get('stocks', [{}])[0].get('qty', None) if sizes and sizes[0].get('stocks') else None
            product_id = product.get('id', "Нет данных")

            price_basic = sizes[0].get('price', {}).get('basic', None)
            price_basic = price_basic / 100 if price_basic else None

            product_info = {
                'brand': brand,
                'color': color,
                'entity': entity,
                'name': name,
                'review_rating': reviewRating,
                'supplier': supplier,
                'supplier_id': supplierId,
                'supplier_rating': supplierRating,
                'product_id': product_id,
                'price_basic': price_basic,
                'qty': qty,
            }

            product_info_list.append(product_info)

        return product_info_list

    def save_to_db(self):
        product_info_list = self.get_product_info()
        if isinstance(product_info_list, dict) and "error" in product_info_list:
            return {"error": "Данных нет для записи в базу"}

        for product_info in product_info_list:
            WHThings.objects.update_or_create(
                product_id=product_info['product_id'],
                defaults={
                    'brand': product_info['brand'],
                    'color': product_info['color'],
                    'entity': product_info['entity'],
                    'name': product_info['name'],
                    'review_rating': product_info['review_rating'],
                    'supplier': product_info['supplier'],
                    'supplier_id': product_info['supplier_id'],
                    'supplier_rating': product_info['supplier_rating'],
                    'price_basic': product_info['price_basic'],
                    'qty': product_info['qty'],
                }
            )
        return {"success": "Данные успешно сохранены в базу данных"}