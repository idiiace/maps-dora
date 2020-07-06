import os

a="db.sqlite3"

def unsplit():
    a=open("db.sqlite1","rb").read()
    b=open("db.sqlite2","rb").read()
    c=open("db.sqlite3","wb").write(a+b)
    print "success"

unsplit()
    
    
    
