# Düğüm oluşturduk
grafik = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}
ziyaret = []
yıgın = []

# Beast First Searching fonksiyonu (Enine Arama)

def bfs(grafik, ziyaret, dugum):
    ziyaret.append(dugum)
    yıgın.append(dugum)

    while yıgın:
        s = yıgın.pop(0)
        print(s, end=" ")

        for komsu in grafik[s]:
            if komsu not in ziyaret:
                yıgın.append(komsu)

bfs(grafik, ziyaret, "A")