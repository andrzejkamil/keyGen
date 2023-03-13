from cx_Freeze import setup, Executable
import time
import os

start_time = time.time()
includefiles = [
                'E:\\Schowek\\Programowanie\\Projekty\\Python\\keysGenerator\\build\\dolepy\\geckodriver.exe',
                'E:\\Schowek\\Programowanie\\Projekty\\Python\\keysGenerator\\build\\dolepy\\Firefox64',
                'E:\\Schowek\\Programowanie\\Projekty\\Python\\keysGenerator\\build\\dolepy\\q0lmi0d1.default-release',
                'E:\\Schowek\\Programowanie\\Projekty\\Python\\keysGenerator\\build\\dolepy\\config.ini',
                'E:\\Schowek\\Programowanie\\Projekty\\Python\\keysGenerator\\build\\dolepy\\INIFileParser.dll',
                'E:\\Schowek\\Programowanie\\Projekty\\Python\\keysGenerator\\build\\dolepy\\INIFileParser.xml',
                'E:\\Schowek\\Programowanie\\Projekty\\Python\\keysGenerator\\build\\dolepy\\keysGenerator.exe',
                'E:\\Schowek\\Programowanie\\Projekty\\Python\\keysGenerator\\build\\dolepy\\assets',
                ]

setup(name='keysGenerator',
      version='0.1',
      options={
          'build_exe': {
              # 'include_files': includefiles,
              'optimize': 2,
          },
      },
      executables=[Executable('main.py')],)
print('\nDone\nTime: ' + str(time.time() - start_time) + ' sec')

# assign size
size = 0

# assign folder path
Folderpath = 'E:\\Schowek\\Programowanie\\Projekty\\Python\\keysGenerator\\build\\exe.win-amd64-3.9'

# get size
for path, dirs, files in os.walk(Folderpath):
    for f in files:
        fp = os.path.join(path, f)
        size += os.path.getsize(fp)

# display size
print("Size: " + str(size/1000000) + " MB")
