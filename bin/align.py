
# CBioVikings Efficient Programming Workshop Example Code

# This code is in the public domain under CC0.  
# https://creativecommons.org/publicdomain/zero/1.0/
# You are free to use it, modify it, adapt it, include it in your own work, etc, all without attribution or license restrictions. 


import argparse
import sys
import parse_fasta
import global_align

def report_error(string):
    sys.stderr.write(string + "\n")
    sys.exit(1)

def main():

    parser = argparse.ArgumentParser(description='CBioVikings Global Sequence Alignment Example')
    parser.add_argument('-f', '--fasta', 
                        required=True, 
                        dest='fasta', 
                        help='Fasta file to read sequences from') 
    parser.add_argument('-m', '--scoring_matrix', 
                        dest='scoring_matrix', 
                        help='Similarity matrix to use for scoring.  Default=identity')
    parser.add_argument('--debug', 
                        action='store_true', 
                        help='Print debug output')
    parser.add_argument('-v', '--verbose', 
                        action='store_true', 
                        dest='verbose', 
                        help='Print verbose output')
    args = parser.parse_args()

    if args.verbose:
        sys.stderr.write("# CBioVikings Global Sequence Alignment\n")
        sys.stderr.write("# fasta file: " + str(args.fasta) + "\n")
        sys.stderr.write("# scoring matrix: " + str(args.scoring_matrix) + "\n")
        if args.debug:
            sys.stderr.write("# debug is on\n")
    
    # read sequences from the fasta file provided
    if args.fasta:
        try:
            # sequences is a dictionary of the fasta entries
            sequences = parse_fasta.parse_fasta(args.fasta)
        except:
            report_error("There are no sequences in the fasta file " + args.fasta)

        # our algorithm will only align two sequences
        if len(sequences.keys()) != 2:
            report_error("Fasta file does not contain 2 sequences")
        else:
            seq1, seq2 = sequences.values()

    # get the similarity scoring matrix to use
    if args.scoring_matrix:
        try:
            scoring_matrix = global_align.get_matrix(args.matrix)
        except:
            report_error("That matrix type is not available")
    else:
        try:
            scoring_matrix = global_align.get_matrix('default')
        except:
            report_error("Default matrix is not available")

    # now actually do the alignment
    if sequences and scoring_matrix:
        try:
            alignment = global_align.align(seq1, seq2, scoring_matrix)
        except:
            raise 

        # print the alignment
        if alignment:
            global_align.print_alignment(alignment)


if __name__ == "__main__":
    main()
