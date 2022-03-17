class PlayerCharacter:
    # Class Object Attribute
    membership = True  # this is static not dynamic

    def __init__(self, name):  # here we have to give our Instanz a name
        if self.membership:
            self.name = name  # self -> is for this instanz value
        # here this is dynamic

    def run(self):
        print("run")

    def shout(self, hello):
        print(f"My name is {self.name}")


# they live in different places in memory, for each instance
player1 = PlayerCharacter("Peter")  # <- there is the name
print(player1.name)
player1.run()
