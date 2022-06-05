
"""
    Функция реализует фильтрацию словаря значений при помощи замыкания/
    В это смысле замыкание может быть применено вместо объявления класса и создания объектов класса
    Вывод: {'Alice': 98, 'Chris': 85}
            {'David': 75}
            {'Bob': 67, 'Ella': 54, 'Grace': 69}
            {'Fiona': 35}
"""
students = {
    'Alice': 98,
    'Bob': 67,
    'Chris': 85,
    'David': 75,
    'Ella': 54,
    'Fiona': 35,
    'Grace': 69
}

def make_students_classifier(lower_bound, upper_bound):
    def classify_student(exam_dict):
        return {k:v for (k,v) in exam_dict.items() if lower_bound <= v < upper_bound}
    return classify_student

gradeA = make_students_classifier(80, 100)
gradeB = make_students_classifier(70, 80)
gradeC = make_students_classifier(50, 70)
gradeD = make_students_classifier(0, 50)

print(gradeA(students))
print(gradeB(students))
print(gradeC(students))
print(gradeD(students))
