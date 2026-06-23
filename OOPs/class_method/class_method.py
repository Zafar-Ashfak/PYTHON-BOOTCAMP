class Person:
    name = "anonymous"

    # def change_name(self, name):
    #     # self.name = name      # creates a new instance
    #     # Person.name = name    # point to the class attribute
    #     self.__class__.name = name  # point to the class attribute

    @classmethod
    def change_name(cls, name):
        cls.name = name

def main():
    p1 = Person()
    p1.change_name("Zafar Ashfaq")
    print(p1.name)
    print(Person.name)

main()