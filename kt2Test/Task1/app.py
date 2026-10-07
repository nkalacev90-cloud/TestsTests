import csv


def read_grades(file_path="grades.csv"):
    """Читает CSV с оценками. Возвращает список словарей (по студенту)."""
    with open(file_path, mode="r", newline="", encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        reader.fieldnames = [
            name.lstrip("\ufeff").strip().strip('"').strip("'")
            for name in reader.fieldnames
        ]
        rows = []
        for row in reader:
            rows.append({
                k: (v.strip().strip('"').strip("'") if isinstance(v, str) else v)
                for k, v in row.items()
            })
    return rows


def arithmetic_mean(a, b, c, d):
    """Среднее арифметическое четырёх чисел."""
    return (float(a) + float(b) + float(c) + float(d)) / 4


def average_for_student(student):
    """Среднее по Test1..Test4 для одного студента."""
    return arithmetic_mean(
        student["Test1"],
        student["Test2"],
        student["Test3"],
        student["Test4"],
    )


def letter_grade(avg):
    """Буквенная оценка по среднему баллу."""
    if avg >= 90:
        return "A"
    if avg >= 80:
        return "B"
    if avg >= 70:
        return "C"
    if avg >= 60:
        return "D"
    return "F"


if __name__ == "__main__":
    rows = read_grades()
    print(f"{'Last name':12} {'First name':12} {'avg':>6}  {'Final':>6}  {'Grade':>5}")
    print("-" * 50)
    for student in rows:
        avg = average_for_student(student)
        final = float(student["Final"])
        print(
            f"{student['Last name']:12} {student['First name']:12} "
            f"{avg:6.2f}  {final:6.2f}  {letter_grade(avg):>5}"
        )