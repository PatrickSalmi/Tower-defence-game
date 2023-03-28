import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_toimii(self):
        self.maksukortti.lataa_rahaa(100)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 11.00 euroa")

    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(300)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.00 euroa")

    def test_saldo_ei_mene_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(1100)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_ota_rahaa_metodi_palauttaa_oikean_totuusarvon(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)
        self.assertEqual(self.maksukortti.ota_rahaa(2000), False)


      
