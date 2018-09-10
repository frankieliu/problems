class queue:
    def __init__(self):
        self.a = []
        self.b = []

    def enqueue(self,value):
        self.a.append(value)

    def dequeue(self):
        if not self.b:
            if not self.a:
                return None
            else:
                while self.a:
                    self.b.append(self.a.pop())
                return self.b.pop()
        else:
            return self.b.pop()

q = queue()
[q.enqueue(i) for i in range(0,10)]
[print(q.dequeue()) for i in range(0,3)]
[q.enqueue(i) for i in range(10,13)]
[print(q.dequeue()) for i in range(0,11)]
