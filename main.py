import json
from datetime import datetime
import os

NOTES_FILE = "notes.json"

def load_notes():
    # Загрузка заметок из файла
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as file:
            try:
                notes = json.load(file)
            except json.JSONDecodeError:
                notes = []
    else:
        notes = []
    return notes

def save_notes(notes):
    #Сохранение заметок 
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=2)

def add_note(title, msg):
    # Добавление новой заметки
    notes = load_notes()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        "id": len(notes) + 1,
        "title": title,
        "message": msg,
        "timestamp": timestamp
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно сохранена.")

def edit_note(note_id, new_title, new_msg):
#    Редактирование заметки по идентификатору.
    notes = load_notes()
    for note in notes:
        if note['id'] == note_id:
            note['title'] = new_title
            note['message'] = new_msg
            note['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print(f"Заметка с идентификатором {note_id} отредактирована.")
            return
    print(f"Заметка с идентификатором {note_id} не найдена.")


def list_notes():
    # Вывод списка заметок
    notes = load_notes()
    if notes:
        print("Список заметок:")
        for note in notes:
            print(f"{note['id']}. {note['title']} ({note['timestamp']})")
            print(note['message'])
            print("-" * 30)
    else:
        print("Список заметок пуст.")

def delete_note(note_id):
    # Удаление заметки по идентификатору
    notes = load_notes()
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print(f"Заметка с идентификатором {note_id} удалена.")
            return
    print(f"Заметка с идентификатором {note_id} не найдена.")

def main():
    while True:
        print("\nВыберите действие:")
        print("1. Просмотреть заметки")
        print("2. Добавить заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("0. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            list_notes()
        elif choice == "2":
            title = input("Введите заголовок заметки: ")
            msg = input("Введите тело заметки: ")
            add_note(title, msg)
        elif choice == "3":
            try:
                note_id = int(input("Введите идентификатор заметки для редактирования: "))
                new_title = input("Введите новый заголовок заметки: ")
                new_msg = input("Введите новое тело заметки: ")
                edit_note(note_id, new_title, new_msg)
            except ValueError:
                print("Ошибка: Введите корректный идентификатор (целое число).")
        elif choice == "4":
            try:
                note_id = int(input("Введите идентификатор заметки для удаления: "))
                delete_note(note_id)
            except ValueError:
                print("Ошибка: Введите корректный идентификатор (целое число).")
        elif choice == "0":
            break
        else:
            print("Неверный ввод. Пожалуйста, введите корректный номер действия.")

if __name__ == "__main__":
    main()