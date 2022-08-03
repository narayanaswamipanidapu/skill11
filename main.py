class Person(object):

    # Constructor
    def __init__(self, Name, From , Destination, Date, Howmany):
        self.Name = Name
        self.From = From
        self.Destination = Destination
        self.Date=Date
        self.Howmany=Howmany



class Employee(Person):
    def __init__(self, Name, From, Destination, Date, Howmany):

        # invoking the init of the parent class
        Person.init(self, Name, From, Destination, Date, Howmany)
    def display(self):
        print(self.Name);
        print(self.From);
        print(self.Destination);
        print(self.Date)
        print(self.Howmany)


a =Employee()

a.__init__('Veda','Vijayawada', 'Hyderabad', '22July', 1)
a.display()

print(" Conformed Details ")

print(" Thankyou For Booking ")

print(" Happy Journey ")
