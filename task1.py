class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insertion_sort(self):
        if not self.head or not self.head.next:
            return

        sorted_head = Node(0) 
        current = self.head

        while current:
            prev = sorted_head
            next_node = current.next

            while prev.next and prev.next.data < current.data:
                prev = prev.next

            current.next = prev.next
            prev.next = current
            current = next_node

        self.head = sorted_head.next

def merge_sorted_lists(l1, l2):
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    if l2:
        tail.next = l2

    return dummy.next

# Тестування
if __name__ == "__main__":

    llist = LinkedList()

    # Вставляємо вузли в початок
    llist.insert_at_beginning(25)
    llist.insert_at_beginning(30)
    llist.insert_at_beginning(35)

    # Вставляємо вузли в кінець
    llist.insert_at_end(40)
    llist.insert_at_end(45)
    llist.insert_at_end(50)

    # Друк зв'язного списку
    print("Зв'язний список:")
    llist.print_list()

    # Видаляємо вузол
    llist.delete_node(40)

    print("\nЗв'язний список після видалення вузла з даними 40:")
    llist.print_list()

    # Пошук елемента у зв'язному списку
    print("\nШукаємо елемент 50:")
    element = llist.search_element(50)
    if element:
        print(element.data)

    # Реверсування списку
    llist.reverse_list()
    print("\nРеверсований список:")
    llist.print_list()

    # Сортування списку вставками
    llist.insertion_sort()
    print("\nВідсортований список:")
    llist.print_list()

    # Об'єднання двох відсортованих списків
    list1 = LinkedList()
    list1.insert_at_end(1)
    list1.insert_at_end(3)
    list1.insert_at_end(5)

    list2 = LinkedList()
    list2.insert_at_end(2)
    list2.insert_at_end(4)
    list2.insert_at_end(6)

    merged_head = merge_sorted_lists(list1.head, list2.head)
    merged_list = LinkedList()
    merged_list.head = merged_head

    print("\nОб'єднаний відсортований список:")
    merged_list.print_list()
