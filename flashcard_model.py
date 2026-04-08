from flashcard_manager import FlashcardManager

class FlashcardModel:
    def __init__(self):
        self.manager = FlashcardManager()
        self.cards = self.manager.get_cards()
        self.current_index = 0
    
    def get_cards(self):
        return self.cards
    
    def get_current_card(self):
        if self.cards and self.current_index < len(self.cards):
            return self.cards[self.current_index]
        return None
    
    def get_current_index(self):
        return self.current_index
    
    def get_total_cards(self):
        return len(self.cards)
    
    def next_card(self):
        if self.current_index < len(self.cards) - 1:
            self.current_index += 1
            return True
        return False
    
    def previous_card(self):
        if self.current_index > 0:
            self.current_index -= 1
            return True
        return False
    
    def add_card(self, question, answer):
        if self.manager.add_card(question, answer):
            self.cards = self.manager.get_cards()
            self.current_index = len(self.cards) - 1
            return True
        return False
    
    def delete_current_card(self):
        if self.manager.delete_card(self.current_index):
            self.cards = self.manager.get_cards()
            # Adjust index if needed
            if len(self.cards) == 0:
                self.current_index = 0
            elif self.current_index >= len(self.cards):
                self.current_index = len(self.cards) - 1
            return True
        return False