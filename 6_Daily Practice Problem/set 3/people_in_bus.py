"""Find the no.of people in a bus, given the data of people onboarding & alighting at each station"""
k=0
def people(p,a,b):
    p = p + a-b

    print(p)
    return p

#a is people onboarding and b is people leaving
a=5
b=2
k= people(k, a, b)
k= people(k, 6, 2)
k= people(k, 4, 3)
k= people(k, 1, 4)
k= people(k, 9, 8)



