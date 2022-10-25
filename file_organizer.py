import os, shutil, sys

class UnvalidTypeError(Exception):
    def __init__(self, value):
        self.value = value

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

def checkValidType(fileType):
    
    try:
        validTypes = ('images', 'documents', 'music', 'videos', 'others')
        if fileType not in validTypes:
            raise UnvalidTypeError("That is not a valid type. Try again.")
    except UnvalidTypeError as UTE:
        print(UTE)
        os.system("PAUSE")
        sys.exit()

def createFolders(option, fileType=''):

    if option == 1:
        if os.path.exists(fileType.capitalize()) == True:
            print(f'{fileType.capitalize()} already exists')
        else:
            print(f'{fileType.capitalize()} created')
            os.mkdir(fileType.capitalize())
    
    else:
        if os.path.exists("Images") == True:
            print('Images already exists')
        else:
            print('Images created')
            os.mkdir("Images")

        if os.path.exists("Documents") == True:
            print('Documents already exists')
        else:
            print('Documents created')
            os.mkdir("Documents")

        if os.path.exists("Videos") == True:
            print('Videos already exists')
        else:
            print('Videos created')
            os.mkdir("Videos")

        if os.path.exists("Music") == True:
            print('Music already exists')
        else:
            print('Music created')
            os.mkdir("Music")

        if os.path.exists("Others") == True:
            print('Others already exists')
        else:
            print('Others created')
            os.mkdir("Others")


def orderFiles(option, fileType=''):
    
    documents = (r".pdf", r".doc", r".docx", r".txt", r".odt", r".xlsx", r".ppt", r"pptx", "documents")
    images = (r".png", r".jpg", r".jpeg", r".gif",r".tiff", r".bmp", "images")
    videos = (r".mp4", r".mkv", r".avi", r".mov",r".flv", r".divx", "videos")
    music = (r".mp3", r".aac", r".wav", r".aiff",r".wma",r".opus",r".ogg", "music")
    others = (r".cpp", r".c", r".h", r".php", r".js", r".py", r".rar", r".zip", r".html",r".tmp",r".dat",r".exe",r".deb",r".dmg"r".psd", "others")

    extensions = [documents, images, videos, music, others]

    if option == 1:
        for extension in extensions:
            if fileType in extension:
                filesToMove = [file for file in os.listdir() if file.endswith(extension)]
                for file in filesToMove:
                    shutil.move(file, fileType.capitalize())
                break
        
        print(f'Files moved to {fileType.capitalize()}:')
        for file in filesToMove:
            print(file)
        os.system("PAUSE")
    
    else:
        FOLDERS = ["Documents", "Images", "Videos", "Music", "Others"]
        index = 0
        for extension in extensions:
            filesToMove = [file for file in os.listdir() if file.endswith(extension)]
            for file in filesToMove:
                shutil.move(file, FOLDERS[index])
            index+=1
            filesToMove.clear()
        os.system("PAUSE")

print("Before start make sure you're in the location you want to use to organize your files. If not you can press CTRL + C to stop this program\n")

option = selectOption()
if option == 1:
    fileType = input("Type in the kind of file you want to order: images, documents, music, videos, others\n")
    checkValidType(fileType.lower())
    createFolders(option, fileType)
    orderFiles(option, fileType)
else:
    createFolders(option)
    orderFiles(option)