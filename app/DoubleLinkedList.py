import Item


class DoubleLinkedList:
    """
        In this class @ param elem in methods is not
        instance of class Item. Instance of item - is only
        wrapper of the element
    """

    def __init__(self):
        self.first = None
        self.last = None

    def push(self, elem):
        item = Item.Item(elem)
        if self.first is None:
            self.first = item
            self.last = item
        else:
            last = self.last
            first = self.first
            self.last = item
            last.next__item = item
            item.next__item = first
            first.prev__item = item
            item.prev__item = last

    def pop(self):
        returned_value = None
        if self.len() != 0:
            prev_last = self.last.prev__item
            returned_value = self.last.elem
            if self.len() > 1:
                first = self.first
                self.last = prev_last
                prev_last.next__item = first
                first.prev__item = prev_last
            else:
                self.first = None
                self.last = None
        return returned_value

    def unshift(self, elem):
        item = Item.Item(elem)
        if self.len():
            first = self.first
            last = self.last
            self.first = item
            item.next__item = first
            item.prev__item = last
            last.next__item = item
            first.prev_item = item
        else:
            self.first = item
            self.last = item

    def shift(self):
        length = self.len()
        returned_value = None
        if length > 1:
            returned_value = self.first
            next__item = self.first.next__item
            self.first = next__item
            self.last.next__item = self.first
            self.first.prev__item = self.last
        elif length == 1:
            returned_value = self.first
            self.first = None
            self.last = None
        return returned_value

    def len(self):
        first = self.first
        if first is None:
            return 0
        current_element = first.next__item
        length = 1
        while current_element != first:
            length += 1
            current_element = current_element.next__item
        return length

    def delete(self, elem):
        first = self.first
        if self.len():
            if first.elem == elem:
                self.shift()
            else:
                current_element = first.next__item
                while first != current_element:
                    if current_element.elem == elem:
                        prev_element = current_element.prev__item
                        prev_element.next__item = current_element.next__item
                        break
                    current_element = current_element.next__item

    def contains(self, elem):
        result = False
        first = self.first
        if first is None:
            return result
        elif first.elem == elem:
            result = True
        current_element = first.next__item
        while current_element != first:
            if current_element.elem == elem:
                result = True
                break
            current_element = current_element.next__item
        return result

    def get_first(self):
        if self.first is not None:
            return self.first.elem
        return None

    def get_last(self):
        if self.last is not None:
            return self.last.elem
        return None
