from celery import shared_task
from .fetchers import ProductFetcher

@shared_task
def fetch_and_save_product(articules):
    fetcher = ProductFetcher(articules)
    fetcher.fetch_data()
    result = fetcher.save_to_db()
    return result