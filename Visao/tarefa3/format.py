import os

root = "/home/arthur/Documents/libraries/OIDv4_ToolKit/OID/Dataset"

filesList = list()
for path, subdirs, files in os.walk(root):
    for name in files:
        if '.txt' in name:
            pathToFile = os.path.join(path, name)
            fileVar = open(pathToFile, 'r')
            fileContent = fileVar.read()
            newFileContent = fileContent.replace('Light bulb', '0')
            filesList.append(pathToFile)
            print(fileContent,'   -------   ', newFileContent)

print(len(filesList))

# print(*files, sep='\n')

