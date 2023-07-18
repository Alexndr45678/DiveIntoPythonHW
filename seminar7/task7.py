import os
import shutil

def sort_dir(dct, folder):
    for dir, _, files in os.walk(folder):
        for file in files:
            ext = file.split('.')[-1]
            for item in dct:
                if ext in dct[item]:
                    if not os.path.isdir(item):
                        os.mkdir(item)
                    shutil.move(f'{folder}/{file}', item)


sort_dir({"video": ["avi", "mov"],
          "data": ["txt", "pdf"]}, 'tmp1')
