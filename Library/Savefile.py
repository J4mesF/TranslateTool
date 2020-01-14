


def Savefile(English,Vietnamese):
    named='Library/'+English+'.txt'
    f=open(named,'w+')
    f.write(English+'\r\n'+Vietnamese)

