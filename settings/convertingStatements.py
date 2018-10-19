# few_statements = """1
# Een opleiding in de buurt van mijn woonplaats
# 2
# Diversiteit in dagelijkse werkzaamheden
# 3
# Werk waarin ik mijn creativiteit kwijt kan"""

helpStrB1 = "<statement id = \""
helpStrB2 = "\">"
helpStrE = ".</statement>"
buildStr = """ """
stNr = 0
lCharBool = False
skipping = False

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

for i in range(len(allStatements)):
    if skipping:
        skipping = False
        continue
    #next
    if lCharBool == True:
        curChar = " "
        lCharBool = False
    else:
        curChar = allStatements[i]
    #next
    if is_number(curChar):
        stNr  = curChar
        if is_number(allStatements[i+1]):
            stNr += allStatements[i+1]
            skipping = True
        #next
        plaksel = helpStrB1
        #import pdb; pdb.set_trace()
        plaksel += stNr
        plaksel += helpStrB2
        lCharBool = True
    elif curChar == "\n":
        plaksel = helpStrE + "\n"
    else:
        plaksel = curChar
    #next
    buildStr += plaksel



allStatements = """1
Een opleiding in de buurt van mijn woonplaats
2
Diversiteit in dagelijkse werkzaamheden
3
Werk waarin ik mijn creativiteit kwijt kan
4
Werk dat voornamelijk bestaat uit klinisch beredeneren
5
Het ervaren van de dankbaarheid van mijn patiënten
6
Werk dat ik mentaal aan kan
7
Werk met maatschappelijk impact
8
Een holistische benadering van patiënten
9
De mogelijkheid ook management taken op je te nemen
10
Werk waarin ik innovatief bezig kan zijn
11
Werken in een academische setting
12
De tijd en inspanning benodigd om een opleidingsplaats te bemachtigen
13
De mogelijkheid het beter te kunnen doen dan mijn peers
14
Maatschappelijke erkenning voor mijn werk krijgen
15
De mogelijkheid onderwijs te gaan geven
16
Merken dat het leven van mijn patiënten verandert door mijn handelen
17
Baanzekerheid
18
Focus op één orgaan(system)
19
Werken in een multidisciplinair team
20
Langdurige patiëntrelaties
21
Een hoge (hiërarchische) positie verwerven
22
De werkomgeving (bijvoorbeeld in of buiten het ziekenhuis)
23
Werk dat socio- psychologische aspecten omvat
24
Werken met een diverse patiënten samenstelling
25
Werken met een specifiek spectrum van ziektes

26
Werk voornamelijk bestaande uit praktische vaardigheden
27
Een hoog inkomen hebben
28
Passend bij mijn toekomstige privé leven
29
Werken met gelijkgezinden
30
Werken met multi-morbiditeit
31
De mening van mijn peers
32
Werk met de nieuwste technische apparaten
33
Een rolmodel in een specifieke specialisme
34
Werk zonder oproepdiensten
35
Een kortdurende opleiding
36
Focus op ondersteunen/ begeleiden van chronisch zieken
37
Focus op preventieve medische zorg
38
De goedkeuring van mijn ouders
39
De mogelijkheid om parttime te werken
40
Werk hebben dat mensen bewonderen
41
Werk dat me in staat stelt mijn studielening snel af te lossen
42
Patiënten te kunnen genezen
43
Opwindend werk met actie
44
Mogelijkheden tot levenslang leren
45
Een te behappen hoeveelheid werk
46
Werk dat ik fysiek aan kan
47
Een subspecialist zijn
48
Werk dat het nemen van risico’s omvat

49
Werk dat het respect van mijn naasten oplevert
50
Werken in een prestigieus specialisme
51
Mijn roeping volgen
52
Werk waarin ik autonoom medische beslissingen kan nemen
53
Mijn eerdere ervaring in een specialisme
54
Carrière perspectieven
55
Mogelijkheden om ook onderzoek te doen
56
De administratieve belasting
57
Werk dat op mijn kwaliteiten aansluit
58
Erkenning krijgen voor mijn excellente werk
59
Trots kunnen zijn op mijn carrière
60
De vrijheid hebben om mijn werk zelf te organiseren
61
Veel routine in het werk
62
Dagelijks contact met patiënten"""
