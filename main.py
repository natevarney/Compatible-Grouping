from array import array
from tokenize import group
import people
import groups
import random
import pprint as pp
import copy

# Given a list of names, generates people objects with random question answers
def generateRandomPeople(namesList:array):
    numPeople = len(namesList)
    questionAnswersList = []

    # Iterate through the number of people in the names list
    for _ in range(numPeople):
        answers = []
        # Create random answers for that person
        for _ in range(5):
            answers.append(random.randint(0, 1))
        questionAnswersList.append(answers)
    # Create the person object and add the person to the people set
    for name,answers in zip(namesList,questionAnswersList):
        person = people.Person(name, -1, answers)
        people.peopleSet.append(person)

# Create groups with max number of groups bounded
# Maximum number of people in a group is also bounded
# Loads all of the people from the people set into individual groups
# Then adds each group into the set of all groups
def loadPeopleIntoGroups(maxGroupSize:int,maxNumGroups:int,groupsObj:groups.Groups):
    # Iterate while we have not exceeded max # of groups and people still exist in set of people
    while len(groups.allGroups) < maxNumGroups and people.peopleSet:
            # Create a new group to hold people
            newGroup = groups.Group([],maxGroupSize)
            # Iterate while the group has not exceeded max group size and people still exist in set of people
            while len(newGroup.group) < maxGroupSize and people.peopleSet:
                    # Get the next person in the people set
                    currentPerson = people.peopleSet.pop()
                    # Add that person to the new group
                    newGroup.addPersonToGroup(currentPerson)
                    # Assign that person the corresponding group number
                    groupNumber = newGroup.groupNumber
                    currentPerson.currentGroup = groupNumber
            # Add the group to the set of all groups
            groupsObj.addGroup(newGroup)
    # If groups are maxed with people and max # of groups has been reached
    # And people still exist in the people set that have not been added to groups, raise error
    if len(people.peopleSet) > 0:
        raise Exception("More people exist in people set, than total allowed to fit into groups.\n The maximum number of people you can have is: "+ str(maxGroupSize*maxNumGroups))

def generateNewState(currentState:groups.Groups):
    newState = copy.deepcopy(currentState)
    newState.swapTwoRandomPeople()
    newState.calcTotalGroupScore()
    return newState

def generateSuccessors(currentState:groups.Groups,numSuccessors:int):
    successorsList = []
    for _ in range(numSuccessors):
        newState = generateNewState(currentState)
        successorsList.append(newState)
    return successorsList

def findBestSuccessor(successorList:list):
    bestSuccessor = None
    bestScore = 0
    for successor in successorList:
        print(successor.totalScore)
        if successor.totalScore > bestScore:
            bestScore = successor.totalScore
            bestSuccessor = successor
    return bestSuccessor
    

    



def main():
    testNames = ['Liam','Noah','Oliver','Elijah','James','William','Benjamin','Lucas','Henry','Theodore','Jack','Levi','Alexander','Jackson','Mateo','Daniel']
    # Maximum # of people that can fit into a group
    maxGroupSize = 4
    # Maximum # of groups that can be created
    maxNumGroups = 4

    # jack = people.Person("Jack",14,[1,1,1,1,1])
    # jack.updateName("Bob")
    # jack.addPersonToPeopleArray()
    # print(people.peopleArray)
    # print([vars(node) for node in people.peopleArray])

    #Create the groups object to hold all of the groups
    groupsObj = groups.Groups(maxNumGroups=4)

    # for _ in range(16):
    #     newPerson = people.Person("bob",-1,[1,1,1])
    #     people.peopleSet.add(newPerson)

    # groups.allGroups.clear()
    # for _ in range(4):
    #     newGroup = groups.Group(set(),4)
    #     while len(newGroup.group) < 4 and len(people.peopleSet) > 0:
    #         currentPerson = people.peopleSet.pop()
    #         newGroup.addPersonToGroup(currentPerson)
    #         groups.allGroups.add(newGroup)

    # randomGroup = list(groups.allGroups)[0]
    # print(vars(list(randomGroup.group)[0]))

    generateRandomPeople(testNames)
    loadPeopleIntoGroups(maxGroupSize,maxNumGroups,groupsObj)

    # pp.pprint(vars(groups.allGroups[0]))
    # groups.allGroups[0].calcGroupScore()
    # pp.pprint(vars(groups.allGroups[0]))
    # for person in groups.allGroups[0].group:
    #     print(person.questionAnswers)
    #pp.pprint([vars(person) for person in list(people.peopleSet)])

    groupsObj.updateGroupsWithAllGroups()
    groupsObj.calcTotalGroupScore()
    print("oldScore = "+str(groupsObj.totalScore))
    successors = generateSuccessors(groupsObj,5)
    bestSuccessor = findBestSuccessor(successors)
    print("bestScore = " + str(bestSuccessor.totalScore))

if __name__=="__main__":
    main()