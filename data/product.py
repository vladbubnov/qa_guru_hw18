import dataclasses


@dataclasses.dataclass
class Product:
    id: str
    name: str
    quantity: str


book_1 = Product(
    id="13",
    name="Computing and Internet",
    quantity="1"
)

book_2 = Product(
    id="13",
    name="Computing and Internet",
    quantity="2"
)

book_3 = Product(
    id="13",
    name="Computing and Internet",
    quantity="3"
)
