import csv

def frequentInPoem():
    txt = ''
    with open('poem.txt', 'r') as f:
        txt = txt +  f.read()
    words = txt.split()
    maxWord = ''
    maxCount = 0
    for i in words:
        if words.count(i) > maxCount and i!="I":
            maxWord = i
            maxCount = words.count(i)
    print(maxCount,',',maxWord)
# frequentInPoem() # uncomment to run Question 1

def stocksAnalyzer():
    stocks = []
    ratios = []
    with open('stocks.csv', 'r') as f:
        csvFile = csv.reader(f)
        next(csvFile)
        for i in csvFile:
            stocks.append(i)
    for i in stocks:
        pe = round(int(i[1])/int(i[2]), 2)
        priceToBook = round(int(i[1])/int(i[3]), 2)
        arr = {'Company Name': i[0], 'PE Ratio': pe, 'PB Ratio': priceToBook}
        ratios.append(arr)
    for i in ratios:
        print(i)
    with open('Output.csv', 'w', newline='') as f:
        fieldnames = ['Company Name', 'PE Ratio', 'PB Ratio']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for i in ratios:
            writer.writerow(i)

# stocksAnalyzer() # uncomment to run Question 2