"""
Given a 100MB log file that looks like this:

charles=3918
alice=0
bob=100
charles=3918
django=77
alice=0

Write a program that removes the duplicate lines and sorts the pairs
by value.
"""

"""
aaaaaaaaaaaaaaaaaaa=1231322
                 lo      hi
"""

# O(k) => O(logk)
def getPersonNumber(s):
    n = len(s)
    
    i = 0
    while i < n and s[i] != "=":
        i += 1
        
    person = s[:i]
    number = s[i+1:]
    return (person, number)
    

def removeDuplicatesAndSortByValue(arr):
    n = len(arr)
    d = collections.defaultdict(set)
    
    res = []
    
    # O(nlogk)
    for s in arr:
        person, number = getPersonNumber(s)
        d[number].add(person)
        
    # O(nlogn)
    sorted_items = sorted(d.items())
    
    # O(n)
    for number, people_set in sorted_items:
        for person in people_set:
            res.append(f'{person}={number}')
    
    return res