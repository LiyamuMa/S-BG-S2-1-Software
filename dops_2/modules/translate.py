class Error(Exception):
    pass

codon_table = {
    
    # Phenylalanine (F), Leucine (L)
    "uuu": "F", "uuc": "F", "uua": "L", "uug": "L",
    "cuu": "L", "cuc": "L", "cua": "L", "cug": "L",

    # Isoleucine (I), Methionine (M) - start codon
    "auu": "I", "auc": "I", "aua": "I", "aug": "M",

    # Valine (V)
    "guu": "V", "guc": "V", "gua": "V", "gug": "V",

    # Serine (S)
    "ucu": "S", "ucc": "S", "uca": "S", "ucg": "S",
    "agu": "S", "agc": "S",

    # Proline (P)
    "ccu": "P", "ccc": "P", "cca": "P", "ccg": "P",

    # Threonine (T)
    "acu": "T", "acc": "T", "aca": "T", "acg": "T",

    # Alanine (A)
    "gcu": "A", "gcc": "A", "gca": "A", "gcg": "A",

    # Tyrosine (Y), Stop
    "uau": "Y", "uac": "Y", "uaa": "Stop", "uag": "Stop",

    # Histidine (H), Glutamine (Q)
    "cau": "H", "cac": "H", "caa": "Q", "cag": "Q",

    # Asparagine (N), Lysine (K)
    "aau": "N", "aac": "N", "aaa": "K", "aag": "K",

    # Aspartic acid (D), Glutamic acid (E)
    "gau": "D", "gac": "D", "gaa": "E", "gag": "E",

    # Cysteine (C), Stop, Tryptophan (W)
    "ugu": "C", "ugc": "C", "uga": "Stop", "ugg": "W",

    # Arginine (R)
    "cgu": "R", "cgc": "R", "cga": "R", "cgg": "R",
    "aga": "R", "agg": "R",

    # Glycine (G)
    "ggu": "G", "ggc": "G", "gga": "G", "ggg": "G",
}
       
#chunk them by three
def chunk_by_three(sequence, frame=1):

    """
    Splits the sequence into codons
    
    Reading starts at the positive given by ``frame`` and moves alone in 
    steps of three. Any leftover nucleotides at the end that do not make a
    full codon is dropped
    
    Args:
        sequence(str): The nucleotide sequence to split.
        frame (int, optional): The reading frame, where 1 starts at the first
        nucleotide (default), 2 at the second, and 3 at the third.
        
    Returns:
        list[str]: Codons. E.g. "ATGCCGA" -> ["ATG", "CCG"]
    """

    start = frame - 1
    codon_list = []

    for i in range(start, len(sequence) -2, 3):
        codon = sequence[i:i + 3]
        codon_list.append(codon)
    return codon_list

def translate_sequence(sequence, frame=1):
    """
    Transslates an mRNA sequence into protein sequence.

    The sequence is split into codons with ``chunk_by_three``, and each codon
    is looked up in ``codon_table``. Stop codons are written as "*". Translation
    does not stop at the first stop codon and is translated all the way through.

    Args:
        sequence(str): The mRNA sequence to be translated. Codons must match the
        keys of ``codon_table``.
        frame(int, optional): The reading frame, defaults to open reading frame 1.

    Returns:
        str: The protein sequence as one-letter amino acid codes, with "*" marking
        stop codons.

    Raises:
        KeyError: If a codon is not found in ``codon_table``.
    """

    list_of_codons = chunk_by_three(sequence, frame)
    protein = []
    
    for codon in list_of_codons:
        amino_acid = codon_table[codon]
        if amino_acid == "Stop":
            protein.append("*")
        else:
            protein.append(amino_acid)
    return "".join(protein)





