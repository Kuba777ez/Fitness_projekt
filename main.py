from tkinter import *
from tkinter import ttk
import tkintermapview
import requests
from bs4 import BeautifulSoup

# Club
clubs: list = []


class Club:
    def __init__(self, name, location, map_widget):
        self.name = name
        self.location = location
        self.coordinates = self.get_coordinates()
        self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1],
                                            text=f'{self.name}')


    def get_coordinates(self) -> list:
        adres_url: str = f'https://pl.wikipedia.org/wiki/{self.location}'
        response_html = BeautifulSoup(requests.get(adres_url).text, 'html.parser')
        return [
            float(response_html.select('.latitude')[1].text.replace(',', '.')),
            float(response_html.select('.longitude')[1].text.replace(',', '.')),
        ]


def add_club() -> None:
    name = entry_nazwa_club.get()
    location = entry_miejscowosc_club.get()

    club = Club(name=name, location=location, map_widget=map_widget_club)

    clubs.append(club)
    print(clubs)

    entry_nazwa_club.delete(0, END)
    entry_miejscowosc_club.delete(0, END)

    entry_nazwa_club.focus()
    update_club_comboboxes()
    show_clubs()




def show_clubs():
    listbox_lista_obiektow_club.delete(0, END)
    for idx, club in enumerate(clubs):
        listbox_lista_obiektow_club.insert(idx, f'{idx + 1}. {club.name}')


def remove_club():
    i = listbox_lista_obiektow_club.index(ACTIVE)
    print(i)
    clubs[i].marker.delete()
    clubs.pop(i)
    show_clubs()


def edit_club():
    i = listbox_lista_obiektow_club.index(ACTIVE)
    name = clubs[i].name
    location = clubs[i].location

    entry_nazwa_club.insert(0, name)
    entry_miejscowosc_club.insert(0, location)

    buttom_dodaj_obiekt_club.config(text='Zapisz', command=lambda: update_club(i))


def update_club(i):
    name = entry_nazwa_club.get()
    location = entry_miejscowosc_club.get()

    clubs[i].name = name
    clubs[i].location = location

    clubs[i].coordinates = clubs[i].get_coordinates()
    clubs[i].marker.delete()
    clubs[i].marker = map_widget.set_marker(clubs[i].coordinates[0], clubs[i].coordinates[1],
                                            text=f'{clubs[i].name} {clubs[i].surname}')

    show_clubs()
    buttom_dodaj_obiekt_club.config(text='Dodaj', command=add_club)

    entry_nazwa_club.delete(0, END)
    entry_miejscowosc_club.delete(0, END)

    entry_nazwa_club.focus()


def show_club_details():
    i = listbox_lista_obiektow_club.index(ACTIVE)
    map_widget.set_zoom(15)
    map_widget.set_position(clubs[i].coordinates[0], clubs[i].coordinates[1])

def get_location_by_club_name(club_name: str) -> str:
    for club in clubs:
        if club.name == club_name:
            return club.location
    return None  # jeśli nie znaleziono


# employee
employees: list = []


class Employee:
    def __init__(self, name, surname, location, map_widget):
        self.name = name
        self.surname = surname
        self.location = location
        self.coordinates = self.get_coordinates()
        self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1],
                                            text=f'{self.name} {self.surname}')

    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        adres_url: str = f'https://pl.wikipedia.org/wiki/{self.location}'
        response_html = BeautifulSoup(requests.get(adres_url).text, 'html.parser')
        return [
            float(response_html.select('.latitude')[1].text.replace(',', '.')),
            float(response_html.select('.longitude')[1].text.replace(',', '.')),
        ]


def add_employee() -> None:
    name = entry_imie_employee.get()
    surname = entry_nazwisko_employee.get()
    selected_club = club_combobox_employee.get()
    location = get_location_by_club_name(selected_club)

    if not location:
        print("Nie wybrano klubu lub klub nie istnieje.")
        return

    employee = Employee(name=name, surname=surname, location=location, map_widget=map_widget_employee)

    employees.append(employee)
    print(employees)

    entry_imie_employee.delete(0, END)
    entry_nazwisko_employee.delete(0, END)
    club_combobox_employee.set("")

    entry_imie_employee.focus()
    show_employees()



def show_employees():
    listbox_lista_obiektow_employee.delete(0, END)
    for idx, employee in enumerate(employees):
        listbox_lista_obiektow_employee.insert(idx, f'{idx + 1}. {employee.name} {employee.surname}')


