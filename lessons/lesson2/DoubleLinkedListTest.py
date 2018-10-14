import unittest
from DoubleLinkedList import DoubleLinkedList


def list_creation(*args):
    linked_list = DoubleLinkedList()
    for val in args:
        linked_list.push(val)
    return linked_list


class TestPushFunction(unittest.TestCase):
    def test_one_element_push(self):
        value = 1
        linked_list = list_creation(value)
        self.assertEqual(linked_list.first(), value)
        self.assertEqual(linked_list.last(), value)
        self.assertEqual(linked_list.len(), 1)

    def test_push_none_type(self):
        linked_list = list_creation(None)
        self.assertEqual(linked_list.first(), None)
        self.assertEqual(linked_list.last(), None)
        self.assertEqual(linked_list.len(), 1)

    def test_two_elements_push(self):
        first_value = 1
        second_value = 2
        linked_list = list_creation(first_value, second_value)
        self.assertEqual(linked_list.first(), first_value)
        self.assertEqual(linked_list.last(), second_value)
        self.assertEqual(linked_list.len(), 2)


class TestPopFunction(unittest.TestCase):
    def test_pop_function(self):
        value = 1
        linked_list = list_creation(value)
        linked_list.pop()
        self.assertEqual(linked_list.first(), None)
        self.assertEqual(linked_list.last(), None)
        self.assertEqual(linked_list.len(), 0)

    def test_pop_empty_list(self):
        linked_list = list_creation()
        linked_list.pop()
        self.assertEqual(linked_list.first(), None)
        self.assertEqual(linked_list.last(), None)
        self.assertEqual(linked_list.len(), 0)


class TestDeleteFunction(unittest.TestCase):
    def test_delete_function(self):
        value = 1
        linked_list = list_creation(value)
        linked_list.delete(value)
        self.assertEqual(linked_list.first(), None)
        self.assertEqual(linked_list.last(), None)
        self.assertEqual(linked_list.len(), 0)

    def test_remove_from_rmpty_list(self):
        linked_list = list_creation()
        self.assertEqual(linked_list.first(), None)
        self.assertEqual(linked_list.last(), None)
        self.assertEqual(linked_list.len(), 0)

    def test_remove_equals_elements(self):
        value = 1
        linked_list = list_creation(value, value)
        linked_list.delete(value)
        self.assertEqual(linked_list.first(), value)
        self.assertEqual(linked_list.last(), value)
        self.assertEqual(linked_list.len(), 1)

    def test_remove_not_found_value(self):
        value = 1
        linked_list = list_creation(value)
        not_found = 2
        linked_list.delete(not_found)
        self.assertEqual(linked_list.first(), value)
        self.assertEqual(linked_list.last(), value)
        self.assertEqual(linked_list.len(), 1)


class TestContainsFunction(unittest.TestCase):
    def test_contains_function(self):
        value = 1
        linked_list = list_creation(value)
        not_found = 2
        self.assertTrue(linked_list.contains(value))
        self.assertFalse(linked_list.contains(not_found))

    def test_contains_none(self):
        value = 1
        linked_list = list_creation(value)
        linked_list.push(value)
        self.assertFalse(linked_list.contains(None))

    def test_contains_empty_list(self):
        linked_list = list_creation()
        self.assertFalse(linked_list.contains(None))
        self.assertFalse(linked_list.contains(1))


class TestUnshiftFunction(unittest.TestCase):
    def test_unshift_function(self):
        value = 1
        linked_list = list_creation(value)
        self.assertEqual(linked_list.first(), value)
        self.assertEqual(linked_list.last(), value)
        self.assertEqual(linked_list.len(), 1)


class TestShiftFunction(unittest.TestCase):
    def test_shift_function(self):
        value = 1
        linked_list = list_creation(value)
        linked_list.shift()
        self.assertEqual(linked_list.first(), None)
        self.assertEqual(linked_list.last(), None)
        self.assertEqual(linked_list.len(), 0)

    def test_shift_empty_list(self):
        linked_list = list_creation()
        linked_list.shift()
        self.assertEqual(linked_list.first(), None)
        self.assertEqual(linked_list.last(), None)
        self.assertEqual(linked_list.len(), 0)



