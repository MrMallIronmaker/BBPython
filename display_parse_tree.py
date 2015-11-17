import tkinter as tk
from block import Block
import parser

class Application(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.pack()
		self.frame = tk.Frame(self)
		self.frame.pack()
		self.display_source("""import parser
from symbol import sym_name
import token
from block import Block

def pretty_print(node, margin=""):
	if type(node) is tuple or type(node) is list:
		pretty_print(i, margin=margin+"|")

q = parser.suite("2**4*3")
tup = parser.st2tuple(q)
pretty_print(tup)""")

	def display_source(self, source):
		# parse it
		q = parser.suite(source)
		tup = parser.st2tuple(q)
		# display the AST
		self.display_ast(tup)

	def display_ast(self, ast):
		self.root_block = Block(self, ast)


root = tk.Tk()
app = Application(master=root)
app.mainloop()