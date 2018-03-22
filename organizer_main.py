import time
zadanie = {}


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
            profile_config('key_profile_contact','key_profile_file')
            print(profil)
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
            Loop = False
            main_menu()
        else:
            print("Brak takiej opcji")

def event_add():
    title_event = input("Tytuł: ")
    time_update = input(time.strftime('%Y%m%d_%H:%M:%S'))
    data_event = input("Data zdarzenia w formacie YYYYMMDD: ")
    timeup_event = input("Godzina rozpoczęcia w formacie HHMM: ")
    timeto_event = input("Godzina zakończenia w formacie HHMM: ")
    timereminder_event = input("Przypomnienie w formacie YYYYMMDDHHMM: ")
    describe_event = input("Opis wydarzenia: ")

def profile_config(key_profile_contact,key_profile_file):
    global profil
    profile_contact = input("Podaj adres e-mail: ")
    profile_file = input("Podaj nazwę pliku: ")
    profil = {'key_profile_contact':profile_contact, 'key_profile_file':profile_file}
    profil['key_profile_contact'] = profile_contact
    profil['key_profile_file'] = profile_file
    return profil

main_menu()