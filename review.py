class Review:

    _all = []

    def __init__(self,recipe,guest,rating,comment=None):
        self._recipe = recipe
        self._guest = guest
        self._rating = rating
        self._comment = comment
        Review._all.append(self)

# GETTERS
    @property
    def recipe(self):
        return self._recipe

    @property
    def guest(self):
        return self._guest

    @property
    def rating(self):
        return self._rating

    @property
    def comment(self):
        return self._comment

# SETTERS
    @recipe.setter
    def recipe(self,recipe):
        self._recipe = recipe

    @guest.setter
    def guest(self,guest):
        self._guest = guest

    @rating.setter
    def rating(self,rating):
        self._rating = rating

    @comment.setter
    def comment(self,comment):
        self._comment = comment

# CLASS METHODS
    @classmethod
    def all(cls):
        return self._all
