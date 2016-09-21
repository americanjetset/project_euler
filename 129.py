def R(k):
    return int(''.join(['1']*k))

def A(n):
    k =1
    if n % 5 == 0 or n % 2 == 0:
        return 0
    else:
        while R(k) % n != 0:
            k += 1
    return k


print(A(11111101))
