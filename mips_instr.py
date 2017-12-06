class MipsIsa:
	'''
	TODO: add documentation
	Core instruction set and pseudoinstructions added
	'''

	OP  = 'opcode'
	FUN = 'funct'
	FRM = 'format'
	FMT = 'fmt'
	FT  = 'ft'

	ISA =
	{
		# core instruction set
		'add'   : {OP: 0,  FUN: 32,   FRM: 'R'},
		'addi'  : {OP: 8,  FUN: None, FRM: 'I'},
		'addiu' : {OP: 9,  FUN: None, FRM: 'I'},
		'addu'  : {OP: 0,  FUN: 33,   FRM: 'R'},
		'and'   : {OP: 0,  FUN: 36,   FRM: 'R'},
		'andi'  : {OP: 12, FUN: 36,   FRM: 'I'},
		'beq'   : {OP: 4,  FUN: None, FRM: 'I'},
		'bne'   : {OP: 5,  FUN: None, FRM: 'I'},
		'j'     : {OP: 2,  FUN: None, FRM: 'J'},
		'jal'   : {OP: 3,  FUN: None, FRM: 'J'},
		'jr'    : {OP: 0,  FUN: 8,    FRM: 'R'},
		'lbu'   : {OP: 36, FUN: None, FRM: 'I'},
		'lhu'   : {OP: 37, FUN: None, FRM: 'I'},
		'll'    : {OP: 48, FUN: None, FRM: 'I'},
		'lui'   : {OP: 15, FUN: None, FRM: 'I'},
		'lw'    : {OP: 35, FUN: None, FRM: 'I'},
		'nor'   : {OP: 0,  FUN: 39,   FRM: 'R'},
		'or'    : {OP: 0,  FUN: 37,   FRM: 'R'},
		'ori'   : {OP: 13, FUN: None, FRM: 'I'},
		'slt'   : {OP: 0,  FUN: 42,   FRM: 'R'},
		'slti'  : {OP: 10, FUN: None, FRM: 'I'},
		'sltiu' : {OP: 11, FUN: None, FRM: 'I'},
		'sltu'  : {OP: 0,  FUN: 43,   FRM: 'R'},
		'sll'   : {OP: 0,  FUN: 0,    FRM: 'R'},
		'srl'   : {OP: 0,  FUN: 2,    FRM: 'R'},
		'sb'    : {OP: 40, FUN: None, FRM: 'I'},
		'sc'    : {OP: 56, FUN: None, FRM: 'I'},
		'sh'    : {OP: 41, FUN: None, FRM: 'I'},
		'sw'    : {OP: 43, FUN: None, FRM: 'I'},
		'sub'   : {OP: 0,  FUN: 34,   FRM: 'R'},
		'subu'  : {OP: 0,  FUN: 35,   FRM: 'R'},
	}

	def __init__(self):
		pass

	def getOpcode(self, instr):
		return ISA[instr][OP]

	def getFunction(self, instr):
		return ISA[instr][FUN]

	def getFormat(self, instr):
		return ISA[instr][FMT]
