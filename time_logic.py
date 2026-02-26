toplamsaniye=int (input("enter a large integer\n "))

saat=toplamsaniye//3600
dakika=(toplamsaniye%3600)//60
saniye=toplamsaniye %60

print(str(toplamsaniye)+" second is "+str(saat)+" hours "+str(dakika)+" minutes , and "+str(saniye)+" seconds .")