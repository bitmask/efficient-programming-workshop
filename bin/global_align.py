import Exceptions

def get_matrix(request):
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
                            'BLOSUM62': {} } #  TODO
    if request in avail_matrices.keys():
        return avail_matrices[request]
    else:
         raise Exceptions.MissingMatrixType("Matrix type " + request + "does not exist")

def align(seq1, seq2, matrix, gap=0):
    row_l=len(seq1)+1
    col_l=len(seq2)+1

    #Fill out the DP matrix 
    DPM=[]
    #first column set
    for j in range(col_l):
        DPM.append([(-j)*gap])
    #first row set
    for i in range(1,row_l):
        DPM[0].append((-i)*gap)
    #fill out the rest
    for i in range(1,row_l):
        chr1=seq1[i-1]
        for j in range(1,col_l):
            chr2=seq2[j-1]
            best = max(DPM[i-1][j-1]+matrix[chr1][chr2], DPM[i][j-1]-gap, DPM[i-1][j]-gap)
            DPM[i].append(best)

    alignment = []
    #Backtracking the DP matrix
    i=row_l-1
    j=col_l-1
    while i!=0 and j!=0:
        chr1 = seq1[i-1]
        chr2 = seq2[j-1]

        match = DPM[i-1][j-1]+matrix[chr1][chr2]
        gap1 = DPM[i-1][j] - gap
        gap2 = DPM[i][j-1] - gap
        #depending on the path followed; we decide gap, match or mismatch
        if gap1 >= match and gap1 >= gap2:
            alignment.append((chr1,'-',' ')) #gap in seq2
            i = i-1
        elif gap2 >= match and gap2 >= gap1:
            alignment.append(('-',chr2,' ')) #gap in seq1
            j = j-1
        else:
            if chr1==chr2:
                alignment.append((chr1,chr2,'|')) #match
            else:
                alignment.append((chr1,chr2,':')) #mismatch
            i = i-1
            j = j-1
    while i!=0:
        chr1 = seq1[i-1]
        alignment.append((chr1,'-',' '))
        i = i-1
    while j!=0:
        chr2 = seq2[j-1]
        alignment.append(('-',chr2,' '))
        j = j-1

    return alignment[::-1]

def print_alignment(alignment):
    print "The final alignment is:\n"
    line1=''
    line2=''
    line3=''
    for (chr1,chr2,algn) in alignment:
        line1 += chr1
        line2 += chr2
        line3 += algn
        
        if len(line1)==50:
            print line1+'\n'+line2+'\n'+line3+'\n'
            line1 = ''
            line2 = ''
            line3 = ''
    print line1+'\n'+line2+'\n'+line3
    return True

