from dops_2.modules.transcribe import transcribe_sequence, invalid_nucleotide

def test_transcribe_dna_uppercase():
    result = transcribe_sequence("AAAAAA")
    assert result == "aaaaaa"

def test_transcribe_dna_strip():
    result = transcribe_sequence("aaa aaa aaa")
    assert result == "aaaaaaaaa"

def test_invalid_nucleotide_log():
    result = invalid_nucleotide("bbbhhhddd")
    assert result == ["B", "H", "D"]

def test_invalid_nucleotide_emptylog():
    result = invalid_nucleotide("ACGTACGT")
    assert result == []