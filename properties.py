class LineItem:
    def __init__(self, sku: str, price: float, amount: int):
        self.sku = sku
        self.price = price
        self.amount = amount

    @property
    def value(self):
        return self.price * self.amount

    @property
    def sku(self):
        return self._sku

    @sku.setter
    def sku(self, value):
        if not value:
            return ValueError(f"Empty sku: {value}")
        self._sku = value

l_obj = LineItem('abc', 2.0, 2)
#l_obj.sku = 10
print(l_obj.value)