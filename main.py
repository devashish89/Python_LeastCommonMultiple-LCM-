import functools

def gcd_2nums(a,b):
    val = min(a,b)
    #print(val)
    lst = list()
    gcd = 1
    for i in range(2,val):
        if (a%i==0 and b%i==0):
            lst.append(i)

    if len(lst)>0:
        return max(lst)

    return gcd

def lcm_2nums(a,b):
    """a*b = lcm(a,b)*hcf(a,b)"""
    return a*b/(gcd_2nums(a,b))

def lcm_2nums_second(a,b):
    """
     logic: lcm(18,24)
     18*1 = 18, 18*2 = 36, 18*3=54, 18*4=72
     24*1=24, 24*2=48, 24*3=72
     so lcm = 72
    :param a: int num
    :param b: int num
    :return: lcm(a,b) int
    """
    max_num = max(a,b)
    min_num = min(a,b)
    i=1
    j=1
    while(i>0):
        #print("i",i)
        while(j>=i):
            #print("j",j)
            #print("max_num*i",max_num*i,"min_num*j",min_num*j)
            if (max_num*i < min_num*j):
                i+=1
            elif (max_num*i == min_num*j):
                return max_num*i
            else:
                j+=1

def main():
    print(gcd_2nums(3,5)) #1
    print(gcd_2nums(36,60)) #12
    print(lcm_2nums.__doc__)
    print(lcm_2nums(30,45)) #90
    print(lcm_2nums(18,24))
    print(lcm_2nums_second.__doc__)
    print(lcm_2nums_second(18,24))
    print(lcm_2nums_second(30,45))

if __name__ == "__main__":
    main()





