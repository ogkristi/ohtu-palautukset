from typing import Any


class IntJoukko:
    def __init__(self, kapasiteetti: int = 5, kasvatuskoko: int = 5):
        self._kapasiteetti = self._validoi_pos_int(kapasiteetti, "kapasiteetti")
        self._kasvatuskoko = self._validoi_pos_int(kasvatuskoko, "kasvatuskoko")

        self._lista = self._luo_lista(self._kapasiteetti)
        self._koko = 0

    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, pituus: int):
        self._kapasiteetti = pituus
        return [0] * pituus

    def _validoi_pos_int(self, arvo: Any, viesti: str):
        if not isinstance(arvo, int) or arvo < 0:
            raise ValueError(f"Huono arvo parametrille: {viesti}")
        return arvo

    def mahtavuus(self):
        return self._koko

    def kuuluu(self, arvo: int):
        return arvo in self._lista

    def lisaa(self, arvo: int):
        if not arvo in self._lista:
            self._lista[self._koko] = arvo
            self._koko += 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self._koko == self._kapasiteetti:
                lista_vanha = self._lista[:]  # Kopioi lista
                self._lista = self._luo_lista(self._koko + self._kasvatuskoko)
                self._lista[: len(lista_vanha)] = lista_vanha

            return True

        return False

    def poista(self, arvo: int):
        try:
            i = self._lista.index(arvo)
            self._lista[i:] = self._lista[i + 1 :] + [0]
            self._koko -= 1
            return True
        except:
            return False

    def to_int_list(self):
        return self._lista[: self._koko]

    @staticmethod
    def yhdiste(a, b):
        a = a.to_int_list()
        b = b.to_int_list()
        tulos = IntJoukko()

        for arvo in a + b:
            tulos.lisaa(arvo)

        return tulos

    @staticmethod
    def leikkaus(a, b):
        a = a.to_int_list()
        b = b.to_int_list()
        tulos = IntJoukko()

        for arvo in a:
            if arvo in b:
                tulos.lisaa(arvo)
        return tulos

    @staticmethod
    def erotus(a, b):
        tulos = IntJoukko()
        a = a.to_int_list()
        b = b.to_int_list()

        for arvo in a:
            if arvo not in b:
                tulos.lisaa(arvo)

        return tulos

    def __str__(self):
        esitys = ", ".join([str(e) for e in self._lista[: self._koko]])
        return "{" + esitys + "}"
