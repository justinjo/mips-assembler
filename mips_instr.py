class MipsInstr:
	'''
	'''
	def __init__(self, instruction, address = None):
		self.__set_defaults__()
		self.set_instr(instruction, address)

	def __set_defaults__(self):
		self.hex = 0
		self.rd = 0
		self.rs = 0
		self.rt = 0
		self.shamt = 0
		self.funct = 0
		self.label = ''
		self.branch_label = ''
		self.immediate = None
		self.jump_address = None

	def set_instr(self, instruction, address = None):
		instr = instruction.replace(',', ' ').split()
		# if len(instr) == 1:
		# 	self.label = instr[0]
		# 	self.opcode = None
		# 	return
		self.address = address

		label_offset = 0
		if is_label(instr[0]):
			label_offset = 1
			self.label = instr[0][:-1]

		self.opcode = instr[0 + label_offset]
		self.opval = ISA[self.opcode][OP]
		self.format = ISA[self.opcode][FMT]
		self.funct = ISA[self.opcode][FUN]

		if self.format == 'R':
			self.rd = REG[instr[1 + label_offset]]
			if self.opcode == 'sll' or self.opcode == 'srl':
				self.rt = REG[instr[2 + label_offset]]
				self.shamt = int(instr[3 + label_offset])
			else:
				self.rs = REG[instr[2 + label_offset]]
				self.rt = REG[instr[3 + label_offset]]
		elif self.format == 'I':
			self.rs = REG[instr[1 + label_offset]]
			self.rt = REG[instr[2 + label_offset]]
			if self.opcode == 'sw':
				offset, reg = instr[3 + label_offset].replace(')', '(').split('(')
				#check if reg or label
				#TODO: sign extend
				self.immediate = 0
			elif self.opcode == 'beq':
				self.branch_label = instr[3 + label_offset]
			else:
				# TODO: sign extend
				self.immediate = int(instr[3 + label_offset])
		elif self.format == 'J':
			self.branch_label = instr[1 + label_offset]

	def build_hex(self):
		self.hex = self.opval << OP_SHIFT
		if self.format == 'R':
			self.hex |= self.rs << RS_SHIFT
			self.hex |= self.rt << RT_SHIFT
			self.hex |= self.rd << RD_SHIFT
			self.hex |= self.shamt << SH_SHIFT
			self.hex |= self.funct << FN_SHIFT
		elif self.format == 'I':
			self.hex |= self.rs << RS_SHIFT
			self.hex |= self.rt << RT_SHIFT
			self.hex |= self.immediate
		elif self.format == 'J':
			self.hex |= self.jump_address

	def get_hex(self):
		# return hex(self.hex)
		return '{0:#0{1}x}'.format(self.hex, 10)

	def is_only_label(self):
		return self.opcode is None

	def has_label(self):
		return self.label != ''

	def set_label(self, label):
		self.label = label[:-1]

	def get_label(self):
		return self.label

	def get_branch_label(self):
		return self.branch_label

	def set_branch_addr(self, address):
		if self.format == 'I':
			self.immediate = address - self.address - 1
		elif self.format == 'J':
			self.jump_address = address

	def needs_address(self):
		if self.format == 'I':
			return self.immediate is None
		elif self.format == 'J':
			return self.jump_address is None
		return False


'''
Core instruction set and pseudoinstructions added
If any of the exported functions fail, they return None
'''

OP_SHIFT = 26
RS_SHIFT = 21
RT_SHIFT = 16
RD_SHIFT = 11
SH_SHIFT = 6
FN_SHIFT = 0

OP  = 'opcode'
FUN = 'funct'
FMT = 'format'

ISA = {
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
	'nop'   : {OP: 0,  FUN: None, FMT: None}
}

REG = {
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

def get_instr_opcode(instr):
	if instr not in ISA:
		return
	return ISA[instr][OP]

def get_instr_function(instr):
	if instr not in ISA:
		return
	return ISA[instr][FUN]

def get_instr_format(instr):
	if instr not in ISA:
		return
	return ISA[instr][FMT]

def get_reg_num(reg):
	if reg not in REG:
		return
	return REG[reg]

def is_label(string):
	if string == '':
		return False
	return string[-1] == ':'





