'''
Esercizio 3C-6. Modificare il codice dell'esercizio 3C-4, affinchè si possa scrivere un codice python che consenta all'utente di 
inserire il nome di un animale ed un habitat. Quando il codice dell'esercizo 3C-4 classifica 
'animale inserito in una delle categorie tra mammiferi, rettili, uccelli o pesci, oltre a mostrare un messaggio a schermo, 
deve salvare tale categoria in una variabile animal_type. Se l'animale inserito non è classificabile in una delle quattro categorie proposte, 
il valore di animal_type sarà ' "unknown".

Inserire, poi, in un dizionario il nome dell'animale, la categoria a cui esso appartiene (animal_type) e l'habitat.

Verificare con un match statement se l'animale e la categoria a cui esso appartiene possano vivere nell'habitat inserito; dunque, verificare:
- se l'animale può vivere nell'habitat specificato, stampare un messaggio appropriato.
- se l'habitat non è compatibile con l'habitat specificato, stampare un avviso.
- Se l'animale o l'habitat non sono riconosciuti, stampare un messaggio di errore.

Le categorie di classificazione devono essere:
- Mammiferi: cane, gatto, cavallo, elefante, leone, balena, delfino.
- Rettili: serpente, lucertola, tartaruga, coccodrillo.
- Uccelli: aquila, pappagallo, gufo, falco, cigno, anatra, gallina, tacchino.
- Pesci: squalo, trota, salmone, carpa.

Categorie di habitat:
- acqua
- aria
- terra

NOTA.
Il codice deve produrre un risultato sensato, ovvero che l'animale inserito possa effettivamente vivere nell'habitat specificato.
Tenere in considerazione il fatto che alcuni animali tra quelli specificati possono vivere in più di un habitat, mentre altri solo in uno.

Suggeirmento: può essere utile per coprire tutti i possibili casi implementare istruzioni match annidate.

Expected Output:

Digita il nome di un animale: leone
Digita l'habitat in cui vive l'animale leone: terra
Output:
Leone appartiene alla categoria dei Mammiferi!
L'animale leone è uno dei mammiferi che può vivere sulla terra!

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digita il nome di un animale: balena
Digita l'habitat in cui vive l'animale balena: acqua
Output:
Balena appartiene alla categoria dei Mammiferi!
L'animale balena è uno dei mammiferi che può vivere in acqua!

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digita il nome di un animale: delfino
Digita l'habitat in cui vive l'animale delfino: terra
Output:
Delfino appartiene alla categoria dei Mammiferi!
Non ho mai visto l'animale delfino vivere nell'habitat terra.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digita il nome di un animale: drago
Digita l'habitat in cui vive l'animale drago: aria
Output:
Non so dire in quale categoria classificare l'animale drago!
Non sono in grado di fornire informazioni sull'habitat aria.
'''

mammiferi:list = ["cane", "gatto", "cavallo", "elefante", "leone", "balena", "delfino"]
rettili:list = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli:list = ["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"] 
pesci:list = ["squalo", "trota", "salmone", "carpa"]



animals: dict = {"animale": "", "animal type": "", "habitat": ""}

animale: str = str(input("digita il nome di un animale: ")).lower()
habitat: str = str(input("inserisci l'habitat dell'animale: ")).lower()



match animale:
    case animale if animale in mammiferi:
        if animale != "balena" or "delfino" and habitat == "terra":
            animals.update({"animale": animale, "animal type": "mammifero", "habitat" : {habitat}})
            print("escluso delfino e balena sono tutti mammiferi di terra")
        elif animale == "balena" or "delfino" and habitat == "acqua":
            animals.update({"animale": animale, "animal type": "mammifero", "habitat" : {habitat}})
            print("Delfino e balena vanno in acqua come mammiferi")
    case animale if animale in rettili: 
        if habitat != "aria":
            animals.update({"animale": animale, "animal type": "rettile", "habitat" : {habitat}})
            print("I rettili in questione possono essere sia di terra che acqua")
    case animale if animale in uccelli:
        if animale == "cigno" or "anatra" or "gallina" or "tacchino" and habitat == "acqua":
            animals.update({"animale": animale, "animal type": "uccello", "habitat" : {habitat}})
            print("L'uccello in questione NON può volare")
        elif animale == "aquila" or "pappagallo" or "gufo" or "falco" and habitat == "aria":
                animals.update({"animale": animale, "animal type": "uccello", "habitat" : {habitat}})
                print("L'uccello in questione può volare")
    case animale if animale in pesci:
        if habitat == "acqua":
            animals.update({"animale": animale, "animal type": "uccello di terra", "habitat" : {habitat}})
        else:
            animals.update({"animale": animale, "animal type": "uccello di terra", "habitat" : {habitat}})
            print("il pesce in questione non è nel suo habitat")



for key, value in animals.items():
    print(key, value)


'''habitats:list = ["acqua", "aria", "terra"]
animale: str = str(input("digita il nome di un animale: ")).lower()
match animale:
    case animale if animale in mammiferi:
        print(f"{animale} appartiene alla categoria mammiferi!")
    case animale if animale in rettili:
        print(f"{animale} appartiene alla categoria rettili!")
    case animale if animale in uccelli:
        print(f"{animale} appartiene alla categoria uccelli!")
    case animale if animale in pesci:
        print(f"{animale} appartiene alla categoria pesci!")
    case _:
        print(f"Non so dire in quale categoria classificare l'animale {animale}")'''