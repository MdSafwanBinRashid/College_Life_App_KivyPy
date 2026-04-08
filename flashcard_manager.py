import json
import os

class FlashcardManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self.file_path = "flashcards.json"
        self.default_cards = [
            {"question": "What is a variable?", "answer": "A container for storing data values"},
            {"question": "What does HTML stand for?", "answer": "Hypertext Markup Language"},
            {"question": "What is the mean of 2, 4, 6, 8?", "answer": "5"},
            {"question": "Symbol for the sample mean?", "answer": "x̄ (x-bar)"},
            {"question": "Newton's second law of motion?", "answer": "F = ma"},
            {"question": "Speed of light in vacuum?", "answer": "3 × 10⁸ m/s"},
            {"question": "Chemical symbol for gold?", "answer": "Au"},
            {"question": "pH of pure water?", "answer": "7"},
            {"question": "Organelle known as the powerhouse?", "answer": "Mitochondria"},
            {"question": "Process by which plants make food?", "answer": "Photosynthesis"},
            {"question": "Unit of electric current?", "answer": "Ampere (A)"},
            {"question": "Formula for standard deviation?", "answer": "√(Σ(x - x̄)² / n)"}
        ]
        self.cards = self.load_cards()
    
    def load_cards(self):
        """Load cards from JSON file, or return defaults if file doesn't exist"""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r') as f:
                    return json.load(f)
            except:
                return self.default_cards.copy()
        else:
            return self.default_cards.copy()
    
    def save_cards(self):
        """Save current cards to JSON file"""
        try:
            with open(self.file_path, 'w') as f:
                json.dump(self.cards, f, indent=2)
        except:
            print("Failed to save flashcards")
    
    def get_cards(self):
        return self.cards
    
    def add_card(self, question, answer):
        if question and answer:
            self.cards.append({"question": question, "answer": answer})
            self.save_cards()
            return True
        return False
    
    def delete_card(self, index):
        if 0 <= index < len(self.cards):
            del self.cards[index]
            self.save_cards()
            return True
        return False