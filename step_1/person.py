
#inheritance

class Person : 
    eyex = 2
    mose = 1
    mouth = 1
    ears = 2
    arms = 2
    legs = 2

    def eat(self) :
        return "eat..."

    def sleep(self) :
        return "Zzzz..."

    def talk(self) : 
        return "talktalk"
    

class Student(Person) :
    def study(self) :
        return 'study...'