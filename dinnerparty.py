class DinnerParty:

    _all = []

    def __init__ (self,invites,guests=None,courses=None):
        self._invites = invites or []
        self._guests = guests or []
        self._courses = courses or []
        DinnerParty._all.append(self)

# INSTANCE METHODS
    def number_of_attendees(self):
        pass #len of invites

    # def recipes(self):
    #     pass # returns a list of all the recipes for the courses featured at the given dinner party
    #
    # def recipe_count(self):
    #     pass #len of recipes
    #
    # def reviews(self):
    #     pass # returns a list of reviews for the recipes of a given dinner party
    # 
    # def highest_rated_recipe(self):
        # pass # returns the highest rated recipe for the given dinner party

# GETTERS
    @property
    def invites(self):
        return self._invites

    @property
    def guests(self):
        return self._guests

    @property
    def courses(self):
        return self._courses

# SETTERS
    @invites.setter
    def invites(self,invites):
        self._invites = invites

    @guests.setter
    def guests(self,guests):
        self._guests = guests

    @courses.setter
    def courses(self,courses):
        self._courses = courses

# CLASS METHODS
    @classmethod
    def all(cls):
        return cls._all
