from curses import ACS_GEQUAL
from tkinter import scrolledtext
from unicodedata import name


class Student:
    # [assignment] Skeleton class. Add your code here

    def __init__(self, name, age, tracks, score):
        self.name=name
        self.age=age 
        self.score=score
        self.tracks = tracks 

    def change_name(self, name):
        self.name = name

    def change_age(self,age):
        self.age = age
        return ("%s is %s years old"%(self.name,self.age))
    
    def add_track(self,track):
        self.tracks.append(track)

    def get_score(self):
        self.score

    def __str__(self):
        return "His name is %s, he is %s years old and his score is %s and his tracks are %s"%(self.name, self.age, self.score,self.tracks)



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track('UI/UX')
Bob.get_score()
print(Bob)

