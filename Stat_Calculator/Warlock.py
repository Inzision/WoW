def warlockaff(Mastery, Crit, Haste, Intellect, Versatility):
    long(Mastery)
    Mastery *= 9.04
    long(Crit)
    Crit *= 7.54
    long(Haste)
    Haste *= 6.79
    long(Intellect)
    Intellect *= 4.54
    long(Versatility)
    Versatility *= 3.04
    Answer = Mastery + Crit + Haste + Intellect + Versatility
    return Answer

def warlockdem(Mastery, Crit, Haste, Intellect, Versatility):
    long(Mastery)
    Mastery *= 4.53
    long(Crit)
    Crit *= 6.03
    long(Haste)
    Haste *= 9.03
    long(Intellect)
    Intellect *= 7.53
    long(Versatility)
    Versatility *= 3.03
    Answer = Mastery + Crit + Haste + Intellect + Versatility
    return Answer

def warlockdest(Mastery, Crit, Haste, Intellect, Versatility):
    long(Mastery)
    Mastery *= 3.04
    long(Crit)
    Crit *= 6.04
    long(Haste)
    Haste *= 7.54
    long(Intellect)
    Intellect *= 9.04
    long(Versatility)
    Versatility *= 4.54
    Answer = Mastery + Crit + Haste + Intellect + Versatility
    return Answer

def WarlockSpecEntry(Spec):
    if Spec == "affliction" or Spec == "aff":
        i = 0
        while i < 2:
            lockaff = [] * 5
            lockaff.append(input("Mastery:"))
            lockaff.append(input("Crit:"))
            lockaff.append(input("Haste:"))
            lockaff.append(input("Intellect:"))
            lockaff.append(input("Versatility:"))
            Answer = warlockaff(*lockaff)
            print Answer
            i += 1
        input()
    elif Spec == "demonology" or Spec == "demo":
        i = 0
        while i < 2:
            lockdem = [] * 5
            lockdem.append(input("Mastery:"))
            lockdem.append(input("Crit:"))
            lockdem.append(input("Haste:"))
            lockdem.append(input("Intellect:"))
            lockdem.append(input("Versatility:"))
            Answer = warlockdem(*lockdem)
            print Answer
            i += 1
        input()
    elif Spec == "destruction" or Spec == "destro":
        i = 0
        while i < 2:
            lockdest = [] * 5
            lockdest.append(input("Mastery:"))
            lockdest.append(input("Crit:"))
            lockdest.append(input("Haste:"))
            lockdest.append(input("Intellect:"))
            lockdest.append(input("Versatility:"))
            Answer = warlockdest(*lockdest)
            print Answer
            i += 1
        input()
    else:
        print "Invalid spec entry."
        input()
