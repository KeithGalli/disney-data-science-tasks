import pytest
from conversion import money_conversion

def test_standard():
	assert money_conversion("$3 million") == 3000000

def test_standard_double_digit():
	assert money_conversion("$99 million") == 99000000

def test_standard_with_decimal():
	assert money_conversion("$3.5 million") == 3500000

def test_standard_multiple_decimals():
	assert money_conversion("$1.234 million") == 1234000

def test_standard_billion():
	assert money_conversion("$1.25 billion") == 1250000000

def test_standard_thousand():
	assert money_conversion("$900.9 thousand") == 900900

def test_range():
	assert money_conversion("$3.5-4 million") == 3500000

def test_range_with_to():
	assert money_conversion("$3.5 to 4 million") == 3500000

def test_number():
	assert money_conversion("$950000") == 950000

def test_number_with_commas():
	assert money_conversion("$127,850,000") == 127850000

def test_number_with_commas_and_decimals():
	assert money_conversion("$10,000,000.50") == 10000000.5

def test_number_with_commas_middle():
	assert money_conversion("estimated $5,000,000 (USD)") == 5000000

def test_other_currency():
	assert money_conversion("60 million Norwegian Kroner (around $8.7 million in 1989)") == 8700000

def test_list():
	assert money_conversion(['$410.6 million (gross)', '$378.5 million (net)']) == 410600000

def test_unkown():
	assert money_conversion("70 crore") is None