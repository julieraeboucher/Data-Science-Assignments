# 1. Define the `Greeter` class
class Greeter:
    # 2. Class variable - array of Greeter instances
    greetings = []

    # 3. Initializer for two instance properties: first and last name
    def __init__(self, first, last):
        """Initializer of class"""
        self.first = first    #: Instance var for perosns first name
        self.last = last  #: Instance var for persons last name
        
    # 4. Instance method to display information about a person
    def display(self):
        """Instance method to display student info"""
        print('Hello ' , self.first , " " , self.last , '!')
        
    # 5. Class method to add a person instance to class array `greetings`
    @staticmethod
    def add_person(person):
        """Class method for adding a peerson to the class var"""
        Greeter.greetings.append(person)

    # 6. Class method to call the `display` method for all students
    @staticmethod
    def display_person():
        """Class method for printing all people"""
        for person in Greeter.greetings:
            person.display()

# 7. create an instance of `Student` and print info
bill = Greeter('Bill', 'Barnes')
bill.display()

# 8. create another instance of `Student` and print info
sally = Greeter('Sally', 'Smith')
sally.display()

# 9. add both students to student array which is a class var
#    using the class method `add_student`
Greeter.add_person(bill)
Greeter.add_person(sally)

# 10. call class method `display_students` to print info
#     for all added students
print('--------')
Greeter.display_person()