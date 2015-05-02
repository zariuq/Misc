i=1
print i
fi = open("runner.py","rw+")
a1 = fi.readlines()
a1[0] = 'i='+str(i+1)+'\n'
fi.seek(0,0)
fi.writelines(a1)
if i >= 10:
    a1[0] = 'i=1\n'
    fi.seek(0,0)
    fi.writelines(a1)
fi.close()
if i < 10:
    execfile("runner.py")
    
'''
Edits its first line to essentially be a for loop.
Kind of fucked up, but I wanted a program that rewrote itself to some positive effect =D
(Credit goes to cousin Dan for noticing that I need .close())
'''
