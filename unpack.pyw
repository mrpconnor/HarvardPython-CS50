"""
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(**coins), "Knuts") 

"""

#first, _ = input("Whats your name?").split(" ")
#print(f"hello, {first}")


"""
def f( *args, **kwargs):
    print("Named:", kargs)

f(galleons=100, sickles=50, knuts=25)
"""