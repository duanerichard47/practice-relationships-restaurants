class Restaurant:
    def __init__(self, name):
        self.name = name
        self.reviews =[]

    def get_name(self):
        return self.name 
    
    def get_reviews(self):
        return self.reviews
    
   
    # def average_rating(self):
    #     total = []
    #     for review in self.reviews:
    #         total.append(review.rating)
    #     return sum(total)/len(total)
    
