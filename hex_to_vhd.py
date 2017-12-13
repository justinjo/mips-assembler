# hex_to_vhd.py
#
# If you would like to run mips_assembler.py so that is generates a VHDL imem,
# use this command:
#
# python mips_assembler.py test.txt | python hex_to_vhd.py
#
# It will create a file defining an imem that is named based on the 
# IMEM_FILE_NAME variable

import fileinput

IMEM_FILE_NAME = "imem.vhd"

def hex_to_vhd(s):
	'''
	converts hex output of MIPS assembler so that it can be copy-pasted into
	a VHDL file
	'''
	num_bytes = 0
	mem_contents = ""
	for line in s.splitlines():
		for i in range(0,4):
			byte = line[(2*i):(2*i)+2]
			to_print = "x\"{!s}\",".format(byte)
			mem_contents += to_print
			num_bytes += 1

	mem_contents = mem_contents[:-1]
	return mem_contents, num_bytes

# Here, we will use the hex_to_vhd function to insert this into our file contained in 
# 
machine_code = ""
for line in fileinput.input():
	machine_code += line

mem_contents, num_bytes = hex_to_vhd(machine_code)

with open('imem_template.txt', 'r') as myfile:
    vhd_file = myfile.read()

vhd_file = vhd_file.format(num_bytes, mem_contents)

with open(IMEM_FILE_NAME, 'w') as new_file:
	new_file.write(vhd_file)
	new_file.close()