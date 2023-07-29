import os

# set your own path here!
# example path: "c:\\Users\\Asus\\Desktop\\folder_to_sort"
dirToSort = "c:\\path here"

os.chdir(dirToSort)
currPath = os.getcwd()
print(f'Current path: {currPath}')

dirToCreate = ['Images', 'Documents', 'Videos', 'Music', 'Others']

filesToCheck = (
    ('.jpg', '.png', '.jpeg'),
    ('.pdf', '.docx', '.txt'),
    ('.mp4', '.mov', '.avi'),
    ('.mp3', '.wav')
)

for dir in dirToCreate:
    if not os.path.exists(dir):
        os.mkdir(dir)

for file in os.listdir():
    if not os.path.isdir(file):
        if file.endswith(tuple(filesToCheck[0])):
                os.rename(file, f'Images/{file}')
        elif file.endswith(tuple(filesToCheck[1])):
            os.rename(file, f'Documents/{file}')
        elif file.endswith(tuple(filesToCheck[2])):
            os.rename(file, f'Videos/{file}')
        elif file.endswith(tuple(filesToCheck[3])):
            os.rename(file, f'Music/{file}')
        elif file.endswith('.py'):
            continue
        else:
            os.rename(file, f'Others/{file}')

print('Sorting Done!')