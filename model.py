#components - dictionary 
prsno_noge_na_suhem = {
    "-udarci na suhem sede po fazah [pozornost: nastavek stopal, vidne faze, kolena dovolj ozko, po koncu faza drsenja]" : ["10 udarcev, vodeno (z modeliranjem) nato samostojno", "15 udarcev, s stetjem po fazah"],
    "-udarci leze na trebuhu - klopca/opora (modeliranje) [pozornost: nastavek stopal, simetricno, kolena dovolj ozko, drsenje po koncu faze drsenja]": ["10 udarcev, vodeno (z modeliranjem) nato samostojno", "15 udarcev, s stetjem po fazah"]
}
prsno_noge_na_robu = {
    "-udarci ob robu bazena na hrbtu (sede) [pozornost: nastavek stopal, kolena dovolj ozko]": ["10 udarcev, vodeno (z modeliranjem) nato samostojno", "15 udarcev, s stetjem po fazah"],
    "-udarci ob robu bazena na trebuhu (leze) [pozornost: nastavek stopal, kolena ne vlecemo pregloboko pod telo, stopala v vodi]" : ["10 udarcev, vodeno (z modeliranjem) nato samostojno", "15 udarcev, s stetjem po fazah"]
}
prsno_noge_easy = {
    "-udarci ob robu - opora (leze, roke na robu telo v legi za prsno) [pozornost: nastavek stopal - v vodi, dolgo drsenje z iztegnjenima nogama in s petama skupaj po zaključku udarca]":["10 udarcev, vodeno (z modeliranjem) nato samostojno","5 udarcev, z modeliranjem po potrebi"],
    "-udarci prsno s oporo v paru (drzijo se za obrocek) [pozornost: pozicija telesa, nastavek stopal, kolena ne vlecemo prevec pod telo]" : ["2 dolzine - menjava v paru na polovici dolzine", "2*2 dolzine - menjava na polovici dolzine v paru"]
}
prsno_noge_OP = {
    "-odriv od stene v OP + 1 udarec prsno noge [pozornost: pozicija telesa - glava v vodi, boki visoko, udarec mocan z vidnimi fazami, sledi drsenje]" : ["5 ponovitev za vsakega - po potrebi z modeliranjem", "vsaj 3 ponovitve za vsakega"],
    "-odriv od stene v OP + 2/3 udarci prsno noge [pozornost: pozicija telesa - glava v vodi, udarec simeticen in mocen,  po vsakem udarcu sledi drsenje]" : ["5 ponovitev za vsakega - po potrebi z modeliranjem", "vsaj 3 ponovitve za vsakega"],
    "-odriv od stene v OP + vdih + 1/2 udarca prsno noge [pozornost: pozicija telesa - glava v vodi do hitrega vdiha, lega se po vdihu ne podre, boki visoko, udarec mocan z vidnimi fazami, ustrezen nastavek]" : ["5 ponovitev za vsakega - po potrebi z modeliranjem", "vsaj 3 ponovitve za vsakega"]
}
prsno_noge_medium = {
    "-delfincki + prsno noge - 1/2 udarca [pozornost: mocen udarec z ustreznim nastavkom, pogled v tla]" : ["2 dolzini", "4 dolzine", "6 dolzin"],
    "-prsno noge z dilco - dihanje po potrebi [pozornost: pozicija telesa, ustrezno dolga faza drsenja, glava v vodi]" : ["2 dolzini", "4 dolzine", "6 dolzin"],
    "-prsno noge z dilco - dihanje na 2/3 udarce [pozornost: med vdihom se pozicija telesa ne podre, ustrezen nastavek, kolena ne pregloboko pod trup]" : ["2 dolzini", "4 dolzine", "6 dolzin"]
}
prsno_noge_hard = {
    "-prsno noge z dilco - vdih na vsak udarec [pozornost: hitrev vdih, stabilno, udarce moc en z ustreznim nastavkom in fazo drsenja]": ["2*2 dolzini", "4 dolzine", "3*2 dolzini", "6 dolzin"],
    "-prsno noge v OP - vdih na 2/3 udarce [pozornost: vdih ne porusi lege telesa - hiter, udarec mocen, kolena dovolj ozko, drsenje po vsakem udarcu]" : ["2*2 dolzini", "4 dolzine", "3*2 dolzini", "6 dolzin"],
    "-prsno udarci priroceno na hrbtu- z dilco (objamejo) [pozornost: kolena v vodi, dovolj ozko, udarec mocen, boki visoko]" : ["2 dolzini", "2*2 dolzini", "4 dolzine"],
    "-prsno udarci + bananice [pozornost: boki visoko po, udarec z ustreznim nastavkom in fazo drsenja, kolena v vodi]" : ["2 dolzini", "2*2 dolzini"],
    "-prsno noge na hrbtu [pozornost: boki visoko, kolena v vodi, dovolj ozko, mocen udarec]" : ["2 dolzini", "2*2 dolzini", "4 dolzine", "3*2 dolzine"]
}
#list of components
prsno_noge = [
    prsno_noge_na_suhem, 
    prsno_noge_na_robu, 
    prsno_noge_easy, 
    prsno_noge_OP, 
    prsno_noge_medium, 
    prsno_noge_hard
    ]
