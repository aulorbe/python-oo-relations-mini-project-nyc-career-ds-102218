from review import Review

class Recipe:

    _all = []

    def __init__(self,reviews=None):
        self._reviews = reviews or []
        Recipe._all.append(self)


#INSTANCE METHODS
    def top_five_reviews(self):
    # returns a list with the five review instances with the highest rating for the given recipe
        reviews = [(review, review.rating) for review in self.reviews]
        reviews.sort(key=lambda tup:tup[1], reverse = True)
        return reviews[:5]

#GETTERS
    @property
    def reviews(self):
        return self._reviews

#SETTERS
    @reviews.setter
    def reviews(self,reviews):
        self._reviews = reviews

#CLASS METHODS
    @classmethod
    def all(cls):
        return cls._all

    @classmethod #NOT FINISHED
    def top_three(cls):
        counter = {}
        for i in recipe.all():
            if recipe.review:
                counter[i] += 1
            else:
                counter[i] = 0





    @classmethod
    def bottom_three(cls):
        pass
