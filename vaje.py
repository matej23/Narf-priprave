import model

prsno_noge_na_suhem = model.NivoOdsekaTehnike(
    [
        model.Vaja("-prsno udarci na suhem sede po fazah", ["nastavek stopal, vidne faze, kolena dovolj ozko, po koncu faza drsenja"], ["10 udarcev, vodeno (z modeliranjem) nato samostojno", "15 udarcev, s stetjem po fazah"]),
        model.Vaja("-prsno udarci leze na trebuhu - klopca/opora (modeliranje)", ["nastavek stopal, simetricno, kolena dovolj ozko, drsenje po koncu faze drsenja"], ["10 udarcev, vodeno (z modeliranjem) nato samostojno", "15 udarcev, s stetjem po fazah"])
    ],
    "prsno noge na suhem"
)
prsno_noge_na_robu = model.NivoOdsekaTehnike(
    [
        model.Vaja("-prsno udarci ob robu bazena na hrbtu (sede)", ["nastavek stopal, kolena dovolj ozko"],["10 udarcev, vodeno (z modeliranjem) nato samostojno", "15 udarcev, s stetjem po fazah"]),
        model.Vaja("-prsno udarci ob robu bazena na trebuhu (leze)", ["nastavek stopal, kolena ne vlecemo pregloboko pod telo, stopala v vodi"], ["10 udarcev, vodeno (z modeliranjem) nato samostojno", "15 udarcev, s stetjem po fazah"])
    ],
    "prsno noge na robu"
)
prsno_noge_easy = model.NivoOdsekaTehnike(
    [
        model.Vaja("-prsno udarci ob robu - opora (leze, roke na robu telo v legi za prsno)", ["nastavek stopal - v vodi, dolgo drsenje z iztegnjenima nogama in s petama skupaj po zakljucku udarca"], ["10 udarcev, vodeno (z modeliranjem) nato samostojno", "5 udarcev, z modeliranjem po potrebi"]),
        model.Vaja("-prsno udarci prsno s oporo v paru (drzijo se za obrocek)", ["pozicija telesa, nastavek stopal, kolena ne vlecemo prevec pod telo"], ["2 dolzine - menjava v paru na polovici dolzine", "2*2 dolzine - menjava na polovici dolzine v paru"])
    ],
    "prsno noge easy"
)
prsno_noge_OP = model.NivoOdsekaTehnike(
    [
        model.Vaja("-odriv od stene v OP + 1 udarec prsno noge)", ["pozicija telesa - glava v vodi, boki visoko, udarec mocan z vidnimi fazami, sledi drsenje"], ["5 ponovitev za vsakega - po potrebi z modeliranjem", "vsaj 3 ponovitve za vsakega"]),
        model.Vaja("-odriv od stene v OP + 2/3 udarci prsno noge", ["pozicija telesa - glava v vodi, udarec simeticen in mocen,  po vsakem udarcu sledi drsenje"], ["5 ponovitev za vsakega - po potrebi z modeliranjem", "vsaj 3 ponovitve za vsakega"]),
        model.Vaja("-odriv od stene v OP + vdih + 1/2 udarca prsno noge", ["pozicija telesa - glava v vodi do hitrega vdiha, lega se po vdihu ne podre, boki visoko, udarec mocan z vidnimi fazami, ustrezen nastavek"], ["5 ponovitev za vsakega - po potrebi z modeliranjem", "vsaj 3 ponovitve za vsakega"])
    ],
    "prsno noge v OP"
)
prsno_noge_medium = model.NivoOdsekaTehnike(
    [
        model.Vaja("-delfincki + prsno noge - 1/2 udarca", ["mocen udarec z ustreznim nastavkom, pogled v tla"], ["2 dolzini", "4 dolzine", "6 dolzin"]),
        model.Vaja("-prsno noge z dilco - dihanje po potrebi", ["pozicija telesa, ustrezno dolga faza drsenja, glava v vodi"], ["2 dolzini", "4 dolzine", "6 dolzin"]),
        model.Vaja("-prsno noge z dilco - dihanje na 2/3 udarce", ["med vdihom se pozicija telesa ne podre, ustrezen nastavek, kolena ne pregloboko pod trup"], ["2 dolzini", "4 dolzine", "6 dolzin"])
    ],
    "prsno noge medium"
)
prsno_noge_hard = model.NivoOdsekaTehnike(
    [
        model.Vaja("-prsno noge z dilco - vdih na vsak udarec", ["hiter vdih, stabilno, udarec mocen z ustreznim nastavkom in fazo drsenja"], ["2*2 dolzini", "4 dolzine", "3*2 dolzini", "6 dolzin"]),
        model.Vaja("-prsno noge v OP - vdih na 2/3 udarce", ["vdih ne porusi lege telesa - hiter, udarec mocen, kolena dovolj ozko, drsenje po vsakem udarcu"], ["2*2 dolzini", "4 dolzine", "3*2 dolzini", "6 dolzin"]),
        model.Vaja("-prsno udarci priroceno na hrbtu - z dilco (objamejo)", ["kolena v vodi, dovolj ozko, udarec mocen, boki visoko"], ["2 dolzini", "2*2 dolzini", "4 dolzine"]),
        model.Vaja("-prsno udarci + bananice", ["boki visoko po, udarec z ustreznim nastavkom in fazo drsenja, kolena v vodi"], ["2 dolzini", "2*2 dolzini"]),
        model.Vaja("-prsno noge na hrbtu", ["boki visoko, kolena v vodi, dovolj ozko, mocen udarec"], ["2 dolzini", "2*2 dolzini", "4 dolzine", "3*2 dolzine"])
    ],
    "prsno noge hard"
)

