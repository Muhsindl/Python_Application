import matplotlib.pyplot as plt
# Ağaç çizimi
x=[8,42,33,38,31,36,29,34,25,16,21,14,19,12,17,8]
y=[7,7,20,20,30,30,40,40,50,40,40,30,30,20,20,7]
# Kök çizimi
x1=[20,20,30,30]
y1=[7,-7,-7,7]
# Süsleme çizimi
x2=[15,35,25,30,20,25,25,20,30,20,30]
y2=[15,15,20,25,25,30,45,10,10,35,35]

plt.plot(x,y,color="#08403E")
plt.plot(x1,y1,color="#520120")
plt.scatter(x2, y2,marker="*",color="#962B09",alpha=0.6)

plt.title("Yılbaşı Ağacı")
plt.show()