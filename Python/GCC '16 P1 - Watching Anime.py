# BRAINSTORMING
# https://dmoj.ca/problem/gcc16p1

# init = input().split("")
# N = range(int(init[1])); A = init[2]; C = init[3]
#
# e.g. 10 3 2
# init would = [10, 3, 2]
# N would = [1,2,3,4,5,6,7,8,9,10]
# A would = 3
# C would = 2

# from this point on, loops can be used and remove ai-ab & ci-di from N, inclusive.
# then finally print() the number of elements in N.

initialLine = input().split(" ")
N = range(int(initialLine[0])); A = range(int(initialLine[1])); C = range(int(initialLine[2]))