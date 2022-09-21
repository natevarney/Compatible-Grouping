from array import array
from tokenize import group
import people
import groups
import random
import pprint as pp


def generateRandomPeople(namesList:array):
    numPeople = len(namesList)
    questionAnswersList = []

    for _ in range(numPeople):
        answers = []
        for _ in range(5):
            answers.append(random.randint(0, 1))
        questionAnswersList.append(answers)

    for name,answers in zip(namesList,questionAnswersList):
        person = people.Person(name, -1, answers)
        people.peopleSet.add(person)

def loadPeopleIntoGroups(maxGroupSize:int,maxNumGroups:int,groupsObj:groups.Groups):
    while len(groups.allGroups) < maxNumGroups and people.peopleSet:
            newGroup = groups.Group(set(),maxGroupSize)
            while len(newGroup.group) < maxGroupSize and people.peopleSet:
                    currentPerson = people.peopleSet.pop()
                    newGroup.addPersonToGroup(currentPerson)
                    groupNumber = newGroup.groupNumber
                    currentPerson.currentGroup = groupNumber
            groupsObj.addGroup(newGroup)
    if len(people.peopleSet) > 0:
        raise Exception("More people exist in people set, than total allowed to fit into groups.\n The maximum number of people you can have is: "+ str(maxGroupSize*maxNumGroups))

    



def main():
    testNames = ['Liam','Noah','Oliver','Elijah','James','William','Benjamin','Lucas','Henry','Theodore','Jack','Levi','Alexander','Jackson','Mateo','Daniel']
    maxGroupSize = 4
    maxNumGroups = 4
    # jack = people.Person("Jack",14,[1,1,1,1,1])
    # jack.updateName("Bob")
    # jack.addPersonToPeopleArray()
    # print(people.peopleArray)
    # print([vars(node) for node in people.peopleArray])

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

    pp.pprint(vars(list(groups.allGroups)[0]))
    pp.pprint(list(list(groups.allGroups)[0].group)[0].currentGroup)
    #pp.pprint([vars(person) for person in list(people.peopleSet)])

if __name__=="__main__":
    main()