#------------------------------
#components - dictionary
prsno_roke_na_suhem = {
    "-zaveslaj na suhem z modeliranjem [pozornost: roke in glava hkrati, ustrezna dolzina zaveslaja, drsenje ob koncu, pospesevanje zaveslaja]" : ["7 zaveslajev, vodeno (z modeliranjem) nato samostojno", "5 - 7 zaveslajev na posameznika"],
    "-zaveslaj na suhem leze (na klopci/opori) [pozornost: zajemanje vode z dlanmi, roke in glava hkrati, ustrezna dolzina zaveslaja]" : ["7 zaveslajev, vodeno (z modeliranjem) nato samostojno", "5 - 7 zaveslajev na posameznika"]
}
prsno_roke_plitvina = {
    "-zaveslaj v plitvini stoje [pozornost: dolzina zaveslaja, hkrati zacneta glava in roke, pozicija glave pred zacetkom in po koncu zaveslaja med rokami - pogled v tla]" : ["skupinsko 5 - 7 ustreznim ponovitev na posameznika", "7 zaveslajev, vodeno"],
    "-prsno zaveslaj leze ob robu bazena - sprednji del telesa v vodi [pozornost: dolzina zavesalaja, drsenje po koncu zaveslaja, pozicija glave ustrezna]" : ["skupinsko 5 - 7 ustreznim ponovitev na posameznika", "7 zaveslajev, vodeno"]
}
prsno_roke_premikanje = {
    "-prsno zaveslaj v plitvini s hojo [pozornost: koordinacija roke-glava, sirina zaveslaja]" : ["2 dolzini", "2*2 dolzini", "4 dolzine"],
    "-prsno zaveslaj v plitvini v paru - v paru se drzijo za noge [pozornost: pozicija telesa, ter glave med in po zaveslaju]" : ["2 dolzini - menjajo na dolzino", "2*2 dolzini - menjajo na dolzino", "4 dolzine - menjajo na 2 dolzini"],
    "-prsno zaveslaj po odrivu od stene v OP (po potrebi lahko dodajo kravl noge) [pozornost: drsenje po in pred zaveslajem - zaveslaj ne porusi pozicije telesa]" : ["5 ponovitev za vsakega - po potrebi z modeliranjem", "vsaj 3 ponovitve za vsakega"]
}
prsno_roke_vkljucevanje = {
    "-kratek prsno zaveslaj + kravl noge [pozornost: kratek zaveslaj, hitro]" : ["2 dolzini", "2*2 dolzini", "4 dolzine", "3*2 dolzini"],
    "-prsno zaveslaj + kravl noge stopnjevanje zaveslaja (ozek, normalen, sirok) [pozornost: sirina zaveslaja, pospesevanje zaveslaja proti koncu]" :  ["2*2 dolzini", "4 dolzine", "3*2 dolzini"],
    "-prsno zaveslaj + prsno noge - kot oblika dihanja (po potrebi na vec udarce) [pozornost: lega telesa, hiter, dovolj majhen krog zaveslaja]" : ["2*2 dolzini", "4 dolzine", "3*2 dolzini"]
}
#list of components
prsno_roke = [
    prsno_roke_na_suhem, 
    prsno_roke_plitvina, 
    prsno_roke_premikanje, 
    prsno_roke_vkljucevanje
    ]
