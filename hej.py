alder = input("Are you old enough? Write your age: ")
#hvis 18+ saa
if alder >= 18:
    print("Welcome")
    print("this is a private website")
    #hvis 18+, saa sporg om 46+
    if alder > 45:
        print("lige gammel nok bro")
        #hvis 46+, saa sporg om 90
        if alder == 90:
            print("gamle ole!")
        #hvis IKKE 90, saa ok
        if alder != 90:
            print("ok")
print("Farvel")
