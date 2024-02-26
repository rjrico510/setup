#!/usr/bin/env python3

def odd(n):
    return bool(n % 2)

def main():
    assert(any([]) == False)
    assert(any([0]) == False)
    assert(any([1]))
    assert(any([1,2]))
    assert(any([0, ""]) == False)
    assert(any([0, "", True]))
    assert(any([0, "", False]) == False)
    assert(any([0, "", 4]))
    assert(any(lambda x: isinstance(x, int) and x % 2 for x in [0, 1, 4]))
    assert(any(odd(x) for x in [0, 2, 4]) == False)
    assert(any(len(x) for x in {'a string', ''}))
    assert(any(len(x) for x in {tuple(), ''}) == False)
    print("success")





if __name__ == "__main__":
    main()