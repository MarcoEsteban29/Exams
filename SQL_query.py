import pandas as pd
import sqlite3


def main():
    with sqlite3.connect("S30 ETL Assignment.db") as conn:
        #Purely SQL query to get the desired output
        total_quantity_query = '''SELECT customer_id, item_name, age, sum(quantity) as quantity
        from (SELECT sales_id,quantity,item_name from orders 
        INNER JOIN items 
        ON items.item_id = orders.item_id) as OrderItems
        INNER JOIN (SELECT sales_id, customers.customer_id as customer_id, age from customers
        INNER JOIN sales 
        ON customers.customer_id = sales.customer_id) as SalesCustomers
        ON OrderItems.sales_id = SalesCustomers.sales_id
        WHERE (age >= 18 AND age <= 35) and (quantity > 0 and quantity != '')
        GROUP BY customer_id, item_name, age
        ;'''
        total_quantity_table = pd.read_sql_query(total_quantity_query,conn)
        total_quantity_table.to_csv('./total-quantity-of-items-sql-query.csv',sep=';', index=False)

    
if __name__ == "__main__":
    main()