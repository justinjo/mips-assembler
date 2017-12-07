class MipsIsa:
	'''
	TODO: add documentation
	Core instruction set and pseudoinstructions added
	If any of the exported functions fail, they return None
	'''

	OP  = 'opcode'
	FUN = 'funct'
	FMT = 'format'

	ISA =
	{
		# core instruction set
		'add'   : {OP: 0,  FUN: 32,   FMT: 'R'},
		'addi'  : {OP: 8,  FUN: None, FMT: 'I'},
		'addiu' : {OP: 9,  FUN: None, FMT: 'I'},
		'addu'  : {OP: 0,  FUN: 33,   FMT: 'R'},
		'and'   : {OP: 0,  FUN: 36,   FMT: 'R'},
		'andi'  : {OP: 12, FUN: 36,   FMT: 'I'},
		'beq'   : {OP: 4,  FUN: None, FMT: 'I'},
		'bne'   : {OP: 5,  FUN: None, FMT: 'I'},
		'j'     : {OP: 2,  FUN: None, FMT: 'J'},
		'jal'   : {OP: 3,  FUN: None, FMT: 'J'},
		'jr'    : {OP: 0,  FUN: 8,    FMT: 'R'},
		'lbu'   : {OP: 36, FUN: None, FMT: 'I'},
		'lhu'   : {OP: 37, FUN: None, FMT: 'I'},
		'll'    : {OP: 48, FUN: None, FMT: 'I'},
		'lui'   : {OP: 15, FUN: None, FMT: 'I'},
		'lw'    : {OP: 35, FUN: None, FMT: 'I'},
		'nor'   : {OP: 0,  FUN: 39,   FMT: 'R'},
		'or'    : {OP: 0,  FUN: 37,   FMT: 'R'},
		'ori'   : {OP: 13, FUN: None, FMT: 'I'},
		'slt'   : {OP: 0,  FUN: 42,   FMT: 'R'},
		'slti'  : {OP: 10, FUN: None, FMT: 'I'},
		'sltiu' : {OP: 11, FUN: None, FMT: 'I'},
		'sltu'  : {OP: 0,  FUN: 43,   FMT: 'R'},
		'sll'   : {OP: 0,  FUN: 0,    FMT: 'R'},
		'srl'   : {OP: 0,  FUN: 2,    FMT: 'R'},
		'sb'    : {OP: 40, FUN: None, FMT: 'I'},
		'sc'    : {OP: 56, FUN: None, FMT: 'I'},
		'sh'    : {OP: 41, FUN: None, FMT: 'I'},
		'sw'    : {OP: 43, FUN: None, FMT: 'I'},
		'sub'   : {OP: 0,  FUN: 34,   FMT: 'R'},
		'subu'  : {OP: 0,  FUN: 35,   FMT: 'R'},
	}

	REG = 
	{
		'$zero' : 0,
		'$at'   : 1,
		'$v0'   : 2,
		'$v1'   : 3,
		'$a0' : 4,
		'$a1' : 5,
		'$a2' : 6,
		'$a3' : 7,
		'$t0' : 8,
		'$t1' : 9,
		'$t2' : 10,
		'$t3' : 11,
		'$t4' : 12,
		'$t5' : 13,
		'$t6' : 14,
		'$t7' : 15,
		'$s0' : 16,
		'$s1' : 17,
		'$s2' : 18,
		'$s3' : 19,
		'$s4' : 20,
		'$s5' : 21,
		'$s6' : 22,
		'$s7' : 23,
		'$t8' : 24,
		'$t9' : 25,
		'$k0' : 26,
		'$k1' : 27,
		'$gp' : 28,
		'$sp' : 29,
		'$fp' : 30,
		'$ra' : 31
	}

	def __init__(self):
		pass

	def getOpcode(self, instr):
		if instr not in self.ISA:
			return
		return self.ISA[instr][OP]

	def getFunction(self, instr):
		if instr not in self.ISA:
			return
		return self.ISA[instr][FUN]

	def getFormat(self, instr):
		if instr not in self.ISA:
			return
		return self.ISA[instr][FMT]

	def getRegNum(self, reg):
		if reg not in self.REG:
			return
		return self.REG[reg]

