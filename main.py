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


class LinkedList:

    def __init__(self):
        self.__first = None
        self.__last = None
        self.__count = 0
    
    def __iter__(self):
        self.__current = self.__first
        return self
    
    def __len__(self):
        return self.__count
    
    def __next__(self):
        current = self.__current
        if self.__current is None:
            raise StopIteration
        self.__current = self.__current.get_next()
        return current

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

    def append(self, element):
        new_node = Node(element)
        if self.__first is None:
            self.__first = new_node
        if self.__last is not None:
            new_node.set_previous(self.__last)
            self.__last.set_next(new_node)
        self.__last = new_node
        self.__count += 1
    
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


if __name__ == '__main__':
    pass