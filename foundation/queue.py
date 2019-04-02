class Queue(object):
# 脚标
    def __init__(self, maxszie):
        self.maxsize = maxsize
        self.queue = [None] * maxsize
        self.front = 0
        self.rear = 0

    def length(self):
        return self.front - self.rear

    def add(self, val):
        if self.rear + 1 = maxsize:
            print("The queue is full")
        else:
            self.queue[self.rear] = val
            self.rear += 1

    def del(self):
        if self.front == self.rear:
            print("The queue is empty")
        else:
            temp = self.queue[self.front]
            self.queue[self.front] = None
            self.fron += 1
            return temp

    
