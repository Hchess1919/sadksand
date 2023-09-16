import random



tutulan=random.randint(1,100)
print("1-100 arası bir sayı tuttum 5 hakkın var")



for hak in range (5):
    tahmin=int(input("tahminin ne"))
    if tahmin== tutulan:
        print("bildin")
        break
    elif tahmin<tutulan: 
        print("yukarıda")
    elif tahmin>tutulan: print ("aşağıda")


print(':( uzuldum ama 5 hakinda bitti :(')
print('💔💔💔💔💔')
print('cevap', tutulan)
exit()  