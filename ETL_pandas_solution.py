import pandas as pd
import sqlite3

order_item_table = sales_customer_table = None

def main():
    with sqlite3.connect("S30 ETL Assignment.db") as conn:
        #Queries to use for pandas solution
        order_item_query = '''SELECT sales_id,quantity,item_name from orders 
        INNER JOIN items 
        ON items.item_id = orders.item_id;
        '''
        sales_customer_query = '''SELECT sales_id, customers.customer_id, age from customers
        INNER JOIN sales 
        ON customers.customer_id = sales.customer_id;
        '''  
        
        order_item_table  = pd.read_sql_query(order_item_query,conn)
        sales_customer_table  = pd.read_sql_query(sales_customer_query,conn)

    #Pandas Solution
    ordered_sales = pd.merge(order_item_table, sales_customer_table, on="sales_id")
    ordered_sales = ordered_sales[(ordered_sales['age'] >= 18) & (ordered_sales['age'] <= 35) & (ordered_sales['quantity'] > 0)]
    ordered_sales = ordered_sales[["customer_id", "age", "item_name", "quantity"]].dropna()
    ordered_sales['quantity'] = ordered_sales['quantity'].astype(int)

    total_item_quantity = ordered_sales.groupby(['customer_id','item_name','age'])['quantity'].sum().reset_index()
    total_item_quantity.rename(columns={'customer_id':'Customer', 'item_name':'Item', 'age':'Age', 'quantity':'Quantity'})
    total_item_quantity.to_csv('./total_quantites_of_item.csv', sep=';', index=False)
        
if __name__ == "__main__":
    main()