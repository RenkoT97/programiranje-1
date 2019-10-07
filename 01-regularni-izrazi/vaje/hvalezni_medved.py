###############################################################################
# Hvaležni medved
#
# Pri tej nalogi bomo napisali nekaj funkcij, ki nam bodo v pomoč pri analizi
# literarnih besedil, kot je na primer koroška narodna pripovedka *Hvaležni
# medved*.
###############################################################################

test_text = """Gori nekje v gorah, ne ve se več, ali je bilo pri Macigoju ali
Naravniku, je šivala gospodinja v senci pod drevesom in zibala otroka. Naenkrat
prilomasti - pa prej ni ničesar opazila - medved in ji moli taco, v kateri je
tičal velik, debel trn. Žena se je prestrašila, a medved le milo in pohlevno
godrnja. Zato se žena ojunači in mu izdere trn iz tace. Mrcina kosmata pa zvrne
zibel, jo pobaše in oddide. Čez nekaj časa pa ji zopet prinese zibel, a zvhano
napolnjeno s sladkimi hruškami . Postavil jo je na tla pred začudeno mater in
odracal nazaj v goščavo. "Poglej no", se je razveselila mati, "kakšen hvaležen
medved. Zvrhano zibelko sladkih hrušk mi je prinesel za en sam izdrt trn"."""

###############################################################################
# 1) Sestavite funkcijo [find_words], ki vrne množico vseh besed, ki se
#    pojavijo v nizu in vsebujejo dan podniz.
#
# Namig: Pomagajte si z regex znakom za mejo [\b].
#
# >>> find_words(test_text, 'de')
# {'izdere', 'debel', 'oddide', 'začudeno'}
###############################################################################
def find_words(niz, podniz):
    sez = []
    for beseda in niz.split():
        if podniz in beseda:
            sez.append(beseda)
    return sez

###############################################################################
# 2) Sestavite funkcijo [find_prefix], ki vrne množico vseh besed, ki se
#    pojavijo v nizu in imajo dano predpono.
#
# >>> find_prefix(test_text, 'zi')
# {'zibala', 'zibel', 'zibelko'}
###############################################################################
import re

def find_prefix(niz, predpona):
    rgx = re.compile(fr"\b({predpona}\w*)")
    return list(set(map(
        lambda m: m.group(1),
        rgx.finditer(niz)
    )))

###############################################################################
# 3) Sestavite funkcijo [find_suffix], ki vrne množico vseh besed, ki se
#    pojavijo v nizu in imajo dano pripono.
#
# >>> find_suffix(test_text, 'la')
# {'zibala', 'razveselila', 'prestrašila', 'šivala', 'opazila', 'tla'}
###############################################################################
def find_suffix(niz, pripona):
    l = []
    sez = re.findall(f"\w*{pripona}\b", niz)
    for i in range(len(sez)):
        for j in range(i+1,len(sez)):
            if sez[i] == sez[j]:
                l.append(j)
    for element in l:
        sez[element] = ""
    if sez[element] == "":
        del sez[element]
    return sez

###############################################################################
# 4) Sestavite funkcijo [double_letters], ki sprejme niz in vrne množico vseh
#    besed, ki vsebujejo podvojene črke.
#
# >>> double_letters('A volunteer is worth twenty pressed men.')
# {'volunteer', 'pressed'}
###############################################################################
'''
def double_letter(niz):
    s = []
    for a in "abcdefghijklmnoprstuvzqwxy":
        rgx = re.compile(\w*a{2}\w*)
        a = re.findall(rgx, niz)
        for element in a:
            s.append(element)
    return s
'''

def double_letters(niz):
    vzorec = r"\w*(\w)\1\w*"
    return [m.group(0) for m in re.finditer(vzorec,niz)]
