#inefficient but correct solution
import string
def compute_beauty(input):
	dict = {}
	beauty_num = 26
	result = 0
	input= input.lower()
	input = input.replace(" ", "")
	exclude = set(string.punctuation)
	for char in input:
		if char in dict:
			dict[char] += 1
		elif char not in exclude:
			dict[char] = 1
	import operator
	dict = sorted(dict.iteritems(), key=operator.itemgetter(1), reverse=True)
	for word, count in dict:
		result += beauty_num * count
		beauty_num -= 1
	return result
linestring = open('beautiful_strings.txt').read()
line_arr = linestring.split('\n')
limit = line_arr[0]
limit = int(limit)
case_num = 1
for line in line_arr[1:]:
	print 'Case #%d: %d' % (case_num, compute_beauty(line))
	case_num += 1
	limit -= 1
	if limit == 0:
		break
##limit = raw_input()
#limit = int(limit)
#case_num = 1
#while limit > 0:
	#str_input = raw_input()
	#print 'Case #%d: %d' % (case_num, compute_beauty(str_input))
	#case_num += 1
	#limit -= 1
