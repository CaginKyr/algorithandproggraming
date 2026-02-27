class Stack:
    """
    -based Stack implementation"""
    
    def __init__(self):
        self.items = []
    
    def visit(self, item):
        """Add an item to the top of the stack"""
        self.items.append(item)
    
    def back(self):
        """Remove and return the top item"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()
    
    def current(self):
        """Return the top item without removing it"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]
    
    def is_empty(self):
        """Check if the stack is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of items in the stack"""
        return len(self.items)
    
    def __str__(self):
        return f"Stack({self.items})"


class TextEditor:
    def __init__(self):
        self.undo_stack = Stack()
        self.redo_stack = Stack()
        self.undo_stack.visit("")

    def type(self, text):
        current = self.undo_stack.current()
        new_text = current + text
        self.undo_stack.visit(new_text)
        self.redo_stack = Stack()

    def undo(self):
        if self.undo_stack.size() <= 1:
            print("Geri alınacak bir şey yok")
            return
        last = self.undo_stack.back()
        self.redo_stack.visit(last)

    def redo(self):
        if self.redo_stack.is_empty():
            print("İleri alınacak bir şey yok")
            return
        text = self.redo_stack.back()
        self.undo_stack.visit(text)

    def show(self):
        print(f"{self.undo_stack.current()}")


editor = TextEditor()

print("Komutlar: yaz | undo | redo | çık")

while True:
    editor.show()
    komut = input("Komut: ").strip()

    if komut == "yaz":
        metin = input("Yazılacak metin: ")
        editor.type(metin)

    elif komut == "undo":
        editor.undo()

    elif komut == "redo":
        editor.redo()

    elif komut == "çık":
        print("Çıkılıyor...")
        break
