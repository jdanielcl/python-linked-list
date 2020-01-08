class Node:

    def __init__(self, element):
        self.__next = None
        self.__previous = None
        self.__data = element

    def __str__(self):
        return str(self.__data)
    
    def __repr__(self):
        return "<Node: %r>"%self.__data
    
    def set_next(self, node):
        self.__next = node
    
    def set_previous(self, node):
        self.__previous = node

    def get_next(self):
        return self.__next
    
    def get_previous(self):
        return self.__previous

    def get_data(self):
        return self.__data
    
    def set_data(self, data):
        self.__data = data

    def show_node_info(self):
        print("data:%r"%self.get_data())
        print("previous: ",self.get_previous())
        print("next: ",self.get_next())


class LinkedListIterator:

    def __init__(self, linked_list, start=None, end=None):
        if start:
            self.start = start
        else:
            self.start = linked_list._LinkedList__first
        self.end = end
    
    def __iter__(self):
        self.__current = self.start
        return self
    
    def __next__(self):
        current = self.__current
        if self.__current is None or\
            (self.__current.get_previous() and self.__current.get_previous() is self.end):
            raise StopIteration
        self.__current = self.__current.get_next()
        return current


class LinkedList:

    def __init__(self, elements=[]):
        self.__first = None
        self.__last = None
        self.__count = 0
        for element in elements:
            self.append(element)

    def __iter__(self):
        return iter(LinkedListIterator(self))
    
    def __len__(self):
        return self.__count

    def __contains__(self, element):
        return self.find(element) is not None
    
    def __add__(self, elements):
        for element in elements:
            self.append(element.get_data())
        return self
    
    def __sub__(self, elements):
        for element in elements:
            self.remove(element.get_data())
        return self
    
    def __selection_sort(self):
        main_node = self.__first
        while main_node.get_next():
            lower = main_node
            for sub_node in iter(self.iter_from_start_point(main_node.get_next())):
                if sub_node.get_data() < lower.get_data():
                    lower = sub_node
            if lower.get_data() < main_node.get_data():
                self.__exchange_nodes_data(main_node, lower)
            main_node = main_node.get_next()

    def __bubble_sort(self):
        end_node = self.__last
        for _ in range(self.__count):
            swap = False
            for node in self.iter_upto_end_point(end_node):
                if node.get_next() and node.get_data() > node.get_next().get_data():
                    self.__exchange_nodes_data(node, node.get_next())
                    swap = True
            if swap is False:
                return
            end_node = end_node.get_previous()
    
    def __recursive_bubble_sort(self):
        end_node = self.__last
        def inner_bubble_sort(end_node):
            if end_node:
                swap = False
                for node in self.iter_upto_end_point(end_node):
                    if node.get_next() and node.get_data() > node.get_next().get_data():
                        self.__exchange_nodes_data(node, node.get_next())
                        swap = True
                if swap:
                    inner_bubble_sort(end_node.get_previous())
        inner_bubble_sort(end_node)
    
    def __insertion_sort(self):
        temp_linked_list = LinkedList()
        temp_linked_list.append(self.__first.get_data())

        def insert_sorted(node):
            last = temp_linked_list.__last()
            while last.get_previous() and last.get_previous.get_data() > node.get_data():
                last = last.get_previous()
            if last.get_previous() is None:
                #lappend
                pass
            elif last.get_next() is None:
                temp_linked_list.append(node.get_data())
            else:
                #insert_before_node(node)
                pass

        for node in self:
            while node.get_previous() and node.get_previous().get_data() > node.get_data():
                self.__exchange_nodes_data(node, node.get_previous())
                node = node.get_previous()

    def __exchange_nodes_data(self, node_a, node_b):
        node_a_data = node_a.get_data()
        node_a.set_data(node_b.get_data())
        node_b.set_data(node_a_data)

    def append(self, *elements):
        for element in elements:
            new_node = Node(element)
            if self.__first is None:
                self.__first = new_node
            if self.__last is not None:
                new_node.set_previous(self.__last)
                self.__last.set_next(new_node)
            self.__last = new_node
            self.__count += 1
    
    def lappend(self, *elements):
        for element in elements:
            new_node = Node(element)
            if self.__last is None:
                self.__last = new_node
            if self.__first:
                new_node.set_next(self.__first)
                self.__first.set_previous(new_node)
            self.__first = new_node
            self.__count += 1

    def __insert_before(self, main_node, node):
        if main_node.get_previous():
            main_node.get_previous().set_next(node)
            node.set_previous(main_node.get_previous())
        else:
            self.__first = node
        main_node.set_previous(node)
        node.set_next(main_node)

    def __insert_after(self, main_node, node):
        if main_node.get_next():
            main_node.get_next().set_previous(node)
            node.set_next(main_node.get_next())
        else:
            self.__last = node
        main_node.set_next(node)
        node.set_previous(main_node)

    def pop(self):
        if self.__last is not None:
            node = self.__last
            if self.__last.get_previous() is not None:
                self.__last.get_previous().set_next(None)
                self.__last = node.get_previous()
            else: # we have only an element in the list
                self.__first = None
                self.__last = None
            del(node)
            self.__count -=1

    def lpop(self):
        if self.__first is not None:
            node = self.__first
            if self.__first.get_next() is not None:
                self.__first = self.__first.get_next()
                self.__first.set_previous(None)
            else:
                self.__first = None
                self.__last = None
            del(node)
            self.__count -= 1
        
    def find(self, element):
        for index, node in enumerate(self):
            if node.get_data() == element:
                return index
    
    def remove(self, element):
        for node in self:
            if node.get_data() == element:
                if node.get_previous() is None: # is the head
                    self.__first = node.get_next()
                if node.get_next() is None: # is the tail
                    self.__last = node.get_previous()
                if node.get_next() and node.get_previous():
                    node.get_previous().set_next(node.get_next())
                    node.get_next().set_previous(node.get_previous())
                if self.__count != 1: # if isn's the last element
                    self.__first.set_previous(None)
                    self.__last.set_next(None)
                del(node)
                self.__count -= 1
                return

    def show_elements(self):
        elements = ''
        for element in self:
            elements += str(element.get_data()) + ', '
        return '[%s]'%elements[:-2]
    
    def iter_from_start_point(self, start_node):
        return iter(LinkedListIterator(self, start_node))
    
    def iter_upto_end_point(self, end_node):
        return iter(LinkedListIterator(self, end=end_node))
    
    def bubble_sort(self):
        return self.__bubble_sort()
    
    def recursive_bubble_sort(self):
        return self.__recursive_bubble_sort()

    def sort(self, method=None):
        sort_method = self.__selection_sort
        if method:
            sort_method = method
        sort_method()


if __name__ == '__main__':
    pass