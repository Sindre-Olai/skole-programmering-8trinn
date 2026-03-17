print("Heisann!")

hvor_mange = input("Hvor mange er dere?")
if int(hvor_mange) < 2:
    print("Velkommen")
else: print("Velkommen alle sammen!")
for i in range(int(hvor_mange)):
    navn = input("Hva heter du person nummer " + format(i+1) + "? ")
    print("Hyggelig å møte deg, " + navn + "!")
    
    alder = input("Hvor gammel er du? ")

    if int(alder) < 12:
        print("Du er et barn!")
    elif int(alder) < 18:
        print("Du er en Ungdom!")
    elif int(alder) > 18:
        print("Du er en voksen!")

    favoritt_farge = input("Hva er din favorittfarge? ")
    print("Ah, " + favoritt_farge + " er en fin farge!")

    def sports_interesse():
        sport = input("Spiller du sport? (ja/nei) ")
        if sport.lower() == "ja":        
            hvilken_sport = input("Hvilken sport spiller du? ")
            print("Kult! " + hvilken_sport + " er en morsom sport!")
        elif sport.lower() == "nei":
            print("Ok men jeg anbefaler å prøve for eksempel basketball, det synes jeg er gøy!")
    sports_interesse()

if int(hvor_mange) < 2:
    print("Ha en fin dag!")
else: print("Ha en fin dag alle sammen!")