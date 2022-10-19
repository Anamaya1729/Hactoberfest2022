class test():
    def __init__ (self,subject1,subject2):
        self.subject1= subject1
        self.subject2= subject2
    def show(self):
        print(self.subject1)
        print(self.subject2)
        #  add   test1,test2
    def __add__ (self,other):
        subject1= self.subject1 + other.subject1
        subject2= self.subject2 + other.subject2
        return test(subject1,subject2)
        #  sub   test1,test2
    def __sub__ (self,other):
        subject1= self.subject1 - other.subject1
        subject2= self.subject2 - other.subject2
        return test(subject1,subject2)
    def __mul__ (self, other):
        self.value1 = self.subject1 * other.subject1
        self.value2 = self.subject2 * other.subject2
        return test(self.value1,self.value2)


t1= test(20,20)
t2= test(20,10)
t3=t1+t2
t3.show()
t3=t1-t2
t3.show()
t4 = t1*t2
t4.show()



