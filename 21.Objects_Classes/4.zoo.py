class Zoo:
    __animal = 0
    def __init__(self,name):
        self.name = name
        self.mammal = []
        self.fish = []
        self.bird= []

    def add_animal(self,species,name):

        if species == 'mammal':
            self.mammal.append(name)
        elif species == 'fish':
            self.fish.append(name)
        elif species == 'bird':
            self.bird.append(name)
        Zoo.__animal += 1

    def get_info(self,species):
        if species == 'mammal':
            return f"{species} in {self.name}: {', '.join(self.mammal)} \nTotal animals: {Zoo.__animal}"
        elif species == 'fish':
            return f"{species} in {self.name}: {', '.join(self.fish)} \nTotal animals: {Zoo.__animal}"
        elif species == 'bird':
            return f"{species} in {self.name}: {', '.join(self.bird)} \nTotal animals: {Zoo.__animal}"


usr_zoo_name = input()

zoo = Zoo(usr_zoo_name)
number_of_lines = int(input())

for line in range(number_of_lines):
    line_command = input().split()
    token1 = line_command[0]
    token2 = line_command[1]
    zoo.add_animal(token1,token2)

type_of_list = input()
print(zoo.get_info(type_of_list))