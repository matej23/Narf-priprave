#class Priprava:
#    def __init__(self, prilagajanje=prilagajanje_vaje, prsno=prsno_vaje, kravl=kravl_vaje, hrbtno=hrbtno_vaje, konec_ure = konec_ure, ogrevanje = ogrevanje):
#        self.prilagajanje = prilagajanje
#        self.prsno = prsno
#        self.kravl = kravl
#        self.hrbtno = hrbtno
#        self.konec_ure = konec_ure
#        self. ogrevanje = ogrevanje
import random
import hashlib
import json
import vaje

class Tehnika:
    def __init__(self, odseki_tehnike, ime): 
        self.odseki_tehnike = odseki_tehnike
        self.ime = ime

    def preveri_ime_odsek(self, odsek_ime):
        imena_odseki = [odsek.ime for odsek in self.odseki_tehnike]
        if odsek_ime in imena_odseki:
            return False
        else: 
            return True

    def dodaj_odsek_tehnike(self, odsek_tehnike):
        self.odseki_tehnike.append(odsek_tehnike)

    def pobrisi_odsek_tehnike(self, odsek_tehnike):
        self.odseki_tehnike.remove(odsek_tehnike)

    def class_odseka_tehnike(self, odsek_tehnike_ime):
        iskan_odsek = None
        for odsek in self.odseki_tehnike:
            if odsek.ime == odsek_tehnike_ime:
                iskan_odsek = odsek
        return iskan_odsek

    def tehnika_v_slovar(self):
        return {
            "ime_tehnike" : self.ime,
            "odseki_tehnike" : [odsek_tehnike.odsek_tehnike_v_slovar() for odsek_tehnike in self.odseki_tehnike]
        }

    @staticmethod
    def tehnika_iz_slovarja(slovar):
        return Tehnika(
            [OdsekTehnike.odsek_tehnike_iz_slovarja(odsek_tehnike) for odsek_tehnike in slovar["odseki_tehnike"]], 
            slovar["ime_tehnike"]
            )

class OdsekTehnike:
    def __init__(self, nivoji, ime):
        self.nivoji = nivoji
        self.ime = ime

    def preveri_ime_nivo(self, nivo_ime):
        imena_nivoji = [nivo.ime for nivo in self.nivoji]
        if nivo_ime in imena_nivoji:
            return False
        else: 
            return True

    def dodaj_nivo(self, nivo):
        self.nivoji.append(nivo)

    def pobrisi_nivo(self, nivo):
        self.nivoji.remove(nivo)
    
    def class_nivo_odseka_tehnike(self, nivo_odsek_tehnike_ime):
        iskan_nivo_odseka = None
        for nivo in self.nivoji:
            if nivo.ime == nivo_odsek_tehnike_ime:
                iskan_nivo_odseka = nivo
        return iskan_nivo_odseka

    def odsek_tehnike_v_slovar(self):
        return {
            "ime_odseka_tehnike" : self.ime,
            "nivo_odsekov_tehnike" : [nivo_odseka_tehnike.nivo_odseka_tehnike_v_slovar() for nivo_odseka_tehnike in self.nivoji]
        }

    @staticmethod
    def odsek_tehnike_iz_slovarja(slovar):
        return OdsekTehnike(
            [NivoOdsekaTehnike.nivo_odseka_tehnike_iz_slovarja(nivo_odseka_tehnike) for nivo_odseka_tehnike in slovar["nivo_odsekov_tehnike"]], 
            slovar["ime_odseka_tehnike"],
            )

class NivoOdsekaTehnike:
    def __init__(self, vaje, ime):
        self.vaje = vaje
        self.ime = ime

    def preveri_ime_vaja(self, vaja_ime):
        imena_vaje = [vaja.ime for vaja in self.vaje]
        if vaja_ime in imena_vaje:
            return False
        else: 
            return True

    def dodaj_vajo(self, vaja):
        self.vaje.append(vaja)

    def pobrisi_vajo(self, vaja):
        self.vaje.remove(vaja)
    
    def class_vaja(self, vaja_ime):
        iskana_vaja = None
        for vaja in self.vaje:
            if vaja.ime == vaja_ime:
                iskana_vaja = vaja
        return iskana_vaja

    def nivo_odseka_tehnike_v_slovar(self):
        return {
            "ime_nivoja_odseka_tehnike" : self.ime,
            "vaje" : [vaja.vaja_v_slovar() for vaja in self.vaje]
        }

    @staticmethod
    def nivo_odseka_tehnike_iz_slovarja(slovar):
        return NivoOdsekaTehnike(
            [Vaja.vaja_iz_slovarja(vaja) for vaja in slovar["vaje"]],
            slovar["ime_nivoja_odseka_tehnike"]
        )

