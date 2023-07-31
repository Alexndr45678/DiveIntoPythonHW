import seminar8
import os
import json
import csv
import pickle


class FileCsv:
    def __init__(self, name) -> None:
        self.name = name
    
    def converted_file(self):
        return seminar8.traverse_directory(self.name)
    
FileCsv('fil1.csv').converted_file()