def are_anagrams(s1, s2, s3):
    # Tutaj umieść swój kod
    l1=list(s1)
    l2=list(s2)
    l3=list(s3)
    for i in (l1):
        if i in l2:
            l2.remove(i)
        else:
            return False
    if len(l2) == 0:
        for i in l1:
            if i in l3:
                l3.remove(i)
            else:
                return False
    if len(l3) == 0:
        return True
    else:
        return False


