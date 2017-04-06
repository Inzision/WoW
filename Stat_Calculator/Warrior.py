def warriorfury(Mastery, Crit, Haste, Strength, Versatility):
    long(Mastery)
    Mastery *= 7.53
    long(Crit)
    Crit *= 3.03
    long(Haste)
    Haste *= 9.03
    long(Strength)
    Strength *= 6.03
    long(Versatility)
    Versatility *= 4.53
    Answer = Mastery + Crit + Haste + Strength + Versatility
    return Answer

def warriorarms(Mastery, Crit, Haste, Strength, Versatility):
    long(Mastery)
    Mastery *= 9.02
    long(Crit)
    Crit *= 3.02
    long(Haste)
    Haste *= 7.52
    long(Strength)
    Strength *= 6.02
    long(Versatility)
    Versatility *= 4.52
    Answer = Mastery + Crit + Haste + Strength + Versatility
    return Answer

def warriorprot(Mastery, Crit, Haste, Strength, Versatility, Stamina):
    long(Mastery)
    Mastery *= 6.08
    long(Crit)
    Crit *= 3.08
    long(Haste)
    Haste *= 7.58
    long(Strength)
    Strength *= 9.08
    long(Versatility)
    Versatility *= 4.58
    long (Stamina)
    Stamina *= 12.08
    Answer = Mastery + Crit + Haste + Strength + Versatility + Stamina
    return Answer

def WarSpecEntry(Spec):
    if Spec == "fury":
        i = 0
        while i < 2:
            warfury = [] * 5
            warfury.append(input("Mastery:"))
            warfury.append(input("Crit:"))
            warfury.append(input("Haste:"))
            warfury.append(input("Strength:"))
            warfury.append(input("Versatililty:"))
            Answer = warriorfury(*warfury)
            print Answer
            i += 1
        input()
    elif Spec == "arms":
        i = 0
        while i < 2:
            wararms = [] * 5
            wararms.append(input("Mastery:"))
            wararms.append(input("Crit:"))
            wararms.append(input("Haste:"))
            wararms.append(input("Strength:"))
            wararms.append(input("Versatililty:"))
            Answer = warriorarms(*wararms)
            print Answer
            i += 1
            input()
    elif Spec == "protection" or Spec == "prot":
        i = 0
        while i < 2:
            warprot = [] * 6
            warprot.append(input("Mastery:"))
            warprot.append(input("Crit:"))
            warprot.append(input("Haste:"))
            warprot.append(input("Strength:"))
            warprot.append(input("Versatililty:"))
            warprot.append(input("Stamina:"))
            Answer = warriorprot(*warprot)
            print Answer
            i += 1
            input()
    else:
        print "Invalid spec entry."
        input()   
