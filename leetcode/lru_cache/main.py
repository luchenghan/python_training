class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache():
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_head(node)
            return node.value
        return -1
    
    def put(self, key:int, value: int):
        if key in self.cache:
            # Update existing key
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_head(node)
        else:
            # Add new key
            node = Node(key, value)
            self.cache[key] = node
            self._add_to_head(node)
            
            if len(self.cache) > self.capacity:
                # Remove LRU (node before tail)
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
    
    def show_cache(self):
        """Display current cache state from most to least recently used"""
        items = []
        current = self.head.next
        while current != self.tail:
            items.append(f"({current.key}:{current.value})")
            current = current.next
        print(f"Cache [MRU -> LRU]: {' -> '.join(items) if items else 'empty'}")
        print(f"Keys in cache: {list(self.cache.keys())}")
        print()

if __name__ == "__main__":
    cache = LRUCache(2)
    
    print("=== LRU Cache Operations ===\n")
    
    print("Operation: put(1, 1)")
    cache.put(1, 1)
    cache.show_cache()
    
    print("Operation: put(2, 2)")
    cache.put(2, 2)
    cache.show_cache()
    
    print("Operation: get(1)")
    result = cache.get(1)
    print(f"Result: {result}")
    cache.show_cache()
    
    print("Operation: put(3, 3) - evicts key 2")
    cache.put(3, 3)
    cache.show_cache()
    
    print("Operation: get(2)")
    result = cache.get(2)
    print(f"Result: {result} (not found)")
    cache.show_cache()