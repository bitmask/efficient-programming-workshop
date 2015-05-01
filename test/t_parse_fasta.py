import unittest

import os
import sys

lib_path = os.path.abspath('../bin')
sys.path.append(lib_path)

from parse_fasta import *
import Exceptions


class TestParseFasta (unittest.TestCase):

    valid = "data/YAL068C.fasta"  # this is a valid fasta file
    invalid_nodata = "data/invalid_nodata.fasta"  # this file contains 0 bytes
    invalid_dne = "data/invalid_dne.fasta"  # this file does not exist

    def setUp(self):
        pass
        
    def tearDown(self):
        pass
        
    def test_parse_fasta(self):
        self.assertEqual(len(parse_fasta(self.valid)), 2, "Fasta file does not contain 2 entries")

    def test_parse_fasta_nodata(self):
        with self.assertRaises(Exceptions.EmptyFasta):
            parse_fasta(self.invalid_nodata)

    def test_parse_fasta_dne(self):
        with self.assertRaises(IOError):
            parse_fasta(self.invalid_dne)

suite = unittest.TestLoader().loadTestsFromTestCase(TestParseFasta)
unittest.TextTestRunner(verbosity=2).run(suite)
