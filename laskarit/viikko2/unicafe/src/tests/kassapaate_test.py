import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_oikea_maara_myyty_ja_rahaa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)

    def test_kateisosto_edullinen_toimii_riittavalla_rahalla(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250), 10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisosto_edullinen_ei_tarpeeksi_rahaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateisosto_maukas_toimii_riittavalla_rahalla(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisosto_maukas_ei_tarpeeksi_rahaa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(350), 350)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_edullinen_toimii_riittavalla_rahalla(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.60 euroa")
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_korttiosto_edullinen_ei_tarpeeksi_rahaa(self):
        maksukortti = Maksukortti(100)

        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(maksukortti), False)
        self.assertEqual(str(maksukortti), "Kortilla on rahaa 1.00 euroa")
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_korttiosto_maukas_toimii_riittavalla_rahalla(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 6.00 euroa")
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_korttiosto_maukas_ei_tarpeeksi_rahaa(self):
        maksukortti = Maksukortti(360)

        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(maksukortti), False)
        self.assertEqual(str(maksukortti), "Kortilla on rahaa 3.60 euroa")
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortille_rahan_lataaminen(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 15.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)

    def test_kortille_negatiivisen_maaran_lataaminen(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        


    