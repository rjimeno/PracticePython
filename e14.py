
# lrd() can be implemented either as lrdf() or as lrds(), with the latter being probably faster than the former.
def lrdf(L):
    r=[]
    for i in L:
        if i in r:
            pass
        else:
            r.append(i)
    return(r)

def lrds(L):
    return(list(set(L)))

def lrd(L):
    return(lrdf(L))

assert(lrd([]) == [])
assert(lrd([1]) == [1])
assert(lrd([1, 1]) == [1])
assert(lrd([2, 1, 2]).sort() == [1, 2].sort())

print(lrd(['a', 'b', 'b', 'c']))