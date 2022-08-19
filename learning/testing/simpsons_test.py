#!/usr/bin/python3

def homer(sd="salad"):
   return f"You don't win friends with {sd}"

def milhouse(mh="milhouse"):
    return f"Everything is coming up {mh}"

def troymcclure(tm=3):
    if tm > 2:
        return f"2 minus {tm} equals negative fun!"
    else:
        return None

def test_homer():
    assert homer("doughnuts") == "You don't win friends with doughnuts"

def test_milhouse():
    assert milhouse("daffodils") == "Everything is coming up daffodils"

def test_troymcclure():
    assert troymcclure(5) == "2 minus 5 equals negative fun!"
    assert not troymcclure(1)

# def test_homer_fail():
#    assert homer("pretzels") == "You don't win friends with salad"