class Vaja:
    def __init__(self, ime, pozornosti, dolzine):
        self.ime = ime
        self.pozornosti = pozornosti
        self.dolzine = dolzine

    def dodaj_pozornost(self, pozornost):
        self.pozornosti.append(pozornost)

    def pobrisi_pozornost(self, pozornost):
        self.pozornosti.remove(pozornost)

    def dodaj_dolzino(self, dolzina):
        self.dolzina.append(dolzina)

    def pobrisi_dolzino(self, dolzina):
        self.dolzine.remove(dolzina)
    
    def vaja_v_slovar(self): 
        return {
            "ime_vaje" : self.ime,
            "pozornosti" : self.pozornosti,
            "dolzine" : self.dolzine
        }

    @staticmethod
    def vaja_iz_slovarja(slovar):
        return Vaja(
            slovar["ime_vaje"], 
            slovar["pozornosti"],
            slovar["dolzine"]
            )
    
    @staticmethod
    def izpisi_vajo(self):
        return f'{self.ime} [pozornosti:{self.pozornosti}] → {self.dolzine}'
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
class Uporabnik:
    def __init__(self, uporabnisko_ime, zasifrirano_geslo, seznam_tehnik = [vaje.prilagajanje, vaje.prsno, vaje.kravl, vaje.hrbtno]):
        self.uporabnisko_ime = uporabnisko_ime
        self.zasifrirano_geslo = zasifrirano_geslo
        #self.baza_priprav = baza_priprav
        self.seznam_tehnik = seznam_tehnik

    def dodaj_pripravo(self, priprava):
        self.baza_priprav.append(priprava)

    def pobrisi_pripravo(self, priprava):
        self.baza_priprav.remove(priprava)

    def dodaj_tehniko(self, tehnika):
        ##pazi ista imena
        self.seznam_tehnik.append(tehnika)

    def pobrisi_tehniko(self, tehnika):
        self.seznam_tehnik.remove(tehnika)

    def class_tehnika(self, tehnika_ime):
        iskana_tehnika = None
        for tehnika in self.seznam_tehnik:
            if tehnika.ime == tehnika_ime:
                iskana_tehnika = tehnika
        return iskana_tehnika

    @staticmethod
    def prijava(uporabnisko_ime, geslo_v_cistopisu):
        uporabnik = Uporabnik.iz_datoteke(uporabnisko_ime)
        if uporabnik is None:
            raise ValueError("Uporabniško ime ne obstaja")
        elif uporabnik.preveri_geslo(geslo_v_cistopisu):
            return uporabnik
        else:
            raise ValueError("Geslo je napačno")

    @staticmethod
    def registracija(uporabnisko_ime, geslo_v_cistopisu):
        if Uporabnik.iz_datoteke(uporabnisko_ime) is not None:
            raise ValueError("Uporabniško ime že obstaja")
        else:
            zasifrirano_geslo = Uporabnik._zasifriraj_geslo(geslo_v_cistopisu)
            uporabnik = Uporabnik(uporabnisko_ime, zasifrirano_geslo)
            uporabnik.v_datoteko()
            return uporabnik

    def _zasifriraj_geslo(geslo_v_cistopisu, sol=None):
        if sol is None:
            sol = str(random.getrandbits(32))
        posoljeno_geslo = sol + geslo_v_cistopisu
        h = hashlib.blake2b()
        h.update(posoljeno_geslo.encode(encoding="utf-8"))
        return f"{sol}${h.hexdigest()}"

    def preveri_geslo(self, geslo_v_cistopisu):
        sol, _ = self.zasifrirano_geslo.split("$")
        return self.zasifrirano_geslo == Uporabnik._zasifriraj_geslo(geslo_v_cistopisu, sol)

    @staticmethod
    def ime_uporabnikove_datoteke(uporabnisko_ime):
        return f"{uporabnisko_ime}.json"

    @staticmethod
    def iz_datoteke(uporabnisko_ime):
        try:
            with open(Uporabnik.ime_uporabnikove_datoteke(uporabnisko_ime)) as datoteka:
                slovar = json.load(datoteka)
                return Uporabnik.iz_slovarja(slovar)
        except FileNotFoundError:
            return None

    def v_datoteko(self):
        with open(
            Uporabnik.ime_uporabnikove_datoteke(self.uporabnisko_ime), "w"
        ) as datoteka:
            json.dump(self.v_slovar(), datoteka, ensure_ascii=False, indent=4)


##NAPISI V SLOVAR IN IZ SLOVARJA ZA PODATKE
    @staticmethod
    def iz_slovarja(slovar):
        uporabnisko_ime = slovar["uporabnisko_ime"]
        zasifrirano_geslo = slovar["zasifrirano_geslo"]
        seznam_tehnik = [Tehnika.tehnika_iz_slovarja(tehnika) for tehnika in slovar["seznam_tehnik"]]
        uporabnik = Uporabnik(uporabnisko_ime, zasifrirano_geslo, seznam_tehnik)
        #uporabnik.sport = {kljuc: Šport.iz_slovarja(
        #    slovar["sport"][kljuc]) for kljuc in slovar["sport"]}
        #uporabnik.seznam = Seznam.iz_slovarja(slovar["seznam"])
        return uporabnik
#
    def v_slovar(self):
        return {
            "uporabnisko_ime": self.uporabnisko_ime,
            "zasifrirano_geslo": self.zasifrirano_geslo,
            "seznam_tehnik" : [tehnika.tehnika_v_slovar() for tehnika in self.seznam_tehnik]
            #"sport": {kljuc: Šport.v_slovar(self.sport[kljuc]) for kljuc in self.sport},
            #"seznam": Seznam.v_slovar(self.seznam)
        }
# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
def random_vaje_iz_nivoja_odseka_tehnike(nivo_odseka_tehnike, stevilo):
    mozne_vaje = nivo_odseka_tehnike.vaje.copy()
    if stevilo == 0: 
        return []
    elif stevilo < 0 or len(mozne_vaje) < stevilo:
        print(f'za nivo odseka tehnike: {nivo_odseka_tehnike.ime} ste zahtevali neustrezno stevilo vaj!')
        return []
    else:
        vse_izbrane = []
        for _ in range(stevilo):
            izbrana = random.choice(mozne_vaje)
            mozne_vaje.remove(izbrana)

            vse_izbrane.append(
                Vaja(
                    izbrana.ime, 
                    [random.choice(izbrana.pozornosti)],
                    [random.choice(izbrana.dolzine)]
                    )
                )
        return vse_izbrane
