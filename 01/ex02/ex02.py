import ex00

def exec_funcs(func):
    def wrapper(*args):
        print("SQUEAK")
        return func(*args)
    return wrapper

@exec_funcs
def wrapp_empty(purse):
    return ex00.empty(purse)

@exec_funcs
def wrapp_add_ingot(prune):
    return ex00.add_ingot(prune)

@exec_funcs
def wrapp_get_ingot(purse):
    return ex00.get_ingot(purse)


"""TESTS_CODE"""
if __name__ == "__main__":
    def test00(purse):
        print("Add: ", end ='')
        d0 = wrapp_add_ingot(purse)
        print("      ", d0)
        print("Get: ", end ='')
        d1 = wrapp_get_ingot(d0)
        print("      ", d1)
        print("Add: ", end ='')
        d2 = wrapp_add_ingot(d1)
        print("      ", d2)
        print("Empty: ", end ='')
        d3 = wrapp_empty(d2)
        print("      ", d3)

    purse = {"gold_ingots": 5}
    print("\nINITIAL_PURSE: ", purse)
    print("\n\t~~TEST00(all_functs)~~")
    test00(purse)
