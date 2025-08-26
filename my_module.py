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
