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
        for _ in range(10):
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
    while len(groupsObj.groups) < maxNumGroups and people.peopleSet:
            # Create a new group to hold people
            newGroup = groups.Group([],maxGroupSize,groupsObj.currentNumGroups)
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
        if successor.totalScore > bestScore:
            bestScore = successor.totalScore
            bestSuccessor = successor
    return bestSuccessor

def attemptToTransition(currentState:groups.Groups):
    successorsList = generateSuccessors(currentState,50)
    bestSuccessor = findBestSuccessor(successorsList)
    if bestSuccessor == None:
        return currentState
    else:
        return bestSuccessor

def runGroupSearch(startState:groups.Groups):
    currentState = attemptToTransition(startState)
    newState = attemptToTransition(currentState)
    transitions = 1

    while currentState.totalScore != newState.totalScore:
        transitions+=1
        currentState = newState
        newState = attemptToTransition(currentState)
    print("Transitions = "+ str(transitions))
    
    return currentState

def runThreadedGroupSearch(namesList:list,maxGroupSize:int,maxNumGroups:int,numThreads:int):
    # Generate people and load them into the people set
    generateRandomPeople(namesList)
    # Create a copy of the people set so we can randomize later
    orgPeopleSet = []
    orgPeopleSet.extend(people.peopleSet)

    # Maintain a list of the best groups we have found from all of our threads
    bestGroupsList = []

    for i in range(numThreads):
        peopleCopy = []
        peopleCopy.extend(orgPeopleSet)
        random.shuffle(peopleCopy)
        people.peopleSet.clear()
        people.peopleSet.extend(peopleCopy)
        groupsObj = groups.Groups(maxNumGroups=maxNumGroups)
        loadPeopleIntoGroups(maxGroupSize,maxNumGroups,groupsObj)
        groupsObj.calcTotalGroupScore()
        print("Thread " +str(i+1)+" starting score = "+str(groupsObj.totalScore))
        bestGroup = runGroupSearch(groupsObj)
        print("Thread " +str(i+1)+" best score = "+str(bestGroup.totalScore))
        print("###################################################################")
        bestGroupsList.append(bestGroup)

    finalBestGroup = findBestSuccessor(bestGroupsList)
    print("Best set of groups has a total score of "+str(finalBestGroup.totalScore))
    return bestGroupsList,finalBestGroup

def displayPeopleInGroups(groupsObj:groups.Groups):
    groups = groupsObj.groups
    for group in groups:
        print("###################################################################")
        print("Group #"+ str(group.groupNumber))
        print("-----------------")
        people = group.group
        for person in people:
            print(person.name)
    return

def main():
    testNames = ['Liam','Noah','Oliver','Elijah','James','William','Benjamin','Lucas','Henry','Theodore','Jack','Levi','Alexander','Jackson','Mateo','Daniel']
    # Maximum # of people that can fit into a group
    maxGroupSize = 4
    # Maximum # of groups that can be created
    maxNumGroups = 4

    #Create the groups object to hold all of the groups
    groupsObj = groups.Groups(maxNumGroups=4)


    generateRandomPeople(testNames)
    loadPeopleIntoGroups(maxGroupSize,maxNumGroups,groupsObj)

    bestGroupsList,bestGroup = runThreadedGroupSearch(testNames,maxGroupSize,maxNumGroups,50)
    displayPeopleInGroups(bestGroup)

if __name__=="__main__":
    main()