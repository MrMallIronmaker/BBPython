import token
import symbol
import tkinter as tk

class Block():
	"Class for managing the graphical blocks that correpond to syntax nodes."

	BORDER_SQUARE = 0

	def __init__(self, parent, ast_node):
		"Construct a block from an optional node."
		self.id = ast_node[0]
		self.frame = tk.LabelFrame(parent.frame)

		if self.id < token.NT_OFFSET:
			# then it's a token
			self.code = ast_node[1]
			self.block_children = []
			label = tk.Label(self.frame, text=self.code)
			label.pack(side=tk.LEFT)
			self.label_children = [label]
		else:
			#self.code = ""
			# Temporary fix: show name of symbol
			self.code = symbol.sym_name[self.id]
			self.block_children = [Block(self, n) for n in ast_node[1:]]
			self.frame["text"] = self.code
		self.frame.pack(side=tk.LEFT)

	def init_graphics(self):

		# border
		self.frame["relief"] = tk.RAISED

		# TODO: color