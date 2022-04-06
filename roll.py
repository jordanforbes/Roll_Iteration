from random import randint as r 

dieList=['2d6','3d8','20d20','8d12']

    def d(s):
        return r(1,s)
    
    def xThrow(n,s):
        result=0
        for x in range(n):
            roll=D.d(s)
            result+=roll
        #finStr= str(n)+'d'+str(s)
        #print(finStr+":"+str(result))
        return result
    
     def throwProc(die='4d20'):
            t=die.rpartition("d")
        n=int(t[0])
        s=int(t[2])
        return D.xThrow(n,s)
            
    def readList(dList=['6d9','3d20','4d6']):
        result=0
        rA=[]
        for d in dList:
            r=D.throwProc(d)
            rA.append(r)
            result +=r
        return result,rA    
    
