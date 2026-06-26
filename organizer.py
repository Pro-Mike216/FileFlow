import os
import shutil
from pathlib import Path

def file_organizer(folder_path):
    # Creating path object
    folder_path = Path(folder_path)
    moves= 0
    #create path object for the new folders to create
    if folder_path.exists() :
        
        Codes=folder_path/"Codes"
        Audios=folder_path/"Audios"
        Archives=folder_path/"Archives"
        Documents=folder_path/"Documents"
        Videos=folder_path/"Videos"
        Pictures=folder_path/"Pictures"
        others=folder_path/"others"
        # creating the folders from the path object i create
        Codes.mkdir(exist_ok=True)
        
        Audios.mkdir(exist_ok=True)
        Archives.mkdir(exist_ok=True)
        Documents.mkdir(exist_ok=True)
        Videos.mkdir(exist_ok=True)
        Pictures.mkdir(exist_ok=True)
        
        others.mkdir(exist_ok=True)

        Picture = [".jpg",".jpeg",".png",".gif",".bmp",".svg"]
        Video =[".mp4",".mov",".avi",".mkv"]
        Document =[".pdf",".docx",".doc",".txt",".xlsx",".pptx"]
        Code =[".py",".js",".html",".css",".c",".cpp",".java"]
        Audio =[".mp3",".wav",".aac",".flac"]
        Archivess =[".zip",".rar",".tar",".gz"]
        # use os.walk() for recursive search 
        for root,dirs,files in os.walk(folder_path):
            # dirs and files are going to be lists of folders and files in that root respectively . we want to remove our folders from dirs
            dirs[:] = [d for d in dirs if d not in ["Pictures","Videos","Codes","Documents","Archives","Audios","others"]]
            for file in files :
               print(f" found file : {file}")
               # create a path object for each file in files so it can be moved to our folders
               p=Path(root)/file
               try:
                 if  p.suffix.lower() in Picture :
                    shutil.move(str(p),str(Pictures))
                 elif p.suffix.lower() in Video :
                    shutil.move(str(p),str(Videos))
                 elif  p.suffix.lower() in Document:
                    shutil.move(str(p),str(Documents))
                 elif  p.suffix.lower() in Code:
                    shutil.move(str(p),str(Codes))
                 elif  p.suffix.lower() in Audio:
                    shutil.move(str(p),str(Audios)) 
                 elif  p.suffix.lower() in Archivess:
                    shutil.move(str(p),str(Archives))
                 else :
                    shutil.move(str(p),str(others))
               except: shutil.Error
               moves+=1

      # use os.walk and topdown to find folders and delete them using os.rmdir() ; it will delete only empty folders        
    for root,dirs,files in os.walk(folder_path,topdown=False):
       dirs[:]=[s for s in dirs if s not in ["Pictures","Videos","Codes","Documents","Archives","Audios","others"]]
       for dir in dirs :
          d=Path(root)/dir 
          try:
             os.rmdir(d)
             print(f"folder : {d} deleted") 
          except :
             OSError        
    print(f"moves made is :{moves}")
    

folder_path=input("enter folder path: ")
file_organizer(folder_path)
    