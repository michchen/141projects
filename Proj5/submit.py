import sys, os

islab = {"01wing": True, "02calc": True, "03selection": True,
         "04loops": True, "05strings": True, "06files": True,
         "07functions": True, "08lists": True, "09dictionary": True,
         "10classes": True, "11advclasses": True, "12linux": True}
def getDir( ):
    cwd = os.getcwd( )
    tree = cwd.split("/")
    print (tree)
    return tree[-1]

def readConfig():
    fname = os.environ['HOME'] + "/.cs141"
    fh = open(fname, "r")
    config = { }
    for line in fh:
        fld = line.split()
        config[fld[0]] = fld[1]
    fh.close()
    return config

dirname = getDir()
cfg = readConfig( )
if dirname in islab:
    cmd = ("~%s/%s 141l%s %s" % (cfg["ta"], cfg["tabin"], cfg["lab"], dirname))
else:
    cmd = ("~%s/%s cs141-%s %s" % (cfg["prof"], cfg["profbin"], cfg["lecture"], dirname))
print (cmd)
os.system(cmd)
