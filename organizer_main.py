def main_menu():
    Loop = True

    print("Organizer")
    print("1. Lista zadań")
    print("2. Konfiguruj profil")
    print("3. Zamknij")

    while Loop:
        opcja = input("Wybierz opcję: ")
        if(opcja == "1"):
            print("Lista zadań")
            event_list_menu()
        elif(opcja == "2"):
            print("Konfiguruj profil")
        elif(opcja == "3"):
            Loop = False
            exit()
        else:
            print("Brak takiej opcji")

def event_list_menu():
    print("Lista zadań")
    print("1. Wyświetl zadania")
    print("2. Dodaj zadanie")
    print("3. Usuń zadanie")
    print("4. Menu główne")

    Loop = True

    while Loop:
        opcja = input("Wybierz opcję: ")
        if(opcja == "1"):
            print("Zadania bieżące")
        elif(opcja == "2"):
            print("Dodaj zadanie")
        elif(opcja == "3"):
            print("Usuń zadanie")
        elif(opcja == "4"):
            main_menu()
        else:
            print("Brak takiej opcji")


main_menu()