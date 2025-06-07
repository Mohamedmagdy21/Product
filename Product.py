class Product :
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product(name={self.name}, price={self.price})"

    def __repr__(self):
        return f"Product({self.name!r}, {self.price!r})"
    

Product1 = Product("Shampoo", 1200.00)
print(Product1.name)
print(Product1.price)
