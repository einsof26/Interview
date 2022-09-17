class Stack:
    def __init__(self, stack):
        self.stack = stack


    # def __str__(self):
    #     return self.stack


    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, new_element):
        self.stack.append(new_element)
        return self.peek()  #Для тестирования

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


# stack = Stack([1, 2, 3])
# print(stack.pop())
# print(stack.size())
# print(stack.pop())
# print(stack.size())
# print(stack.pop())
# print(stack.size())
# print(stack.isEmpty())