import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DADOS_DIR = BASE_DIR / "dados"

customers = pd.read_csv(DADOS_DIR  / "olist_customers_dataset.csv")
geolocation = pd.read_csv(DADOS_DIR  / "olist_geolocation_dataset.csv")
order_items = pd.read_csv(DADOS_DIR  / "olist_order_items_dataset.csv")
order_payments = pd.read_csv(DADOS_DIR  / "olist_order_payments_dataset.csv")
order_reviews = pd.read_csv(DADOS_DIR  / "olist_order_reviews_dataset.csv")
orders = pd.read_csv(DADOS_DIR  / "olist_orders_dataset.csv")
products = pd.read_csv(DADOS_DIR  / "olist_products_dataset.csv")
sellers = pd.read_csv(DADOS_DIR  / "olist_sellers_dataset.csv")
product_category = pd.read_csv(DADOS_DIR  / "product_category_name_translation.csv")

# Tipagem de dados correta - Orders
orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
orders['order_approved_at'] = pd.to_datetime(orders['order_approved_at'])
orders['order_delivered_carrier_date'] = pd.to_datetime(orders['order_delivered_carrier_date'])
orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date'])
orders['order_estimated_delivery_date'] = pd.to_datetime(orders['order_estimated_delivery_date'])

# Tipagem de dados correta - Order Items
order_items['shipping_limit_date'] = pd.to_datetime(order_items['shipping_limit_date'])

# Removendo ordens duplicadas em orders
orders = orders.drop_duplicates('order_id')