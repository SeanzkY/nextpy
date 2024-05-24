DOG_TALK = "woof woof"
CAT_TALK = "meow"
SKUNK_TALK = "tsssss"
UNICORN_TALK = "Good day, darling"
DRAGON_TALK = "Raaaawr"
ZOO_NAME = "Hayaton"


class Animal:
    """
    a class that represents an animal in a zoo and the animal's most basic functionality
    """
    zoo_name = ZOO_NAME

    def __init__(self, name, hunger=0):
        """
        initialize an object that represents an animal
        :param name: this is the given name of the animal
        :type name: str
        :param hunger: this represents the animal's hunger when 0 means it not hungry and the more it increases =
        more hungry
        :type hunger: int
        """
        self._name = name
        self._hunger = hunger

    def get_name(self):
        """
        get name
        :return: the name given to this specific animal
        :rtype: str
        """
        return self._name

    def is_hungry(self):
        """
        whether the animal is hungry or not
        :return: true if the animal is hungry else false based on the animal's level of hunger
        :rtype: bool

        """
        return self._hunger > 0

    def feed(self):
        """
        feeds the animal - decrease it's level of hunger
        """
        self._hunger -= 1

    def talk(self):
        """
        make the animal talk - different animals might make different sounds, prints the sound the animal make
        """
        pass


class Dog(Animal):
    """
    a class that represents a dog in a zoo
    """
    def talk(self):
        print(DOG_TALK)

    def special_fetch(self):
        """
        an action specifically made for a dog - make a sound - prints the sound
        """
        print("There you go, sir!")


class Cat(Animal):
    """
    a class that represents a cat in a zoo
    """
    def talk(self):
        print(CAT_TALK)

    def chase_laser(self):
        """
        an action specifically made for a cat - make a sound - prints the sound
        """
        print("Meeeeow")


class Skunk(Animal):
    """
    a class that represents a skunk in a zoo
    """
    def __init__(self, name, hunger=0, stink_count=6):
        """
        initialize an object that represents a skunk
        :param stink_count: a number that represents how bad does the skunk smell
        :type stink_count: int
        """
        super().__init__(name, hunger)
        self._stink_count = stink_count

    def talk(self):
        print(SKUNK_TALK)

    def stink(self):
        """
        an action specifically made for a skunk - make a sound - prints the sound
        """
        print("Dear Lord!")


class Unicorn(Animal):
    """
    a class that represents a unicorn in a zoo
    """
    def talk(self):
        print(UNICORN_TALK)

    def sing(self):
        """
        an action specifically made for a unicorn - make a sound - prints the sound
        """
        print("I am not your toy...")


class Dragon(Animal):
    """
    a class that represents a dragon in a zoo
    """
    def __init__(self, name, hunger=0, color="green"):
        super().__init__(name, hunger)
        self._color = color

    def talk(self):
        print(DRAGON_TALK)

    def breath_fire(self):
        """
        an action specifically made for a dragon - make a sound - prints the sound
        """
        print("$@#$#@$")


def main():
    zoo_lst = [Dog("Brownie", 10), Cat("Zelda", 3), Skunk("Stinky"),
               Unicorn("keith", 7), Dragon("Lizzy", 1450), Dog("Doggo", 80),
               Cat("kitty", 80), Skunk("Stinky Jr.", 80), Unicorn("Clair", 80),
               Dragon("McFly", 80)]

    for animal in zoo_lst:
        if animal.is_hungry():
            print(type(animal).__name__ + " " + animal.get_name())
            while animal.is_hungry():
                animal.feed()
        animal.talk()
        # prints the special function used for each object which inherits from animal
        if isinstance(animal, Dog):
            animal.special_fetch()

        elif isinstance(animal, Cat):
            animal.chase_laser()

        elif isinstance(animal, Skunk):
            animal.stink()

        elif isinstance(animal, Unicorn):
            animal.sing()

        elif isinstance(animal, Dragon):
            animal.breath_fire()

    print(Animal.zoo_name)


if __name__ == '__main__':
    main()
