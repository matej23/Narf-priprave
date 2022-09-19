import bottle
import model

@bottle.get('/')
def osnovni_zaslon():
    return bottle.template("osnovna_stran.html")

bottle.run(debug=True, reloader=True)