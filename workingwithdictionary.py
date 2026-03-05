# talaba_0 = {
#     'ism':'alijon',
#     'familiya':'shamshiyev',
#     'yosh':22,
#     'fakultet':'matematika',
#     'kurs':4
#     }

# print(talaba_0.items())

# for kalit, qiymat in talaba_0.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat} \n") 



# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310',
#     'hamida':'galaxy s9',
#     'maryam':'huawei p30',
#     'tohir':'iphone x',
#     'umar':'iphone x'    
#     }
# for kalit, qiymat in telefonlar.items():
#     print(f"Ism: {kalit.title()}")
#     print(f"telefon: {qiymat} \n") 


# telefonlar.keys()


# 1-Task
# python_words = {
#     'integer':'Butun son',
#     'float': "O'nlik son",
#     'boolean':"Mantiqiy qiymat",
#     'for':"Biror amalni qayta-qayta bajarish tsikli",
#     'if':'Shartlarni tekshirish operatori'
#     }





# for key in sorted(python_words.keys()):
#     print(key)


# for value in sorted(python_words.values()):
#     print(value)






# 2-Task

# davlatlar = {
#     "o'zbekiston":'toshkent',
#     'aqsh':'washington d.c.',
#     'rossiya':'moskva',
#     'tojikiston':'dushanbe',
#     "qirg'iziston":'bishkek',
#     'qozog\'iston':'nursulton',
#     'malayziya':'kuala-lumpur',
#     'singapur':'sungapur',
#     'italiya':'rim'}

# country = str(input("davlatni nomini kiriting: "))

# for name in davlatlar.keys():
#     if name==country:
#         print(f"Siz kiritgan davlarni poytaxti {davlatlar[name]}")
#     else:
#         print("Bizda bunday ma'lumot yo'q")


# country = input('Qaysi davlatning poytaxtini bilishni istaysiz?:').lower()
# capital = davlatlar.get(country)
# if capital==None:
#     print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')    
# else:
#     print(f"{country.upper()}ning poytaxti {capital.title()} shahri")






# 3-Task
menu = {
        'osh':20000,
        "lag'mon":22000,
        'non':4000,
        'choy':5000,
        'shashlik':12000,
        'somsa':6000,
        'tabaka':15000
        }




print('3 ta taom buyurtma bering.')
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom:").lower())

for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q.")






