import mips_instr
from mips_instr import MipsInstr

def gen_hex_instr(instructions):
	labels = {}
	curr_address = 0
	curr_label = ''
	set_label = False
	mips_instructions = []
	hex_instructions = []

	# first pass
	for instr in instructions:
		new_instr = MipsInstr(instr, curr_address)

		if new_instr.is_only_label():
			curr_label = new_instr.get_label()
			set_label = True
			continue

		if set_label:
			new_instr.set_label(curr_label)
			set_label = False
		
		if new_instr.has_label():
			labels[new_instr.get_label()] = curr_address

		mips_instructions.append(new_instr)
		curr_address += 1

	# second pass
	for instr in mips_instructions:
		if instr.needs_address():
			instr.set_branch_addr(labels[instr.get_branch_label()])
		instr.build_hex()
		hex_instructions.append(instr.get_hex())

	return hex_instructions

'''
12110003
01084020
12530002
01294820
014a5020
016b5820
08000008
02108020
02318820

12110003
01084020
12530002
01294820
014a5020
016b5820
08000008
02108020
02318820
'''