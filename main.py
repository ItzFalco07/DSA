class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def listToArr(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    print(arr)


class Node():
    def __init__(self, val = 0, key = 0 , next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key

# LRU cache
class LRUCache(object):
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def moveToHead(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        node.prev = self.head
        self.head.next = node
    
    def removeLru(self):
        # remove lru from list
        lru = self.tail.prev
        self.tail.prev = lru.prev
        lru.prev.next = self.tail
        #remove lru from hashmap
        del self.cache[lru.key]
        
    
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            self.moveToHead(node)
            return self.cache[key].val
        else:
            return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache[key].val = value
            self.moveToHead(self.cache[key])
            return
        
        if len(self.cache) >= self.cap:
            # remove lru from List and hash
            self.removeLru()
        # add the node to head
        new_node = Node(value, key)
        self.cache[key] = new_node
        self.moveToHead(new_node)
        return
            
        

    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)