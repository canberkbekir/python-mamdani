import pandas as pd
from io import StringIO

"""
•	Frekans, Hertz cinsinden
•	Saldiri açisi, derece cinsinden
•	Metre cinsinden akor uzunluğu
•	Serbest akiş hizi, metre/saniye cinsinden.
•	Yer değiştirme kalinliği, metre cinsinden.
Sonuç özelliği:
•	Desibel cinsinden ölçeklendirilmiş ses basinci seviyesi. (kisaltmasi, SBS)

"""

dataFile = open("doc/data.dat")
data = pd.read_table(dataFile)
#Yukarı dosyamızdan veriyi okuyoruz aşağıda ise bu okduğumuz veriyi list'e çeviriyoruz.
dataList = data.values.tolist()
"""
•	Listedeki herhangi bir veriyi çekmek için ilk alan yani "i" kismi hangi row olduğu ikinci kısım ise hangi kolon olduğu

for i in range(0, len(dataList)):

     print(dataList[i][2])
"""
