"""
Write a Python class Restaurant with attributes like menu_items, book_table, and customer_orders, and methods like add
_item_to_menu, book_tables, and customer_order.
Perform the following tasks now:

Now add items to the menu.
Make table reservations.
Take customer orders.
Print the menu.
Print table reservations.
Print customer orders.
Note: Use dictionaries and lists to store the data.
"""
class Restaurant:
    def __init__(self):
        self.menu_items={}
        self.book_table=[]
        self.customer_orders=[]
    def add_item_to_menu(self,item,price):
        self.menu_items[item]=price
    def book_tables(self,table):
        self.book_table.append(table)
    def customer_order(self,table,order):
        order_details={'Table_Number':table,"order":order}
        self.customer_orders.append(order_details)
    def print_menu(self):
        print("Items\tPrice")
        for i,j in self.menu_items.items():
            print("{}\t:{}".format(i,j))
    def print_reservations(self):
        for i in self.book_table:
            print("Table:{}".format(i))
    def print_customer_orders(self):
        for i in self.customer_orders:
            print("Table:{}\t{}".format(i['Table_Number'],i['order']))
res=Restaurant()
print("Menu Card")
print("---------------------------------------")
res.add_item_to_menu('Rice',20)
res.add_item_to_menu('Chapati',10)
res.add_item_to_menu('eggs',20)
res.add_item_to_menu('fish',50)

res.book_tables(1)
res.book_tables(2)
res.book_tables(3)
res.book_tables(4)

res.customer_order(1,'Rice')
res.customer_order(1,'eggs')
res.customer_order(2,'Rice')
res.customer_order(2,'fish')
print(res.customer_orders)

print("---------------------------------------")
res.print_reservations()
print("---------------------------------------")
res.print_customer_orders()