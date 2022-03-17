# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def adding_things(cls, num1, num2):
        # with the cls we instantiate this Object from this func with the @classmethod - even if we don't have any Instance of this class
        return cls("Teddy", num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2  # we can't instantiate an Object from a static func


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat("Kurt", 15)
cat2 = Cat("Private", 12)
cat3 = Cat("Dexter", 9)


# 2 Create a function that finds the oldest cat
def get_oldestCat(*Cat):
    allCats = list(Cat)

    oldestCat = allCats[0]
    for cat in allCats:

        if cat.age > oldestCat.age:
            oldestCat = cat
    return oldestCat


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

oldestCat = get_oldestCat(cat1, cat2, cat3)

print(f"Th eoldest cat is {oldestCat.age} years old.")

newCat = Cat.adding_things(2, 3)
print(newCat.age)
