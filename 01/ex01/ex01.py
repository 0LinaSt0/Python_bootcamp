import ex00
    
def create_purse(golds):
    return {"gold_ingots": golds}

def gold_in_purse(purse):
    gold = 0
    for key in purse:
        if key == "gold_ingots":
            gold += purse[key]
    return gold

def all_gold(*purses):
    gold_count = 0
    for purse in purses:
        if not purse:
            continue
        gold_count += gold_in_purse(purse)
    return gold_count

def gold_for_every_gentlemen(gold_count):
    equally_gold = gold_count // 3
    remainder = gold_count - (equally_gold * 3)
    gold_g0 = gold_g1 = gold_g2 = equally_gold

    while remainder:
        if remainder:
            gold_g0 += 1
            remainder -= 1
        else:
            break
        if remainder:
            gold_g1 += 1
            remainder -= 1
        else:
            break
        if remainder:
            gold_g2 += 1
            remainder -= 1
        else:
            break
  
    return (gold_g0, gold_g1, gold_g2) 

def result_booty(gentls_gold):
    p0 = create_purse(gentls_gold[0])
    p1 = create_purse(gentls_gold[1])
    p2 = create_purse(gentls_gold[2])
    return (p0, p1, p2)

def split_booty(*purses):
    booty = all_gold(*purses)
    
    return result_booty(gold_for_every_gentlemen(booty))


"""TESTS_CODE"""
if __name__ == "__main__":
    def test00():
        print("inpt: ", {"gold_ingots":3}, {"gold_ingots":2}, {"apples":10})
        print("outp: ", split_booty({"gold_ingots":3}, {"gold_ingots":2}, {"apples":10}))

    def test01():
        print("inpt: ", {"pies":3}, {"birds":2}, {"apples":10})
        print("outp: ", split_booty({"pies":3}, {"birds":2}, {"apples":10}))

    def test02():
        print("inpt: ", {"pies":3, "gold_ingots":1}, {"birds":2}, {"apples":10})
        print("outp: ", split_booty({"pies":3, "gold_ingots":1}, {"birds":2}, {"apples":10}))

    def test03():
        print("inpt: ", {"gold_ingots":0}, {"gold_ingots":0})
        print("outp: ", split_booty({"gold_ingots":0}, {"gold_ingots":0}))

    def test04():
        print("inpt: ", {"gold_ingots":565})
        print("outp: ", split_booty({"gold_ingots":565}))

    print("\t~~TEST00(default)~~")
    test00()
    print("\n\t~~TEST01(without_gold)~~")
    test01()
    print("\n\t~~TEST02(just_one_gold)~~")
    test02()
    print("\n\t~~TEST03(zero_gold)~~")
    test03()
    print("\n\t~~TEST04(many_gold)~~")
    test04()
