from unittest import TestCase
from main import LinkedList, Node


class NodeTest(TestCase):

    def setUp(self):
        self.value_a = 10
        self.node_a = Node(self.value_a)
        self.value_b = 20
        self.node_b = Node(self.value_b)

    def test_get_data(self):
        self.assertEqual(self.value_a, self.node_a.get_data())
        self.assertEqual(self.value_b, self.node_b.get_data())
    
    def test_set_next(self):
        self.node_a.set_next(self.node_b)
        self.assertEqual(self.node_a._Node__next, self.node_b)
    
    def test_set_previous(self):
        self.node_b.set_previous(self.node_a)
        self.assertEqual(self.node_b._Node__previous, self.node_a)
    
    def test_get_next(self):
        self.node_a.set_next(self.node_b)
        self.assertEqual(self.node_a.get_next(), self.node_a._Node__next)
    
    def test_get_previous(self):
        self.node_b.set_previous(self.node_a)
        self.assertEqual(self.node_b.get_previous(), self.node_b._Node__previous)

    def test_get_str(self):
        self.assertEqual(str(self.value_a), str(self.node_a))

    def test_repr(self):
        self.assertEqual(repr(self.node_a), "<Node: 10>")


    
def remove_test_aditional_data(func):
    def wrapper(self, *args, **kwargs):
        self.linked_list.append(2, 3)
        func(self, *args, **kwargs)
    return wrapper