def remove_employee():
    i = listbox_lista_obiektow_employee.index(ACTIVE)
    print(i)
    employees[i].marker.delete()
    employees.pop(i)
    show_employees()


def edit_employee():
    i = listbox_lista_obiektow_employee.index(ACTIVE)
    name = employees[i].name
    surname = employees[i].surname
    location = employees[i].location

    entry_imie_employee.insert(0, name)
    entry_nazwisko_employee.insert(0, surname)
    entry_miejscowosc_employee.insert(0, location)

    buttom_dodaj_obiekt_employee.config(text='Zapisz', command=lambda: update_employee(i))


def update_employee(i):
    name = entry_imie_employee.get()
    surname = entry_nazwisko_employee.get()
    location = entry_miejscowosc_employee.get()

    employees[i].name = name
    employees[i].surname = surname
    employees[i].location = location

    employees[i].coordinates = employees[i].get_coordinates()
    employees[i].marker.delete()
    employees[i].marker = map_widget.set_marker(employees[i].coordinates[0], employees[i].coordinates[1],
                                                text=f'{employees[i].name} {employees[i].surname}')

    show_employees()
    buttom_dodaj_obiekt_employee.config(text='Dodaj', command=add_employee)

    entry_imie_employee.delete(0, END)
    entry_nazwisko_employee.delete(0, END)
    entry_miejscowosc_employee.delete(0, END)

    entry_imie_employee.focus()


def show_employee_details():
    i = listbox_lista_obiektow_employee.index(ACTIVE)
    map_widget.set_zoom(15)
    map_widget.set_position(employees[i].coordinates[0], employees[i].coordinates[1])


# user
users: list = []


class User:
    def __init__(self, name, surname, location, map_widget):
        self.name = name
        self.surname = surname
        self.location = location
        self.coordinates = self.get_coordinates()
        self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1],
                                            text=f'{self.name} {self.surname}')


    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        adres_url: str = f'https://pl.wikipedia.org/wiki/{self.location}'
        response_html = BeautifulSoup(requests.get(adres_url).text, 'html.parser')
        return [
            float(response_html.select('.latitude')[1].text.replace(',', '.')),
            float(response_html.select('.longitude')[1].text.replace(',', '.')),
        ]


def add_user() -> None:
    name = entry_imie_user.get()
    surname = entry_nazwisko_user.get()
    selected_club = club_combobox_user.get()
    location = get_location_by_club_name(selected_club)

    if not location:
        print("Nie wybrano klubu lub klub nie istnieje.")
        return

    user = User(name=name, surname=surname, location=location, map_widget=map_widget_user)

    users.append(user)
    print(users)

    entry_imie_user.delete(0, END)
    entry_nazwisko_user.delete(0, END)
    club_combobox_user.set("")

    entry_imie_user.focus()
    show_users()



def show_users():
    listbox_lista_obiektow_user.delete(0, END)
    for idx, user in enumerate(users):
        listbox_lista_obiektow_user.insert(idx, f'{idx + 1}. {user.name} {user.surname}')


def remove_user():
    i = listbox_lista_obiektow_user.index(ACTIVE)
    print(i)
    users[i].marker.delete()
    users.pop(i)
    show_users()


def edit_user():
    i = listbox_lista_obiektow_user.index(ACTIVE)
    name = users[i].name
    surname = users[i].surname
    location = users[i].location

    entry_imie_user.insert(0, name)
    entry_nazwisko_user.insert(0, surname)
    entry_miejscowosc_user.insert(0, location)

    buttom_dodaj_obiekt_user.config(text='Zapisz', command=lambda: update_user(i))


def update_user(i):
    name = entry_imie_user.get()
    surname = entry_nazwisko_user.get()
    location = entry_miejscowosc_user.get()

    users[i].name = name
    users[i].surname = surname
    users[i].location = location

    users[i].coordinates = users[i].get_coordinates()
    users[i].marker.delete()
    users[i].marker = map_widget.set_marker(users[i].coordinates[0], users[i].coordinates[1],
                                            text=f'{users[i].name} {users[i].surname}')

    show_users()
    buttom_dodaj_obiekt_user.config(text='Dodaj', command=add_user)

    entry_imie_user.delete(0, END)
    entry_nazwisko_user.delete(0, END)
    entry_miejscowosc_user.delete(0, END)

    entry_imie_user.focus()


def show_user_details():
    i = listbox_lista_obiektow_user.index(ACTIVE)
    map_widget.set_zoom(15)
    map_widget.set_position(users[i].coordinates[0], users[i].coordinates[1])


