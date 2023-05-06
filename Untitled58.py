#!/usr/bin/env python
# coding: utf-8

# Create a function that takes an integer and returns a list from 1 to the given number, where:
# If the number can be divided evenly by 4, amplify it by 10 (i.e. return 10 times the number).
# If the number cannot be divided evenly by 4, simply return the number.
# 

# In[1]:


def amplify(num):
    return [(n*10 if n % 4 == 0 else n)for n in range(1, num+1)]


# In[2]:


amplify(4)


# In[3]:


amplify(3) 


# In[4]:


amplify(25)


# Create a function that takes a list of numbers and return the number that's unique.
# 

# In[5]:


def unique(lst):
    for num in lst:
        if lst.count(num) == 1:
            return num


# In[6]:


unique([3, 3, 3, 7, 3, 3])


# In[7]:


unique([0, 0, 0.77, 0, 0])


# In[8]:


unique([0, 1, 1, 1, 1, 1, 1, 1])


# Your task is to create a Circle constructor that creates a circle with a radius provided by an argument. The circles constructed must have two getters getArea() (PIr^2) and getPerimeter() (2PI*r) which give both respective areas and perimeter (circumference).
# For help with this class, I have provided you with a Rectangle constructor which you can use as a base example.
# 

# In[12]:


import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def getArea(self):
        return round(math.pi * self.radius ** 2)
    def getPerimeter(self):
        return round(2 * math.pi * self.radius)


# In[13]:


circy = Circle(11)
circy.getArea()


# In[14]:


circy = Circle(4.44)
circy.getPerimeter()


# Create a function that takes a list of strings and return a list, sorted from shortest to longest.
# 

# In[20]:


def sort_by_lenght(lst):
    return sorted(lst, key=len)


# In[22]:


sort_by_lenght(["Google", "Apple", "Microsoft"])


# In[24]:


sort_by_lenght(["Leonardo", "Michelangelo", "Raphael", "Donatello"])


# In[25]:


sort_by_lenght(["Turing", "Einstein", "Jung"])


# Create a function that validates whether three given integers form a Pythagorean triplet. The sum of the squares of the two smallest integers must equal the square of the largest number to be validated.
# 

# In[26]:


def is_triplet(a, b, c):
    a, b, c = sorted([a, b, c])
    return a**2 + b**2 == c**2


# In[27]:


is_triplet(3, 4, 5)


# In[28]:


is_triplet(13, 5, 12)


# In[29]:


is_triplet(1, 2, 3)


# In[ ]:




