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

    # Used to change a person objects name
    def updateName(self,newName:str):
        self.name = newName
    
    # Used to change a person objects group #
    def updateGroup(self,newGroup:int):
        self.currentGroup = newGroup

    # Used to update the answers array of a person object
    def updateAnswers(self,newAnswers:array):
        self.questionAnswers = newAnswers

    # Adds the person to the set of all people
    def addPeopleArray(self):
        peopleSet.append(self)

    # Removes a person from the set of all people
    def removePeopleArray(self):
        peopleSet.remove(self)