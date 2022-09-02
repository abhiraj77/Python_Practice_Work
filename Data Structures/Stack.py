# A stack is a linear data structure that follows the principle of Last In First Out (LIFO). This means the last element inserted inside the stack is removed first.

# Basic Operations in Stack:
# Push
# Pop
# isFull
# isEmpty
# Peak: Get the value of the top element without removing it

# Stack Implementation

# Creating a stack
def create_stack():
    stack = []
    return stack

# isEmpty function
def check_empty(stack):
    return len(stack) == 0

# Push function
def push(stack, item):
    stack.append(item)
    return stack

# Pop function
def pop(stack):
    if check_empty(stack):
        return "Stack is empty"
    return stack.pop()

def peek(stack):
    if check_empty(stack):
        return "Stack is empty"
    return stack[-1]

stack = create_stack()
push(stack, 2)
push(stack, 3)
push(stack, 4)
push(stack, 5)
push(stack, 6)
print(f"popped item: {pop(stack)}")
print(f"Empty? {check_empty(stack)}")
print(f"Stack after poping an item: {stack}")
print(f"Stack peek on the top element: {peek(stack)}")

new_stack = create_stack()

print(f"Empty? {check_empty(new_stack)}")
print(f"poping from empty stack: {pop(new_stack)}")
