import os
def deleteCopiFiles():
    # DELTE FILES WITH IN NAME INCLUDE 'copia'
    for filename in os.listdir('filter-data/Tinku'):

        if 'copia' in filename:
            os.remove('filter-data/Tinku/'+filename)
            print('data/train/Tinku/'+filename)

deleteCopiFiles()