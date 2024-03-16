
#task 1
# input = input("enter foods: ")
# class Person:
#     def __init__(self, name, foods_loves, foods_hate, inp):
#         self.name = name
#         self.foods_loves = foods_loves
#         self.foods_hate = foods_hate
#         self.inp = inp
#
#     def food_love(self):
#         return f"{self.name} eats the {self.foods_loves} and loves it!"
#
#     def food_hate(self):
#         return f"{self.name} eats the {self.foods_hate} and hates it!"
#
#
# obj = Person("Sam",["ice cream"], ["carrots"], input=inp)
# if inp == "ice cream":
#     print(obj.food_love())
#
# elif inp == "carrots":
#     print(obj.food_hate())
#
# else:
#     print(f"Sam eats {inp}")
#
#     print(obj)

#task 2
# inp = input("Enter two attributes: ")

# class Book:
#     def __init__(self, title, author, inp):
#         self.title = title
#         self.author = author
#         self.inp = inp
#
#     def titlee(self):
#         return f"{self.title}"
#
#     def authorr(self):
#         return f"{self.author}"
#
#     def get_titlee(self):
#         return f"Title: {self.title}"
#
#     def get_authorr(self):
#         return f"Author: {self.author}"
#
#
#
# obj = Book("Harry Potter", "J.K. Rowling", inp=inp)
# if inp == "title":
#     print(obj.titlee())
#
# elif inp == "author":
#     print(obj.authorr())
#
# elif inp == "get_title":
#     print(obj.get_titlee())
#
# elif inp == "get_author":
#     print(obj.get_authorr())
#task 3
# class Country:
#     def __init__(self, country, population, area):
#         self.is_big = ""
#         self.country = country
#         self.population = population
#         self.area = area
#
#         if self.population > 250000 and self.area > 3000:
#             self.is_big = True
#
#         self.is_big = False
#
#
#     def compare(self, other):
#         if self.population < other.population:
#             return f"{self.country} has a larger population denastiy than {other.country}"
#
#
# obj = Country("Australia", 23545500, 7692024)
# obj1 = Country("Andorra", 76098, 468)
# print(obj.is_big)
# print(obj1.is_big)
# print(obj1.compare(obj))


