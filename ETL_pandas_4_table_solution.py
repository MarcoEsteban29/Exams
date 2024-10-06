import pandas as pd
import sqlite3

order_table = item_table = sales_table = customer_table = None

def main():
    with sqlite3.connect("S30 ETL Assignment.db") as conn:
        #Queries to use for pandas solution
        orders_query = '''SELECT sales_id,item_id,quantity from orders'''
        items_query = '''SELECT item_id,item_name from items'''
        sales_query = '''SELECT sales_id, customer_id from sales'''
        customers_query = '''SELECT customer_id, age from customers'''


        order_table  = pd.read_sql_query(orders_query,conn)
        item_table  = pd.read_sql_query(items_query,conn)
        sales_table  = pd.read_sql_query(sales_query,conn)
        customer_table  = pd.read_sql_query(customers_query,conn)   

        orders_items = order_table.merge(item_table, on="item_id")
        sales_customers = sales_table.merge(customer_table, on="customer_id")

    #Pandas Solution
    ordered_sales = pd.merge(orders_items, sales_customers, on="sales_id")
    ordered_sales = ordered_sales[(ordered_sales['age'] >= 18) & (ordered_sales['age'] <= 35) & (ordered_sales['quantity'] > 0)]
    ordered_sales = ordered_sales[["customer_id", "age", "item_name", "quantity"]].dropna()
    ordered_sales['quantity'] = ordered_sales['quantity'].astype(int)

    total_item_quantity = ordered_sales.groupby(['customer_id','item_name','age'])['quantity'].sum().reset_index()
    total_item_quantity.rename(columns={'customer_id':'Customer', 'item_name':'Item', 'age':'Age', 'quantity':'Quantity'})
    total_item_quantity.to_csv('./total_quantites_of_item2.csv', sep=';', index=False)
        
if __name__ == "__main__":
    main()