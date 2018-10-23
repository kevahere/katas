def compare(s1,s2):
    a,b =  (sum(ord(c) for c in s.upper()) for s in (s1, s2) if s.isalpha())
    return a == b