prsno_noge = model.OdsekTehnike(
    [
        prsno_noge_na_suhem,
        prsno_noge_na_robu,
        prsno_noge_easy,
        prsno_noge_OP,
        prsno_noge_medium,
        prsno_noge_hard
    ],
    "prsno noge"
)
# ------------------------------
prsno_roke_na_suhem = model.NivoOdsekaTehnike(
    [
        model.Vaja( "-zaveslaj na suhem z modeliranjem", ["roke in glava hkrati, ustrezna dolzina zaveslaja, drsenje ob koncu, pospesevanje zaveslaja"], ["7 zaveslajev, vodeno (z modeliranjem) nato samostojno", "5 - 7 zaveslajev na posameznika"]),
        model.Vaja("-zaveslaj na suhem leze (na klopci/opori)", ["zajemanje vode z dlanmi, roke in glava hkrati, ustrezna dolzina zaveslaja"], ["7 zaveslajev, vodeno (z modeliranjem) nato samostojno", "5 - 7 zaveslajev na posameznika"])
    ],
    "prsno roke na suhem"
)
prsno_roke_plitvina = model.NivoOdsekaTehnike(
    [
        model.Vaja("-zaveslaj v plitvini stoje", ["dolzina zaveslaja, hkrati zacneta glava in roke, pozicija glave pred zacetkom in po koncu zaveslaja med rokami - pogled v tla"], ["skupinsko 5 - 7 ustreznim ponovitev na posameznika", "7 zaveslajev, vodeno"]),
        model.Vaja("-prsno zaveslaj leze ob robu bazena - sprednji del telesa v vodi", ["dolzina zavesalaja, drsenje po koncu zaveslaja, pozicija glave ustrezna"], ["skupinsko 5 - 7 ustreznim ponovitev na posameznika", "7 zaveslajev, vodeno"])
    ],
    "prsno roke plitvina"
)
prsno_roke_premikanje = model.NivoOdsekaTehnike(
    [
        model.Vaja("-prsno zaveslaj v plitvini s hojo", ["koordinacija roke-glava, sirina zaveslaja"], ["2 dolzini", "2*2 dolzini", "4 dolzine"]),
        model.Vaja("-prsno zaveslaj v plitvini v paru - v paru se drzijo za noge", ["pozicija telesa, ter glave med in po zaveslaju"], ["2 dolzini - menjajo na dolzino", "2*2 dolzini - menjajo na dolzino", "4 dolzine - menjajo na 2 dolzini"]),
        model.Vaja("-prsno zaveslaj po odrivu od stene v OP (po potrebi lahko dodajo kravl noge)", ["drsenje po in pred zaveslajem - zaveslaj ne porusi pozicije telesa"], ["5 ponovitev za vsakega - po potrebi z modeliranjem", "vsaj 3 ponovitve za vsakega"])
    ],
    "prsno roke premikanje"
)
prsno_roke_vkljucevanje = model.NivoOdsekaTehnike(
    [
        model.Vaja("-kratek prsno zaveslaj + kravl noge", ["kratek zaveslaj, hitro"], ["2 dolzini", "2*2 dolzini", "4 dolzine", "3*2 dolzini"]),
        model.Vaja("-prsno zaveslaj + kravl noge stopnjevanje zaveslaja (ozek, normalen, sirok)", ["sirina zaveslaja, pospesevanje zaveslaja proti koncu"], ["2*2 dolzini", "4 dolzine", "3*2 dolzini"]),
        model.Vaja("-prsno zaveslaj + prsno noge - kot oblika dihanja (po potrebi na vec udarce)", ["lega telesa, hiter, dovolj majhen krog zaveslaja"], ["2*2 dolzini", "4 dolzine", "3*2 dolzini"])
    ],
    "prsno roke vkljucevanje"
)

