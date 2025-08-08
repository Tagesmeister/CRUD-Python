from dataclasses import dataclass
from Database import DB


@dataclass
class Person:
    firstName: str
    lastName: str
    email: str
    phone: str


db = DB()

while True:
    print("What action do you want?")

    answer = input(
        "1 = create | 2 = update | 3 = delete | 4 = showAll | 5 = Show with ID: "
    )
    if answer in ["1", "2", "3", "4", "5"]:
        match answer:
            case "1":
                Data = Person(
                    input("First name REQUIRED: "),
                    input("Last name REQUIRED: "),
                    input("E-mail REQUIRED: "),
                    input("Phone: "),
                )
                db.CreateEntry(Data)

            case "2":

                id = input("ID: ")

                try:
                    id = int(id)
                except:
                    print("Wrong Input")
                    exit()

                index = input("Which value do you want to change INDEX: ")
                try:
                    index = int(index)
                except:
                    print("Invalid Input")
                    exit()

                person = db.GetEntryByID(id)

                if person:
                    listPerson = list(person[0])
                    listPerson.pop(0)
                    print(listPerson)
                    print("No entry has been found")

                    newValue = input(f"{type(listPerson[index]).__name__} Value: ")

                    listPerson[index] = newValue

                    personDB = Person(
                        listPerson[0],
                        listPerson[1],
                        listPerson[2],
                        listPerson[3],
                    )

                    db.Update(personDB, id)
                else:
                    print("No entries have been found")
                    exit()

            case "3":
                id = input("ID: ")
                try:
                    id = int(id)
                    db.DeleteById(id)

                except:
                    print("Invalid input")
                    exit()

            case "4":
                people = db.GetAllEntry()
                if len(people) > 0:
                    for x in people:
                        print(x)
                else:
                    print("No Entry has been found")

            case "5":
                people = db.GetAllEntry()

                if len(people) > 0:
                    id = input("ID: ")
                    try:
                        id = int(id)
                    except:
                        print("Invalid Input")
                        exit()
                    person = db.GetEntryByID(id)
                    if person:
                        print(person)
                    else:
                        print("No entries have been found")

                else:
                    print("No entries has been found")

    else:
        print("Wrong input")
