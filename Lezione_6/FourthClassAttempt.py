class Animal:
    
    def __init__(self,name,legs):
        self.name = name
        self.legs = legs
    

    def changeLegs(self, new_legs):
        self.legs = new_legs

    def setLegs(self, new_legs):
        self.legs = new_legs
    
    def getLegs(self):
        return self.legs
    
    def printInfo(self):
        print(f"name: {self.name}, legs: {self.legs}")
    

dog = Animal("Dog",3)
bird = Animal("bird",2)

print(f"{dog.name} name animal 1, {bird.name} name animnal 2")

dog.legs = 3
print(f"{dog.name} has now {dog.legs} legs")

bird.setLegs(3)
print(f"legs of {bird.name} are now {bird.legs}")


print(f"{dog.getLegs()} legs {dog.name}, {bird.getLegs()} legs {bird.name}")

dog.printInfo()
bird.printInfo()


    