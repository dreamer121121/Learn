def devide(n):
    result = []
    prime = int(2)
    while (prime<=n):
        k= n % prime
        if( k == 0):
            n=n/prime
            result.append(prime)
        else:
            prime=prime+1
    return set(result)
print(devide(13))