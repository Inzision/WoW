def priestshadow(Mastery, Crit, Haste, Intellect, Versatility):
    long(Mastery)
    Mastery *= 4.56
    long(Crit)
    Crit *= 7.56
    long(Haste)
    Haste *= 6.06
    long(Intellect)
    Intellect *= 9.06
    long(Versatility)
    Versatility *= 3.06
    Answer = Mastery + Crit + Haste + Intellect + Versatility
    return Answer

def priestholy(Mastery, Crit, Haste, Intellect, Versatility):
    long(Mastery) 
    Mastery *= 7.53
    long(Crit) 
    Crit *= 6.03
    long(Haste) 
    Haste *= 4.53
    long(Intellect)
    Intellect *= 9.03
    long(Versatility)
    Versatility *= 3.03
    Answer = Mastery + Crit + Haste + Intellect + Versatility
    return Answer

def priestdiscipline(Mastery, Crit, Haste, Intellect, Versatility):
    long(Mastery)
    Mastery *= 4.56
    long(Crit)
    Crit *= 6.06
    long(Haste)
    Haste *= 7.56
    long(Intellect)
    Intellect *= 9.06
    long(Versatility)
    Versatility *= 3.06
    Answer = Mastery + Crit + Haste + Intellect + Versatility
    return Answer

def PriestSpecEntry(Spec):
    if Spec == "shadow" or Spec == "spriest":
        i = 0
        while i < 2:
            priestshad = [] * 5
            priestshad.append(input("Mastery:"))
            priestshad.append(input("Crit:"))
            priestshad.append(input("Haste:"))
            priestshad.append(input("Intellect:"))
            priestshad.append(input("Versatility:"))
            Answer = priestshadow(*priestshad)
            print Answer
            i += 1
        input()
    elif Spec == "holy":
        i = 0
        while i < 2:
            priesthol= [] * 5
            priesthol.append(input("Mastery:"))
            priesthol.append(input("Crit:"))
            priesthol.append(input("Haste:"))
            priesthol.append(input("Intellect:"))
            priesthol.append(input("Versatility:"))
            Answer = priestholy(*priesthol)
            print Answer
            i += 1
        input()
    elif Spec == "discipline" or Spec == "disc":
        i = 0
        while i < 2:
            priestdisc = [] * 5
            priestdisc.append(input("Mastery:"))
            priestdisc.append(input("Crit:"))
            priestdisc.append(input("Haste:"))
            priestdisc.append(input("Intellect:"))
            priestdisc.append(input("Versatility:"))
            Answer = priestdiscipline(*priestdisc)
            print Answer
            i += 1
        input()
    else:
        print "Invalid spec entry."
        input()
