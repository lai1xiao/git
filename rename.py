# -*- coding: cp936 -*-

import datetime
import os
bdir = "f:\\layers\\"
dlists = os.listdir(bdir)
dlists.sort(key=lambda fn:os.path.getmtime(bdir+'\\'+fn))

fdir = bdir + dlists[-1]
strings = "������%s��" % fdir
queren = raw_input(strings)

if queren == 'n':
    fdir = raw_input("�����ļ���:")
    
flists = os.listdir(fdir)
for f in flists:
    fname = fdir +"\\"+ f
    nname = os.path.splitext(fname)[0]
    os.rename(fname,nname)
