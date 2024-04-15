import csv
def runCode():
    with open('items.csv', 'r') as f:
        reader = csv.DictReader(f)
        item = list(reader)
        for i in item:
            print(i)
runCode()