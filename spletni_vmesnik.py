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
    #uporabnik = trenutni_uporabnik(upor)
    return bottle.template("osnovna_stran.html", tehnike = uporabnik.seznam_tehnik)

# @bottle.get('/<disciplina>/')
# def stran_za_disciplino(disciplina, vaje):
#    return bottle.template('vse_tehnike.html', tehnika = disciplina, vaje_tehnika = vaje)

bottle.run(debug=True, reloader=True)
