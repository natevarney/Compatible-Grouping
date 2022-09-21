from array import array


peopleSet = set()

class Person:
    def __init__(self, name:str = '', currentGroup:int = -1, questionAnswers:array = []):
        self.name = name
        self.currentGroup = currentGroup
        self.questionAnswers = questionAnswers

    def updateName(self,newName:str):
        self.name = newName

    def updateGroup(self,newGroup:int):
        self.currentGroup = newGroup

    def updateAnswers(self,newAnswers:array):
        self.questionAnswers = newAnswers

    def addPeopleArray(self):
        peopleSet.add(self)

    def removePeopleArray(self):
        peopleSet.remove(self)