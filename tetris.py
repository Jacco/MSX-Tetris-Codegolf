# 882 non space chars (TODO make it work on replit)
import curses as c
from keyboard import is_pressed as k
from random import *
from time import *

def main(s):
    def tos(v): return format(v, 'b').replace('0', '  ').replace('1','🟦')
    c.noecho()
    X=112
    S=[0]*X
    M=[0]*X
    B=[0]*X
    N=[0]*X
    H=E=T=D=0
    U="222200f0222200f0011300470644071004460740031100170464072001310027026406300132006304620360023100360660066006600660"
    for i in range(1,X):
        S[i-1]=2049
        M[i]=int(U[i-1],16)
    S[20]=8190
    while True:
        if k(1):break
        H=k(75)-k(77)
        F=(1-(E%4==3)*4)*-k('.')-(1-(E%4==0)*4)*k(',')
        V=(T%3==0)|(k(80))
        if D==0:
            W=20
            for i in range(20,3,-1):
                S[i]=S[i]|B[i]
                S[W]=S[i]
                s.addstr(W,0, tos(S[i]))
                W=W-(S[W]!=4095)
            E=randint(0,26);X=4;Y=1
        for i in range(Y-1,Y+4):
            Z=(i>=Y)*2**X
            B[i]=M[E*4+i-Y+1]*Z
            N[i]=M[(E+F)*4+i-Y+1]*Z #rotated
            K=S[i]
            G=B[i]
            H=H*((K&int(G*2**H))==0)
            V=V*((S[i+1]&G)==0)
            F=F*((K&N[i])==0)
            s.addstr(i,0, tos(K|G))
        s.addstr(22,0,"")
        s.refresh()
        T+=1
        D=1-(T%3==1)*(V==0)
        Y=Y+V;X=X+H*(1-V)
        E=E+F*(V-1)*(H==0)
        sleep(0.1)

c.wrapper(main)
