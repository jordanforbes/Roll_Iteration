# turn=0

# p()
# sc(p1,e1)
# p()

# ### game loop ###
# while hp(e1)>0:
#     turn+=1
#     p("turn "+s(turn))
#     p1.attack(e1)
#     p("==end turn==")
#     p()
#     sc(p1,e1)
#     p()



#dieList=['2d6','3d8','20d20','8d12']
#debug units
#p(e1.hp)
#hp(e1)

#game loop
#hp=hp(p1)

u1= u.Unit()           

p1= u.Player()
e1= u.Enemy()
print("hp",e1)

print(vars(p1))
print(vars(u1))
print(vars(e1))
    

print(D.hit())
    
    
x=D.readList()
print(x)

x=D.readList(dieList)
print(x)
    
print(throwProc())
print(throwProc('2d6'))
print(throwProc('420d666'))

def rollCombo(die=[d(10),d(6)]):
    add=0
    for x in die:
        add += x
    
    print(add)
    
rollList=[2,6,4,10,20,100]

def rollSet(die):
    results= []
    for x in die:
        results.append(d(x))
    print(results)
    
rollSet(rollList)

print(multiThrow(8,20))
print(multiThrow(2,6))


def roller():
    rolls=[]

    rolls.append(d(6))
    rolls.append(d(6))
    rolls.append(d(6))
    rolls.append(d(6))
    rolls.append(d(6))

    return rolls


rolls=roller()
print(rolls)
    
rollCombo(rolls)
