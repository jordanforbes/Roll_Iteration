from random import randint as r 



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
        
    @staticmethod
    def hit(s=20):
    
        n=D.d(s)
        print(n)
        if n==1:
            return "crit fail"
        elif n==20: 
            return "crit success"
        elif n<6:
            return "fail"
        elif n<10:
            return "mixed hit"
        else:
            return "success"
    

        