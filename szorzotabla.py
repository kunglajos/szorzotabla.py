def tabla7():
    n = 1
    while n < 11:
        # A modern Pythonban a print-hez zárójel kell, 
        # az end=" " gondoskodik róla, hogy egy sorba írja őket
        print(n * 7, end=" ")
        n = n + 1
    print() # Ez egy új sort kezd, miután a ciklus véget ért

def tabla7tripla():
    print('A 7-es szorzótábla három példányban :')
    tabla7()
    tabla7()
    tabla7()
