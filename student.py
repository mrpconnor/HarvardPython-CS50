
class Student:
    def __init__(self, name, house, patronus):
       # if not name:
           # raise ValueError("Missing Name")
        #if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            #raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        patronus = input("Charm: ")
        return cls(name, house, patronus)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not  name:
            raise ValueError("Missing Name")
        self._name = name

    # Getter
    @property
    def house(self):
        return self._house

    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

    #student = get_student()
    #print(f"{student.name} from {student.house}")

    def charm(self):
        match self.patronus:
            case "Stag":
                return "stag"
            case "Otter":
                return "otter"
            case "Terrier":
                return "terrier"
            case _:
                return "None"
def main():
   student = Student.get
   #print(student)
   #print(f"{student.name} from {student.house}")
   print("Expecto Patronum!")
   print(student.charm())

#def get_student():

  #  name = input("Name: ")
  #  house = input("House: ")
  #  patronus = input("Patronus: ")
 #   return Student(name, house, patronus)
    



#return {"name": name, "house": house}
#return (name, house)
#return [name, house]

main()
#if __name__ == "__main__":