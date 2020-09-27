import re

amounts = r"thousand|million|billion"
number = r"\d+(,\d{3})*\.*\d*"
standard = fr"\${number}(-|\sto\s)?({number})?\s({amounts})"

def word_to_value(word):
	value_dict = {"thousand": 1000, "million": 1000000, "billion": 1000000000}
	return value_dict.get(word.lower(), 1)

def parse_word_syntax(string):
	stripped_string = string.replace(",", "")
	value = float(re.search(number, stripped_string).group())
	modifier = word_to_value(re.search(amounts, string, flags=re.I).group())
	return value*modifier

def parse_value_syntax(string):
	stripped_string = string.replace(",", "")
	return float(re.search(number, stripped_string).group())

def money_conversion(money):
	if type(money) == list:
		money = money[0]

	word_syntax = re.search(standard, money, flags=re.I)
	value_syntax = re.search(fr"\${number}", money)

	if word_syntax:
		return parse_word_syntax(word_syntax.group())
	elif value_syntax:
		return parse_value_syntax(value_syntax.group())
	else:
		return None