import bottle
import model

PISKOTEK_UPORABNISKO_IME = "uporabnisko_ime"
SKRIVNOST = "skrivnost"


def shrani_stanje(uporabnik):
    uporabnik.v_datoteko()

def trenutni_uporabnik():
    uporabnisko_ime = bottle.request.get_cookie(
        PISKOTEK_UPORABNISKO_IME, secret=SKRIVNOST)
    if uporabnisko_ime:
        return model.Uporabnik.iz_datoteke(uporabnisko_ime)
    else:
        bottle.redirect("/prijava/")


@bottle.get("/prijava/")
def prijava_get():
    return bottle.template("prijava.html", napaka=None, x=1)


@bottle.post("/prijava/")
def prijava_post():
    uporabnisko_ime = bottle.request.forms.getunicode("uporabnisko_ime")
    geslo_v_cistopisu = bottle.request.forms.getunicode("geslo")
    if not uporabnisko_ime:
        return bottle.template("registracija.html", napaka="Vnesi uporabniško ime!", x=1)
    try:
        model.Uporabnik.prijava(uporabnisko_ime, geslo_v_cistopisu)
        bottle.response.set_cookie(
            PISKOTEK_UPORABNISKO_IME, uporabnisko_ime, path="/", secret=SKRIVNOST)
        bottle.redirect("/")
    except ValueError as e:
        return bottle.template("prijava.html", napaka=e.args[0], x=1)


@bottle.get("/registracija/")
def registracija_get():
    return bottle.template("registracija.html", napaka=None, x=1)


@bottle.post("/registracija/")
def registracija_post():
    uporabnisko_ime = bottle.request.forms.getunicode("uporabnisko_ime")
    geslo_v_cistopisu = bottle.request.forms.getunicode("geslo")
    if not uporabnisko_ime:
        return bottle.template("registracija.html", napaka="Vnesi uporabniško ime!", x=1)
    try:
        model.Uporabnik.registracija(uporabnisko_ime, geslo_v_cistopisu)
        bottle.response.set_cookie(
            PISKOTEK_UPORABNISKO_IME, uporabnisko_ime, path="/", secret=SKRIVNOST)
        bottle.redirect("/")
    except ValueError as e:
        return bottle.template("registracija.html", napaka=e.args[0], x=1)


@bottle.get("/odjavi/se/")
def odjava():
    bottle.response.delete_cookie(PISKOTEK_UPORABNISKO_IME, path="/")
    bottle.redirect("/prijava/")

@bottle.get('/')
def osnovni_zaslon():
    uporabnik = trenutni_uporabnik()
    shrani_stanje(uporabnik)
    return bottle.template("osnovna_stran.html", x = 1, upo = uporabnik)

@bottle.get("/baza_priprav/")
def baza_priprav():
    return bottle.template("baza_priprav.html", napaka=None, x=1)

@bottle.get("/vaje/")
def vaje():
    uporabnik = trenutni_uporabnik()
    shrani_stanje(uporabnik)
    return bottle.template("vaje.html", napaka=None, x=1, tehnike = uporabnik.seznam_tehnik)

@bottle.get("/generator_priprav/")
def generator():
    return bottle.template("generator.html", napaka=None, x=1)
    
@bottle.get("/iskanje_priprav/")
def iskanje():
    return bottle.template("isci_pripravo.html", napaka=None, x=1)
    
@bottle.get('/vaje/<tehnika>/')
def stran_za_disciplino(tehnika):
    uporabnik = trenutni_uporabnik()
    shrani_stanje(uporabnik)
    izbran = None
    for stil in uporabnik.seznam_tehnik:
        if stil.ime == tehnika:
            izbran = stil
        else:
            pass
    return bottle.template('vse_tehnike.html', izpis = izbran, x=2)

