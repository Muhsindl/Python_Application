class Student:
    def __init__(self, name, midterm, final):
        # Öğrenci bilgilerini al
        self.name = name
        self.midterm = midterm
        self.final = final

    def calculate_average(self, midterm_weight=0.4, final_weight=0.6):
        # Ağırlıklı ortalamayı hesapla
        return (self.midterm * midterm_weight) + (self.final * final_weight)


class School:
    def __init__(self):
        self.students = []  # Öğrencileri tutacak liste

    def add_student(self, student):
        # Öğrenciyi listeye ekle
        self.students.append(student)

    def highest_grade(self, midterm_weight=0.4, final_weight=0.6):
        # İlk öğrenciyi varsayılan olarak en yüksek notlu kabul et
        top_student = self.students[0]

        # Tüm öğrenciler arasında en yüksek ortalamayı bul
        for student in self.students:
            avg = student.calculate_average(midterm_weight, final_weight)
            top_avg = top_student.calculate_average(midterm_weight, final_weight)
            if avg > top_avg:
                top_student = student

        return top_student


def main():
    school = School()  # Okul nesnesi oluştur

    # Kullanıcıdan öğrenci sayısını al
    num_students = int(input("Kaç öğrenci eklemek istersiniz? "))

    # Öğrencileri ekle
    for _ in range(num_students):
        name = input("Öğrencinin adını girin: ")
        midterm = float(input(f"{name} için vize notunu girin: "))
        final = float(input(f"{name} için final notunu girin: "))

        student = Student(name, midterm, final)  # Öğrenci nesnesi oluştur
        school.add_student(student)  # Öğrenciyi okula ekle

    # Kullanıcıdan yeni vize ve final oranları al
    midterm_weight = float(input("Vize notunun ağırlığını girin (varsayılan %40): ") or 0.4)
    final_weight = float(input("Final notunun ağırlığını girin (varsayılan %60): ") or 0.6)

    # Yeni oranlarla en yüksek notu bulan öğrenci
    top_student = school.highest_grade(midterm_weight, final_weight)
    print(f"Yeni ağırlıklarla en yüksek notu alan öğrenci: {top_student.name} ({top_student.calculate_average(midterm_weight, final_weight):.2f})")


# Programı çalıştır
if __name__ == "__main__":
    main()
