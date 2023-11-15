import random
import time

class PriorityQueueNode:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, item, priority):
        new_node = PriorityQueueNode(item, priority)
        if self.head is None or priority > self.head.priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and priority <= current.next.priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def dequeue(self):
        if not self.is_empty():
            item = self.head.item
            self.head = self.head.next
            return item


size1 = int(input("Введите размер матрицы M1: "))
M1 = []

for i in range(size1):
    row = []
    for j in range(size1):
        row.append(0)
    M1.append(row)

for i in range(size1):
    for j in range(i + 1, size1):
        M1[i][j] = M1[j][i] = random.randint(0, 1)

lists = [[] for _ in range(size1)]
for i in range(size1):
    for j in range(size1):
        if M1[i][j] == 1:
            lists[i].append(j)


def breadth_first_search(G):
    size_G = len(G)
    NUM = [False] * size_G
    global first

    def BFS(v):
        queue = []
        queue.append(v)
        NUM[v] = True

        while queue:
            v = queue.pop(0)
            print(v, end=' ')

            for i in range(size_G):
                if G[v][i] == 1 and not NUM[i]:
                    queue.append(i)
                    NUM[i] = True

    if not NUM[first]:
        BFS(first)


def bbreadth_first_search(adj_list):
    size_G = len(adj_list)
    NUM = [False] * size_G
    global first

    def BFS(v):
        queue = []
        queue.append(v)
        NUM[v] = True
        while queue:
            v = queue.pop(0)
            print(v, end=' ')

            for i in adj_list[v]:
                if not NUM[i]:
                    queue.append(i)
                    NUM[i] = True

    if not NUM[first]:
        BFS(first)


def Breadth_First_Search(G):
    size_G = len(G)
    NUM = [False] * size_G
    global first

    def BFS(v):
        priority_queue = PriorityQueue()
        priority_queue.enqueue(v, 0)
        NUM[v] = True

        while not priority_queue.is_empty():
            v = priority_queue.dequeue()
            print(v, end=' ')

            for i in range(size_G):
                if G[v][i] == 1 and not NUM[i]:
                    priority_queue.enqueue(i, 0)
                    NUM[i] = True

    if not NUM[first]:
        BFS(first)

print("Матрица смежности для M1:")
for row in M1:
    print(row)

first = int(input("Введите начальную вершину для обхода: "))

print("\nСписок смежности для M1: ")
for i, verticles in enumerate(lists):
    print(f"Вершина {i}: {verticles}")

print("Результат обхода в ширину:")
start_time = time.time()
breadth_first_search(M1)
elapsed_time = time.time() - start_time
print(f"\nВремя работы: {elapsed_time} секунд")

print("\nРезультат обхода в ширину для списка смежности:")
bbreadth_first_search(lists)

print("\nРезультат обхода в ширину с использованием очереди:")
start_time = time.time()
Breadth_First_Search(M1)
elapsed_time = time.time() - start_time
print(f"\nВремя работы: {elapsed_time} секунд")
?
