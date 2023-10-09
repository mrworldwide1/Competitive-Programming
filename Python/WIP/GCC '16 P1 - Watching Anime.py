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
# use list methods to remove entire range of hours weeb cannot watch anime
# or just use dictionary with key:value format as hour:availablity
totalHours = {}
N, A, C = (map(int, input().split()))

for hour in range(N):
    totalHours[hour+1] = "can"

for streaming in range(A):
    ai, bi = (map(int, input().split()))
    while ai <= bi:
        totalHours[ai] = "cannot"
        ai+=1


# print(hours)