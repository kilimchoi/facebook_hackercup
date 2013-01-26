import collections

def initial_seq(k, a, b, c, r):
    v = a
    for _ in xrange(k):
        yield v
        v = (b * v + c) % r

def find_min(n, k, a, b, c, r):
    m = [0] * (2 * k + 1)
    for i, v in enumerate(initial_seq(k, a, b, c, r)):
        m[i] = v
    ks = range(k+1)
    print "ks is: ", ks
    print " "
    s = collections.Counter(m[:k])
    print "s is: ", s
    for i in xrange(k, len(m)):
        m[i] = next(j for j in ks if not s[j])
        ks.remove(m[i])
        s[m[i-k]] -= 1
    return m[k + (n - k - 1) % (k + 1)]

linestring = open('min.txt').read()
line_arr = linestring.split('\n')
limit = line_arr[0]
limit = int(limit)
case_num = 1
import itertools as it
items = it.izip(it.islice(line_arr, 1, None, 2), it.islice(line_arr, 2, None, 2))
for line1, line2 in items:
    n, k = line1.split()
    n, k = int(n), int(k)
    a, b, c, r = line2.split()
    a, b, c, r = int(a), int(b), int(c), int(r)
    print 'Case #%d: %d' % (case_num, find_min(n, k, a, b, c, r))
    case_num += 1
    limit -= 1
    if limit == 0:
        break