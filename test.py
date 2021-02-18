def are_anagrams(s1, s2, s3):
    l1=list(s1)
    l2=list(s2)
    l3=list(s3)

#jeśli nie są tej samej długości to na pewno nie są anagramami i dalsze sprawdzanie nie ma sensu
    if len(l1) != len(l2) or len(l2) != len(l3):
        return False
    for i in (l1):
        if i in l2:
 #jeśli litera z pierwszego słowa występuje w drugim to kasujemy ją z listy
            l2.remove(i)
        else:
#jeśli w słowie drugim brakuje litery ze słowa pierwszego to nie będzie to anagram
            return False

#sprawdzamy analogicznie słowo trzecie
    for i in l1:
        if i in l3:
            l3.remove(i)
        else:
            return False

#jeśli funkcja doszła do tego miejsca to znaczy że słowa są anagramami
    return True