# Główne okno
root = Tk()
root.geometry("1200x700")
root.title('Kluby Fitness')

# tworzenie zakładek
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# tworzenie ramek dla zakładek
frame_club = Frame(notebook)
frame_user = Frame(notebook)
frame_employee = Frame(notebook)

# dodawanie ramek do zakładek
notebook.add(frame_club, text='Kluby')
notebook.add(frame_user, text='Użytkownicy')
notebook.add(frame_employee, text='Pracownicy')

# ramka_mapa_club
f_map_club = Frame(frame_club)
f_map_club.grid(row=0, column=0, columnspan=2)

# CLUB map
map_widget_club = tkintermapview.TkinterMapView(f_map_club, width=1200, height=400, corner_radius=0)
map_widget_club.grid(row=0, column=0, columnspan=2)
map_widget_club.set_position(52.23, 21.00)
map_widget_club.set_zoom(6)

# ramka_mapa_user
f_map_user = Frame(frame_user)
f_map_user.grid(row=0, column=0, columnspan=2)

# USER map
map_widget_user = tkintermapview.TkinterMapView(f_map_user, width=1200, height=400, corner_radius=0)
map_widget_user.grid(row=0, column=0, columnspan=2)
map_widget_user.set_position(52.23, 21.00)
map_widget_user.set_zoom(6)

# ramka_mapa_employee
f_map_employee = Frame(frame_employee)
f_map_employee.grid(row=0, column=0, columnspan=2)

# EMPLOYEE map
map_widget_employee = tkintermapview.TkinterMapView(f_map_employee, width=1200, height=400, corner_radius=0)
map_widget_employee.grid(row=6, column=0, columnspan=2)
map_widget_employee.set_position(52.23, 21.00)
map_widget_employee.set_zoom(6)


# ramka_lista_obiektow_club
f_list_club = Frame(frame_club)
f_list_club.grid(row=1, column=0)

label_lista_obiektow_club = Label(f_list_club, text='Lista klubów:')
label_lista_obiektow_club.grid(row=1, column=0)

listbox_lista_obiektow_club = Listbox(f_list_club, width=50, height=10)
listbox_lista_obiektow_club.grid(row=2, column=0, columnspan=3)

button_pokaz_szczegoly_club = Button(f_list_club, text='Pokaż szczegóły', command=show_club_details)
button_pokaz_szczegoly_club.grid(row=3, column=0)
button_usun_obiekt_club = Button(f_list_club, text='Usuń', command=remove_club)
button_usun_obiekt_club.grid(row=3, column=1)
button_edytuj_obiekt_club = Button(f_list_club, text='Edytuj', command=edit_club)
button_edytuj_obiekt_club.grid(row=3, column=2)

# ramka_formularz_club
f_form_club = Frame(frame_club)
f_form_club.grid(row=1, column=1, padx=10, pady=10)

label_formularz_club = Label(f_form_club, text='Formularz:')
label_formularz_club.grid(row=0, column=0)

label_nazwa_club = Label(f_form_club, text='Nazwa klubu:')
label_nazwa_club.grid(row=1, column=0, sticky=W)

label_miejscowosc_club = Label(f_form_club, text='Miejscowość:')
label_miejscowosc_club.grid(row=3, column=0, sticky=W)

entry_nazwa_club = Entry(f_form_club)
entry_nazwa_club.grid(row=1, column=1)

entry_miejscowosc_club = Entry(f_form_club)
entry_miejscowosc_club.grid(row=3, column=1)

buttom_dodaj_obiekt_club = Button(f_form_club, text='Dodaj', command=add_club)
buttom_dodaj_obiekt_club.grid(row=5, column=0, columnspan=2)

# ramka_lista_obiektow_employee
f_list_employee = Frame(frame_employee)
f_list_employee.grid(row=1, column=0)

label_lista_obiektow_employee = Label(f_list_employee, text='Lista pracowników:')
label_lista_obiektow_employee.grid(row=1, column=0)

listbox_lista_obiektow_employee = Listbox(f_list_employee, width=50, height=10)
listbox_lista_obiektow_employee.grid(row=2, column=0, columnspan=3)

