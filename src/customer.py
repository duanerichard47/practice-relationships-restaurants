from review import Review #  got this wrong

class Customer:
   
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.reviews =[]
        

    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_reviews(self):
        return self.reviews
    
    def add_review(self, restaurant,rating):
        # return self.reviews[0].get.rating ==5  got this wrong
        review = Review(self, restaurant, rating)
        self.reviews.append(review)
        return self.reviews
      # the customer is in self

    def review_count(self):
            # len(self.reviews) == 1  got this wrong returns T or F
            # return self.reviews
        return len(self.reviews)
