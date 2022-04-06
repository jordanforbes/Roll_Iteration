from random import randint as r 

dieList=['2d6','3d8','20d20','8d12']

#D for Dice
class D:

    @staticmethod
    def d(s):
        return r(1,s)
    
    @staticmethod   
    def xThrow(n,s):
        result=0
        for x in range(n):
            roll=D.d(s)
            result+=roll
        #finStr= str(n)+'d'+str(s)
        #print(finStr+":"+str(result))
        return result
            
    @staticmethod
    def throwProc(die='4d20'):
        t=die.rpartition("d")
        n=int(t[0])
        s=int(t[2])
        return D.xThrow(n,s)
                
    @staticmethod
    def readList(dList=['6d9','3d20','4d6']):
        result=0
        rA=[]
        for d in dList:
            r=D.throwProc(d)
            rA.append(r)
            result +=r
        return result,rA    
    
def d20(n):
    if n == 20:
        return "crit hit"
    if n ==0:
        return "crit fail"
    if n >=10:
        return "success"
    
    
x=D.readList()
print(x)

x=D.readList(dieList)
print(x)
    
#print(throwProc())
#print(throwProc('2d6'))
#print(throwProc('420d666'))

#def rollCombo(die=[d(10),d(6)]):
#    add=0
#    for x in die:
#        add += x
    
#    print(add)
    
#rollList=[2,6,4,10,20,100]

#def rollSet(die):
#    results= []
#    for x in die:
#        results.append(d(x))
#    print(results)
    
#rollSet(rollList)

#print(multiThrow(8,20))
#print(multiThrow(2,6))


#def roller():
#    rolls=[]

#    rolls.append(d(6))
#    rolls.append(d(6))
#    rolls.append(d(6))
#    rolls.append(d(6))
#    rolls.append(d(6))

#    return rolls


#rolls=roller()
#print(rolls)
    
#rollCombo(rolls)
