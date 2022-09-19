import bottle
import model

@bottle.get('/')
def osnovni_zaslon():
    mozne_vaje = model.Priprava()
    return bottle.template("osnovna_stran.html", vaje = mozne_vaje)

#@bottle.get('/<disciplina>/')
#def stran_za_disciplino(disciplina, vaje):
#    return bottle.template('vse_tehnike.html', tehnika = disciplina, vaje_tehnika = vaje)

bottle.run(debug=True, reloader=True)