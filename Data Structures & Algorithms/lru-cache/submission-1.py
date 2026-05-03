class ListNode:
    def __init__(self, key, val, prev, next):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:
    capacity: int
    count: int
    lru: ListNode
    mru: ListNode
    cache: Dict[int, ListNode]

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.lru = ListNode(0, 0, None, None)
        self.mru = self.lru
        self.cache = {}


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]

            if node.next:
                node.next.prev = node.prev
                node.prev.next = node.next
                node.prev = self.mru
            
                self.mru.next = node
                self.mru = node
                node.next = None
    
            return self.cache[key].val
        
        return -1
        

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            node = self.cache[key]
            if node.next:
                node.next.prev = node.prev
                node.prev.next = node.next
                node.prev = self.mru
                self.mru.next = node
                self.mru = node
                node.next = None
            node.val = value

            return
        
        newNode = ListNode(key, value, self.mru, None)
        self.mru.next = newNode
        self.mru = newNode
        self.cache[key] = newNode
        

        if self.count == self.capacity:
            nodeToRemove = self.lru.next
            del self.cache[nodeToRemove.key]
            nodeToRemove.next.prev = nodeToRemove.prev
            self.lru.next = nodeToRemove.next
        
            
        else: 
            self.count += 1