prsno_roke = model.OdsekTehnike(
    [
        prsno_roke_na_suhem,
        prsno_roke_plitvina,
        prsno_roke_premikanje,
        prsno_roke_vkljucevanje
    ],
    "prsno roke"
)
# ------------------------------
prsno_osnove = model.NivoOdsekaTehnike(
    [
        model.Vaja("-prsno 1+3", ["kratek zaveslaj, ustrezna koordinacija roke/glava - noge, udarec mocen, ucinkovit, faza drsenja"], ["2 dolzini", "2*2 dolzini", "4 dolzine", "3*2 dolzini"]),
        model.Vaja("-prsno 1+2", ["udarca mocna, po vsakem faza drsenja, po zaveslaju lega se vedno stabilna"], ["2*2 dolzini", "4 dolzine", "3*2 dolzini"]),
        model.Vaja("-prsno 1+1", ["udarec z ustreznim nastavkom, mocan, zaveslaj kratek s pospesevanjem, pozicija telesa stabilna"], ["2*2 dolzini", "4 dolzine", "3*2 dolzini"])
    ],
    "prsno osnove"
)
prsno_utrjevanje = model.NivoOdsekaTehnike(
    [
        model.Vaja("-prsno z poudarjenim drsenjem", ["3s po udarcu, boki ne padajo, zacetek naslednjega zaveslaja koroke in glava prebijeta gladino - brez potapljanja"], ["2*2 dolzini", "4 dolzine", "3*2 dolzini", "6 dolzin", "4*2 dolzini"]),
        model.Vaja("-prsno cela tehnika", ["koordinacija roke/glava - noge"], ["2*2 dolzini", "4 dolzine", "3*2 dolzini", "6 dolzin", "4*2 dolzini"]),
        model.Vaja("-prsno vaje : menjajo na dolzino: 1+3, 1+2, 1+1, prsno drsenje", ["mocni udarci z vidnim nastavkom"], ["4 dolzine", "8 dolzin"])
    ],
    "prsno utrjevanje"
)

