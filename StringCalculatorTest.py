def test_single_number():
    assert StringCalculator.add("1") == 1

def test_two_numbers():
    assert StringCalculator.add("1,2") == 3

def test_multiple_numbers():
    assert StringCalculator.add("1,2,3,4,5") == 15

def test_newline_delimiters():
    assert StringCalculator.add("1\n2,3") == 6

def test_custom_delimiter():
    assert StringCalculator.add("//;\n1;2") == 3

def test_negative_numbers():
    with pytest.raises(Exception) as excinfo:
        StringCalculator.add("1,-2,3,-4")
    assert str(excinfo.value) == "Negatives not allowed: -2, -4"

def test_numbers_bigger_than_1000():
    assert StringCalculator.add("2,1001,1000") == 1002

def test_delimiters_of_any_length():
    assert StringCalculator.add("//[***]\n1***2***3") == 6
