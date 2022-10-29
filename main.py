import os, sys
import file_organizer_functions as FOF

def selectOption():
    try:
        option = int(input("Choose an option to organize your files in the current directory:\n1; Organize one type of files\n2; Organize all files\n"))
        if option < 1 or option > 2:
            raise ValueError
        return option
    except ValueError:
        print("Select a valid option, try again.")
        os.system("PAUSE")
        sys.exit()

print("Before start make sure you're in the location you want to use to organize your files. If not you can press CTRL + C to stop this program\n")

option = selectOption()
if option == 1:
    fileType = input("Type in the kind of file you want to order: images, documents, music, videos, others\n")
    FOF.checkValidType(fileType.lower())
    FOF.createFolders(option, fileType)
    FOF.orderFiles(option, fileType)
else:
    FOF.createFolders(option)
    FOF.orderFiles(option)