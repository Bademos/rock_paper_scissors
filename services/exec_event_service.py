import json
def print_list(lst):
    for i in range(len(lst)):
        print(lst[i].replace('\xa0', ''))
hui = {}
with open("events.txt", "r") as f:
    hui = json.load(f)
while True:
    year = input("Input year:")
    if (int(year) > 0 and int(year) < 2000 ):
        print_list(hui[str(year)])
    else:
        break
