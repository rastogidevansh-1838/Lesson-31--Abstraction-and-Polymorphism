class India():
    def capital(Self):
        print("The capital of India is New Delhi")
    def language(self):
        print("The most widely spoken language in India is Hindi")
    def type(self):
        print("India is a devoloping country")
class USA():
    def capital(self):
        print("The capital of USA is Washington D.C.")
    def language(self):
        print("English is the primary language of USA")
    def type(self):
        print("USA is a devoloped country")
obj_ind = India()
obj_usa = USA()
for country in(obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()