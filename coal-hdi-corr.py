import csv

def readcsv(filepath):
    x = []
    with open(filepath, newline="") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            x.append(row)

    return x

def calcmean(x):
    return sum(x)/len(x)

def calccorr(x, y):
    x_mean = calcmean(x)
    y_mean = calcmean(y)

    sq_diff_from_mean_x = 0
    sq_diff_from_mean_y = 0
    prod_diff_from_mean = 0


    for i in x:
        sq_diff_from_mean_x += (i - x_mean) ** 2
        
    for j in y:
        sq_diff_from_mean_y += (j - y_mean) ** 2

    for x_i, y_i in zip(x, y):
        prod_diff_from_mean += (x_i - x_mean) * (y_i - y_mean)

    return prod_diff_from_mean/((sq_diff_from_mean_x * sq_diff_from_mean_y) ** 0.5)


file_1 = "Data - Coal - Correlations.csv"
file_2 = "Data - HDI - Correlations.csv"
a = list(readcsv(file_1))
b = list(readcsv(file_2))

corr = {}

for col in range(1,12):
    year = a[0][col]
    coal = []
    hdi = []
    for row in range(1,7):
        
        coal.append(float(a[row][col]))
        hdi.append(float(b[row][col]))

    corr[year] = calccorr(coal,hdi)

print("\n")
print (corr)  
print ("\n")
print("The average correlation is " + (str(calcmean(list(corr.values())))))

# end
