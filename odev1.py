#SORU 1

#String(str) = Tırnak içerisinde yazılan metinsel veri tipleridir.
a = "ArinSinal"

#Sayısal Veri Tipleri
#İnteger(int) = Tam sayıları belirten veri tipidir.
b = 5
#float = Ondalıklı sayıları belirten veri tipidir.
c = 6.5

#Boolean Veri Tipleri
#Bool = Bir ifadenin doğru veya yanlış olduğunu değerlendirir.
print(27<25) #ifadesinin çıktısı False olacağı gibi
print(50<75) # ifadesinin çıktısı True olacaktır.

#Sequence (Sıralama) Veri Tipleri
#list = Köşeli parantezle gösterilen liste tipidir. Yapısındsa değişiklik yapılabilir.
list1 = [1,2,3]
#Tuple(demet) = Parantezle veya virgülle gösterilen değiştirilemeyen veri tipleridir.
sınıf = ("ali","ayşe","fatma")
#Set(Küme) = List'e benzer fakat set içindeki elemanlar sıralanamaz ve indexlenemez.
fruits = {"banana", "grape", "cherry"}
print(fruits) #çıktısı karışık gelecektir.{'banana', 'grape', 'cherry'}
#Dictionary = Sıralanamaz ancak değiştirilebilir veri topluluğudur.
sozluk = {
  "uretici": "Renault",
  "model": "Clio",
  "yil": 2009
}

#SORU 2
# Üye isimleri, Ödev tanımı, açıklama ekranında yazılı olan metinler vb. = string
# Yorum adedi = int
# Bitirme oranı = float

#SORU 3
total_lessons = 4
completed_lessons = int(input("Enter the number of completed lessons: "))
if completed_lessons != 0:
    percent_complete = (completed_lessons/total_lessons)*100
    print(percent_complete)
else:
    print(0)