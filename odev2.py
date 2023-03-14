# odev2
Bir öğrenci kayıt sistemi yazdığımızı düşünelim. Sistemimizdeki öğrencileri bir listede sadece ad soyad olacak şekilde tutalım.

Bu öğrenci kayıt sistemine;

Aldığı isim soy isim ile listeye öğrenci ekleyen;
ogrenci_liste=["beyza caştur","emine caştur","ali caştur","muttalip caştur"]
ogrenci_liste.append("beyza caştur")
print(ogrenci_liste)
*****************************************************
Aldığı isim soy isim ile eşleşen değeri listeden kaldıran;
ogrenci_liste.remove("beyza caştur")
print(ogrenci_liste)
*****************************************************
Listeye birden fazla öğrenci eklemeyi mümkün kılan;
ogrenci_liste.extend(["huriye caştur","veli caştur"])
print(ogrenci_liste)
*****************************************************
Listedeki tüm öğrencileri tek tek ekrana yazdıran;
for i in ogrenci_list:
       print(i)
****************************************************************          
Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan;
i=0
while i< len (ogrenci_list):
        print( str(i) + ogrenci_list[i] + nosu)
        i+=1
******************************************************************
Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız);
silinecek_ogrenci=int(input("silinecek öğrenci sayısını giriniz: ")) 

a=0
while a< silinecek_ogrenci :
    i=str(input("öğrencinin adını giriniz: "))
    ogrenci_list.remove(i)
    a+=1
print(ogrenci_list)

fonksiyonları geliştiriniz ve her bir fonksiyonu en az bir kere çağırarak konsolda test ediniz.

Ödevde kullanacağınız döngülerin bir tanesi for bir tanesi while döngüsü olması istenmektedir.

****************************************************************************************************


