import json

class ReviewHandler:
    def __init__(self):
        self.reviews = {}

    def add_review(self, user_id, stars, text):
        self.reviews[user_id] = {'stars': stars, 'text': text}
        self.save_reviews()

    def save_reviews(self):
        with open('data/reviews.json', 'w') as file:
            json.dump(self.reviews, file)

    def load_reviews(self):
        try:
            with open('data/reviews.json', 'r') as file:
                self.reviews = json.load(file)
        except FileNotFoundError:
            pass