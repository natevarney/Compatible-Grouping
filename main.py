import people
import groups


def main():
    # jack = people.Person("Jack",14,[1,1,1,1,1])
    # jack.updateName("Bob")
    # jack.addPersonToPeopleArray()
    # print(people.peopleArray)
    # print([vars(node) for node in people.peopleArray])

    groupsObj = groups.Groups(set(),maxNumGroups=4)

    for _ in range(16):
        newPerson = people.Person("bob",-1,[1,1,1])
        people.peopleSet.add(newPerson)

    groups.allGroups.clear()
    for _ in range(4):
        newGroup = groups.Group(set(),4)
        while len(newGroup.group) < 4 and len(people.peopleSet) > 0:
            currentPerson = people.peopleSet.pop()
            newGroup.addPersonToGroup(currentPerson)
            groups.allGroups.add(newGroup)

    randomGroup = list(groups.allGroups)[0]
    print(vars(list(randomGroup.group)[0]))

if __name__=="__main__":
    main()