import collections
import os, sys

def next(ary, start):
    j = start
    l = len(ary)
    ret = start - 1
    while j < l and ary[j]:
        ret = j
        j += 1
    return ret

linestring = open('find_the_min_input.txt').read()
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

    m = [0] * (4 * k)
    s = [0] * (k+1)
    m[0] = a
    if m[0] <= k:
        s[m[0]] = 1
    for i in xrange(1, k):
        m[i] = (b * m[i-1] + c) % r
        if m[i] < k+1:
            s[m[i]] += 1

    p = next(s, 0)
    m[k] = p + 1
    p = next(s, p+2)

    for i in xrange(k+1, n):
        if m[i-k-1] > p or s[m[i-k-1]] > 1:
            m[i] = p + 1
            if m[i-k-1] <= k:
                s[m[i-k-1]] -= 1
            s[m[i]] += 1
            p = next(s, p+2)
        else:
            m[i] = m[i-k-1]
        if p == k:
            break

    if p != k:
        print 'Case #%d: %d' % (case_num, m[n-1])
    else:
        print 'Case #%d: %d' % (case_num, m[i-k + (n-i+k+k) % (k+1)])
    case_num += 1
    limit -= 1
    if limit == 0:
        break