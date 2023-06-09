import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 15.00 euroa")

    def test_saldo_vähenee_oikein_jos_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")

    def test_syo_maukkaasti_Saldo_ei_muutu(self):
        self.maksukortti.ota_rahaa(1500)
        
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")


    def test_rahat_riittivät(self):
        self.maksukortti = Maksukortti(500)

        self.assertEqual(self.maksukortti.ota_rahaa(500), True) 
        self.assertEqual(self.maksukortti.ota_rahaa(501), False)



