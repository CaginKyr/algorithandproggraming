class Queue:
    """Array-based Queue implementation using deque"""
    
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """Add an item to the rear of the queue"""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return the front item"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        first_item = self.items[0]
        self.items = self.items[1:] if len(self.items) > 1 else []
        return first_item
    
    def front(self):
        """Return the front item without removing it"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]
    
    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of items in the queue"""
        return len(self.items)
    
    def __str__(self):
        return f"Queue({list(self.items)})"


queue = Queue()

queue.enqueue(("Ali'nin dosyası", 5))
queue.enqueue(("Ayşe'nin dosyası", 2))
queue.enqueue(("Veli'nin dosyası", 8))

toplam_bekleme = 0
gecen_sure = 0

while not queue.is_empty():
    isim, sayfa = queue.dequeue()
    print(f"{isim} yazdırıldı ({sayfa} sayfa) - {gecen_sure} dk bekledi")
    toplam_bekleme += gecen_sure
    gecen_sure += sayfa

print(f"\nToplam bekleme süresi: {toplam_bekleme} dk")
