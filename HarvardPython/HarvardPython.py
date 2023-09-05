#i = 0
#while i < 3:
#    print("woof")
#    i += 1

#for i in [0, 1, 2]:
#    print("woof")

#for i in range(3):
#    print("woof")

#print("meow\n" * 3, end="")

#while True:
#    n = int(input("What is N"))
#    if n > 0:
#        break

#for _ in range(n):
#    print("woof")

def main():
    number = get_number()
    woof(number)

def get_number():
    while True:
        n = int(input("What is N"))
        if n > 0:
            return n

def woof(n):
    for _ in range(n):
        print("woof")
        #
main()
