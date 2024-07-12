
def mismatch_pos(s1, s2):
    idx = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            return idx

        idx += 1

    len_s1 = len(s1)
    len_s2 = len(s2)
    if len_s1 == len_s2:
        return -1   # Same strings, so no mismatch
    else:
        return idx



print (mismatch_pos('abc', 'abcd'), mismatch_pos('abcd','abc'))

