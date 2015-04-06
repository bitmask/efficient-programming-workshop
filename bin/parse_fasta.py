import Exceptions

def parse_fasta(fasta_filename):
    """Validate FASTA file
    @return a dictionary
    @param fasta FASTA file of protein sequences (iterator)
    """

    sequences = {}

    with open(fasta_filename, "r") as fasta:

        # do our best to accept any input that looks vaguely valid
        for line in fasta:
    
            if line.startswith(">"):
                # take everything up to the first space as the id
                # get rid of the leading >
                # and get rid of the newline
                fasta_id = line.split(" ")[0].replace(">", "", 1).rstrip('\n')
                            
                seq = []
                wholeseq = ''
                if fasta_id == "":
                    raise Exceptions.MissingId("invalid if there is no fasta_id")
    
            else:
                seq.append(line.rstrip('\n'))
                # handle sequences on multiple lines
                wholeseq = "".join(seq)
                if len(wholeseq) == 0:
                    raise Exceptions.MissingSequence("invalid if there is no sequence")
                sequences[fasta_id] = wholeseq

    if len(sequences) == 0:
        raise Exceptions.EmptyFasta("invalid if there is nothing in the fasta file")

    return sequences

