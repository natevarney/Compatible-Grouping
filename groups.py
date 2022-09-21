from array import array
import people

class Groups:
    def __init__(self, groupsSet:set = set(), maxNumGroups:int = 0):
        global allGroups
        allGroups = groupsSet
        self.maxNumGroups = maxNumGroups
        self.currentNumGroups = len(groupsSet)

        if self.currentNumGroups > self.maxNumGroups:
            raise Exception("Inputted group set exceeds maximum number of total groups.")

    def addGroup(self,group):
        if len(allGroups) < self.maxNumGroups:
            allGroups.add(group)
            self.currentNumGroups += 1
        else:
            print("The maximum number of groups has already been created. Group could not be added.")

    def removeGroup(self,group):
        if group in allGroups:
            allGroups.remove(group)
            self.currentNumGroups -= 1
        else:
            print("Group does not exist in the set of all groups. Could not remove group.")


class Group:
    def __init__(self, group:set = set(), maxGroupSize:int = 0):
        self.maxGroupSize = maxGroupSize
        self.group = group
        self.groupNumber = len(allGroups) + 1
        self.currentGroupSize = len(self.group)

        if self.currentGroupSize > self.maxGroupSize:
            raise Exception("Inputted group exceeds maximum number of people allowed in a group")

    def addPersonToGroup(self,person:people.Person):
        # if len(self.group) < self.maxGroupSize:
        self.group.add(person)
        #     self.currentGroupSize += 1
        # else:
        #     print("Group is full, person could not be added to group.")

    def removePersonFromGroup(self,person:people.Person):
        if person in self.group:
            self.group.remove(person)
            self.currentGroupSize -= 1
        else:
            print("Person is not in group, could not remove person from group.")