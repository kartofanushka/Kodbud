import requests
import pprint

"""
print(type(True))

a=1
b=2
c=3
# if True:(b>a):
    # print(a)
    
if b>a and b>c: #True and False
    print(a)
if b>a or b>c: #True or False
    print("ksjdf")
if not b>c:
    print("jfg")
if (b>a and b>c)or (b>a or b>c) and not b>c:
    print("ksjfh")


import time
my_time=int(time.strftime("%H"))
print("My time is: ", my_time)

print(time.ctime())
print(type(time.time()),time.time())
if my_time>=7 and my_time<=12:
    print("Morning")
elif my_time>12 and my_time<=17:
    print("Day")
elif my_time>17 and my_time<=22:
    print("Evrning")
else:
    print("Night")
    """
    
url='https://swapi.dev/api/'
"""   
{
    "people": "https://swapi.dev/api/people/", 
    "planets": "https://swapi.dev/api/planets/", 
    "films": "https://swapi.dev/api/films/", 
    "species": "https://swapi.dev/api/species/", 
    "vehicles": "https://swapi.dev/api/vehicles/", 
    "starships": "https://swapi.dev/api/starships/"
}
"""
responce=requests.get(url).json() #""
# responce=requests.get(url).text #''

# print(responce)

people_api=responce.get("people")
starships_api=responce.get("starships")
print(people_api)
# for p in people_api:
#     print(p["name"])

def chk_people():
    for i in range (1,6):
        responce=requests.get(people_api+"/"+str(i)).json()
        print(responce["name"], responce["height"])


def chk_planets(): #get planet name and diametr and sort it by diametr asc
    responce=requests.get(url+"/planets").json()
    # print(responce)
    print(responce["results"][0]) #1st element
    print(responce["results"][0]["name"]) #1st element name
    name=[]
    di=[]
    planet={}
    for p in responce["results"]:
        name.append(p["name"])
        di.append(int(p["diameter"]))
        print(p["name"],p["diameter"])
    # print(responce.get[3]('height'))
    di_sorted=sorted(di) #.sort()
    print(name,di,di_sorted)
    for l in di_sorted:
        di.index(l)
        planet[name[di.index(l)]]=di[di.index(l)]
    print(planet)
def chk_starships():
    responce=requests.get(starships_api).json()
    # print(responce)
    print(responce["results"][0]) #1st element
    print(responce["results"][0]["name"]) #1st element name

    # for p in responce["results"]:
    #     print(p["name"])
    # print(responce.get[3]('height'))
    # print(responce)
    
# starships max speed
# HW1
# Выведите максимальную скорость 5 космических кораблей из всех.
# API — starships_api = response.get('starships')
# Максимальная скорость — max_atmosphering_speed
def chk_starships_m_s():
    
    responce=requests.get(starships_api).json()
    name=[]
    speed=[]
    while responce['next'] !=None:
           
        # print(responce['next'])
        # print(responce["results"][0]) #1st element
        # print(responce["results"][0]["name"]) #1st element name
       
        for p in responce["results"]:
            p["max_atmosphering_speed"]=p["max_atmosphering_speed"].replace('km', '').strip()
            # print(responce["results"].index(p))
            if p["max_atmosphering_speed"].isdigit():
            
                name.append(p["name"])
                speed.append(int(p["max_atmosphering_speed"]))
               
        # print(name[speed.index(max(speed))], max(speed))
        responce=requests.get(responce['next']).json()
    # print(len(name),len(speed))
    # print(speed)
    t=1
    fastestn=[]
    fastests=[]
    for p in speed:
        while t<6:
            popindex=speed.index(max(speed))
            ext_speed=speed.pop(popindex)
            ext_name=name.pop(popindex)
            print(t,'. ',ext_speed,'\t',ext_name)
            t+=1
            fastestn.append(ext_name)
            fastests.append(ext_speed)
    return(fastestn,fastests)
# chk_starships_m_s()
    
# HW2
# Сравните их максимальную скорость и выведите название самого быстрого корабля.
def fastest_ship():
    data=chk_starships_m_s()
    print(data)
    name=data[0]
    speed=data[1]
    popindex=speed.index(max(speed))
    ext_speed=speed[popindex]
    ext_name=name[popindex]
    return(str(ext_speed)+'\t'+ext_name)
print(fastest_ship())

def chk_starships_m_s_1st(): 
    # это то что я сдала. тут самый быстрый из пеервых 5 кораблей , зачли, но это хрень
    responce=requests.get(starships_api).json()
    name=[]
    speed=[]
    for p in responce["results"]:
        if responce["results"].index(p)<5:
            if p["max_atmosphering_speed"]!='n/a':
                name.append(p["name"])
                speed.append(int(p["max_atmosphering_speed"]))
            # print(responce["results"].index(p)+1,". ",p["name"],p["max_atmosphering_speed"])

    print(name[speed.index(max(speed))], max(speed))
# chk_starships_m_s_1st()

def chk_starships_1st_10(): #print 1st 10 starships in api
    responce=requests.get(starships_api).json()
    for p in responce["results"]:
        # print(responce["results"].index(p))
        if responce["results"].index(p)<10:
            print(responce["results"].index(p)+1,". ",p["name"],p["max_atmosphering_speed"])
# chk_starships_1st_10()

def chk_people1():
    responce=requests.get("https://swapi.dev/api/people/").json()
    print(responce)
    print(responce["results"][1]["name"])
    
    for p in responce["results"]:
        print(p["name"])
    # print(responce.get[3]('height'))
    # print(responce)
# chk_people()
#chk_people1()
# chk_starships()
# chk_planets()
# chk_starships_m_s()