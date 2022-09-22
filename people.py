from array import array


peopleSet = []

class Person:
    def __init__(self, name:str = '', currentGroup:int = -1, questionAnswers:array = []):
        # Name of the person (String)
        self.name = name
        # Current group # that they are in (Int)
        self.currentGroup = currentGroup
        # An array of 1s and 0s representing answers to yes/no questions (list)
        self.questionAnswers = questionAnswers

    def updateName(self,newName:str):
        self.name = newName

    def updateGroup(self,newGroup:int):
        self.currentGroup = newGroup

    def updateAnswers(self,newAnswers:array):
        self.questionAnswers = newAnswers

    def addPeopleArray(self):
        peopleSet.append(self)

    def removePeopleArray(self):
        peopleSet.remove(self)