class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.data = [None for i in range(size)]
        self.front, self.rear = None, None

    def record(self, order_id):
        if(self.front is None):
            # if queue is empty
            self.front, self.rear = 0, -1
        elif((self.rear+1)%self.size == self.front):
            self.front = (self.front+1)%self.size

        self.rear = (self.rear+1)%self.size
        self.data[self.rear] = order_id

    def get_last(self, i):
        index = (self.front + self.size - i)%self.size
        return self.data[index]

queue = CircularQueue(3)
queue.record(1)
queue.record(2)
queue.record(3)
queue.record(4)
queue.record(5)
queue.record(6)
print queue.get_last(2)
print queue.get_last(1)
