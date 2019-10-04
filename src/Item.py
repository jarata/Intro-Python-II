class Item:
    def __int__(self, name, description):
        self.name = name
        self.description = description
        
    def __repr__(self):
        return f"{self.name}: {self.description}"