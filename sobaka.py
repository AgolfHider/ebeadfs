import random
class Dog:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.food = 0.15
        self.alive = True

    def to_eat(self):
        print('Time to eat')
        self.food += 0.12
        self.gladness -= 2

    def to_sleep(self):
        print('Time to sleep')
        self.gladness += 3

    def to_play(self):
        print('time to play')
        self.gladness += 5
        self.food -= 0.08

    def is_alive(self):
        if self.food < -0.5:
            print("You are hungry")
            self.alive = False
        elif self.gladness <= 0:
            print("depression")
            self.alive = False
        elif self.food > 5 and self.gladness >=650:
            print("Happy life")
            self.alive = False
        else:
            print("Too late")
    def end_of_day(self):
        print(
            f"gladness - {self.gladness}\n"            
            f"food - {round(self.food,  2)}"
        )

    def live(self, day):
        print(f'Day#{day} of {self.name} life')
        magic = random.randint(1, 3)
        if  magic == 1:
            self.to_eat()
        elif magic == 2:
            self.to_sleep()
        elif magic == 3:
            self.to_play()
        self.end_of_day()
        self.is_alive()

Sharik = Dog('Sharik')
for day in range(365):
    if Sharik.alive == False:
        break
    Sharik.live(day)