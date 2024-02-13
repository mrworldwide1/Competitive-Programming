N = int(input())

T = 0

for i in range(N):
    pepepr = input()
    if pepepr == "Poblano":
        T+= 1500
    elif pepepr == "Mirasol":
        T+=6000
    elif pepepr == "Serrano":
        T+=15500
    elif pepepr == "Cayenne":
        T+=40000
    elif pepepr == "Thai":
        T+=75000
    elif pepepr == "Habanero":
        T+=125000

print(T)

# alt method of using dict instead
# # spicelist = {
# "Poblano" : 1500,
# "Mirasol" : 6000,
# "Serrano" : 15500,
#}
#
# T += spicelist[inpput]
##
#
#