import time
import random

global lista_zadan
lista_zadan = []

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
            list_of_event(zadanie)
        elif(opcja == "2"):
            print("Dodaj zadanie")
            event_add()
        elif(opcja == "3"):
            print("Usuń zadanie")
        elif(opcja == "4"):
            Loop = False
            main_menu()
        else:
            print("Brak takiej opcji")

def event_add():
    global zadanie
    event_id = random.randrange(1,1000,1)
    title_event = input("Tytuł: ")
    time_update = input(time.strftime('%Y%m%d_%H:%M:%S'))
    data_event = input("Data zdarzenia w formacie YYYYMMDD: ")
    timeup_event = input("Godzina rozpoczęcia w formacie HHMM: ")
    timeto_event = input("Godzina zakończenia w formacie HHMM: ")
    timereminder_event = input("Przypomnienie w formacie YYYYMMDDHHMM: ")
    describe_event = input("Opis wydarzenia: ")
    zadanie = {'id':event_id,'dodano':time_update,'tytuł':title_event,'data zadania':data_event,'czas rozpoczęcia':timeup_event,'czas zakończenia':timeto_event,'przypomnienie':timereminder_event,'opis':describe_event}
    lista_zadan.append(zadanie)
    return zadanie



def profile_config(key_profile_contact,key_profile_file):
    global profil
    profile_contact = input("Podaj adres e-mail: ")
    profile_file = input("Podaj nazwę pliku: ")
    profil = {'key_profile_contact':profile_contact, 'key_profile_file':profile_file}
    profil['key_profile_contact'] = profile_contact
    profil['key_profile_file'] = profile_file
    return profil

def list_of_event(zadanie):
    print(zadanie)
    print(lista_zadan)
    #for k,v in zadanie.items():
    #    print(k + '     ' + str(v))
    for i in lista_zadan:
        for k,v in zadanie.items():
            print(k + '     ' + str(v))





main_menu()