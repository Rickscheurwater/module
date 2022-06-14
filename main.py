from my_module import functions

mytekst = open("names.txt","rt");

for regel in mytekst:
    print(functions.sanitize(regel))

for lijst in mytekst:
        print(functions.create_person(lijst))

persons = []
for regel in open("names.txt", 'rt'):
    lst = functions.sanitize(regel)
    person = functions.create_person(lst)
    person = functions.add_fullname(person)
    persons.append(person)

functions.print_persons(persons)