@bottle.get("/<tehnika>/<odsek>/<nivo_odsek>/posodobi_vaja/")
def posodobi_vaja(tehnika, odsek, nivo_odsek):
    uporabnik = trenutni_uporabnik()

    vaja_ime_ = bottle.request.query.getunicode('vaja')
    vaja_ime = vaja_ime_.replace("/", " oz. ")
    pozor = bottle.request.query.getunicode('pozornosti')
    pozornosti = pozor.split(';')
    dolz = bottle.request.query.getunicode('dolzina')
    dolzine = dolz.split(';')

    tehnika_class = uporabnik.class_tehnika(tehnika)
    odsek_class = tehnika_class.class_odseka_tehnike(odsek)
    nivo_odsek_class = odsek_class.class_nivo_odseka_tehnike(nivo_odsek)

    #if nivo_odsek_class.preveri_ime_vaja(vaja_ime):
    #    nova_vaja = model.Vaja(
    #        f'-{vaja_ime}',
    #        pozornosti, 
    #        dolzine
    #    )
    #    nivo_odsek_class.dodaj_vajo(nova_vaja)
#
    #    shrani_stanje(uporabnik)
    #    niz =  f'/vaje/{tehnika}/'
#
    #    return bottle.redirect(niz)
    #else:
    #    #ime ze obstaja
    #    return bottle.redirect('/')
    nova_vaja = model.Vaja(
        f'-{vaja_ime}',
        pozornosti, 
        dolzine
    )

    nivo_odsek_class.dodaj_vajo(nova_vaja)
    shrani_stanje(uporabnik)
    niz =  f'/vaje/{tehnika}/'

    return bottle.redirect(niz)

@bottle.get("/<tehnika>/<odsek>/posodobi_nivo_odsek/")
def posodobi_nivo_odsek(tehnika, odsek):
    uporabnik = trenutni_uporabnik()

    nivo_odsek_ime = bottle.request.query.getunicode('nivo_odseka_tehnike')

    tehnika_class = uporabnik.class_tehnika(tehnika)
    odsek_class = tehnika_class.class_odseka_tehnike(odsek)
    
    #if odsek_class.preveri_ime_nivo(nivo_odsek_ime):
    #    nov_nivo = model.NivoOdsekaTehnike([], nivo_odsek_ime)
    #    odsek_class.dodaj_nivo(nov_nivo)
#
    #    shrani_stanje(uporabnik)
    #    niz =  f'/vaje/{tehnika}/'
#
    #    return bottle.redirect(niz)
    #else:
    #    #ime ze obstaja
    #    return bottle.redirect('/')

    nov_nivo = model.NivoOdsekaTehnike([], nivo_odsek_ime)
    odsek_class.dodaj_nivo(nov_nivo)

    shrani_stanje(uporabnik)
    niz =  f'/vaje/{tehnika}/'

    return bottle.redirect(niz)

@bottle.get("/<tehnika>/posodobi_odsek/")
def posodobi_odsek(tehnika):
    uporabnik = trenutni_uporabnik()
    odsek_ime = bottle.request.query.getunicode('odsek_tehnike')

    tehnika_class = uporabnik.class_tehnika(tehnika)
    #if tehnika_class.preveri_ime_odsek(odsek_ime):
    #    nov_odsek = model.OdsekTehnike([], odsek_ime)
    #    tehnika_class.dodaj_odsek_tehnike(nov_odsek)
#
    #    shrani_stanje(uporabnik)
    #    niz =  f'/vaje/{tehnika}/'
#
    #    return bottle.redirect(niz)
    #else:
    #    #ime ze obstaja
    #    return bottle.redirect('/')

    nov_odsek = model.OdsekTehnike([], odsek_ime)
    tehnika_class.dodaj_odsek_tehnike(nov_odsek)

    shrani_stanje(uporabnik)
    niz =  f'/vaje/{tehnika}/'
    
    return bottle.redirect(niz)

@bottle.get("/izbrisi_vaja/<vaja_ime>/<vaja_nivo>/<vaja_odsek>/<vaja_tehnika>/")
def izbrisi_vaja(vaja_ime, vaja_nivo, vaja_odsek, vaja_tehnika):
    uporabnik = trenutni_uporabnik()

    tehnika_class = uporabnik.class_tehnika(vaja_tehnika)
    odsek_class = tehnika_class.class_odseka_tehnike(vaja_odsek)
    nivo_odsek_class = odsek_class.class_nivo_odseka_tehnike(vaja_nivo)
    vaja_izbris = nivo_odsek_class.class_vaja(vaja_ime)

    nivo_odsek_class.pobrisi_vajo(vaja_izbris)

    shrani_stanje(uporabnik)
    niz = f'/vaje/{vaja_tehnika}/'
    return bottle.redirect(niz)

bottle.run(debug=True, reloader=True)
