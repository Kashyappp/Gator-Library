import time

class ReservationMinHeap:
    def __init__(self):
        self.map = {}  # using dictionary to map index
        self.minheap = []  # this is where we will be storing the nodes

    def swap(self, i, j):
        self.minheap[i], self.minheap[j] = self.minheap[j], self.minheap[i]

    def heapify(self, index):
        parent = (index - 1) // 2
        while index > 0 and (self.minheap[index][1] < self.minheap[parent][1] or (self.minheap[index][1] == self.minheap[parent][1] and self.minheap[index][2] < self.minheap[parent][2])):
            self.swap(index, parent)
            index = parent
            parent = (index - 1) // 2

    def rev_heapify(self, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        smallest = index

        if left_child < len(self.minheap) and (
            self.minheap[left_child][1] < self.minheap[smallest][1]
            or (
                self.minheap[left_child][1] == self.minheap[smallest][1]
                and self.minheap[left_child][2] < self.minheap[smallest][2]
            )
        ):
            smallest = left_child

        if right_child < len(self.minheap) and (
            self.minheap[right_child][1] < self.minheap[smallest][1]
            or (
                self.minheap[right_child][1] == self.minheap[smallest][1]
                and self.minheap[right_child][2] < self.minheap[smallest][2]
            )
        ):
            smallest = right_child

        if smallest != index:
            self.swap(index, smallest)
            self.rev_heapify(smallest)

    def insert_node(self, patron_id, prior_num, timestamp):
        self.minheap.append([patron_id, prior_num, timestamp])
        i = len(self.minheap) - 1
        self.map[patron_id] = i
        self.heapify(i)

    def get_min(self):
        if len(self.minheap) != 0:
            temp = self.minheap[0]

            if len(self.minheap) == 1:
                self.map.pop(self.minheap[0][0])
                self.minheap.pop()

            elif len(self.minheap) == 0:
                return

            else:
                self.map.pop(self.minheap[0][0])
                self.map[self.minheap[-1][0]] = 0
                self.minheap[0] = self.minheap.pop()
                self.rev_heapify(0)

            return temp

    def delete_node(self, patron_id):
        if patron_id not in self.map:
            print(f"Patron ID {patron_id} not found in the heap.")
            return

        i = self.map[patron_id]

        if i != len(self.minheap) - 1:
            self.map[self.minheap[-1][0]] = i
            del self.map[patron_id]
            self.minheap[i] = self.minheap.pop()
            self.rev_heapify(i)

        else:
            del self.map[patron_id]
            self.minheap.pop()

    def update_node(self, patron_id, prior_num, timestamp):
        if patron_id not in self.map:
            print(f"Patron ID {patron_id} not found in the heap.")
            return

        i = self.map[patron_id]

        if self.minheap[i][1] < prior_num <= self.minheap[i][1] * 2:
            self.minheap[i][1] = self.minheap[i][1] + 10
        elif prior_num > self.minheap[i][1] * 2:
            self.delete_node(patron_id)
            return

        self.minheap[i][1] = prior_num
        self.minheap[i][2] = timestamp
        self.heapify(i)
        self.rev_heapify(i)
import time

import time

# Test Case 1
heap1 = ReservationMinHeap()
heap1.insert_node(102, 2, time.time())
heap1.insert_node(101, 1, time.time())
heap1.insert_node(103, 3, time.time())
print(f"Heap 1: {heap1.minheap}")

# Test Case 2
heap2 = ReservationMinHeap()

heap2.insert_node(201, 3, time.time())
heap2.insert_node(202, 1, time.time())
heap2.insert_node(204, 4, time.time())
heap2.insert_node(203, 2, time.time())

print(f"Heap 2: {heap2.minheap}")

# Test Case 3
heap3 = ReservationMinHeap()

heap3.insert_node(301, 1, time.time())
heap3.insert_node(302, 1, time.time())
heap3.insert_node(303, 1, time.time())
print(f"Heap 3: {heap3.minheap}")

# Test Case 4
heap4 = ReservationMinHeap()

heap4.insert_node(401, 5, time.time())
heap4.insert_node(402, 5, time.time())
heap4.insert_node(403, 5, time.time())
print(f"Heap 4: {heap4.minheap}")

# Test Case 5
heap5 = ReservationMinHeap()

heap5.insert_node(501, 1, time.time())
heap5.insert_node(502, 2, time.time())
heap5.insert_node(503, 3, time.time())
heap5.insert_node(504, 4, time.time())
heap5.insert_node(505, 5, time.time())
heap5.insert_node(506, 6, time.time())
heap5.insert_node(507, 7, time.time())
heap5.insert_node(508, 8, time.time())
heap5.insert_node(509, 9, time.time())
heap5.insert_node(510, 10, time.time())

heap5.delete_node(509)
print(f"Heap 5: {heap5.minheap}")

# Test Case 6
heap6 = ReservationMinHeap()

heap6.insert_node(601, 1, time.time())
heap6.insert_node(602, 1, time.time())
heap6.insert_node(603, 1, time.time())
#heap6.update_node(602, 2, time.time())
#heap6.update_node(603, 3, time.time())

heap6.delete_node(601)
print(f"Heap 6: {heap6.minheap}")
