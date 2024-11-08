# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:
    species = "Canis lupus familiaris"

    def __init__(self, n, a):
        self.name = n
        self.age = a
        self.fetch_count = 0
    
    def __str__(self) -> str:
        s = (f"{self.name} is {self.age} years old")
        return s
    
    def play_fetch(self, num_fetch):
        self.fetch_count += num_fetch

    def reset_fetch(self):
        self.fetch_count = 0

# instances of the Dog class
logan = Dog("logan", 8)
cookie = Dog("cookie", 8)
maple = Dog("maple", 1)

logan.play_fetch