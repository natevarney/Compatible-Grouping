from array import array
import people
import random

# Holds all group objects
allGroups = []

# Class for all groups
class Groups:
    def __init__(self, maxNumGroups:int = 0):
        # Maximum number of groups allowed
        self.maxNumGroups = maxNumGroups
        self.groups = []
        # The current number of groups in the allGroups array
        self.currentNumGroups = len(self.groups)
        # Total score (sum of all groups scores)
        self.totalScore = 0

        # If groups already exist in the all groups array and it exceeds the max # of groups throw an error
        if self.currentNumGroups > self.maxNumGroups:
            raise Exception("Inputted group set exceeds maximum number of total groups.")

    def addGroup(self,group):
        if len(self.groups) < self.maxNumGroups:
            self.groups.append(group)
            self.currentNumGroups += 1
        else:
            print("The maximum number of groups has already been created. Group could not be added.")

    def removeGroup(self,group):
        if group in self.groups:
            self.groups.remove(group)
            self.currentNumGroups -= 1
        else:
            print("Group does not exist in the set of all groups. Could not remove group.")

    def updateGroupsWithAllGroups(self):
        self.groups = allGroups

    def updateAllGroupsWithGroups(self):
        allGroups.clear()
        allGroups.extend(self.groups)

    def calcTotalGroupScore(self):
        if len(self.groups) == 0:
            self.totalScore = 0
        else:
            self.totalScore = 0
            for group in self.groups:
                group.calcGroupScore()
                self.totalScore += group.groupScore

    def swapTwoRandomPeople(self):
        numGroups = len(self.groups)
        if numGroups <= 1:
            print("Can not swap people, less than 2 groups exist")
            return
        else:
            groupOneIndex = random.randint(0,len(self.groups)-1)
            groupTwoIndex = groupOneIndex
            while groupOneIndex == groupTwoIndex:
                groupTwoIndex = random.randint(0,len(self.groups)-1)
        groupOne = self.groups[groupOneIndex]
        groupTwo = self.groups[groupTwoIndex]

        groupOnePeople = groupOne.group
        groupTwoPeople = groupTwo.group
        numPeopleG1 = len(groupOnePeople)
        numPeopleG2 = len(groupTwoPeople)

        if numPeopleG1 == 0 or numPeopleG2 == 0:
            print("One of the groups contains no people, can not make swap.")
            return
        else:
            if numPeopleG1 == 1 and numPeopleG2 != 1:
                g1PersonIndex = 0
                g2PersonIndex = g1PersonIndex
                while g1PersonIndex == g2PersonIndex:
                    g2PersonIndex = random.randint(0,numPeopleG2-1)
            elif numPeopleG2 == 1:
                g2PersonIndex = 0
                g1PersonIndex = g2PersonIndex
                while g1PersonIndex == g2PersonIndex:
                    g1PersonIndex = random.randint(0,numPeopleG1-1)
            else:
                g1PersonIndex = random.randint(0,numPeopleG1-1)
                g2PersonIndex = g1PersonIndex
                while g1PersonIndex == g2PersonIndex:
                    g2PersonIndex = random.randint(0,numPeopleG2-1)
        
        personOne = groupOnePeople[g1PersonIndex]
        personTwo = groupTwoPeople[g2PersonIndex]

        groupOnePeople[g1PersonIndex] = personTwo
        groupTwoPeople[g2PersonIndex] = personOne

        personOne.currentGroup = groupTwo.groupNumber
        personTwo.currentGroup = groupOne.groupNumber


        


class Group:
    def __init__(self, group:list = [], maxGroupSize:int = 0, groupNumber:int = 0):
        self.maxGroupSize = maxGroupSize
        self.group = group
        self.groupNumber = groupNumber + 1
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
                
