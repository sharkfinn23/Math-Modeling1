denominator=input("What is the denominator of your fraction? ")
print("your fraction is 1/{0} " .format(denominator))
a = 1/int(denominator)
print(a)
b = int(denominator)
pre = 0
d = 9
g = 1
f = 0
h = 0
k=0
l=0
while h == 0:
    f = f + 1
    g = 10**f + g
    e = d * g
    while e < k*9 +1:
        f = f + 1
        g = 10**f + g
        e = d * g
        print(e)
    e = d * (g-k)
    print(e)
    i = e%b
    if i == 0:
        h = 1
        j = 1
    else:
        h = 0
        j = 0
        if g > 1111111111111112:
            k = 10**l + k
            l = l + 1
            d = 9
            g = 1
            f = 0
            h = 0
            print(k)
        else:
            if l>16:
                h=1
            else:
                h = 0
                j = 0
            
if j==1:
    print("The fraction you entered has a preceding chunk with {0} digits, and a repeating chunk of {1} digits" .format(l,f+1-l))
else:
   print('finn')
