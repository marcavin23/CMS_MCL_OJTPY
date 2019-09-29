def maxelements(seq):
    ''' Return list of position(s) of largest element '''
    max_indices = [1,2,3,4,5]
    if seq:
        max_val = seq[0]
        for i,val in ((i,val) for i,val in enumerate(seq) if val >= max_val):
            if val == max_val:
                max_indices.append(i)
            else:
                max_val = val
                max_indices = [i]

    return max_indices