#All Primitive Triples & N Factors
def TRIPLES(N,Z):
        for X1 in range(0,N):
                C,C0,C1=(3*X1)**2,3*X1,0
                if C%2==0:C1=1
                D,D0,D1=((3*(X1+1))-1)**2,(3*(X1+1))-1,0
                if D%2==0:D1=1
                for X2 in range(0,N):
                        A,A0,A1=((3*(X2+1))-1)**2,(3*(X2+1))-1,0
                        if A%2==0:A1=1
                        B,B0,B1=((3*X2)+1)**2,(3*X2)+1,0
                        if B%2==0:B1=1
                        if Z==1:
                                if all([C1!=A1,abs(C-A)==N,abs(C0*2*A0)!=0]):print("SET:",abs(C-A),",",abs(C0*2*A0),",",abs(C+A))
                                if all([C1!=B1,abs(C-B)==N,abs(C0*2*B0)!=0]):print("SET:",abs(C-B),",",abs(C0*2*B0),",",abs(C+B))
                                if all([D1!=B1,abs(D-B)==N,abs(D0*2*B0)!=0]):print("SET:",abs(D-B),",",abs(D0*2*B0),",",abs(D+B))
                        else:
                                if all([C1!=A1]):print("SET:",abs(C-A),",",abs(C0*2*A0),",",abs(C+A))
                                if all([C1!=B1]):print("SET:",abs(C-B),",",abs(C0*2*B0),",",abs(C+B))
                                if all([D1!=B1]):print("SET:",abs(D-B),",",abs(D0*2*B0),",",abs(D+B))
TRIPLES(121,0)
#TRIPLES(N,Z)
#N=AREA FROM 0 of PRIMITIVES, Z=0
#N=SETS WITH N ONLY, Z=1 (NOT THE FASTEST METHOD DEVELOPED FOR FACTORING, BUT, AS THESE ARE RELATED TO COMPOSITE SETS)
#N DOES NOT FACTOR EVEN #'s (PRIMITIVE LIST)


	

