import random
def intoMixedFrac(N,D):
    a = N%D
    b = N//D
    return a,b
    
def intoFrac(Q,R,D):
    a = Q*D + R
    return a

MixedFracQues = int(input("\nHow many questions you want to create of \"converting Mixed Fraction into Fraction\"  :"))
FracQues = int(input("\nHow many questions you want to create of \"converting Fraction into Mixed Fraction\"  :"))
N =[]
D =[]
Q =[]
R =[]

print("\n--------------------------------------------------------------------------------")
print("\nEnter fraction values for creating question : ")
print("\n--------------------------------------------------------------------------------")

for i in range(MixedFracQues):
    print(f"Q. {i+1} Enter value of Numerator ")
    m = int(input())
    N.append(m)
    print("Enter value of Denominator ")
    n = int(input())
    D.append(n)
    a,b= intoMixedFrac(N[i],D[i])
    Q.append(a)
    R.append(b)

Quotient =[]
Remainder =[]
Divisor =[]
Numerator = []
print("--------------------------------------------------------------------------------")
print("\nEnter mixed fraction values for creating question : ")
print("\n--------------------------------------------------------------------------------")
for i in range(FracQues):
    print(f"\nQ. {i+1} Enter value of Quotient ")
    q = int(input())
    Quotient.append(q)
    print("\nEnter value of Remainder ")
    r = int(input())
    Remainder.append(r)
    print("\nEnter value of Divisor ")
    d = int(input())
    Divisor.append(d)
    a1 = intoFrac(Quotient[i],Remainder[i],Divisor[i])
    Numerator.append(a1)

for i in range(0,MixedFracQues):
    print(f"\nQ.{i+1} Convert the given fraction into mixed fraction {N[i]}/{D[i]}")
    print(f"1. {random.randint( Q[i],R[i])}({random.randint (Q[i],R[i])}/{D[i]}) ")
    print(f"\t\t2. {Q[i]}({R[i]}/{D[i]})")
    print(f"\n3. {random.randint( Q[i],R[i])} ({random.randint( Q[i],R[i])}/{random.randint( Q[i],R[i])})")
    print(f"\t\t4. {random.randint(Q[i],R[i])}({random.randint(Q[i],R[i])}/{D[i]})")

for i in range(0,FracQues):
    print(f"\nQ.{i+1} Convert the given mixed fraction into fraction {Quotient[i]}({Remainder[i]}/{Divisor[i]})")
    print(f"1. {random.randint (Quotient[i],Remainder[i])}/{random.randint( Quotient[i],Remainder[i])} ")
    print(f"\t\t2. {Numerator[i]}/{Divisor[i]}")
    print(f"\n3. {random.randint (Quotient[i],Remainder[i])}/{Divisor[i]} ") 
    print(f"\t\t4. {random.randint (Quotient[i],Remainder[i])}/{random.randint( Quotient[i],Remainder[i])} ")
