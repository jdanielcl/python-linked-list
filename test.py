from unittest import TestCase
from main import LinkedList, Node, SortedLinkedList


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

def exchange_test_aditional_data(func):
    def wrapper(self, *args, **kwargs):
        self.linked_list.append(2, 3, 4, 5)
        self.assertEqual(self.linked_list.show_elements(),'[1, 2, 3, 4, 5]')
        func(self, *args, **kwargs)
    return wrapper

def sort_dataset_one(func):
    def wrapper(self, *args, **kwargs):
        self.linked_list.pop()
        self.linked_list.append(5, 4, 3, 2, 1)
        self.assertEqual(self.linked_list.show_elements(),'[5, 4, 3, 2, 1]')
        func(self, *args, **kwargs)
        self.assertEqual(self.linked_list.show_elements(),'[1, 2, 3, 4, 5]')
    return wrapper

def sort_dataset_two(func):
    def wrapper(self, *args, **kwargs):
        self.linked_list.append(5,3,4,2)
        self.assertEqual(self.linked_list.show_elements(), "[1, 5, 3, 4, 2]")
        func(self, *args, **kwargs)
        self.assertEqual(self.linked_list.show_elements(),'[1, 2, 3, 4, 5]')
    return wrapper

def sort_dataset_three(func):
    def wrapper(self, *args, **kwargs):
        self.linked_list.append(2, 3, 4, 5)
        self.assertEqual(self.linked_list.show_elements(), "[1, 2, 3, 4, 5]")
        func(self, *args, **kwargs)
        self.assertEqual(self.linked_list.show_elements(), "[1, 2, 3, 4, 5]")
    return wrapper

def sort_dataset_four(func):
    def wrapper(self, *args, **kwargs):
        self.linked_list.append(2, 2, 2, 1)
        self.assertEqual(self.linked_list.show_elements(), "[1, 2, 2, 2, 1]")
        func(self, *args, **kwargs)
        self.assertEqual(self.linked_list.show_elements(), "[1, 1, 2, 2, 2]")
    return wrapper

def sort_dataset_five(func):
    def wrapper(self, *args, **kwargs):
        self.linked_list.append(2, -2, 2, 1)
        self.assertEqual(self.linked_list.show_elements(), "[1, 2, -2, 2, 1]")
        func(self, *args, **kwargs)
        self.assertEqual(self.linked_list.show_elements(), "[-2, 1, 1, 2, 2]")
    return wrapper

