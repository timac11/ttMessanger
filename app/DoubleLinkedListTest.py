import unittest
import DoubleLinkedList


def list_creation():
    pass


class TestPushFunction(unittest.TestCase):
    def test_one_element_push(self):
        list = DoubleLinkedList.DoubleLinkedList()
        value = 1
        list.push(value)
        self.assertEqual(list.get_first(), value)
        self.assertEqual(list.get_last(), value)
        self.assertEqual(list.len(), value)

    def test_two_elements_push(self):
        list = DoubleLinkedList.DoubleLinkedList()
        first_value = 1
        second_value = 2
        list.push(first_value)
        list.push(second_value)
        self.assertEqual(list.get_first(), first_value)
        self.assertEqual(list.get_last(), second_value)
        self.assertEqual(list.len(), 2)


class TestPopFunction(unittest.TestCase):
    def test_pop_function(self):
        list = DoubleLinkedList.DoubleLinkedList()
        value = 1
        list.push(value)
        list.pop()
        self.assertEqual(list.get_first(), None)
        self.assertEqual(list.get_last(), None)
        self.assertEqual(list.len(), 0)

    def test_pop_empty_list(self):
        list = DoubleLinkedList.DoubleLinkedList()
        list.pop()
        self.assertEqual(list.get_first(), None)
        self.assertEqual(list.get_last(), None)
        self.assertEqual(list.len(), 0)


class TestDeleteFunction(unittest.TestCase):
    def test_delete_function(self):
        list = DoubleLinkedList.DoubleLinkedList()
        value = 1
        list.push(value)
        list.delete(value)
        self.assertEqual(list.get_first(), None)
        self.assertEqual(list.get_last(), None)
        self.assertEqual(list.len(), 0)

    def test_remove_from_rmpty_list(self):
        list = DoubleLinkedList.DoubleLinkedList()
        self.assertEqual(list.get_first(), None)
        self.assertEqual(list.get_last(), None)
        self.assertEqual(list.len(), 0)

    def test_remove_equals_elements(self):
        list = DoubleLinkedList.DoubleLinkedList()
        value = 1
        list.push(value)
        list.push(value)
        list.delete(value)
        self.assertEqual(list.get_first(), value)
        self.assertEqual(list.get_last(), value)
        self.assertEqual(list.len(), 1)

    def test_remove_not_found_value(self):
        list = DoubleLinkedList.DoubleLinkedList()
        value = 1
        not_found = 2
        list.push(value)
        list.delete(not_found)
        self.assertEqual(list.get_first(), value)
        self.assertEqual(list.get_last(), value)
        self.assertEqual(list.len(), 1)


class TestContainsFunction(unittest.TestCase):
    def test_contains_function(self):
        list = DoubleLinkedList.DoubleLinkedList()
        value = 1
        list.push(value)
        not_found = 2
        self.assertTrue(list.contains(value))
        self.assertFalse(list.contains(not_found))

    def test_contains_none(self):
        list = DoubleLinkedList.DoubleLinkedList()
        value = 1
        list.push(value)
        self.assertFalse(list.contains(None))

    def test_contains_empty_list(self):
        list = DoubleLinkedList.DoubleLinkedList()
        self.assertFalse(list.contains(None))
        self.assertFalse(list.contains(1))


class TestUnshiftFunction(unittest.TestCase):
    def test_unshift_function(self):
        list = DoubleLinkedList.DoubleLinkedList()
        value = 1
        list.unshift(value)
        self.assertEqual(list.get_first(), value)
        self.assertEqual(list.get_last(), value)
        self.assertEqual(list.len(), 1)


class TestShiftFunction(unittest.TestCase):
    def test_shift_function(self):
        list = DoubleLinkedList.DoubleLinkedList()
        value = 1
        list.unshift(value)
        list.shift()
        self.assertEqual(list.get_first(), None)
        self.assertEqual(list.get_last(), None)
        self.assertEqual(list.len(), 0)

    def test_shift_empty_list(self):
        list = DoubleLinkedList.DoubleLinkedList()
        list.shift()
        self.assertEqual(list.get_first(), None)
        self.assertEqual(list.get_last(), None)
        self.assertEqual(list.len(), 0)



