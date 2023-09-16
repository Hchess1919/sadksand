import random

o1=input("1 ögrenci adı yazın")
o2=input("1 ögrenci adı daha yazın")
o3=input("1 ögrenci adı daha yazın")
o4=input("1 ögrenci adı daha yazın")
o5=input("1 ögrenci daha yazın")


sinif=[o1,o2,o3,o4,o5]

print("kurada çıkan öğrenci:")
print(random.choice(sinif))