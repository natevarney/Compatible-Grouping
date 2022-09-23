from array import array
import people

# Holds all group objects
allGroups = []

# Class for all groups
class Groups:
    def __init__(self, maxNumGroups:int = 0):
        # Maximum number of groups allowed
        self.maxNumGroups = maxNumGroups
        # The current number of groups in the allGroups array
        self.currentNumGroups = len(allGroups)
        # Total score (sum of all groups scores)
        self.totalScore = 0

        # If groups already exist in the all groups array and it exceeds the max # of groups throw an error
        if self.currentNumGroups > self.maxNumGroups:
            raise Exception("Inputted group set exceeds maximum number of total groups.")

    def addGroup(self,group):
        if len(allGroups) < self.maxNumGroups:
            allGroups.append(group)
            self.currentNumGroups += 1
        else:
            print("The maximum number of groups has already been created. Group could not be added.")

    def removeGroup(self,group):
        if group in allGroups:
            allGroups.remove(group)
            self.currentNumGroups -= 1
        else:
            print("Group does not exist in the set of all groups. Could not remove group.")

    def calcTotalGroupScore(self):
        if len(allGroups) == 0:
            self.totalScore = 0
        else:
            self.totalScore = 0
            for group in allGroups:
                group.calcGroupScore()
                self.totalScore += group.groupScore

class Group:
    def __init__(self, group:list = [], maxGroupSize:int = 0):
        self.maxGroupSize = maxGroupSize
        self.group = group
        self.groupNumber = len(allGroups) + 1
        self.currentGroupSize = len(self.group)
        self.groupScore = 0

        if self.currentGroupSize > self.maxGroupSize:
            raise Exception("Inputted group exceeds maximum number of people allowed in a group")

    def addPersonToGroup(self,person:people.Person):
        if len(self.group) < self.maxGroupSize:
            self.group.append(person)
            self.currentGroupSize += 1
        else:
            print("Group is full, person could not be added to group.")

    def removePersonFromGroup(self,person:people.Person):
        if person in self.group:
            self.group.remove(person)
            self.currentGroupSize -= 1
        else:
            print("Person is not in group, could not remove person from group.")

    def calcGroupScore(self):
        if len(self.group) == 0:
            self.groupScore = 0
        else:
            self.groupScore = 0
            for i in range(len(self.group)):
                personOne:people.Person = self.group[i]
                pOneAnswers = personOne.questionAnswers
                for j in range(i+1,len(self.group)):
                    personTwo:people.Person = self.group[j]
                    pTwoAnswers = personTwo.questionAnswers
                    for a1,a2 in zip(pOneAnswers,pTwoAnswers):
                        if a1 == a2:
                            self.groupScore += 1
                
