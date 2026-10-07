import pytest

from app import read_grades, arithmetic_mean, average_for_student, letter_grade


STUDENTS = read_grades()


def test_csv_has_students():
    assert len(STUDENTS) >= 1


def test_csv_headers():
    assert "Test1" in STUDENTS[0]
    assert "Final" in STUDENTS[0]
    assert "Last name" in STUDENTS[0]


def test_csv_no_bom_in_first_header():
    first_key = next(iter(STUDENTS[0]))
    assert not first_key.startswith("\ufeff"), f"BOM в заголовке: {first_key!r}"


def test_csv_known_students_present():
    names = {(s["Last name"], s["First name"]) for s in STUDENTS}
    assert ("Alfalfa", "Aloysius") in names
    assert ("Heffalump", "Harvey") in names


def test_csv_values_are_numeric():
    for s in STUDENTS:
        for key in ("Test1", "Test2", "Test3", "Test4", "Final"):
            float(s[key])


@pytest.mark.parametrize(
    "student",
    STUDENTS,
    ids=[f"{s['Last name']}_{s['First name']}" for s in STUDENTS],
)
def test_average_in_valid_range(student):
    avg = average_for_student(student)
    tests = [float(student[f"Test{i}"]) for i in range(1, 5)]
    assert min(tests) <= avg <= max(tests)


def test_arithmetic_mean_basic():
    assert arithmetic_mean(1, 2, 3, 4) == 2.5


def test_arithmetic_mean_floats():
    assert arithmetic_mean(40.0, 90.0, 100.0, 83.0) == pytest.approx(78.25)


def test_arithmetic_mean_negative():
    assert arithmetic_mean(-1, 1, 1, 1) == pytest.approx(0.5)


@pytest.mark.parametrize(
    "avg, expected",
    [
        (95.0, "A"),
        (90.0, "A"),
        (89.99, "B"),
        (80.0, "B"),
        (79.99, "C"),
        (70.0, "C"),
        (69.99, "D"),
        (60.0, "D"),
        (59.99, "F"),
        (0.0, "F"),
    ],
)
def test_letter_grade(avg, expected):
    assert letter_grade(avg) == expected