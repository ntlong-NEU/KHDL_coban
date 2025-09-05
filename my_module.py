print("My mudule is imported")

data = [1,2,3,4,2,4,5,2]

def count_fre(text:str, lower = True)->dict:
    if lower:
        text = text.lower()
    fre = {}
    words = text.split()
    for w in words:
        if w in fre:
            fre[w] += 1
        else:
            fre[w] = 1
    return fre 
# check prime
def is_prime(n:int)->bool:
    """check prime numbers"""
    if n<=1:
        return False
    else:
        for d in range(2,int(n**0.5)+1):
            if n%d==0:
                return False
    return True 
