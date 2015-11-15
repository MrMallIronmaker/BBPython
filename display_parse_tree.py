import tkinter as tk
from block import Block
import parser

class Application(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.pack()
		self.frame = tk.Frame(self)
		self.frame.pack()
		self.display_source("16 * \"na\" + \" Watman\"")

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