def show(name, lastname):
    print(name+' '+lastname)
person = ["Ariel", "Betancud"]
show(person[0], person[1])
show(*person)
person2 = ("Osvaldo", "Giordanini")
show(*person2)
person3 = {"lastname" : "Lucero", "name" : "Natalia"}
show(**person3)