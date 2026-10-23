from dops_2.modules.translate import chunk_by_three, translate_sequence

def test_chunk_by_three_check():
    assert chunk_by_three("acggtgcag") == ["acg", "gtg", "cag"]

def test_translate_aa():
    assert translate_sequence("aaaaaaaaa") == "KKK"

def test_translate_stop():
    assert translate_sequence("gaagaaugauga") == "EE**"

def test_translate_stop_ORF2():
    assert translate_sequence("gaagaaugauga", 2) == "KND"

def test_translate_stop_ORF3():
    assert translate_sequence("gaagaaugauga", 3) == "RMM"