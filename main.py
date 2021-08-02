def past(h, m, s):
    h = (h*60)*60
    m*=60
    s+=m+h
    return s*1000