class LinkedListTest(TestCase):

    def setUp(self):
        self.linked_list = LinkedList()
        self.linked_list.append(1)

    def test_get_first_element(self):
        self.assertEqual(self.linked_list._LinkedList__first, self.linked_list.get_first())
    
    def test_get_last_element(self):
        self.assertEqual(self.linked_list._LinkedList__last, self.linked_list.get_last())
    
    def test_set_first_element(self):
        node = Node(2)
        self.linked_list.set_first(node)
        self.assertEqual(self.linked_list._LinkedList__first, node)
    
    def test_set_last_element(self):
        node = Node(2)
        self.linked_list.set_last(node)
        self.assertEqual(self.linked_list._LinkedList__last, node)

    def test_append(self):
        # first element
        self.assertEqual(self.linked_list.get_first().get_data(), 1)
        self.assertEqual(self.linked_list.get_last().get_data(), 1)
        self.assertEqual(self.linked_list._LinkedList__count, 1)
        self.linked_list.append(2)
        # second element
        self.assertEqual(self.linked_list.get_first().get_data(), 1)
        self.assertEqual(self.linked_list.get_last().get_data(), 2)
        self.assertEqual(self.linked_list._LinkedList__count, 2)
        # chained elements
        self.assertEqual(self.linked_list.get_first()._Node__next.get_data(), 2)
        self.assertEqual(self.linked_list.get_last()._Node__previous.get_data(), 1)
    
    def test_lappend_empty_list(self):
        self.linked_list.pop()
        self.assertEqual(self.linked_list.show_elements(), "[]")
        self.linked_list.lappend(3)
        self.assertEqual(self.linked_list.show_elements(), "[3]")
    
    def test_lappend_not_empty_list(self):
        self.linked_list.lappend(2)
        self.assertEqual(self.linked_list.show_elements(), "[2, 1]")
        self.linked_list.lappend(3)
        self.assertEqual(self.linked_list.show_elements(), "[3, 2, 1]")
    
    def test_multiple_append(self):
        self.linked_list.append(2, 3, 4, 5)
        self.assertEqual(self.linked_list.show_elements(), "[1, 2, 3, 4, 5]")

    def test_insert_before_unique_node(self):
        main_node = self.linked_list.get_first()
        node = Node(2)
        self.linked_list._LinkedList__insert_before(main_node, node)
        self.assertEqual(self.linked_list.show_elements(), "[2, 1]")
    
    def test_insert_before_between_two(self):
        self.linked_list.append(3)
        self.assertEqual(self.linked_list.show_elements(), "[1, 3]")
        main_node = self.linked_list.get_last()
        node = Node(2)
        self.linked_list._LinkedList__insert_before(main_node, node)
        self.assertEqual(self.linked_list.show_elements(), "[1, 2, 3]")
    
    def test_insert_after_unique_node(self):
        main_node = self.linked_list.get_first()
        node = Node(2)
        self.linked_list._LinkedList__insert_after(main_node, node)
        self.assertEqual(self.linked_list.show_elements(), "[1, 2]")
    
    def test_insert_after_between_two(self):
        self.linked_list.append(3)
        self.assertEqual(self.linked_list.show_elements(), "[1, 3]")
        main_node = self.linked_list.get_first()
        node = Node(2)
        self.linked_list._LinkedList__insert_after(main_node, node)
        self.assertEqual(self.linked_list.show_elements(), "[1, 2, 3]")

    def test_find(self):
        self.assertEqual(self.linked_list.find(1), 0)

    def test_not_find(self):
        self.assertIsNone(self.linked_list.find(10))
    
    def test_pop_unique_element(self):
        self.assertIsNone(self.linked_list.pop())
        self.assertIsNone(self.linked_list.get_first())
        self.assertIsNone(self.linked_list.get_last())

    def test_lpop_unique_element(self):
        self.assertIsNone(self.linked_list.lpop())
        self.assertIsNone(self.linked_list.get_first())
        self.assertIsNone(self.linked_list.get_last())

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
        self.assertEqual(self.linked_list.get_first().get_data(), 1)
        self.assertEqual(self.linked_list.get_last().get_data(), 1)
        self.assertEqual(self.linked_list._LinkedList__count, 1)
    
    def test_lpop_element(self):
        self.linked_list.append(2)
        self.assertEqual(self.linked_list._LinkedList__count, 2)
        self.linked_list.lpop()
        self.assertEqual(self.linked_list.get_first().get_data(), 2)
        self.assertEqual(self.linked_list.get_last().get_data(), 2)
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
        start_node = self.linked_list.get_first().get_next()
        my_iterator = self.linked_list.iter_from_start_point(start_node)
        self.assertEqual(next(my_iterator).get_data(), 2)
        self.assertEqual(next(my_iterator).get_data(), 3)

    @remove_test_aditional_data
    def test_remove_first_number(self):
        lenght = len(self.linked_list)
        self.linked_list.remove(1)
        self.assertEqual(self.linked_list.get_first().get_data(), 2)
        self.assertIsNone(self.linked_list.get_first().get_previous())
        self.assertEqual(len(self.linked_list), lenght-1)
    
    @remove_test_aditional_data
    def test_remove_last_number(self):
        lenght = len(self.linked_list)
        self.linked_list.remove(3)
        self.assertEqual(self.linked_list.get_last().get_data(), 2)
        self.assertIsNone(self.linked_list.get_last().get_next())
        self.assertEqual(len(self.linked_list), lenght-1)

    @remove_test_aditional_data
    def test_remove_middle_number(self):
        lenght = len(self.linked_list)
        self.linked_list.remove(2)
        self.assertEqual(self.linked_list.get_first().get_data(), 1)
        self.assertEqual(self.linked_list.get_last().get_data(), 3)
        self.assertEqual(self.linked_list.get_last().get_previous().get_data(), 1)
        self.assertEqual(self.linked_list.get_first().get_next().get_data(), 3)
        self.assertEqual(len(self.linked_list), lenght-1)

    def test_remove_first_of_two(self):
        self.linked_list.append(2)
        lenght = len(self.linked_list)
        self.linked_list.remove(1)
        self.assertEqual(self.linked_list.get_first().get_data(), 2)
        self.assertEqual(self.linked_list.get_last().get_data(), 2)
        self.assertIsNone(self.linked_list.get_last().get_previous())
        self.assertIsNone(self.linked_list.get_first().get_next())
        self.assertEqual(len(self.linked_list), lenght-1)

    def test_remove_last_of_two(self):
        self.linked_list.append(2)
        lenght = len(self.linked_list)
        self.linked_list.remove(2)
        self.assertEqual(self.linked_list.get_first().get_data(), 1)
        self.assertEqual(self.linked_list.get_last().get_data(), 1)
        self.assertIsNone(self.linked_list.get_last().get_previous())
        self.assertIsNone(self.linked_list.get_first().get_next())
        self.assertEqual(len(self.linked_list), lenght-1)

    def test_remove_the_only_one(self):
        self.linked_list.remove(1)
        self.assertIsNone(self.linked_list.get_last())
        self.assertIsNone(self.linked_list.get_first())
    
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
        self.assertEqual(self.linked_list.get_last().get_data(), 1)
    
    @exchange_test_aditional_data
    def test_exchange_extreme_nodes(self):
        node_a = self.linked_list.get_first()
        node_b = self.linked_list.get_last()
        self.linked_list._LinkedList__exchange_nodes_data(node_a, node_b)
        self.assertEqual(self.linked_list.show_elements(),'[5, 2, 3, 4, 1]')

    @exchange_test_aditional_data
    def test_exchange_inner_nodes(self):
        node_a = self.linked_list.get_first().get_next()
        node_b = self.linked_list.get_last().get_previous()
        self.linked_list._LinkedList__exchange_nodes_data(node_a, node_b)
        self.assertEqual(self.linked_list.show_elements(),'[1, 4, 3, 2, 5]')

    @exchange_test_aditional_data
    def test_exchange_inner_neighbor_nodes(self):
        node_a = self.linked_list.get_first().get_next().get_next()
        node_b = self.linked_list.get_last().get_previous()
        self.linked_list._LinkedList__exchange_nodes_data(node_a, node_b)
        self.assertEqual(self.linked_list.show_elements(),'[1, 2, 4, 3, 5]')
    
    @exchange_test_aditional_data
    def test_exchange_first_neighbor_nodes(self):
        node_a = self.linked_list.get_first()
        node_b = self.linked_list.get_first().get_next()
        self.linked_list._LinkedList__exchange_nodes_data(node_a, node_b)
        self.assertEqual(self.linked_list.show_elements(),'[2, 1, 3, 4, 5]')

    @exchange_test_aditional_data
    def test_exchange_last_neighbor_nodes(self):
        node_a = self.linked_list.get_last()
        node_b = self.linked_list.get_last().get_previous()
        self.linked_list._LinkedList__exchange_nodes_data(node_a, node_b)
        self.assertEqual(self.linked_list.show_elements(),'[1, 2, 3, 5, 4]')

    def test_exchange_lasts_remaining_nodes(self):
        self.linked_list.append(2)
        node_a = self.linked_list.get_first()
        node_b = self.linked_list.get_last()
        self.assertEqual(self.linked_list.show_elements(),'[1, 2]')
        self.linked_list._LinkedList__exchange_nodes_data(node_a, node_b)
        self.assertEqual(self.linked_list.show_elements(),'[2, 1]')

    @sort_dataset_one
    def test_selection_sort_data_set_one(self):
        self.linked_list.sort()        

    def test_init_with_list(self):
        linked_list = LinkedList([1, 2, 3, 4, 5])
        self.assertEqual(linked_list.show_elements(),"[1, 2, 3, 4, 5]")

    @sort_dataset_two
    def test_selection_sort_data_set_two(self):
        self.linked_list.sort()
    
    @sort_dataset_three
    def test_selection_sort_sorted_array(self):
        self.linked_list.sort()
    
    @sort_dataset_four
    def test_selection_sort_repeated_elements(self):
        self.linked_list.sort()

    @sort_dataset_five
    def test_selection_sort_negative_elements(self):
        self.linked_list.sort()
    
    @exchange_test_aditional_data
    def test_iterator_upto_end_point(self):
        end_node = self.linked_list.get_last().get_previous()
        # iterate upto 4, it doesn't include the item
        my_iterator = self.linked_list.iter_upto_end_point(end_node)
        self.assertEqual(next(my_iterator).get_data(), 1)
        self.assertEqual(next(my_iterator).get_data(), 2)
        self.assertEqual(next(my_iterator).get_data(), 3)
        self.assertEqual(next(my_iterator).get_data(), 4)
        self.assertRaises(StopIteration, next, my_iterator)
    
    @sort_dataset_one
    def test_bubble_sort_data_set_one(self):
        self.linked_list.sort(self.linked_list.bubble_sort)

    @sort_dataset_two
    def test_bubble_sort_data_set_two(self):
        self.linked_list.sort(self.linked_list.bubble_sort)

    @sort_dataset_three
    def test_bubble_sort_sorted_array(self):
        self.linked_list.sort(self.linked_list.bubble_sort)
    
    @sort_dataset_four
    def test_bubble_sort_repeated_elements(self):
        self.linked_list.sort(self.linked_list.bubble_sort)

    @sort_dataset_five
    def test_bubble_sort_negative_elements(self):
        self.linked_list.sort(self.linked_list.bubble_sort)

    @sort_dataset_one
    def test_recursive_bubble_sort_data_set_one(self):
        self.linked_list.sort(self.linked_list.recursive_bubble_sort)

    @sort_dataset_two
    def test_recursive_bubble_sort_data_set_two(self):
        self.linked_list.sort(self.linked_list.recursive_bubble_sort)

    @sort_dataset_three
    def test_recursive_bubble_sort_sorted_array(self):
        self.linked_list.sort(self.linked_list.recursive_bubble_sort)
    
    @sort_dataset_four
    def test_recursive_bubble_sort_repeated_elements(self):
        self.linked_list.sort(self.linked_list.recursive_bubble_sort)

    @sort_dataset_five
    def test_recursive_bubble_sort_negative_elements(self):
        self.linked_list.sort(self.linked_list.recursive_bubble_sort)

    @sort_dataset_one
    def test_insertion_sort_data_set_one(self):
        self.linked_list = self.linked_list.sort(self.linked_list.insertion_sort)

    @sort_dataset_two
    def test_insertion_sort_data_set_two(self):
        self.linked_list = self.linked_list.sort(self.linked_list.insertion_sort)

    @sort_dataset_three
    def test_insertion_sort_sorted_array(self):
        self.linked_list = self.linked_list.sort(self.linked_list.insertion_sort)
    
    @sort_dataset_four
    def test_insertion_sort_repeated_elements(self):
        self.linked_list = self.linked_list.sort(self.linked_list.insertion_sort)

    @sort_dataset_five
    def test_insertion_sort_negative_elements(self):
        self.linked_list = self.linked_list.sort(self.linked_list.insertion_sort)


class SortedLinkedListTest(TestCase):

    def setUp(self):
        self.sorted_linked_list = SortedLinkedList()

    def test_append(self):
        self.sorted_linked_list.append(10)
        self.assertEqual(self.sorted_linked_list.show_elements(), '[10]')
        self.sorted_linked_list.append(30)
        self.assertEqual(self.sorted_linked_list.show_elements(), '[10, 30]')
        self.sorted_linked_list.append(20)
        self.assertEqual(self.sorted_linked_list.show_elements(), '[10, 20, 30]')
        self.sorted_linked_list.append(15, 25)
        self.assertEqual(self.sorted_linked_list.show_elements(), '[10, 15, 20, 25, 30]')
    
    def test_creation_from_iterable(self):
        self.sorted_linked_list = SortedLinkedList([9, 1, 8, 3, 7, 10, 2])
        self.assertEqual(self.sorted_linked_list.show_elements(), '[1, 2, 3, 7, 8, 9, 10]')
    
    def test_append_equal_values(self):
        self.sorted_linked_list = SortedLinkedList([2, 1, 3, 1, 2, 3, 2])
        self.assertEqual(self.sorted_linked_list.show_elements(), '[1, 1, 2, 2, 2, 3, 3]')