prsno_koordinacija = model.OdsekTehnike(
    [
        prsno_osnove,
        prsno_utrjevanje
    ],
    "prsno koordinacija"
)
# ------------------------------
prsno = model.Tehnika(
    [
        prsno_noge,
        prsno_roke,
        prsno_koordinacija
    ],
    "prsno"
)
# ------------------------------------------------------------------------------------------------------------------
kravl_noge_na_suhem = model.NivoOdsekaTehnike(
    [
        model.Vaja("-kravl udarci na suhem sede - najprej pocasi, nato hitro", ["spicke, ni krcenja kolen, enakomerno po amplitudi"], ["10s s stetjem", "10 - 15s"]),
        model.Vaja("-kravl udarci na suhem - enakomerna frekvenca in amplituda", ["iztgenjenost nog, brez krcenja v kolenih, spicke"], ["10s s stetjem", "10 - 15s"])
    ],
    "kravl noge na suhem"
)
kravl_noge_na_robu = model.NivoOdsekaTehnike(
    [
        model.Vaja("-kravl udarci ob robu bazena na hrbtu (sede)", ["enakomerno po frekvenci in amplitudi, spicke"], ["10s s stetjem", "10 - 15s"]),
        model.Vaja("-kravl udarci ob robu bazena na trebuhu (leze)", ["enakomerno, stopala ne prihajajo prevec iz vode, ni krcenja kolen"], ["10s s stetjem", "10 - 15s"]),
        model.Vaja("-kravl udarci ob robu/opora (leze, roke na robu/na opori telo v legi za kravl)", ["lega telesa - glava v vodi, udarci enakomerni, spicke"], ["2*10s, vodeno nato samostojno", "15s, z modeliranjem po potrebi"])
    ],
    "kravl noge na robu"
)
kravl_noge_OP_gibljivo_easy = model.NivoOdsekaTehnike(
    [
        model.Vaja("-odriv od stene v OP + 3s kravl noge", ["pozicija telesa - glava v vodi, boki visoko, udarci enakomerni in tehnicno ustrezni"], ["5 ponovitev za vsakega - po potrebi z modeliranjem", "vsaj 3 ponovitve za vsakega"]),
        model.Vaja("-odriv od stene v OP + vsaj 3-5m kravl noge (max dolzina)", ["pozicija telesa - glava v vodi, roke iztegnjene v smeri gibanja, udarci vidni in enakomerni po amplitudi"], ["5 ponovitev za vsakega", "vsaj 3 ponovitve za vsakega, vedno dlje"]),
        model.Vaja("-odriv od stene v OP + 1/2 vdiha + 3s kravl noge", ["pozicija telesa - glava v vodi do hitrega vdiha, lega se po vdihu ne podre, boki visoko, udarci mocni vednar z ustrezno amplitudo in frekvenco"], ["5 ponovitev za vsakega", "vsaj 3 ponovitve za vsakega"]),
        model.Vaja("-vlecenje s crvom/desko + kravl noge", ["glava v vodi, udarci ustrezni - spicke, dovolj mocni, brez krcenja kolen"], ["2*1 dolzina", "2 dolzini"]),
        model.Vaja("-delfincki + kravl noge", ["pozicija glave - v vodi, roke iztgenjene, telo napeto, udarci ustrezni"], ["2 dolzini", "2*2 dolzini", "4 dolzine"])
    ],
    "kravl noge v OP/gibljivo/easy"
)
kravl_noge_medium = model.NivoOdsekaTehnike(
    [
        model.Vaja("-kravl noge z dilco - glava v vodi, dihanje po potrebi", ["boki visoko, vdih hiter, ne podre lege telesa, udarci ucinkoviti in ustrezno izvedeni"], ["2*2 dolzini", "4 dolzine", "3*2 dolzine"]),
        model.Vaja("-bananice + kravl/hrbtno noge", ["boki visoko, roke iztgenjene, udarci enakomerni in ucinkoviti - vsaj 2/3s"], ["2*2 dolzini", "4 dolzine", "3*2 dolzine"]),
        model.Vaja("-kravl/hrbtno noge na hrbtu z dilco (objamejo)", ["boki visoko, udarci ucinkoviti, ni prekomernega stopanja na tla"], ["2*2 dolzini", "4 dolzine"])
    ],
    "kravl noge medium"
)
kravl_noge_hard = model.NivoOdsekaTehnike(
    [
        model.Vaja("-kravl noge v OP - dihanje po potrebi", ["vdih hitre, ne podre lege telesa, udarci mocni in ucinkoviti"], ["2*2 dolzini", "4 dolzine", "3*2 dolzine"]),
        model.Vaja("-noge kravl/hrbtno - obracajo na 3s iz trebuha na hrbet in nazaj", ["udarci mocni, ucinkoviti in enakomerni, med obratom pozicija ostane dokaj stabilna"], ["2*2 dolzini", "2 dolzini"]),
        model.Vaja("-kravl noge na hrbtu/hrbtno noge (vzrocenje)", ["boki visoko, udarci enakomerni po amplitudi in frekvenci, telo napeto"], ["2*2 dolzini", "4 dolzine", "2 dolzini"])
    ],
    "kravl noge hard"
)

