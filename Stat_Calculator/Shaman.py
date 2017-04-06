def shamanele(Mastery, Crit, Haste, Intellect, Versatility):
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
def shamanresto(Mastery, Crit, Haste, Intellect, Versatility):
    long(Mastery)
    Mastery *= 7.58
    long(Crit)
    Crit *= 6.08
    long(Haste)
    Haste *= 4.58
    long(Intellect)
    Intellect *= 9.08
    long(Versatility)
    Versatility *= 3.08
    Answer = Mastery + Crit + Haste + Intellect + Versatility
    return Answer
def shamanenh(Mastery, Crit, Haste, Agility, Versatility):
    long(Mastery)
    Mastery *= 7.52
    long(Crit)
    Crit *= 3.02
    long(Haste)
    Haste *= 6.02
    long(Agility)
    Agility *= 9.02
    long(Versatility)
    Versatility *= 4.52
    Answer = Mastery + Crit + Haste + Agility + Versatility
    return Answer

def ShamanSpecEntry(Spec):
    if Spec == "elemental" or Spec == "thesenate" or Spec == "senate" or Spec == "ele":
        i = 0
        while i < 2:
            shamele = [] * 5
            shamele.append(input("Mastery:"))
            shamele.append(input("Crit:"))
            shamele.append(input("Haste:"))
            shamele.append(input("Intellect:"))
            shamele.append(input("Versatility:"))
            Answer = shamanele(*shamele)
            print Answer
            i += 1
        input()
    elif Spec == "restoration" or Spec == "resto":
        i = 0
        while i < 2:
            shamresto = [] * 5
            shamresto.append(input("Mastery:"))
            shamresto.append(input("Crit:"))
            shamresto.append(input("Haste:"))
            shamresto.append(input("Intellect:"))
            shamresto.append(input("Versatility:"))
            Answer = shamanresto(*shamresto)
            print Answer
            i += 1
        input()
    elif Spec == "enhancement" or Spec == "enhance" or Spec == "enh":
        i = 0
        while i < 2:
            shamenh = [] * 5
            shamenh.append(input("Mastery:"))
            shamenh.append(input("Crit:"))
            shamenh.append(input("Haste:"))
            shamenh.append(input("Agility:"))
            shamenh.append(input("Versatility:"))
            Answer = shamanenh(*shamenh)
            print Answer
            i += 1
        input()
    else:
        print "Invalid spec entry."
        input()
