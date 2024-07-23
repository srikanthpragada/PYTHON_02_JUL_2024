class Queue_Iterator:
    def __init__(self, data):
        self.data = data
        self.pos = 0

    def __next__(self):
        if self.pos == len(self.data):
            raise StopIteration

        self.pos += 1
        return self.data[self.pos - 1]


class Queue:
    def __init__(self):
        self.data = []

    def add(self, value):
        self.data.append(value)

    def remove(self):
        value = self.data[0]
        del self.data[0]
        return value

    def clear(self):
        self.data.clear()

    @property
    def length(self):
        return len(self.data)

    def search(self, search_value):
        for idx, value in enumerate(self.data):
            if value == search_value:
                return idx

        return -1

    def __iter__(self):
        return Queue_Iterator(self.data)


q = Queue()
q.add(10)
print(q.length)
q.add(20)
q.add(30)
print(q.remove())

for n in q:
    print(n)

print(q.search(20), q.search(50))
