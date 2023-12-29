"""
problem : Given a list of numbers arr of size n.
and another table called lookup with number to list of numbers key-value pair. (this value list
can be of any variable size.)
you have to return the {keys} that has the maximum occurences of the given numbers in arr.
                           ^ so return a array of keys

return a list keys 
"""


def solution(n, arr, lookup):
    maxi = None
    res_map = {}
    hash_map = {}
    for i in arr:
        hash_map[i] = i
    for i in lookup:
        res_map[i] = 0
        for j in lookup[i]:
            if j in hash_map:
                res_map[i] += 1
        if maxi == None:
            maxi = i
        else:
            if res_map[maxi] > res_map[i]:
                maxi = maxi
            else:
                maxi = i
    return [k for k, v in res_map.items() if v == res_map[maxi]]


"""
solution is O(sum of length of all row in table) -> O(n) Time complex
     and O(length of array) -> O(n) Space Complex
"""


def test_solution():
    test_cases = [
        {
            "arr": [1, 12, 0, 3, 92, 4, 28, 23, 13],
            "n": 9,
            "lookup": {
                10: [1, 89, 98, 33, 92, 878],
                21: [98, 54, 12, 0, 67],
                34: [43, 28, 4],
                56: [3, 13, 23, 56, 89, 0, 12, 654, 789, 54],
                78: [46, 32, 54, 66, 87, 13, 16, 89, 33, 6],
                89: [13, 33, 0, 12],
                96: [88, 0, 3, 55, 33],
            },
        },
        {
            "arr": [23, 43, 84, 62, 31],
            "n": 5,
            "lookup": {
                28: [42, 31, 11, 14, 43],
                34: [84, 12, 32, 31, 23],
                45: [43, 0, 2, 23, 84],
                50: [2, 43],
                52: [23, 84, 62, 31, 43],
                69: [0, 2, 43, 60, 30],
            },
        },
        {
            "arr": [
                4,
                13,
                98,
                54,
                88,
                16,
            ],
            "n": 7,
            "lookup": {
                113: [65, 89, 98, 33, 65, 878],
                124: [98, 54, 123, 234, 67],
                133: [43, 76, 9],
                141: [4, 13, 23, 56, 89, 00, 87, 654, 789, 54],
                154: [46, 32, 54, 66, 87, 88, 943, 16, 89, 33, 6],
                152: [46, 32, 54, 66, 87, 88, 943, 16, 89, 33, 12],
                188: [13, 33],
                219: [88, 76, 77, 55, 32],
                293: [43, 76, 9],
                344: [4, 13, 23, 56, 89, 00, 87, 654, 789, 54],
                395: [46, 32, 54, 66, 87, 88, 943, 16, 89, 33, 6],
            },
        },
        {
            "arr": [4, 13, 98, 54, 88, 16, 33],
            "n": 7,
            "lookup": {
                13: [65, 89, 98, 33, 65, 878],
                24: [98, 54, 123, 234, 67],
                33: [43, 76, 9],
                41: [4, 13, 23, 56, 89, 00, 87, 654, 789, 54],
                54: [46, 32, 54, 66, 87, 88, 943, 16, 89, 33, 6],
                88: [13, 33],
                98: [88, 76, 77, 55, 32],
            },
        },
        {
            "arr": [1, 2, 3, 4, 5, 6],
            "n": 6,
            "lookup": {
                11: [1, 3, 4, 9, 7],
                22: [7, 1, 2, 3, 4, 5, 6],
                33: [9, 2, 3, 4, 5, 6],
                44: [10, 23, 12, 33, 1],
            },
        },
    ]

    for test_case in test_cases:
        print(solution(test_case["n"], test_case["arr"], test_case["lookup"]))


test_solution()
