import os, shutil, sys

class UnvalidTypeError(Exception):
    def __init__(self, value):
        self.value = value

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
        if os.path.exists(fileType) == True:
            print(f'{fileType.capitalize()} already exists')
        else:
            print(f'{fileType.capitalize()} created')
            os.mkdir(fileType.capitalize())
    
    else:
        FOLDERS = {
            "Documents": (os.mkdir("Documents") if os.path.exists("Documents") == False else print("Documents already exists")),
            "Images": (os.mkdir("Images") if os.path.exists("Images") == False else print("Images already exists")),
            "Videos": (os.mkdir("Videos") if os.path.exists("Videos") == False else print("Videos already exists")),
            "Music": (os.mkdir("Music") if os.path.exists("Music") == False else print("Music already exists")),
            "Others": (os.mkdir("Others") if os.path.exists("Others") == False else print("Others already exists"))
        }
        print("All files organized")
        FOLDERS.keys()

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