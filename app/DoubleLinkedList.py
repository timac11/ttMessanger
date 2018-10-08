from Item import Item


class DoubleLinkedList:
    """
        In this class @ param elem in methods is not
        instance of class Item. Instance of item - is only
        wrapper of the element
    """

    def __init__(self):
        self.__first = None
        self.__last = None

    def push(self, elem):
        item = Item(elem)
        if self.__first is None:
            self.__first = item
            self.__last = item
        else:
            last = self.__last
            self.__last = item
            last.next__item = item
            item.prev__item = last

    def pop(self):
        returned_value = None
        if self.len() != 0:
            prev_last = self.__last.prev__item
            returned_value = self.__last.elem
            if self.len() > 1:
                self.__last = prev_last
                prev_last.next__item = None
            else:
                self.__first = None
                self.__last = None
        return returned_value

    def unshift(self, elem):
        item = Item(elem)
        if self.len():
            first = self.__first
            self.__first = item
            item.next__item = first
            first.prev_item = item
        else:
            self.__first = item
            self.__last = item

    def shift(self):
        length = self.len()
        returned_value = None
        if length > 1:
            returned_value = self.__first
            next__item = self.__first.next__item
            self.__first = next__item
            self.__first.prev__item = None
        elif length == 1:
            returned_value = self.__first
            self.__first = None
            self.__last = None
        return returned_value

    def len(self):
        first = self.__first
        if first is None:
            return 0
        current_element = first.next__item
        length = 1
        while current_element is not None:
            length += 1
            current_element = current_element.next__item
        return length

    def delete(self, elem):
        first = self.__first
        if self.len():
            if first.elem == elem:
                self.shift()
            else:
                current_element = first.next__item
                while current_element is not None:
                    if current_element.elem == elem:
                        prev_element = current_element.prev__item
                        prev_element.next__item = current_element.next__item
                        break
                    current_element = current_element.next__item

    def contains(self, elem):
        result = False
        first = self.__first
        if first is None:
            return result
        elif first.elem == elem:
            result = True
        current_element = first.next__item
        while current_element is not None:
            if current_element.elem == elem:
                result = True
                break
            current_element = current_element.next__item
        return result

    def first(self):
        if self.__first is not None:
            return self.__first.elem
        return None

    def last(self):
        if self.__last is not None:
            return self.__last.elem
        return None
