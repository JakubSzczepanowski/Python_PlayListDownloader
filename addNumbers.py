import os
import pathlib

daty = {}

i = 1
for elem in os.listdir():
    if '.m4a' in elem:
        daty[elem] = pathlib.Path(elem).stat().st_mtime

daty = dict(sorted(daty.items(), key=lambda item: item[1]))
for e in daty.keys():
    os.rename(e, f'{i}. {e}')
    i += 1