import csv
import math

with open("data.csv", newline = "") as f :
    c = csv.reader(f)
    l = list(c)



marks = []

for i in range(len(l)):
    n = l[i][0]
    marks.append(float(n))

total = 0
for a in marks:
    total = total + a

mean = total/len(marks)
print(mean)

xjsub = []

for i in marks:
    a = int(i) - mean
    s = a**2
    xjsub.append(s)


addition = 0
for t in xjsub:
    addition = addition + t


result = addition/(len(marks)-1)
sd = math.sqrt(result)
print(sd)