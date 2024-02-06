import numpy as np
derece=int(input("Derece (Açı) giriniz: "))
radyan=float((derece*np.pi)/180)
gradyan=float((derece*200)/180)
print(derece,"derecesi = ",radyan,"radyandır.")
print("-"*25)
print(derece,"derecesi = ",gradyan,"gradyandır.")