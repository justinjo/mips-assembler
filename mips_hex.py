import mips_instr
from mips_instr import MipsISA

def gen_hex_instr(instructions):
	ISA = MipsISA()
	split_instructions = [instr.replace(',', ' ').split() for instr in instructions]
	for instr in split_instructions:
		if mips_instr.is_label(instr[0]):
			print(ISA.get_instr_opcode(instr[1]) >> 2)
		else:
			print(ISA.get_instr_opcode(instr[0]) >> 2)
	hex_instructions = instructions
	return hex_instructions


def lshift(n, shift):
	pass

