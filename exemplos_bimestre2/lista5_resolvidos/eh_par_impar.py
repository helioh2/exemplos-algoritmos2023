def e_par(x):
    if x%2==0:
        return True
    else:
        return False

print(e_par(4))
print(e_par(5))

def e_impar(n):
    return not e_par(n)
    
print(e_impar(2))
print(e_impar(3))

