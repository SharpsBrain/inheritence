#!/usr/bin/env python
# coding: utf-8

# In[8]:


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("Sharps", "Brain")
x.printname()
class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)
x = Student("Sharps","Channel")
x.printname()


# In[ ]:




