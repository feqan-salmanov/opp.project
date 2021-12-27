def ucbucax(a,b,c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

a = lambda a,b,c : a**2 + b**2 == c**2
print(a(3,4,5))