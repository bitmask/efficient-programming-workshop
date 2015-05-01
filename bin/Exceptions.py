# Errors related to FASTA files


class EmptyFasta(Exception):
    pass


class MissingId(Exception):
    pass


class MissingSequence(Exception):
    pass


# Errors related to alignment

class MissingMatrixType(Exception):
    pass
