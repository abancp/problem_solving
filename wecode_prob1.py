import datetime
import json

s = datetime.datetime.now()

"""
 _________________________________________________
|_____testcase____|___size___|__ time__|__result__|
| small_testcase1 |   7.4 mb |  0.21 s | ['49']   |
| small_testcase2 |   6.4 mb |  0.17 s | ['37']   |
| small_testcase3 |  26.9 mb |  0.77 s | ['75']   |
| small_testcase4 |  21.4 mb |  0.62 s | ['145']  |
|_small_testcase5_|_ 33.0_mb_|__1.04 s_|_['184']__|
|_________________________________________________|
| large_testcase1 | 206.0 mb |  5.07 s | ['1033'] |
| large_testcase2 | 389.6 mb |  ---- s | ['---']  |
| large_testcase3 |  81.1 mb |  1.92 s | ['715']  |
| large_testcase4 | 167.4 mb |  0.21 s | ['911']  |
|_large_testcase5_|_111.0_mb_|__2.95 s_|_['250']__|
|_________________|__________|_________|__________|

"""


def sold():
    with open("/home/aban/Desktop/Python/problem solving/small_testcase2.txt", "r") as f:
        maxi = None
        c = 1
        lookup = None
        hash_map = {}
        res_map = {}
        for item in f:
            if c == 2:
                for o in json.loads(item):
                    hash_map[o] = o
            if c == 3:
                lookup = json.loads(item)
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
                print(maxi)
                print([k for k, v in res_map.items() if v == res_map[maxi]])
                # print(list(res_map.keys()))
            c += 1

# def solo():
#     with open("/home/aban/Desktop/Python/problem solving/large_testcase2.txt", "r") as f:
#         maxi = None
#         c = 1
#         lookup = None
#         hash_map = {}
#         res_map = {}
#         for item in f:
#             if c == 3:
#                 json.loads(item)
#             c += 1
sold()


print(datetime.datetime.now() - s)
