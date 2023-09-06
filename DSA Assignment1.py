
# 1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_zero_sum_sublists(self):
        sum_map = {}
        cumulative_sum = 0
        current = self.head
        while current:
            cumulative_sum += current.data
            if cumulative_sum == 0 or cumulative_sum in sum_map:
                if cumulative_sum == 0:
                    self.head = current.next
                else:
                    sum_map[cumulative_sum].next = current.next
                cumulative_sum = 0
                sum_map.clear()
            else:
                sum_map[cumulative_sum] = current
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")



linked_list = LinkedList()
elements = [6, -6, 8, 4, -12, 10, 2, -2]
for element in elements:
    linked_list.append(element)

print("Original linked list:")
linked_list.display()

linked_list.delete_zero_sum_sublists()

print("Linked list after deleting zero sum sublists:")
linked_list.display()


# 2
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_in_groups(head, k):
    def reverse_list(start, end):
        prev, curr = None, start
        while curr != end:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node 
        return prev
    
    count = 0
    curr = head
    while curr and count < k:
        curr = curr.next
        count += 1
    if count < k:
        return head 
    new_head = reverse_list(head, curr) 
    head.next = reverse_in_groups(curr, k)
    return new_head


def linked_list_from_array(arr):
    head = None
    tail = None 
    for val in arr:
        new_node = ListNode(val)
        if not head:
            head = new_node
            tail = new_node 
        else:
            tail.next = new_node 
            tail = new_node 
    return head             



def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


arr = [1,2,3,4,5,6,7,8]
head = linked_list_from_array(arr)

print("Original Linked List:")
print_linked_list(head)

k = 3
head = reverse_in_groups(head, k)

print(f"Linked List reversed in groups of {k}:")
print_linked_list(head)


# 3
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_at_alternate_position(head1, head2):
    current1 = head1
    current2 = head2

    while current1 and current2:
        next1 = current1.next
        next2 = current2.next

        current1.next = current2
        current2.next = next1

        current1 = next1
        current2 = next2

    return head1

def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

def create_linked_list(arr):
    if not arr:
        return None

    head = Node(arr[0])
    current = head
    for data in arr[1:]:
        current.next = Node(data)
        current = current.next
    return head

list1 = create_linked_list([1, 3, 5, 7])
list2 = create_linked_list([2, 4, 6])

print("List 1:")
print_linked_list(list1)

print("List 2:")
print_linked_list(list2)

merge_at_alternate_position(list1, list2)

print("Merged List:")
print_linked_list(list1)


# 4
def count_pairs_with_sum(arr, target_sum):

    num_count = {}
    pair_count = 0

    for num in arr:
        difference = target_sum - num

        if difference in num_count:
            pair_count += num_count[difference]

        num_count[num] = num_count.get(num, 0) + 1

    return pair_count


arr = [1, 5, 7, -1, 5]
target_sum = 6

result = count_pairs_with_sum(arr, target_sum)
print(f"Number of pairs with sum {target_sum}: {result}")

# 5
def find_duplicates(arr):
    i = set()
    duplicates = set()
    
    for num in arr:
        if num in i:
            duplicates.add(num)
        else:
            i.add(num)
    
    return duplicates

input_array = [1, 2, 3, 4, 5, 2, 6, 7, 3]
result = find_duplicates(input_array)
print("Duplicates in the array:", result)

# 6
def find_kth_largest_smallest(nums, k):
    nums_sorted = sorted(nums)
    kth_smallest = nums_sorted[k - 1]

    nums_sorted_desc = sorted(nums, reverse=True)
    kth_largest = nums_sorted_desc[k - 1]

    return kth_largest, kth_smallest


nums = [12, 3, 5, 7, 19, 4]
K = 3
kth_largest, kth_smallest = find_kth_largest_smallest(nums, K)
print("Array:",nums)
print(f"{K}th largest number: ", kth_largest)
print(f"{K}th smallest number: ", kth_smallest)

# 7
def move_negatives_to_one_side(arr):
    left_L = 0
    right_R = len(arr) - 1

    while left_L < right_R:
        if arr[left_L] >= 0 and arr[right_R] < 0:
            arr[left_L], arr[right_R] = arr[right_R], arr[left_L]
            left_L += 1
            right_R -= 1
        elif arr[left_L] < 0:
            left_L += 1
        else:
            right_R -= 1

    return arr

input_array = [1, -2, 3, -4, 5, -6]
result_array = move_negatives_to_one_side(input_array)
print(result_array)


# 8

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

def reverse_string(input_string):
    stack = Stack()

    for char in input_string:
        stack.push(char)

    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string

input_string = "Hello, World!"
output = reverse_string(input_string)
print("Input String:", input_string)
print("Reversed String:", output)


# 9

def evaluate_postfix_expression(expression):
    stack = []
    operators = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: x / y}

    for i in expression.split():
        if i.isdigit():  
            stack.append(int(i))
        elif i in operators:  
            if len(stack) >= 2:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = operators[i](operand1, operand2)
                stack.append(result)
            else:
                raise ValueError("Invalid postfix expression: Not enough operands for operator")
        else:
            raise ValueError("invalid postfix expression")

    if len(stack) == 1:
        return stack[0]
    else:
        raise ValueError("Invalid postfix expression: Too many operands")

postfix_expression = "2 4 + 5 * 6 -"
result = evaluate_postfix_expression(postfix_expression)
print("Result:", result)


# 10

class QueueUsingStack:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, item):
        self.enqueue_stack.append(item)

    def dequeue(self):
        if not self.dequeue_stack:
            if not self.enqueue_stack:
                return None
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        return self.dequeue_stack.pop()

    def is_empty(self):
        return not self.enqueue_stack and not self.dequeue_stack

    def size(self):
        return len(self.enqueue_stack) + len(self.dequeue_stack)

queue = QueueUsingStack()

print("Is the queue empty?", queue.is_empty())  

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue size:", queue.size()) 

print("Dequeue:", queue.dequeue())  
print("Dequeue:", queue.dequeue())  

queue.enqueue(4)

print("Queue size:", queue.size())  

print("Is the queue empty?", queue.is_empty())  

print("Dequeue:", queue.dequeue())  
print("Dequeue:", queue.dequeue())  

print("Is the queue empty?", queue.is_empty())  



