# Graf (Ağaç) oluşturuldu
grafik={
        "A":["B","C"],
        "B":["D","E"],
        "C":["F"],
        "D":[],
        "E":[],
        "F":[]     
        }
ziyaret=set()
# Depth First Searching fonksiyonu (Derinine Arama Yöntemi)
def dfs(grafik,ziyaret,dugum):
    if dugum not in ziyaret:
        print(dugum)
        ziyaret.add(dugum)
        for komsu in grafik[dugum]:
            dfs(grafik,ziyaret,komsu)

dfs(grafik,ziyaret,"A")