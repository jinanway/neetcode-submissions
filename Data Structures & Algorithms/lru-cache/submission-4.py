class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = dict()
        self.last = []

        print(self.hashmap)

    def get(self, key: int) -> int:
        if(key in self.hashmap):
            if(key in self.last):
                del self.last[self.last.index(key)]
            self.last.append(key)
            print(self.hashmap)
            return self.hashmap[key]
        else:
            print(self.hashmap)
            return -1

    def put(self, key: int, value: int) -> None:
        if(len(self.hashmap) >= self.capacity and key not in self.hashmap):
            if(self.last[0] in self.hashmap):
                del self.hashmap[self.last[0]]
            del self.last[0]

        if(key in self.last):
            del self.last[self.last.index(key)]
        self.last.append(key)
        self.hashmap[key] = value
        print(self.hashmap)
        return
