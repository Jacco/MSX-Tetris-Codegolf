1 DEFINTA-Z:SCREEN1:X=112:DIMS(X),B(X
),N(X),M(X):S$="222200f0222200f001130
0470644071004460740031100170464072001
3100270264063001320063046203600231003
60660066006600660":FORI=1TOX:VPOKE383
+I,-(I>9)*254:S(I-1)=2049:M(I)=VAL("&
h"+MID$(S$,1,1)):NEXT:S(20)=8190
2 A=STICK(0):A$=INKEY$:H=(A=3)-(A=7):
N=(1+(EMOD4=3)*4)*-(A$=".")+(1+(EMOD4
=0)*4)*(A$=","):V=(TMOD3=0)OR(A=5):IF
D=0THENW=20:FORI=20TO4STEP-1:S(I)=S(I
)ORB(I):S(W)=S(I):LOCATE8,W:PRINTBIN$
(S(W)):W=W+(S(W)<>4095):NEXT:E=RND(-T
IME)*27:X=4:Y=1
3 FORI=Y-1TOY+3:Z=-(I>=Y)*2^X:B(I)=M(
E*4+I-Y+1)*Z:N(I)=M((E+N)*4+I-Y+1)*Z:
K=S(I):G=B(I):H=H*-((KANDG*2^H)=0):V=
V*((S(I+1)ANDG)=0):N=N*-((KANDN(I))=0
):LOCATE8,I:PRINTBIN$(KORG):NEXT:T=T+
1:D=1-(TMOD3=1)*(V=0):Y=Y+V:X=X+H*(1-
V):E=E+N*(V-1)*(H=0):GOT02