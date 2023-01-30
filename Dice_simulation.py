#Az import random sor betölti a Python random modulját, amely a véletlenszámok generálását teszi lehetővé.
import random
#A dice függvény fogadja az argumentumként megadott number_of_dice értéket, amely megadja, hány dobókockát szeretne a felhasználó dobni.
def dice(number_of_dice):
#A results lista létrehozása, amely a dobás eredményeit fogja tárolni.
    results = []
#A for ciklus végigmegy a number_of_dice értékig, és minden iterációban generál egy véletlenszámot 1 és 6 között a random.randint függvénnyel.
    for i in range(0,number_of_dice):
        result = random.randint(1,6)
        results.append(result)
    return results
#A number_of_dice értékét a input függvénnyel kérjük be a felhasználótól, és azt az int függvénnyel konvertáljuk egész számmá.
number_of_dice = int(input("How many dice would you like to roll? "))
#A while ciklus ellenőrzi, hogy a number_of_dice értéke nem haladja-e meg a 5-öt. Ha igen, akkor újra kérjük be a felhasználótól.
while number_of_dice > 5:
    number_of_dice = int(input("You may only have a limit of 5 dice, enter a number under 5. "))
#A dice függvényt meghívjuk a number_of_dice argumentummal, és az eredményt kiíratjuk a print függvénnyel.
print(dice(number_of_dice))
