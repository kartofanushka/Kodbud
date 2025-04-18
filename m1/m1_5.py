# add to dict
# result_price['USA'] = '0.62510000'
# {'USA': '0.62510000', 'EU': '0.61900000'}

films = {
    "Бойцовский клуб": "Брэд Питт",
    "Я легенда": "Вил Смит",
    "Пираты Карибского Моря": "Джонни Депп",
    'ff':'hh'
}
print(films['ff']) # show dict value
print(films.keys())
# print(films[1]) # show dict value
print(films.keys())

# print(films.get(input(1), ""))
# if film in films:
#     print(films.get(film))
    
# d={123,123}
# d2=d
# print(d2)

# Комментарий преподавателя:
# Ничего не понятно. Какой вопрос? Что отвечать: число или индекс? Если индекс, то с нуля или с единицы?

# Без читов не разобрался. Зачитываю!

# # ============= 1 =====================
# quest=[
# {'qq':'question text1', 'answers':[4,5],'correct_a':4},
# {'qq':'question text2', 'answers':[2,5,6],'correct_a':5},
# {'qq':'question text3', 'answers':[4,5],'correct_a':4},
# {'qq':'question text4', 'answers':[4,5],'correct_a':4}
# ]
# i=0
# for q in quest:
#     print(q['qq'])
#     print(q['answers'])
#     u_an=int(input('input answer: '))
#     # if u_an> len(q['answers']) or u_an<=0:
#     if q['answers'][u_an-1]==q['correct_a']:
#         print('correct')
#         i +=1
#     else:
#         print('(((')
# print('-'*20)
# print('набралт очков: ',i)
# if i>=3:
#     print('«Ты победил»')
# else:
#     print(' «Ты проиграл»')
# ========/1================
#работает но на леое срабатывание любой цифры не обрабатывает
# # =======2============
# v_songs = {
#     'World in My Eyes': 4.86,
#     'Sweetest Perfection': 4.43,
#     'Personal Jesus': 4.56,
#     'Halo': 4.9,
#     'Waiting for the Night': 6.07,
#     'Enjoy the silence': 4.20 ,
#     'Policy of Truth': 4.76,
#     'Blue Dress': 4.29,
#     'clean': 5.83,
# }
# num= int(input('How many songs? '))
# choice=[]
# stime=0
# for i in range(num):
#     song=input('Song ')
#     choice.append(song)
#     if song in v_songs:
#         stime = stime + v_songs.get(song)

# print('Playlist:', choice, 'total songs time: ', "%d:%02d" % (int(stime), (stime*60) % 60), 'min')
# # ======/2==========

# for j  in choice:
#      if s in v_songs:
# # #     sum time
    
    
# # musics = [{},{},{}]
# musics = {'song1':5.01}
# number = input('how many?') 

# ========3=======
prod_id = {
    'Лампа':'1',
    'Стол':'2',
    'Диван':'5',
    'Стул':'6'
 }

store = {
    '1':[
        {'qua':27,'price':42}],
    '2':[
        {'qua':22,'price':510},
        {'qua':32,'price':520},],
    '5':[
        {'qua':2,'price':1200},
        {'qua':1,'price':1150}],
    '6':[
        {'qua':50,'price':100},
        {'qua':12,'price':95},
        {'qua':43,'price':97}]
}

for prod in prod_id.keys():
    prodid = prod_id.get(prod)
    prodname = prod
    # print(prodid)
    # print(prodname)
    qua=0
    price=0
    if prodid in store:
        ostatok=store.get(prodid)
        # print(store.get(prodid))
        for p in ostatok:           
            qua = qua + p['qua']
            price = price + p['price']*p['qua']
        # print(qua, price)
        print(prodname+' — '+str(qua)+' шт., стоимость — '+str(price)+' р.')

# ============/3======

# with 1 as key to list
x=56
y=x
ll = [dict(zip([1],[x]))]
stocks = ['reliance', 'infosys', 'tcs']
prices = [2175, 1127, 2750]

new_dict = {stocks: prices for stocks,
			prices in zip(stocks, prices)}
print(new_dict)

# display list
print(ll)