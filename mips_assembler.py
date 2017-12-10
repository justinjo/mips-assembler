import sys
import mips_hex

'''
Supports core instruction set, labels, and some pseudoinstructions
Does not support directives, the core arithmetic instruction set, or comments
'''

def read_file(file_name):
	instr_queue = []
	file = open(file_name)
	for line in file:
		if line != '':
			instr_queue.append(line)
	return instr_queue

if __name__ == '__main__':
	print('Running ' + sys.argv[0] + '...')
	num_files = len(sys.argv) - 1
	if num_files != 1:
		print('Please include a text file containing the mips program')
		sys.exit()

	file_name = sys.argv[1]
	instructions = read_file(file_name)
	hex_instructions = mips_hex.gen_hex_instr(instructions)
	for instr in hex_instructions:
		print(instr)