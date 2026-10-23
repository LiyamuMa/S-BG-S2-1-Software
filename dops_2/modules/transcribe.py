class Error(Exception):
    pass

Valid = ["A", "C", "G", "T", "N"]  

def invalid_nucleotide(nucleotides):
    invalid_log = []
    """
    Checks if the nucleotide is invalid
    """
    for N in nucleotides:
        if N.upper() not in Valid and N.upper() not in invalid_log:
            invalid_log.append(N.upper())
    return(invalid_log)

def transcribe_sequence(dna_sequence):
    """
    Transcribes a DNA sequence
    """

    stripped = "".join(dna_sequence.split())

    invalid = invalid_nucleotide(stripped)

    if invalid:
        raise Error(f"Invalid nucleotide(s) in sequence: {invalid}")
    
    mRNA = stripped.upper().replace("T", "U").lower()
    return mRNA
        