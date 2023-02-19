
from os import listdir
from os.path import isfile, join
import os

photos = 0
kopialubnie = []
usuniete = 0
path = input("Podaj sciezke do folderu ze zdjeciami:")
os.path.normpath(path)

kopie = 0

wszystkieZdj = [f for f in listdir(os.path.normpath(rf"{path}")) if isfile(join(os.path.normpath(rf"{path}"), f))]

for x in wszystkieZdj:
    for y in wszystkieZdj:
        if x == y:
            pass
        else:
            zjebanyPathX = rf"{path}\\{x}"
            zjebanyPathY = rf"{path}\\{y}"

            dobryPathX = os.path.normpath(zjebanyPathX)
            dobryPathY = os.path.normpath(zjebanyPathY)
            try:
                if os.path.getsize(rf"{dobryPathX}") == os.path.getsize(rf"{dobryPathY}"):
                    os.remove(fr"{path}\{x}")
                    kopie += 1
                    print(f"Usunięto {x}")
                else:
                    pass
            except FileNotFoundError:
                pass
print(f"Usunięto {kopie}")