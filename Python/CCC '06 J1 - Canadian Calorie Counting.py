b = input(); s = input(); dr = input(); de = input()
cals = 0

match b:
    case "1":
        cals+=461
    case "2":
        cals+=431
    case "3":
        cals+=420
    case "4":
        pass

match s:
    case "1":
        cals+=100
    case "2":
        cals+=57
    case "3":
        cals+=70
    case "4":
        pass
    
match dr:
    case  "1":
        cals+=130
    case  "2":
        cals+=160
    case  "3":
        cals+=118
    case  "4":
        pass
    
match de:
    case  "1":
        cals+=167
    case  "2":
        cals+=266
    case  "3":
        cals+=75
    case  "4":
        pass
print(f"Your total Calorie count is {cals}.")