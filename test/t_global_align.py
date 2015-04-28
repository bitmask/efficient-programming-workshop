import unittest

import os, sys
lib_path = os.path.abspath('../bin')
sys.path.append(lib_path)

from global_align import *
import Exceptions

import parse_fasta

class TestGlobalAlign (unittest.TestCase):

    def setUp(self):
        pass
        
    def tearDown(self):
        pass
        
    def test_get_scoring_matrix(self):
        self.assertTrue(get_scoring_matrix('default'), "Can't fetch default (identity) scoring matrix")
        with self.assertRaises(Exceptions.MissingMatrixType):
            get_scoring_matrix('dne')

    def test_align(self):
        # get some valid data from a test file
        valid = "data/YAL068C.fasta" 
        seq1, seq2 = parse_fasta.parse_fasta(valid).values()

        expected = 'expected' # TODO expected return value of align
        self.assertEquals(align(seq1, seq2, get_scoring_matrix('default')), expected, "Alignment did not work properly")
    
suite = unittest.TestLoader().loadTestsFromTestCase(TestGlobalAlign)
unittest.TextTestRunner(verbosity=2).run(suite)
