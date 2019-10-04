# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, room):
        self.room = room
        self.items = []
        
    def __repr__(self):
        return f"Player is currently in {self.room}"
    
    
# sq brackets for objects
# parens for functions