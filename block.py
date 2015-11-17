import token
import symbol
import tkinter as tk

class Block():
	"Class for managing the graphical blocks that correpond to syntax nodes."

	BORDER_SQUARE = 0

	def __init__(self, parent, ast_node):
		"Construct a block from an optional node."
		# First, check if it's worth making a subnode.
		while ast_node[0] >= token.NT_OFFSET and len(ast_node) <= 2:
			# if not, go down one level.
			ast_node = ast_node[1]

		# Initialize data we'll need to use later.
		self.id = ast_node[0]
		self.frame = tk.LabelFrame(parent.frame)

		# Is it a token [leaf of parse tree] or a symbol?
		if self.id < token.NT_OFFSET:
			# then it's a token
			self.code = ast_node[1]
			self.block_children = []
			label = tk.Label(self.frame, text=self.code)
			label.pack(side=tk.LEFT)
			self.label_children = [label]
		else:
			self.code = ""
			# debugging option on the line beneath
			# self.code = symbol.sym_name[self.id]
			self.block_children = [Block(self, n) for n in ast_node[1:]]
			self.frame["text"] = self.code
		self.init_graphics()

	def init_graphics(self):

		# border
		self.frame["relief"] = tk.RAISED

		# packing direction
		# TODO: check if the last literal is a newline, if so, pack TOP
		if len(self.block_children) > 0 and self.block_children[-1].id == token.NEWLINE:
			self.frame.pack(side=tk.TOP)
		else:
			self.frame.pack(side=tk.LEFT)

		# TODO: color