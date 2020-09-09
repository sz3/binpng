from os import path
from tempfile import TemporaryDirectory
from unittest import TestCase

from binpng.binpng import encode, decode


PROJ_ROOT = path.abspath(path.join(path.dirname(path.realpath(__file__)), '..'))


class BinPngTest(TestCase):
    def setUp(self):
        self.tempdir = TemporaryDirectory()

    def tearDown(self):
        with self.tempdir:
            pass

    def test_encode_decode(self):
        sample_file = path.join(PROJ_ROOT, 'binpng', 'palette.py')
        enc_file = path.join(self.tempdir.name, 'encoded.png')
        encode(sample_file, enc_file)

        dec_file = path.join(self.tempdir.name, 'decoded.py')
        decode(enc_file, dec_file)

        with open(sample_file, 'rb') as f:
            expected = f.read()
        with open(dec_file, 'rb') as f:
            actual = f.read()
        self.assertEqual(actual, expected)
