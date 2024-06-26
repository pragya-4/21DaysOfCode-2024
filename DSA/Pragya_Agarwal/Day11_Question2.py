class PriorityQueue:
    def __init__(self):
        self.heap = []
    def insert(self, item):
        self.heap.append(item)
        self.heapify_up(len(self.heap) - 1)
    def extract_min(self):
        if not self.heap:
            return None

        min_element = self.heap[0]
        last_element = self.heap.pop()

        if self.heap:
            self.heap[0] = last_element
            self.heapify_down(0)

        return min_element

    def heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[parent_index] <= self.heap[index]:
                break
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            index = parent_index

    def heapify_down(self, index):
        while True:
            left_child_index=2*index+1
            right_child_index=2*index+2
            smallest_index =index

            if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest_index]:
                smallest_index = left_child_index
            if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest_index]:
                smallest_index = right_child_index
            if smallest_index == index:
                break
            self.heap[index], self.heap[smallest_index] = self.heap[smallest_index], self.heap[index]
            index = smallest_index

priority_queue = PriorityQueue()
priority_queue.insert(4)
priority_queue.insert(2)
print(priority_queue.extract_min())  
print(priority_queue.extract_min())  

