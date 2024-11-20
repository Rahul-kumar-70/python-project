"""
Write a Python class Inventory with attributes like item_id, item_name, stock_count, and price, and methods like add_item,
 update_item, and check_item_details.Use a dictionary to store the item details, where the key is the item_id
  and the value is a dictionary containing the item_name, stock_count, and price.
"""
class Inventory:
    def __init__(self):
        self.inventory={}
    def add_item(self,item_id,item_name,stock_count,price):
        self.inventory[item_id]={'item_name':item_name,'stock_count':stock_count,'price':price}
    def update_item(self,item_id,stock_count,price):
        if item_id in self.inventory:
            self.inventory[item_id]['stock_count']=stock_count
            self.inventory[item_id]['price'] = price
        else:
            print("items not found in Inventory ")
    def check_item_details(self,item_id):
        if item_id in self.inventory:
            item=self.inventory[item_id]
            print("item_id:",item_id,', item_name:',item['item_name'],', stock_count:',item['stock_count'],', price:',item['price'])


inv=Inventory()
inv.add_item('E101','laptop',20,20000)
inv.add_item('E102','T.V',21,10000)
inv.add_item('E103','Mobail',15,15000)

inv.check_item_details('E101')
inv.check_item_details('E102')
inv.check_item_details('E103')
print("------------------------------------------------------------------")
print("After update")
print("------------------------------------------------------------------")
inv.update_item('E101',30,30000)
inv.update_item('E102',80,20000)
inv.update_item('E103',10,10000)

inv.check_item_details('E101')
inv.check_item_details('E102')
inv.check_item_details('E103')