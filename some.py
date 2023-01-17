#!/usr/bin/env python3

def some(coll, pred=lambda x:x):
    """Return true if pred(item) os true for some item in coll"""
    return next((True for item in coll if pred(item)), False)

def odd(n):
    return bool(n % 2)

def main():
    assert(some([0, "", True]))
    assert(some([0, "", False]) == False)
    assert(some([0, "", 4]))
    assert(some([0, 1, 4], lambda x: isinstance(x, int) and x % 2))
    assert(some([0, 2, 4], odd) == False)
    assert(some({'a string', ''}, len))
    assert(some({tuple(), ''}, len) == False)
    print("success")





if __name__ == "__main__":
    main()