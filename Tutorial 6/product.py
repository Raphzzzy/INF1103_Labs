
class product:
    # Constructor
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    # Get Product ID
    def get_product_id(self):
        return self.__product_id

    # Update stock quantity
    def update_stock(self, quantity):
        if quantity >= 0:
            self.__stock = quantity
        else:
            print("Invalid stock quantity")

    # Display product information
    def display_information(self):
        print(f"Product ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock} units")
        print("---------------------------")

    # Convert product object into dictionary
    def to_dict(self):
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }
