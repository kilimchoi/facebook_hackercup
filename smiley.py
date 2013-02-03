#wrong solution
def smiley(string):
	boolean = False
	open_paren_bool = False
	colon_bool = False
	paren_diff = 0
	for ch in string:
		if ch == "(":
			if colon_bool:
				paren_diff -= 1
				colon_bool = False
				continue
			paren_diff += 1
			open_paren_bool = True
		if ch == ":":
			colon_bool = True
		if ch == ")":
			if colon_bool:
				paren_diff -= 1
				colon_bool = False
				continue
			paren_diff -= 1
			open_paren_bool = False
		if ch.isalpha():
			boolean = True
		if ch == " ":
			boolean = True
	if paren_diff <= 0 and not open_paren_bool:
		boolean = True
	if paren_diff > 0:
		boolean = False
	if boolean:
		return "YES"
	return "NO"


linestring = open('smiley_input.txt').read()
line_arr = linestring.split('\n')
limit = line_arr[0]
limit = int(limit)
case_num = 1
for line in line_arr[1:]:
	print 'Case #%d: %s' % (case_num, smiley(line))
	case_num += 1
	limit -= 1
	if limit == 0:
		break

