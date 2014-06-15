
## Unit 3 Homework: parse/convert str regular expression to API

REGRAMMAR = grammar("""
RE => ## your description here
""", whitespace="")

def parse_re(pattern):
	return convert(parse('RE', pattern, REGRAMMAR))

def convert(tree):
	# your code here



#plus(opt(alt(lit('a'), lit('b'))))
#"(a|b)?+"
