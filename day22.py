def reconstruction(words, s):
    words = set(words)
    res = []

    n = len(s)
    i = j = 0

    while j < n:
        if s[i:j+1] in words:
            res.append(s[i:j+1])
            i = j + 1
        else:
            if j == n - 1:
                return None
        
        j += 1
    
    return res

dictionary = ['bed', 'bath', 'bedbath', 'and', 'beyond']
word = 'bedbathandbeyond'
result = [['bed', 'bath', 'and', 'beyond'], ['bedbath', 'and', 'beyond']]
assert reconstruction(dictionary, word) in result

dictionary = ['quick', 'brown', 'the', 'fox']
word = 'thequickbrownfox'
result = [['the','quick','brown','fox']]
assert reconstruction(dictionary, word) in result

dictionary = ['quick', 'the', 'fox']
word = 'thequickbrownfox'
assert reconstruction(dictionary, word) is None