class LinkedListTest(TestCase):

    def setUp(self):
        self.linked_list = LinkedList()
        self.linked_list.append(1)

    def test_append(self):
        # first element
        self.assertEqual(self.linked_list._LinkedList__first.get_data(), 1)
        self.assertEqual(self.linked_list._LinkedList__last.get_data(), 1)
        self.assertEqual(self.linked_list._LinkedList__count, 1)
        self.linked_list.append(2)
        # second element
        self.assertEqual(self.linked_list._LinkedList__first.get_data(), 1)
        self.assertEqual(self.linked_list._LinkedList__last.get_data(), 2)
        self.assertEqual(self.linked_list._LinkedList__count, 2)
        # chained elements
        self.assertEqual(self.linked_list._LinkedList__first._Node__next.get_data(), 2)
        self.assertEqual(self.linked_list._LinkedList__last._Node__previous.get_data(), 1)
    
    def test_multiple_append(self):
        self.linked_list.append(2, 3, 4, 5)
        self.assertEqual(self.linked_list.show_elements(), "[1, 2, 3, 4, 5]")

    def test_find(self):
        self.assertEqual(self.linked_list.find(1), 0)

    def test_not_find(self):
        self.assertIsNone(self.linked_list.find(10))
    
    def test_pop_unique_element(self):
        self.assertIsNone(self.linked_list.pop())
        self.assertIsNone(self.linked_list._LinkedList__first)
        self.assertIsNone(self.linked_list._LinkedList__last)

    def test_lpop_unique_element(self):
        self.assertIsNone(self.linked_list.lpop())
        self.assertIsNone(self.linked_list._LinkedList__first)
        self.assertIsNone(self.linked_list._LinkedList__last)

    def test_pop_in_empty_list(self):
        self.assertIsNone(self.linked_list.pop())
        self.assertIsNone(self.linked_list.pop())

    def test_lpop_in_empty_list(self):
        self.assertIsNone(self.linked_list.lpop())
        self.assertIsNone(self.linked_list.lpop())

    def test_pop_element(self):
        self.linked_list.append(2)
        self.assertEqual(self.linked_list._LinkedList__count, 2)
        self.linked_list.pop()
        self.assertEqual(self.linked_list._LinkedList__first.get_data(), 1)
        self.assertEqual(self.linked_list._LinkedList__last.get_data(), 1)
        self.assertEqual(self.linked_list._LinkedList__count, 1)
    
    def test_lpop_element(self):
        self.linked_list.append(2)
        self.assertEqual(self.linked_list._LinkedList__count, 2)
        self.linked_list.lpop()
        self.assertEqual(self.linked_list._LinkedList__first.get_data(), 2)
        self.assertEqual(self.linked_list._LinkedList__last.get_data(), 2)
        self.assertEqual(self.linked_list._LinkedList__count, 1)
    
    def test_show_elements(self):
        self.assertEqual(self.linked_list.show_elements(), '[1]')
        self.linked_list.append(2)
        self.assertEqual(self.linked_list.show_elements(), '[1, 2]')

    def test_show_empty_list(self):
        self.linked_list.pop()
        self.assertEqual(self.linked_list.show_elements(), '[]')
    
    def test_len_method(self):
        self.assertEqual(self.linked_list._LinkedList__count, 1)
        self.assertEqual(len(self.linked_list), 1)
        self.linked_list.append(2)
        self.assertEqual(self.linked_list._LinkedList__count, 2)
        self.assertEqual(len(self.linked_list), 2)
    
    def test_cero_len_method(self):
        self.linked_list.pop()
        self.assertEqual(self.linked_list._LinkedList__count, 0)
        self.assertEqual(len(self.linked_list), 0)

    def test_contains(self):
        self.assertTrue(1 in self.linked_list)

    def test_not_contains(self):
        self.assertFalse(2 in self.linked_list)
    
    def test_iterator(self):
        self.linked_list.append(2)
        my_iterator = iter(self.linked_list)
        self.assertEqual(str(next(my_iterator)), "1")
        self.assertEqual(str(next(my_iterator)), "2")
        self.assertRaises(StopIteration, next, my_iterator)
        my_iterator = iter(self.linked_list)
        self.assertEqual(str(next(my_iterator)), "1")
    
    @remove_test_aditional_data
    def test_iterator_from_start_point(self):
        # start from 2
        start_node = self.linked_list._LinkedList__first.get_next()
        my_iterator = self.linked_list.iter_from_start_point(start_node)
        self.assertEqual(next(my_iterator).get_data(), 2)
        self.assertEqual(next(my_iterator).get_data(), 3)

    @remove_test_aditional_data
    def test_remove_first_number(self):
        lenght = len(self.linked_list)
        self.linked_list.remove(1)
        self.assertEqual(self.linked_list._LinkedList__first.get_data(), 2)
        self.assertIsNone(self.linked_list._LinkedList__first.get_previous())
        self.assertEqual(len(self.linked_list), lenght-1)
    
    @remove_test_aditional_data
    def test_remove_last_number(self):
        lenght = len(self.linked_list)
        self.linked_list.remove(3)
        self.assertEqual(self.linked_list._LinkedList__last.get_data(), 2)
        self.assertIsNone(self.linked_list._LinkedList__last.get_next())
        self.assertEqual(len(self.linked_list), lenght-1)

    @remove_test_aditional_data
    def test_remove_middle_number(self):
        lenght = len(self.linked_list)
        self.linked_list.remove(2)
        self.assertEqual(self.linked_list._LinkedList__first.get_data(), 1)
        self.assertEqual(self.linked_list._LinkedList__last.get_data(), 3)
        self.assertEqual(self.linked_list._LinkedList__last.get_previous().get_data(), 1)
        self.assertEqual(self.linked_list._LinkedList__first.get_next().get_data(), 3)
        self.assertEqual(len(self.linked_list), lenght-1)

    def test_remove_first_of_two(self):
        self.linked_list.append(2)
        lenght = len(self.linked_list)
        self.linked_list.remove(1)
        self.assertEqual(self.linked_list._LinkedList__first.get_data(), 2)
        self.assertEqual(self.linked_list._LinkedList__last.get_data(), 2)
        self.assertIsNone(self.linked_list._LinkedList__last.get_previous())
        self.assertIsNone(self.linked_list._LinkedList__first.get_next())
        self.assertEqual(len(self.linked_list), lenght-1)

    def test_remove_last_of_two(self):
        self.linked_list.append(2)
        lenght = len(self.linked_list)
        self.linked_list.remove(2)
        self.assertEqual(self.linked_list._LinkedList__first.get_data(), 1)
        self.assertEqual(self.linked_list._LinkedList__last.get_data(), 1)
        self.assertIsNone(self.linked_list._LinkedList__last.get_previous())
        self.assertIsNone(self.linked_list._LinkedList__first.get_next())
        self.assertEqual(len(self.linked_list), lenght-1)

    def test_remove_the_only_one(self):
        self.linked_list.remove(1)
        self.assertIsNone(self.linked_list._LinkedList__last)
        self.assertIsNone(self.linked_list._LinkedList__first)
    
    def test_add_method(self):
        add_linked_list = LinkedList()
        add_linked_list.append(2, 3)
        self.linked_list += add_linked_list
        self.assertEqual(len(self.linked_list), 3)
    
    def test_add_void_linked_list(self):
        add_linked_list = LinkedList()
        self.linked_list += add_linked_list
        self.assertEqual(len(self.linked_list), 1)
    
    @remove_test_aditional_data
    def test_sub_method(self):
        original_lenght = len(self.linked_list)
        subtract_linked_list = LinkedList()
        subtract_linked_list.append(2, 3)
        temp_lenght = len(subtract_linked_list)
        self.linked_list -= subtract_linked_list
        self.assertEqual(len(self.linked_list), original_lenght-temp_lenght)
        self.assertEqual(self.linked_list._LinkedList__last.get_data(), 1)
    
    def test_init_with_list(self):
        linked_list = LinkedList([1, 2, 3, 4, 5])
        self.assertEqual(linked_list.show_elements(),"[1, 2, 3, 4, 5]")