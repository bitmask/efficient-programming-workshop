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
        valid = "data/small.fasta" 
        seq1, seq2 = parse_fasta.parse_fasta(valid).values()
        expected_align = [ ('A', 'A', '|'), ('-', 'C', ' '), ('D', 'D', '|'), ('E', 'E', '|') ]
        expected_score = 1
        actual = align(seq1, seq2, get_scoring_matrix('default'))
        self.assertEquals(actual[0], expected_align, "Alignment is not correct")
        self.assertEquals(actual[1], expected_score, "Alignment score is not correct")
        print_alignment(actual[0])

    def test_align_larger(self):
        valid = "data/YAL068C.fasta" 
        seq1, seq2 = parse_fasta.parse_fasta(valid).values()
        actual = align(seq1, seq2, get_scoring_matrix('default'))
        expected_score = 116
        self.assertEquals(actual[1], expected_score, "Alignment score is not correct")
        print_alignment(actual[0])

    def test_tenuous(self):
        valid = "data/tenuous.fasta" 
        seq1, seq2 = parse_fasta.parse_fasta(valid).values()
        expected_align = [('C', 'C', '|'), ('C', 'D', ':'), ('C', 'E', ':'), ('C', 'C', '|'), ('D', 'C', ':'), ('E', 'C', ':'), ('C', 'C', '|')]
        expected_score = -1
        actual = align(seq1, seq2, get_scoring_matrix('default'))
        self.assertEquals(actual[0], expected_align, "Alignment is not correct")
        self.assertEquals(actual[1], expected_score, "Alignment score is not correct")
        print_alignment(actual[0])
  
suite = unittest.TestLoader().loadTestsFromTestCase(TestGlobalAlign)
unittest.TextTestRunner(verbosity=2).run(suite)
