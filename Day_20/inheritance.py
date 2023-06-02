class Animal:
    def __init__(self) -> None:
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self) -> None:
        super().__init__()
        #self.num_eyes = 4 # This line of code would have seen the inherited attribute and reassigned it to 4.

    def breathe(self):
        super().breathe()
        print("Doing this underwater.")

    def swim(self):
        print("Moving in water.")