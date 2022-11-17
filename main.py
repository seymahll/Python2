print("Merhaba Etiya")
# string : metinler  "" kullanılır
text = 'hilal'
print(text)
# integer : tam sayı "" kullanılmaz
number = 5
print(number)
# float : ondalıklı sayı 
dnumber = 5.3
print(dnumber)
# boolean : True , False
# matematiksel operatörler
print(number + 5)
print(number - 5)
print(number * 5)
print(number / 5)
print(number % 5) #mod bölümde kalanı verir
# mantıksal operatörler
print(1==2)
print(1!=2)
print(1>2)
print(1<2)
print(1<=2)
print(1>=2)
print(10%2==0)
print(50/2==25)
print(50/2==25.0)
# string fonksiyonları
text = 'Merhaba Etiya'
print(text.upper()) # Metni byk yazdır
print(text.lower()) # Metni kçk yazdır
print(text.startswith("Met")) # Cümle başı ... ile başlıyor mu?
print(text.endswith("Etiya")) # Cümle sonu ... ile bitiyor mu?
# f string
name = 'Hilal'
age = 27
company = 'Etiya'
print(f"{name} {age} yasinda ve {company}'da calisiyor")
name = 'Hilal'
age = "27"
company = 'Etiya' 
print(name + age + company) 