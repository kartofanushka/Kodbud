films=[]
film1=input("введитеназвание фильма 1 ")
film2=input("введитеназвание фильма 2 ")
film3=input("введитеназвание фильма 3 ")

films.append(film1)#добавление эл в конец списка
films.append(film2)
films.append(film3)

films.sort()

print(films)