class Node:

    def __init__(self, element):
        self.__next = None
        self.__previous = None
        self.__data = element

    def __str__(self):
        return str(self.__data)
    
    def __repr__(self):
        return "<Node: %r>"%self.__str__
    
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
    
    def show_elements(self):
        elements = ''
        for element in self:
            elements += str(element.get_data()) + ', '
        print('[%s]'%elements[:-2])


if __name__ == '__main__':
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.show_elements()
    print(len(ll))
    ll.pop()
    ll.show_elements()
    print(len(ll))
    ll.append(40)
    ll.append(50)
    ll.append(60)
    ll.show_elements()
    print(len(ll))
    ll.lpop()
    ll.show_elements()
    print(len(ll))
    print(ll.find(20))
    print(30 in ll)
    print(40 in ll)