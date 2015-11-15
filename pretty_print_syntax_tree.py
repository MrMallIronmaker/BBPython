import parser
from symbol import sym_name
import token
from block import Block

def pretty_print(node, margin=""):
	if type(node) is tuple or type(node) is list:
		for i in node:
			pretty_print(i, margin=margin+"|")
	elif type(node) is int:
		try:
			if node < token.NT_OFFSET:
				print(margin + token.tok_name[node])
			else:
				print(margin + sym_name[node])
		except KeyError:
			print("Shoot, it borked. Blame Paul.")
	elif type(node) is str:
		print(margin + "|" + node)
	else:
		print("error")

q = parser.suite("2**4*3")
tup = parser.st2tuple(q)
pretty_print(tup)