from typing import TypeVar, List
from random import random
from math import floor
# from time import time

T = TypeVar('T')


class RandomItemSelector:
    _items: List[T]
    _items_len: int
    _previous_selected_index: int = None
    _previous_selected_item: T = None

    def __init__(self, items: List[T]):
        self._items = items
        self._items_len = len(items)

    def get_random_item(self) -> T:
        if self._previous_selected_index == None:
            self._previous_selected_index = floor(random() * self._items_len)
            return self._items[self._previous_selected_index]

        while True:
            selected_index = floor(random() * self._items_len)
            if (self._previous_selected_index != selected_index):
                self._previous_selected_index = selected_index
                return self._items[self._previous_selected_index]

    def get_random_item_alt(self) -> T:
        if self._previous_selected_index == None:
            self._previous_selected_index = floor(random() * self._items_len)
            return self._items[self._previous_selected_index]

        available_items = self._items.copy()
        available_items.pop(self._previous_selected_index)

        selected_index = floor(random() * (self._items_len - 1))

        if selected_index >= self._previous_selected_index:
            self._previous_selected_index = selected_index + 1
        else:
            self._previous_selected_index = selected_index

        return available_items[selected_index]


ris = RandomItemSelector(['foo', 'bar', 'baz', 'qux'])

# now = time()

# for _ in range(100_000):
#   ris.get_random_item()

# print(time() - now)

# now = time()

# for _ in range(100_000):
#   ris.get_random_item_alt()

# print(time() - now)
