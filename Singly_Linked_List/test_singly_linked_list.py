#!/usr/bin/env python3

from singly_linked_list import LinkedList, Node

def main():
    my_linked_list = LinkedList(0)
    my_linked_list.append(1)
    my_linked_list.append(2)
    my_linked_list.pop()
    my_linked_list.set_value(0, 10)
    my_linked_list.insert(1, 100)
    print(my_linked_list.get(1))
    print('--------')
    my_linked_list.print_list()


if __name__ == '__main__':
    main()