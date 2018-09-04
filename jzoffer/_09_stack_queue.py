class Solution:
    def __init__(self):
        self.stackA = []
        self.stackB = []

    def push(self, element):
        self.stackA.append(element)

    def pop(self):
        if not self.stackA and not self.stackB:
            return 'the Queue is empty'

        if not self.stackB:
            while self.stackA:
                self.stackB.append(self.stackA.pop())

        while self.stackB:
            return self.stackB.pop()

