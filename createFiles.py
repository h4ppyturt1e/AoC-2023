# create python files and according test files for each day in the advent of code

import os
import shutil

def createFiles():
    print('Creating files...')
    for i in range(1,26):
        # create folder
        foldername = 'Day ' + str(i)
        if not os.path.exists(foldername):
            os.makedirs(foldername)
        
        # create python file
        filename = os.path.join(foldername, 'day' + str(i) + '.py')
        if not os.path.exists(filename):
            shutil.copyfile('template.py', filename)
        
        # create test file
        filename = os.path.join(foldername, 'test.txt')
        if not os.path.exists(filename):
            with open(filename, 'w') as f:
                f.write('')
    return

if __name__ == '__main__':
    createFiles()
