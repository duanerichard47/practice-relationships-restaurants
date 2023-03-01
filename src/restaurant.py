class Restaurant:
    def __init__(self, name):
        self.name = name
        self.reviews =[]

    def get_name(self):
        return self.name 
    
    def get_reviews(self):
        return self.reviews