kravl_noge = model.OdsekTehnike(
    [
        kravl_noge_na_suhem,
        kravl_noge_na_robu,
        kravl_noge_OP_gibljivo_easy,
        kravl_noge_medium,
        kravl_noge_hard
    ],
    "kravl noge"
)
# ------------------------------
kravl_dihanje_na_suhem = model.NivoOdsekaTehnike(
    [
        model.Vaja("-kravl superman/dihanje na stran na suhem", ["glava lezi na roki, ni dviga glave, le obrat, nato vracanje v zacetno pozicijo"], ["7-10 ponovitev za posameznika, vodeno nato samostojno", "5-10 ponovitev, po potrebi z modeliranjem"]),
        model.Vaja("-kravl na boku, vdih na stran", ["roka iztegnjena nudi oporo, ni dvigovanja glave, le obrat"], ["7-10 ponovitev za posameznika, vodeno nato samostojno", "5-10 ponovitev, po potrebi z modeliranjem"])
    ],
    "kravl dihanje na suhem"
)
kravl_dihanje_easy = model.NivoOdsekaTehnike(
    [
        model.Vaja("-kravl ena roka na robu, druga ob telesu, dihanje na stran", ["vdih hiter, ni dviga glava od telesa, le obrat, glava po koncu v zacetno pozicijo"], ["7-10 ponovitev za posameznika, vodeno nato samostojno", "5-10 ponovitev, po potrebi z modeliranjem"]),
        model.Vaja("-kravl dihanje na stran v plitvini s hojo (ena roka v vzrocenju, ena ob telesu)", ["glava po hitrem vdihu brez dviga glave nazaj v zacetno pozicijo, obraz v vodi, pogled dol"], ["2 dolzini", "2*2 dolzini - po potrebi z modeliranjem", "4 dolzine - roko menjajo na dolzino"])
    ],
    "kravl dihanje easy"
) 
kravl_dihanje_medium = model.NivoOdsekaTehnike(
    [
        model.Vaja("-kravl dihanje na stran z dilco - vzrocena roka na dilci za oporo", ["ni dvigovanja glave ob vdihu na stran, udarci mocni in enakomerni"], ["2*2 dolzini - menjava roke na 2 dolzini", "4 dolzine - menjava roke na vsako dolzino", "3*2 dolzine - menjava roke na vsako dolzino"]),
        model.Vaja("-kravl dihanje z obratom na hrbet (prekomeren obrat v bolj stabilno lego)", ["pri vdihu/prehodu na hrbet in nazaj se lega bistveno ne podre, glava se od roke ne dviguje le obraca"], ["2*2 dolzini - menjava roke na 2 dolzini", "4 dolzine - menjava roke na vsako dolzino", "3*2 dolzine - menjava roke na vsako dolzino"])
    ],
    "kravl dihanje medium"
)
kravl_dihanje_hard = model.NivoOdsekaTehnike(
    [
        model.Vaja("-kravl superman", ["vdih hiter in ustrezno izveden, glava po vdihu nazaj v zacetno lego"], ["2*2 dolzini - menjava roke na 2 dolzini", "4 dolzine - menjava roke na vsako dolzino", "3*2 dolzine - menjava roke na vsako dolzino"]),
        model.Vaja("-kravl noge na boku z vdihom na stran", ["roka v vzorcenju iztegnjena in stabilna pred, med in po vdihu, udarci mocni in enakomerni"], ["2*2 dolzini - menjava roke na 2 dolzini", "4 dolzine - menjava roke na vsako dolzino", "3*2 dolzine - menjava roke na vsako dolzino"])
    ],
    "kravl dihanje hard"
)

