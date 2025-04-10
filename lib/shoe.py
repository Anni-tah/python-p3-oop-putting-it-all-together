#!/usr/bin/env python3

class Shoe:
    def __init__(self,brand, size):
        self.brand=brand
        self.size=size
        self.condition=None
    @property
    def size(self):
        """Size property"""
        return self._size
    @size.setter
    def size(self, size):
        """size must be an integer"""
        if isinstance(size, int):
            self._size=size
        else:
            print("size must be an integer")

    def cobble(self):
        """Shoe can be repaired"""
        self.condition="New"
        print("Your shoe is as good as new!")