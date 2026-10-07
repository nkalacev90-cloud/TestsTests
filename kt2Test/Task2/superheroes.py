import json


def load_data(file_path):
    with open(file_path, encoding="utf-8") as f:
        return json.load(f)


def save_data(data, file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def add_members(data, new_members):
    """Добавляет новых супергероев в data['members']."""
    data["members"].extend(new_members)
    return data


def sort_members_by_age(data):
    """Сортирует members по возрасту (по возрастанию)."""
    data["members"] = sorted(data["members"], key=lambda m: m["age"])
    return data


def main():
    # 1. Загрузка
    data = load_data("superheroes.json")
    print("=== Исходные супергерои ===")
    for m in data["members"]:
        print(f"{m['name']} ({m['age']})")

    # 2. Добавляем 3 новых супергероя (2+)
    new_members = [
        {
            "name": "Spider-Man",
            "age": 17,
            "secretIdentity": "Peter Parker",
            "powers": ["Web-slinging", "Spider-sense", "Super strength"],
        },
        {
            "name": "Iron Man",
            "age": 48,
            "secretIdentity": "Tony Stark",
            "powers": ["Powered armor", "Flight", "Genius intellect"],
        },
        {
            "name": "Thor",
            "age": 1500,
            "secretIdentity": "Thor Odinson",
            "powers": ["Thunder", "Super strength", "Immortality"],
        },
    ]
    data = add_members(data, new_members)

    # 3. Сортировка по возрасту
    data = sort_members_by_age(data)

    # 4. Сохранение в новый файл
    save_data(data, "superhero_new.json")

    print("\n=== Отсортированные по возрасту ===")
    for m in data["members"]:
        print(f"{m['name']:20} — {m['age']:>8}")


if __name__ == "__main__":
    main()