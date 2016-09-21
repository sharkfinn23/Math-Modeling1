numerator=input("What is the numerator of your fraction? ")
denominator=input("What is the denominator of your fraction? ")
print("your fraction is {1}/{0} " .format(denominator, numerator))
if int(numerator)>int(denominator):
    x = int(numerator)/int(denominator) - int(numerator)%int(denominator)/int(denominator)
    numerator = int(numerator) - int(denominator)
    print(x)
else:
    x= 0
if int(numerator)==int(denominator):
    x=1
    h=1
    j=1
    l=0
    f=0
else:
    print('finn')
if int(denominator)%int(numerator) == 0:
    denominator = int(denominator)/int(numerator)
else:
    print('finn')
a = int(numerator)/int(denominator)
print(a)
b = int(denominator)
if h==0:
    pre = 0
    d = 9
    g = 1
    f = 0
    h = 0
    k=0
    l=0
else:
    h=1
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
    print("The fraction you entered has {2} before the decimal, a preceding chunk with {0} digits, and a repeating chunk of {1} digits" .format(l,f+1-l,x))
else:
    print('finn')
