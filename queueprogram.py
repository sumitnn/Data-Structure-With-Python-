# implement queue using class

class Queue:
    def __init__(self):
        self.array = []

    def enquee(self, value):
        self.array.append(value)
        return self.array

    def dequee(self):
        return self.array.pop(0)

    def front(self):
        return self.array[0]

    def rear(self):
        return self.array[-1]

    def allitems(self):
        return self.array


# object
obj = Queue()
print(obj.allitems())
print(obj.enquee(10))
print(obj.enquee(10))
print(obj.enquee(100))
print(obj.front())
print(obj.allitems())
print(obj.rear())
print(obj.allitems())
print(obj.dequee())
print(obj.dequee())
print(obj.allitems())