kravl_dihanje = model.OdsekTehnike(
    [
        kravl_dihanje_na_suhem,
        kravl_dihanje_easy,
        kravl_dihanje_medium,
        kravl_dihanje_hard
    ],
    "kravl dihanje"
)
# ------------------------------
kravl_zaveslaj_na_suhem = model.NivoOdsekaTehnike(
    [
        model.Vaja("-kravl  zaveslaj z eno roko na suhem leze", ["roka pred zacetkom prenosa iztegnjena, vdih koordiniran ustrezno z zaveslajem, roka po koncu zaveslaja iztegnjena v zacetni legi, faza drsenja"], ["7-10 ponovitev za posamazenika - na zacetku z eno roko, nato izmenicno", "5-10 ponovitev, po potrebi z modeliranjem, nato samostojno"]),
        model.Vaja("-kravl  zaveslaj z eno roko na suhem v predklonu", ["roka v podvodnem delu iztegnjena, pred prenosom stegnjena, vdih ustrezno izveden, na koncu prvotna lega"], ["7-10 ponovitev za posamazenika - na zacetku z eno roko, nato izmenicno", "5-10 ponovitev, po potrebi z modeliranjem, nato samostojno"])
    ],
    "kravl zaveslaj na suhem"
)
kravl_zaveslaj_easy = model.NivoOdsekaTehnike(
    [
        model.Vaja("-kravl zaveslaj ob robu (roka ki ne dela zaveslaja caka na robu bazena)", ["pred prenosom roka iztegnjena, vidne faze, ni dviga glava od telesa, le obrat, ob zakljucku zacetna pozicija"], ["7-10 ponovitev za posameznika, vodeno nato samostojno", "5-10 ponovitev, po potrebi z modeliranjem"]),
        model.Vaja("-kravl zaveslaji v plitvini s hojo (na zacetku samo ena roka, nato ob ustrezni izvedbi tudi izmenicno)", ["pospesevanje zaveslaja proti koncu, sledi faza drsenja, glava se pri vdihu ne dviguje od telesa"], ["2 dolzini", "2*2 dolzini - po potrebi z modeliranjem", "4 dolzine - roko menjajo na dolzino"])
    ],
    "kravl zavesalj easy"
) 
kravl_zaveslaj_medium = model.NivoOdsekaTehnike(
    [
        model.Vaja("-kravl zaveslaji z dilco - roka, ki ne dela zaveslaja na dilci za oporo", ["zaveslaj ne podre lege telesa, ustrezno izveden z iztegnjeno roko, ni dvigovanja glave ob vdihu na stran, udarci mocni in enakomerni"], ["2*2 dolzini - menjava roke na 2 dolzini", "4 dolzine - menjava roke na vsako dolzino", "3*2 dolzine - menjava roke na vsako dolzino"]),
        model.Vaja("-kravl zaveslaji - z vmesnim stopanjem na tla ko plavalec ne uspe zadrzati stabilne pozicije", ["zaveslaj pretirano ne podre lege telesa, udarci ucinkoviti, ni dviga glave gor"], ["2*2 dolzini - menjava roke na 2 dolzini", "4 dolzine - menjava roke na vsako dolzino", "3*2 dolzine - menjava roke na vsako dolzino"])
    ],
    "kravl zaveslaj medium"
)
kravl_zaveslaj_hard = model.NivoOdsekaTehnike(
    [
        model.Vaja("-kravl zaveslaj (ena roka na dolzino)", ["lega telesa stabilna, vdih na stran ne gor, udarci enakomerni in mocni"], ["2*2 dolzini", "4 dolzine", " 3*2 dolzine", "6 dolzin"]),
        model.Vaja("-kravl zaveslaj 3 - 3", ["dihanje na obe roki stabilno z ustreznim vdihom na stran, roka, ki ne dela zaveslaja je iztegnjena"], ["2*2 dolzini", "4 dolzine", " 3*2 dolzine", "6 dolzin"]),
        model.Vaja("-kravl zaveslaj 2 - 2", ["dihanje na obe roki stabilno z ustreznim vdihom na stran, roka, ki ne dela zaveslaja je iztegnjena"], ["2*2 dolzini", "4 dolzine", " 3*2 dolzine", "6 dolzin"]),
        model.Vaja("-kravl zaveslaj 1 - 1 z dilco", ["med zaveslajema faza drsenja, vdih na stran in zaveslaj ne porusi lege telesa"], ["2*2 dolzini", "4 dolzine", " 3*2 dolzine", "6 dolzin"])
    ],
    "kravl zaveslaj hard"
)

kravl_zaveslaj = model.OdsekTehnike(
    [
        kravl_zaveslaj_na_suhem,
        kravl_zaveslaj_easy,
        kravl_zaveslaj_medium,
        kravl_zaveslaj_hard
    ],
    "kravl zaveslaj"
)
# ------------------------------
kravl_utrjevanje = model.NivoOdsekaTehnike(
    [
        model.Vaja("-kravl roka roko caka (dihanje na eno stran)", ["med zaveslajema kratla faza drsenja, ne hitijo, udarci mocni in enakomerni"], ["4 dolzine", "3*2 dolzine", "6 dolzin"]),
        model.Vaja("-kravl roka roko caka (dihanje na vsak zaveslaj)", ["stabilno, druga roka iztegnjena, viok tonus telesa, noge ucinkovite"], ["4 dolzine", "3*2 dolzine", "6 dolzin"]),
        model.Vaja("-kravl cela tehnika (lahko roka roko lovi)", ["zakljucek zaveslaja izrazit, roka po koncu zaveslaja iztegnjena, tonus telesa visok"], ["4 dolzine", "3*2 dolzine", "6 dolzin"])
    ],
    "kravl utrjevanje"
)

kravl_utrjevanje_cela_tehnika = model.OdsekTehnike(
    [
        kravl_utrjevanje
    ],
    "kravl utrjevanje cele tehnike"
)
# ------------------------------
kravl = model.Tehnika(
    [
        kravl_noge,
        kravl_dihanje,
        kravl_zaveslaj,
        kravl_utrjevanje_cela_tehnika
    ],
    "kravl"
)
# ------------------------------------------------------------------------------------------------------------------
hrbtno = model.Tehnika(
    [

    ],
    "hrbtno"
)
# ------------------------------------------------------------------------------------------------------------------
prilagajanje = model.Tehnika(
    [

    ],
    "prilagajanje na vodo"
)