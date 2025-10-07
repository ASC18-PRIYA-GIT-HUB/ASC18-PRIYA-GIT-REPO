store_name = "ShopEase"
welcome_message = f"Welcome to {store_name} - Your Online Marketpalce!"
print(welcome_message)
item_count = 150
item_price = 29.99
is_available = True
item_description = "A varsatile gadget for everyday use."
item_tags = {"gedget", "electroics", "utility"}
item_details ={"barnd" : "TechCorp", "warrenty": "2 years"}
item_id = None
print(f"Item Count: {item_count}")
print(f"Item Price: ${item_price}")
print(f"Is Available: {is_available}")
print(f"Item description: {item_description}")
print(f"Item Tags: {item_tags}")
print(f"Item Details: {item_details}")
print(f"Item ID: {item_id}")
total_cost = item_count * item_price
total_cost_str = str(total_cost)
print("Total Cost for {item_count} items: ${total_cost_str}")
item_count_str = "200"
item_count_int = int(item_count_str)
print(f"Converted ITem Count: {item_count_int}")
item_count_float = float(item_count_int)
print(f"Item count as float: {item_count_float}")