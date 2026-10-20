# *******************************************************************************
# Author: Samuel Dou
# Assignment: Lab 9
# Date: 5/29/25
# Description: This program launches an application using pygubu that
# accesses US Census Bureau data, listing the amount of people of a certain name
# and gender, ordered by year.
#
# Inputs: Name(str), Gender(m/f combo box)
#
# Outputs: List of Data in Application
#
# Sources: Assignment 09 Specifications
# *******************************************************************************
import tkinter as tk
import pygubu
import os
from Person import *

PROJECT_PATH = os.path.dirname(__file__)
PROJECT_UI = os.path.join(PROJECT_PATH, "browser.ui")


class BrowserApp:
    def __init__(self, parent):
        self.start_ui(parent)
        self.setup_tree()
        self.setup_gender_combo()

    def start_ui(self, parent):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.__mainwindow = builder.get_object('top_frame', parent)
        builder.connect_callbacks(self)

        self.__gender_combo = builder.get_object('gender_combo', parent) # assign variables for combo and name
        self.__name_entry = builder.get_object('name_entry', parent)
        self.__tree = builder.get_object('treeview', parent)

    def setup_tree(self):
        tree = self.__tree
        tree.configure(columns = (0, 1, 2, 3, 4))

        tree.heading(0, text='Name', anchor = tk.W)
        tree.heading(1, text='Year')
        tree.heading(2, text='Gender')
        tree.heading(3, text='NameCount')
        tree.heading(4, text='Total')

        tree.column(0, width=100, anchor=tk.CENTER)
        tree.column(1, width=100, anchor=tk.CENTER)
        tree.column(2, width=100, anchor=tk.CENTER)
        tree.column(3, width=100, anchor=tk.CENTER)
        tree.column(4, width=100, anchor=tk.CENTER)

    def setup_gender_combo(self):
        self.__gender_combo['values'] = ['M', 'F']

    def gender_selected(self, event):
        self.fetch_persons()

    def name_changed(self, event):
        self.fetch_persons()

    @staticmethod
    def persons_tuple(person):
        return (
            person.get_name(),
            person.get_year(),
            person.get_gender(),
            person.get_namecount(),
            person.get_total()
        )

    def fetch_persons(self):
        persons = Person.fetch_person(self.__name_entry.get(), self.__gender_combo.get())
        for i in self.__tree.get_children():
            self.__tree.delete(i)

        for i in range(len(persons)):
            self.__tree.insert('', 'end', values=BrowserApp.persons_tuple(persons[i]))

    def run(self):
        self.__mainwindow.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Name and Gender Browser")
    app = BrowserApp(root)
    app.run()
