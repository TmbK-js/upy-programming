#average of the weather
#db: 32,35,40,50,29,25,34,35,37,40
weather = [32,35,40,50,29,25,34,35,37,40]
DO = weather[0]
LD = weather[-1]

print("Average of F and L: ", (DO + LD)/2)
print("Last Day hotter than Day one: ", (DO < LD))