def get_count(sentence):
    s = 0
    for i in 'aeiou':
        s += sentence.count(i)
    return(s)