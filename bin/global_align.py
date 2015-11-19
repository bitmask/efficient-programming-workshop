# -*- coding: utf-8 -*-
import Exceptions


def fill_dpm(seq1, seq2, scoring_matrix, gap_penalty):
    #Function to fill out the Dynamic Programming matrix for 2 given sequences

    #Initialize the DP_matrix
    dpm = [[0]*(len(seq2)+1) for i in range(len(seq1)+1)]
    
    # HERE COMES THE CODE #
    """
    PSEUDOCODE
        for i=0 : length(A)
            dpm(i,0) ← (-1)*i

        for j=0 to length(B)
            dpm(0,j) ← (-1)*j

        for i=1 to length(A)
            for j=1 to length(B)
            {
                s =  1 if Ai = Bj, (-1) otherwise
                Match ← dpm(i-1,j-1) + s
                Delete ← dpm(i-1, j) - 1
                Insert ← dpm(i, j-1) - 1
                dpm(i,j) ← max(Match, Insert, Delete)
             }
    """

    return dpm


def backtrack_dpm(seq1, seq2, dpm, scoring_matrix, gap_penalty):
    # Backtrack and construct the alignment from given DP_matrix

    # Backtracking starts at the last cell of DP_matrix dpm[i][j]
    i = len(seq1)
    j = len(seq2)

    alignment = []  # alignment is currently empty
    
    # i and j will represent our current position in the dpm
    # Iterate over i and j simultaneously, until one becomes 0
    while i != 0 and j != 0:
        chr1 = seq1[i-1]
        chr2 = seq2[j-1]

        cell = dpm[i-1][j-1]

        # What would be the score of the cell if seq1[i] and seq2[j] are matched
        if cell + scoring_matrix[chr1][chr2] == dpm[i][j]:
            if chr1 == chr2:
                alignment.append((chr1, chr2, '|'))  # match
            else:
                alignment.append((chr1, chr2, ':'))  # mismatch
            i -= 1
            j -= 1
        # What would be the score if we have a gap aligned with seq1[i]
        elif cell - gap_penalty == dpm[i-1][j]:
            alignment.append((chr1, '-', ' '))
            i -= 1
        else:
            alignment.append(('-', chr2, ' '))
            j -= 1

    # since we hit the wall in DP (1st col or 1st row), there are just gaps left to align
    while i != 0:
        chr1 = seq1[i-1]
        alignment.append((chr1, '-', ' '))
        i -= 1
    while j != 0:
        chr2 = seq2[j-1]
        alignment.append(('-', chr2, ' '))
        j -= 1

    return alignment[::-1]


def align(seq1, seq2, scoring_matrix, gap_penalty=2):
    # Aligns two given sequences with dynamic programming
    # Output is a list of 3-tuples (chr1,chr2,("|" for match, ":" for mismatch, " " for gap))
    print("aligning two sequences: ")
    print("Seq1:"+seq1)
    print("Seq2:"+seq2)

    #Fill out the dynamic programming matrix
    dpm = fill_dpm(seq1, seq2, scoring_matrix, gap_penalty)
    #Backtrack on DPM and get the alignment
    alignment = backtrack_dpm(seq1, seq2, dpm, scoring_matrix, gap_penalty)

    return alignment, dpm[-1][-1]  # return the alignment and its score


def print_alignment(alignment):
    # Prints the alignment
    print("The final alignment is:\n")
    line1 = ''
    line2 = ''
    line3 = ''

    for (chr1, chr2, algn) in alignment:
        line1 += chr1
        line2 += chr2
        line3 += algn

        #limit each line with 50 characters
        if len(line1) == 50:
            print(line1+'\n'+line2+'\n'+line3+'\n')
            line1 = ''
            line2 = ''
            line3 = ''

    print(line1 + '\n' + line2 + '\n' + line3)
    return True

def get_scoring_matrix(request):
    avail_matrices = { 'default': 
                            {'A': 
                                {'A':1, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'K':0, 'L':0, 'M':0, 'N':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'V':0, 'W':0, 'Y':0},
                               'C':  
                                {'A':0, 'C':1, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'K':0, 'L':0, 'M':0, 'N':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'V':0, 'W':0, 'Y':0},
                               'D':
                                {'A':0, 'C':0, 'D':1, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'K':0, 'L':0, 'M':0, 'N':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'V':0, 'W':0, 'Y':0},
                               'E':
                                {'A':0, 'C':0, 'D':0, 'E':1, 'F':0, 'G':0, 'H':0, 'I':0, 'K':0, 'L':0, 'M':0, 'N':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'V':0, 'W':0, 'Y':0},
                               'F':
                                {'A':0, 'C':0, 'D':0, 'E':0, 'F':1, 'G':0, 'H':0, 'I':0, 'K':0, 'L':0, 'M':0, 'N':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'V':0, 'W':0, 'Y':0},
                               'G':
                                {'A':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':1, 'H':0, 'I':0, 'K':0, 'L':0, 'M':0, 'N':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'V':0, 'W':0, 'Y':0},
                               'H':
                                {'A':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':1, 'I':0, 'K':0, 'L':0, 'M':0, 'N':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'V':0, 'W':0, 'Y':0},
                               'I':
                                {'A':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':1, 'K':0, 'L':0, 'M':0, 'N':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'V':0, 'W':0, 'Y':0},
                               'K':
                                {'A':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'K':1, 'L':0, 'M':0, 'N':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'V':0, 'W':0, 'Y':0},
                               'L':
                                {'A':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'K':0, 'L':1, 'M':0, 'N':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'V':0, 'W':0, 'Y':0},
                               'M':
                                {'A':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'K':0, 'L':0, 'M':1, 'N':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'V':0, 'W':0, 'Y':0},
                               'N':
                                {'A':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'K':0, 'L':0, 'M':0, 'N':1, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'V':0, 'W':0, 'Y':0},
                               'P':
                                {'A':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'K':0, 'L':0, 'M':0, 'N':0, 'P':1, 'Q':0, 'R':0, 'S':0, 'T':0, 'V':0, 'W':0, 'Y':0},
                               'Q':
                                {'A':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'K':0, 'L':0, 'M':0, 'N':0, 'P':0, 'Q':1, 'R':0, 'S':0, 'T':0, 'V':0, 'W':0, 'Y':0},
                               'R':
                                {'A':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'K':0, 'L':0, 'M':0, 'N':0, 'P':0, 'Q':0, 'R':1, 'S':0, 'T':0, 'V':0, 'W':0, 'Y':0},
                               'S':
                                {'A':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'K':0, 'L':0, 'M':0, 'N':0, 'P':0, 'Q':0, 'R':0, 'S':1, 'T':0, 'V':0, 'W':0, 'Y':0},
                               'T':
                                {'A':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'K':0, 'L':0, 'M':0, 'N':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':1, 'V':0, 'W':0, 'Y':0},
                               'V':
                                {'A':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'K':0, 'L':0, 'M':0, 'N':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'V':1, 'W':0, 'Y':0},
                               'W':
                                {'A':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'K':0, 'L':0, 'M':0, 'N':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'V':0, 'W':1, 'Y':0},
                               'Y':
                                {'A':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'K':0, 'L':0, 'M':0, 'N':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'V':0, 'W':0, 'Y':1},
                              }, 
                             'BLOSUM62' : {}  # TODO
                            }
    if request in avail_matrices.keys():
        return avail_matrices[request]
    else:
        raise Exceptions.MissingMatrixType("Matrix type " + request + "does not exist")
