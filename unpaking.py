# Unpack a tuple into variables.
a=(1,2,5,8,3)
b,c,d,e,f=a
print(b,c,d,e,f)
n,*m=a
print(n,m)
