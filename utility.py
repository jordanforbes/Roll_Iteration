#print
def p(x=""):
    print(x)

#print vars    
def v(x):
    p(vars(x))
    return vars(x)
    
#to string
def s(i):
    return str(i)

#hp    
def hp(t):
    h=t.hp
    #p(str(t.name)+" HP: "+str(h))
    return h
    
def klax(st="###"):
    k="###"+s(st)+"###"
    p(k)
    return k

#scorecard    
def sc(pl,en):
    klax("SCORE")
    v(pl)
    v(en)
    klax()