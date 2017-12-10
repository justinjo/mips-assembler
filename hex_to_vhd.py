IMEM_VAR_NAME = "imemBytes"

def hex_to_vhd(s):
	'''
	converts hex output of MIPS assembler so that it can be copy-pasted into
	a VHDL file
	'''
	line_num = 0
	vhdl_lines = ""
	for line in s.splitlines():
		for i in range(0,4):
			byte = line[(2*i):(2*i)+2]
			to_print = "{!s}({:d}) <= x\"{!s}\";\n".format(IMEM_VAR_NAME,i+4*line_num, byte)
			vhdl_lines += to_print
		line_num += 1

	print(vhdl_lines)

hex_to_vhd("12300003\n01084020\n12720002")