#------------------------------
#components - dictionary
prsno_osnove = {
    "-prsno 1+3 [pozornost: kratek zaveslaj, ustrezna koordinacija roke/glava - noge, udarec mocen, ucinkovit, faza drsenja]" : ["2 dolzini", "2*2 dolzini", "4 dolzine", "3*2 dolzini"],
    "-prsno 1+2 [pozornost: udarca mocna, po vsakem faza drsenja, po zaveslaju lega se vedno stabilna]" : ["2*2 dolzini", "4 dolzine", "3*2 dolzini"],
    "-prsno 1+1 [pozornost: udarec z ustreznim nastavkom, mocan, zaveslaj kratek s pospesevanjem, pozicija telesa stabilna]" : ["2*2 dolzini", "4 dolzine", "3*2 dolzini"]
}
prsno_utrjevanje = {
    "-prsno z poudarjenim drsenjem [pozornost: 3s po udarcu, boki ne padajo, zacetek naslednjega zaveslaja koroke in glava prebijeta gladino - brez potapljanja]" : ["2*2 dolzini", "4 dolzine", "3*2 dolzini", "6 dolzin", "4*2 dolzini"],
    "-prsno cela tehnika [pozornost: koordinacija roke/glava - noge]" : ["2*2 dolzini", "4 dolzine", "3*2 dolzini", "6 dolzin", "4*2 dolzini"],
    "-prsno vaje : menjajo na dolzino: 1+3, 1+2, 1+1, prsno drsenje [pozornost: mocni udarci z vidnim nastavkom]" : ["4 dolzine", "8 dolzin"]
}
#list of components
prsno_koordinacija = [
    prsno_osnove, 
    prsno_utrjevanje
    ]
#------------------------------
#list of lists of components
prsno_vaje = [
    prsno_noge, 
    prsno_roke, 
    prsno_koordinacija
]
#------------------------------------------------------------------------------------------------------------------
def random_from_component(component, n):
    if n < 0 or n > len(list(component.keys())):
        return "IZBOR NI MOZEN - ZAHTEVAL SI PREVELIKO STEVILO VAJ IZ NEKEGA SKLOPA"
    elif n == 0:
        return []
    else:
        import random
        lst = []
        component_copy = component.copy()
        for i in range(n):
            el_all = {}
            el = random.choice(list(component_copy.keys()))
            el_repeat = random.choice(component_copy[el])
            el_all[el] = el_repeat
            del component_copy[el]
            lst.append(el_all)
            i = i + 1
        return lst

def component_exercises(component):
    return len(list(component.keys()))

def selection_to_random_component(lst, list_of_components):
    if len(lst) != len(list_of_components):
        return "IZBOR VAJ NI USTREZEN"
    else:
        selection = []
        for i in range(len(lst)):
            data = lst[i]
            lst_of_data = random_from_component(list_of_components[i], data)
            for j in range(len(lst_of_data)):
                selection.append(lst_of_data[j])
        return selection

def split_int_to_list(number):
    [int(i) for i in str(number)]
    
class Priprava:
    def __init__(self, prilagajanje = {}, prsno = {}, kravl = {}, hrbtno = {}, konec_ure = "igra"):
        self.prilagajanje = prilagajanje
        self.prsno = prsno
        self.kravl = kravl
        self.hrbtno = hrbtno
        self.konec_ure = konec_ure

#    def v_slovar(self):
#        return {
#            "PRILAGAJANJE": self.prilagajanje, 
#            "PRSNO VAJE": self.prsno, 
#            "KRAVL VAJE": self.kravl, 
#            "HRBTNO VAJE": self.hrbtno
#            }
#
# random_from_component(prsno_noge_na_suhem,1)
# selection_to_random_component([1,1,1,1,1,1], prsno_noge)