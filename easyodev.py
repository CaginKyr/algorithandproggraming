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

stack = Stack()

while True:
    print("1. Siteye git")
    print("2. Geri dön")
    print("3. Şu an nerdeyim?")
    print("4. Browser geçmişini göster")
    print("5. Çıkış")

    deger = int(input("Lütfen işlem seçiniz. \n") )
    if deger == 1:
        site = input("Gitmek istediğin sitenin URL'ini yaz. \n\n")
        stack.visit(site)
        print(f"{site} sitesine gidildi!\n\n")
    elif deger == 2:
        stack.back()
    elif deger == 3:
        if stack.is_empty():
            print("Hiçbir siteye gidilmedi!\n\n ")
            continue
        current_site = stack.current()
        print(f"Şu an {current_site} sitesinde bulunuyorsunuz!\n\n")
    elif deger == 4:
        if stack.is_empty():
            print("Hiçbir siteye gidilmedi!\n\n")
            continue
        print("Browser geçmişi:\n")
        for site in stack.items:
            print(site)
    elif deger == 5:
        print("Çıkış yapılıyor...")
        break


    


    
    


