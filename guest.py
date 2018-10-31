from recipe import Recipe
from review import Review
from course import Course
from invite import Invites

class Guest:

    _all = []

    def __init__(self, name, invites=None,reviews=None):
        self._name = _name
        self._invites = invites or []
        self._reviews = reviews or []
        Guest._all.append(self)

# REGULAR INSTANCE METHODS ##

    def number_of_invites(self):
    #returns the number of dinner party invites a guest has recieved
        return len(self.invites)

    def rsvp(self,invite,rsvp_status):
    #takes in a Boolean and updates guest's RSVP status & returns that status
        # invitation = [i for i in invites.all() if i.guest == self and if i.dinner_party == invite.dinner_party][0]
        # invitation.rsvp = True
        # return invitation.rsvp
        invite.rsvp = rsvp_status
        return invite.rsvp

    def review_recipe(self,recipe,rating,comment):
    # adds a guest's review w/rating & comment to a recipe; returns recipe's reviews
        new_review = Review(self,recipe,rating,comment=None)
        recipe.reviews.append(new_review)
        self.reviews.append(new_review)
        return recipe.reviews

    def favorite_recipe(self):
    # returns guest's favorite recipe (recipe w/highest rating from that specific guest)
        recipe_reviews = {}
        for i in self.reviews:
            recipe_reviews[i] = i._rating
        max_rating = max(recipe_reviews, key=recipe_reviews.get)
        return max_rating.recipe


# GETTERS
    @property
    def name(self): # returns a list of all of the guest's invites
        return self._name

    @property
    def invites(self): #returns a list of all of the guest's reviews
        return self._invites

    @property
    def reviews(self):
        return self._reviews


# SETTERS
    @name.setter
    def name(self,name):
        self._name = name

    @invites.setter
    def invites(self,invites):
        self._invites = invites

    @reviews.setter
    def reviews(self,reviews):
        self._reviews = _reviews


# CLASS METHODS
    @classmethod
    def all(cls):
        return cls._all

    @classmethod
    def most_popular(cls): #returns most popular guest (guest w/most invites)
        guests_invites = {}
        for i in Guest._all:
            guests_invites[i] = len(i.invites)
        return max(guests_invites, key=guests_invites.get)

    @classmethod
    def toughest_critic(self):
        pass #UNFINISHED!

    @classmethod
    def most_active_critic(cls): #returns guest with most recipe reviews
        guests_reviews = {}
        for i in Guest._all:
            guests_reviews[i] = len(i.reviews)
        return max(guests_reviews, key=guests_reviews.get)
