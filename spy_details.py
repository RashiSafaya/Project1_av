# default user details

class spy:

    name = "Rashi Safaya",
    salutation = "Ms.",
    age = 21,
    rating = 4.5,
    is_online = True
    chats = []
    current_status_message = None

    def setSpy(self, name, salutation, age, rating, is_online):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True


    # getter methods

    def getName(self):
        return self.name
    def getSalutation(self):
        return self.salutation
    def getage(self):
        return self.age
    def getrating(self):
        return self.rating
    def getis_online(self):
        return self.is_online




friends = [
    {
        'name': "Dinesh Sharma",
        'salutation': "Mr.",
        'age': 23,
        'rating': 4,
        'chats': []
    },

    {
        'name': "Feroz Shah",
        'salutation': "Mr.",
        'age': 27,
        'rating': 4.3,
        'chats': []

    },

    {
        'name': "Shailja Kumar",
        'salutation': "Mrs.",
        'age': 24,
        'rating': 3.9,
        'chats': []

    }

]


