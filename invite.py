class Invite:

    _all = []

    def __init__(self,rsvp=False,guest,dinner_party):
        self._accepted = rsvp
        self._guest = guest
        self._dinner_party = dinner_party
        Invite._all.append(self)

# GETTERS
    @property
    def accepted(self):
        return self._accepted

    @property
    def guest(self):
        return self._guest

    @property
    def dinner_party(self):
        return self._dinner_party

# SETTERS
    @accepted.setter
    def accepted(self,rsvp):
        self._accepted = rsvp

    @guest.setter
    def guest(self,guest):
        self._guest = guest

    @dinner_party.setter
    def dinner_party(self,dinner_party):
        self._dinner_party = dinner_party


# CLASS METHODS
    @classmethod
    def all(cls):
        return cls._all
