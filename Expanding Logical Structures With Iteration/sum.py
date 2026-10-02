def sum_to_n(n):
    count=1
    total=0
    while(count<=n):
        total+=count
        count+=1
    return total
print(sum_to_n(5))

def sum_from_m_to_n(m,n):
    index=m
    result=0
    while(index<=n):
        result+=index
        index+=1
    return result
print(sum_from_m_to_n(3,5))

def sum_odd(m,n):
    result=0
    index=m
    while(index <= n):
        if(index % 2==1):
            result+=index
        index+=1
    return result
print(sum_odd(2,7))
            
            
    