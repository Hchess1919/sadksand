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
    if tahmin <1 or tahmin> 100: print("1 ila 100 arasında dedim")


print(':( uzuldum ama 5 hakinda bitti :(')
print('💔💔💔💔💔')
print('cevap', tutulan)
exit()