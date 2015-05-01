import Exceptions


def parse_fasta(fasta_filename):
    """Validate FASTA file
    @return a dictionary keyed on fasta id to sequence
    @param fasta_filename filename of file to parse
    """

    sequences = {}

    with open(fasta_filename, "r") as fasta:

        fasta_id = None
        # do our best to accept any input that looks vaguely valid
        for line in fasta:
            if line.startswith(">"):
                # take everything up to the first space as the id
                # get rid of the leading >
                # and get rid of the newline
                fasta_id = line.split(" ")[0].replace(">", "", 1).rstrip('\n')
                            
                seq = []
                if fasta_id == "":
                    raise Exceptions.MissingId("invalid if there is no fasta_id")
    
            else:
                seq.append(line.rstrip('\n'))
                # handle sequences on multiple lines
                whole_seq = "".join(seq)
                if len(whole_seq) == 0:
                    raise Exceptions.MissingSequence("invalid if there is no sequence")
                sequences[fasta_id] = whole_seq

    if len(sequences) == 0:
        raise Exceptions.EmptyFasta("invalid if there is nothing in the fasta file")

    return sequences
