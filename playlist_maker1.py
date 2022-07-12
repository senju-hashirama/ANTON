#playlist_maker.py
from tkinter import Tk
from tkinter.filedialog import askopenfilenames
from pathlib import Path

#functions
def create(path,file,b):
        a=open(path+b+".wpl","w")  #opens a wpl file

        files=file #uses the bellow unction to get files to be added 
        text="\n"
        count=0
        for j in files:   #loop to add music to wpl file
            count=count+1
            txt="""<media src="{}" /> \n""" .format(Path(j)) # Path() is used to convert / in the path to \
            text=text+txt+"\n"
        wpl_file="""<?wpl version="1.0"?> \n<smil> \n<head>  \n<meta name="ItemCount" content="{}"/> \n<title>{}</title> \n</head>
\n<body> \n<seq>{}</seq> \n</body> \n</smil>
 """ .format(count,"playlist",text) #adds number of songs, the name and the songs

        a.write(wpl_file) # writes the file 
        a.close()        
def get_dir():

        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        filename = askopenfilenames() # show an "Open" dialog box and return the path to the selected file

        return filename


def add_music(path,playlist):

        #this is a really bad implimentation but it does the work pretty fine.
        #the original file is opened and then the user can choose the new songs and it will be added
        a=get_dir()
        count=len(a)
        file=open(path+playlist+".wpl","r")
        wpl=file.readlines()
        for i in a:         
                wpl=wpl[:12]+["""<media src="{}" /> \n""" .format(Path(i))]+wpl[12:]
        file.close()
        print(wpl)

        
        file1=open(path+playlist+".wpl","w")
        file1.writelines(wpl)
        file1.close()
#if __name__=="__main__": #checks if the file is being run as a module or a file
                          #for now remove this and try
       # create()
        
