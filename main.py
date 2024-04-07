import wikipedia
wikipedia.set_lang("uz")


while True:
   
    
    def wiki(text):
        try:
            print(wikipedia.summary(text))
        except:
            print("Kechirasiz, malumot topilmadi! ")

    soz = input("Qidirish uchun so'z kiriting: ")
    wiki(soz)



       



















# import wikipedia
# matn = wikipedia.summary("Uzbekistan")
# print(matn)