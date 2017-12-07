import sys
import mips_instr as mips
from mips_instr import MipsISA

def open_file(file_name):
	instr_queue = []
	file = open(file_name)
	for line in file:
		instr_queue.append(line)
	return instr_queue

if __name__ == '__main__':
	print('Running ' + sys.argv[0] + '...')
	num_files = len(sys.argv) - 1
	if num_files != 1:
		print('Please include a text file: mips_program')
		sys.exit()

	file_name = sys.argv[1]
	instructions = open_file(file_name)
	ISA = MipsISA()

	for instr in instructions:
		spaced_line = instr.replace(',', ' ')   # split the line by commas and spaces
		split_instr = spaced_line.split()
		if mips.is_label(split_instr[0]):
			print(ISA.get_instr_opcode(split_instr[1]) >> 2)
		else:
			print(ISA.get_instr_opcode(split_instr[0]) >> 2)
