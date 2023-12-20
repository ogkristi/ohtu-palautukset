class Tekoaly:
    def __init__(self):
        self._avaruus = "kps"
        self._laskuri = 0

    def anna_siirto(self):
        self._laskuri = (self._laskuri + 1) % len(self._avaruus)

        return self._avaruus[self._laskuri]

    def aseta_siirto(self, siirto):
        # ei tehdä mitään
        pass


# "Muistava tekoäly"
class TekoalyParannettu:
    def __init__(self, max_koko):
        self._muisti = []
        self._max_koko = max_koko

    def aseta_siirto(self, siirto):
        # jos muisti täyttyy, unohdetaan vanhin siirto
        if len(self._muisti) == self._max_koko:
            self._muisti = self._muisti[1:] + [siirto]
        else:
            self._muisti.append(siirto)

    def anna_siirto(self):
        if len(self._muisti) < 2:
            return "k"

        viimeisin_siirto = self._muisti[-1]

        frek = {"k": 0, "p": 0, "s": 0}

        for i, siirto in enumerate(self._muisti[:-1]):
            if siirto == viimeisin_siirto:
                seuraava = self._muisti[i + 1]
                frek[seuraava] += 1

        # Tehdään siirron valinta esimerkiksi seuraavasti;
        # - jos kiviä eniten, annetaan aina paperi
        # - jos papereita eniten, annetaan aina sakset
        # muulloin annetaan aina kivi
        if frek["k"] > frek["p"] or frek["k"] > frek["s"]:
            return "p"
        elif frek["p"] > frek["k"] or frek["p"] > frek["s"]:
            return "s"
        else:
            return "k"

        # Tehokkaampiakin tapoja löytyy, mutta niistä lisää
        # Johdatus Tekoälyyn kurssilla!
