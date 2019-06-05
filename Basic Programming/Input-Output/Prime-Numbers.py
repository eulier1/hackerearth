num = int(input())
result = []

for divisor in range(2,num):
    prime = True
    for dividend in range(2,divisor):
        if divisor % dividend == 0:
            prime = False
    if prime:
        result.append(str(divisor))
        
print(" ".join(result))
