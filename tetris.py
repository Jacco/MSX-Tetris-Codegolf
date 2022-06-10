import curses as c
from time import *
from random import *

def main(s):
    q = list('🟫🟦🟧🟪🟥🟩🟨')
    def tos(v,c): return '{0:012b}'.format(v).replace('0', '⬛').replace('1',c)
    def mrg(b,f): return ''.join([ l if l!='⬛' else r for l,r in zip(b,f)])
    c.noecho()
    s.nodelay(True)
    X=112
    S=[0]*X
    M=[0]*X
    B=[0]*X
    N=[0]*X
    O=['']*X
    P=H=E=T=D=0
    U="222200f0222200f0011300470644071004460740031100170464072001310027026406300132006304620360023100360660066006600660"
    for i in range(1,X):
        S[i-1]=2049
        M[i]=int(U[i-1],16)
    S[20]=8190
    for i in range(20,0,-1): # TODO compress share loop
      O[i]=tos(S[i],'⬜')
    while True:
        k=s.getch()
        while s.getch()!=-1: pass
        if k==27:break
        H=(k==260)-(k==261)
        F=(1-(E%4==3)*4)*-(k==46)-(1-(E%4==0)*4)*(k==44)
        V=(T%3==0)|(k==258)
        if D==0:
            W=20
            for i in range(20,3,-1):
                S[i]=S[i]|B[i]
                O[i]=mrg(O[i],tos(B[i],q[E//4]))
                S[W]=S[i]
                O[W]=O[i]
                s.addstr(W,0, O[i])
                J=S[W]!=4095
                P+=J==0
                W=W-J
                
            E=randint(0,26);X=4;Y=1
        for i in range(Y-1,Y+4):
            Z=(i>=Y)*2**X
            B[i]=M[E*4+i-Y+1]*Z
            N[i]=M[(E+F)*4+i-Y+1]*Z
            K=S[i]
            G=B[i]
            H=H*((K&int(G*2**H))==0)
            V=V*((S[i+1]&G)==0)
            F=F*((K&N[i])==0)
            s.addstr(i,0,mrg(O[i],tos(G,q[E//4])))
        s.addstr(22,0,"SCORE: {}".format(P))
        c.curs_set(0)
        s.refresh()
        T+=1
        D=1-(T%3==1)*(V==0)
        Y=Y+V;X=X+H*(1-V)
        E=E+F*(V-1)*(H==0)
        sleep(0.3)

c.wrapper(main)
