
def test():
    nb = 2 + 4
    return nb

def test2(): # la même chose que la premiere example test
    return 2 + 4

n2 = test2()
n = test()

print(n, n2)