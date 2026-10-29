class Error(Exception):
    pass

Valid = ["A", "C", "G", "T", "N"]  

def invalid_nucleotide(nucleotides):
    
    """
    Finds invalid nucleotides in a sequence i.e NOT A, C, G, T, and N

    Each character is converted to uppercase and compared against the module
    level ``Valid`` list. Each invalid character is reported once, in order
    of first appearance

    Args:
        nucleotides (str): The sequence to check. Whitespace is not skipped
        here, so will be reported as invalid

    Returns:
        list[str]: Unique invalid characters, uppercased. An empty list means
        the sequence is valid
    """

    invalid_log = []
    
    for N in nucleotides:
        if N.upper() not in Valid and N.upper() not in invalid_log:
            invalid_log.append(N.upper())
    return(invalid_log)

def transcribe_sequence(dna_sequence):
    """
    Transcribes a DNA sequence into mRNA

    Whitespace is stripped, the sequence validated, and T is replaced with U.
    The result is returned in lowercase.

    Args:
        dna_sequence(str): DNA sequence containing A, C, G, T, or N (case-insensitive).
        Spaces, tabs, and newlines are ignored

    Returns:
        str: mRNA sequence e.g. "ATGC" -> "augc"

    Raises:
        Error: Lists the invalid nucleotides if encountered in the dna_sequence
    """

    stripped = "".join(dna_sequence.split())

    invalid = invalid_nucleotide(stripped)

    if invalid:
        raise Error(f"Invalid nucleotide(s) in sequence: {invalid}")
    
    mRNA = stripped.lower().replace("t", "u")
    return mRNA