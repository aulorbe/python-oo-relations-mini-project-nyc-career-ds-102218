class Course:

    _all = []

    def __init__(self,dinner_party,recipe):
        self._dinner_party = dinner_party
        self._recipe = recipe
        Course._all.append(self)

# GETTERS

    @property
    def dinner_party(self):
        return self._dinner_party

    @property
    def recipe(self):
        return self._recipe

# SETTERS

    @dinner_party.setter
    def dinner_party(self,dinner_party):
        self._dinner_party = dinner_party

    @recipe.setter
    def recipe(self,recipe):
        self._recipe = recipe 


# CLASS METHODS
    @classmethod
    def all(cls):
        return cls._all
