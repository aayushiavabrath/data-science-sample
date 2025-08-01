class OrderQueue:  
    def __init__(self):
        self.heap = [None]
        self.size = 0

    def add_order(self, saladOrder):
        self.size += 1
        self.heap.append(saladOrder)
        self.percUp(self.size)

    def process_next_order(self):
        if self.size == 0:
            return ""
        else:
            min_order = self.heap[1]
            self.heap[1] = self.heap[self.size]
            self.heap.pop()
            self.size -= 1
            self.percDown(1)
            return min_order.info()

    def percUp(self,i):
        while i // 2 > 0:
            if self.heap[i].time < self.heap[i // 2].time:
                self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2

    def percDown(self,i):
        while (i * 2) <= self.size:
            mc = self.minChild(i)
            if self.heap[i].time > self.heap[mc].time:
                self.heap[i], self.heap[mc] = self.heap[mc], self.heap[i]
            i = mc

    def minChild(self,i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heap[i*2] < self.heap[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
        
