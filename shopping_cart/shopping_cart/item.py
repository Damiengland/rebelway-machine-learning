from dataclasses import dataclass, field
from shopping_cart.random_num_utils import RandomUtils

@dataclass
class Item:
    name: str
    type: str
    _price: float = 0.0
    id: str = field(default_factory=RandomUtils.generate_random_id)

    @property
    def price(self):
        return round(self._price, 2)
    
    @property
    def search_string(self):
        return f"{self.name} {self.type}"