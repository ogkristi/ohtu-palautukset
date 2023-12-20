from tuomari import Tuomari
from tekoaly import Tekoaly, TekoalyParannettu


class KiviPaperiSakset:
    def _onko_ok_siirto(self, siirto):
        return siirto in "kps"

    def pelaa(self):
        tuomari = Tuomari()

        while True:
            ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
            tokan_siirto = self._tokan_siirto(ekan_siirto)

            if not self._onko_ok_siirto(ekan_siirto) or not self._onko_ok_siirto(
                tokan_siirto
            ):
                break

            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

        print("Kiitos!")
        print(tuomari)

    def _tokan_siirto(self, ekan_siirto):
        return "k"

    @staticmethod
    def kaksinpeli():
        return KPSPelaajaVsPelaaja()

    @staticmethod
    def yksinpeli():
        return KPSTekoaly(Tekoaly())

    @staticmethod
    def yksinpeli_haastava():
        return KPSTekoaly(TekoalyParannettu(10))


class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def _tokan_siirto(self, ekan_siirto):
        return input("Toisen pelaajan siirto: ")


class KPSTekoaly(KiviPaperiSakset):
    def __init__(self, tekoaly) -> None:
        self._tekoaly = tekoaly

    def _tokan_siirto(self, ekan_siirto):
        siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        self._tekoaly.aseta_siirto(ekan_siirto)

        return siirto
