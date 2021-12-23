# implementing stack using class
class Stack:
    def __init__(self):
        self.array = []

    def push(self, value):
        self.array.append(value)
        return print(self.array)

    def Pop(self):
        self.array.pop()
        return print(self.array)

    def isempty(self):
        if self.array == []:
            return "Empty"
        return "NOT Empty"

    def top(self):
        return self.array[-1]

    def displayallvalues(self):
        return print(self.array)


# object initailizaton
obj = Stack()
print(obj.isempty())
obj.push(10)

print(obj.isempty())
print(obj.top())
obj.push(20)
obj.push(30)
obj.displayallvalues()
obj.push(40)
print(obj.top())
obj.Pop()
obj.Pop()
print(obj.top())
obj.displayallvalues()