button_pokaz_szczegoly_employee = Button(f_list_employee, text='Pokaż szczegóły', command=show_employee_details)
button_pokaz_szczegoly_employee.grid(row=3, column=0)
button_usun_obiekt_employee = Button(f_list_employee, text='Usuń', command=remove_employee)
button_usun_obiekt_employee.grid(row=3, column=1)
button_edytuj_obiekt_employee = Button(f_list_employee, text='Edytuj', command=edit_employee)
button_edytuj_obiekt_employee.grid(row=3, column=2)

# ramka_formularz_employee
f_form_employee = Frame(frame_employee)
f_form_employee.grid(row=1, column=1, padx=10, pady=10)

label_formularz_employee = Label(f_form_employee, text='Formularz:')
label_formularz_employee.grid(row=0, column=0)

label_imie_employee = Label(f_form_employee, text='Imie:')
label_imie_employee.grid(row=1, column=0, sticky=W)

label_nazwisko_employee = Label(f_form_employee, text='Nazwisko:')
label_nazwisko_employee.grid(row=2, column=0, sticky=W)

label_miejscowosc_employee = Label(f_form_employee, text='Miejscowość:')


entry_imie_employee = Entry(f_form_employee)
entry_imie_employee.grid(row=1, column=1)

entry_nazwisko_employee = Entry(f_form_employee)
entry_nazwisko_employee.grid(row=2, column=1)

entry_miejscowosc_employee = Entry(f_form_employee)


buttom_dodaj_obiekt_employee = Button(f_form_employee, text='Dodaj', command=add_employee)
buttom_dodaj_obiekt_employee.grid(row=5, column=0, columnspan=2)

# ramka_lista_obiektow_user
f_list_user = Frame(frame_user)
f_list_user.grid(row=1, column=0)

label_lista_obiektow_user = Label(f_list_user, text='Lista użytkowników:')
label_lista_obiektow_user.grid(row=1, column=0)

listbox_lista_obiektow_user = Listbox(f_list_user, width=50, height=10)
listbox_lista_obiektow_user.grid(row=2, column=0, columnspan=3)

button_pokaz_szczegoly_user = Button(f_list_user, text='Pokaż szczegóły', command=show_user_details)
button_pokaz_szczegoly_user.grid(row=3, column=0)
button_usun_obiekt_user = Button(f_list_user, text='Usuń', command=remove_user)
button_usun_obiekt_user.grid(row=3, column=1)
button_edytuj_obiekt_user = Button(f_list_user, text='Edytuj', command=edit_user)
button_edytuj_obiekt_user.grid(row=3, column=2)

# ramka_formularz_user
f_form_user = Frame(frame_user)
f_form_user.grid(row=1, column=1, padx=10, pady=10)

label_formularz_user = Label(f_form_user, text='Formularz:')
label_formularz_user.grid(row=0, column=0)

label_imie_user = Label(f_form_user, text='Imie:')
label_imie_user.grid(row=1, column=0, sticky=W)

label_nazwisko_user = Label(f_form_user, text='Nazwisko:')
label_nazwisko_user.grid(row=2, column=0, sticky=W)

label_miejscowosc_user = Label(f_form_user, text='Miejscowość:')


entry_imie_user = Entry(f_form_user)
entry_imie_user.grid(row=1, column=1)

entry_nazwisko_user = Entry(f_form_user)
entry_nazwisko_user.grid(row=2, column=1)

entry_miejscowosc_user = Entry(f_form_user)


buttom_dodaj_obiekt_user = Button(f_form_user, text='Dodaj', command=add_user)
buttom_dodaj_obiekt_user.grid(row=5, column=0, columnspan=2)

from tkinter import StringVar
from tkinter.ttk import Combobox

# --- Zmienna z listą klubów do rozwijanej listy ---
def update_club_comboboxes():
    club_names = [club.name for club in clubs]
    club_combobox_user['values'] = club_names
    club_combobox_employee['values'] = club_names

# --- Dla Użytkownika ---
label_klub_user = Label(f_form_user, text='Nazwa Klubu:')
label_klub_user.grid(row=4, column=0, sticky=W)

club_combobox_user_var = StringVar()
club_combobox_user = Combobox(f_form_user, textvariable=club_combobox_user_var, state="readonly")
club_combobox_user.grid(row=4, column=1)

# --- Dla Pracownika ---
label_klub_employee = Label(f_form_employee, text='Nazwa Klubu:')
label_klub_employee.grid(row=4, column=0, sticky=W)

club_combobox_employee_var = StringVar()
club_combobox_employee = Combobox(f_form_employee, textvariable=club_combobox_employee_var, state="readonly")
club_combobox_employee.grid(row=4, column=1)



root.mainloop()