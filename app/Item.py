class Item:
    def __init__(self, elem):
        self.elem = elem
        self.prev__item = self
        self.next__item = self