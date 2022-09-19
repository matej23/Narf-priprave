import bottle
import model

def trenutni_uporabnik():
    return model.Uporabnik()

@bottle.get('/')
def osnovni_zaslon():
    uporabnik = trenutni_uporabnik()
    return bottle.template("osnovna_stran.html", tehnike = uporabnik.seznam_tehnik)

# @bottle.get('/<disciplina>/')
# def stran_za_disciplino(disciplina, vaje):
#    return bottle.template('vse_tehnike.html', tehnika = disciplina, vaje_tehnika = vaje)

bottle.run(debug=True, reloader=True)
