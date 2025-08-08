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

    match answer:
        case "1":
            Data = Person(
                input("First name REQUIRED: "),
                input("Last name REQUIRED: "),
                input("E-mail REQUIRED: "),
                input("Phone: "),
            )
            db.CreateEntry(Data)
        
        case "3":
            id = input("ID: ")
            db.DeleteById()

        case "2":
            id = input("ID: ")
            person = db.GetEntryByID(id)

            listPerson = list(person[0])
            listPerson.pop(0)

            print(listPerson)

            index = input("Which value do you want to change INDEX: ")
            newValue = input(f"{type(listPerson[int(index)]).__name__} Value: ")

            listPerson[int(index)] = newValue

            personDB = Person(
                listPerson[0],
                listPerson[1],
                listPerson[2],
                listPerson[3],
            )

            db.Update(personDB, id)
        case "4":
            db.GetAllEntry()
            
        case "5":
            id = input("ID: ")
            person = db.GetEntryByID(id)
            print(person)

