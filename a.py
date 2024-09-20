import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from os import system
from sklearn.preprocessing import LabelEncoder , MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.metrics import accuracy_score , classification_report
from sklearn.svm import SVC
import warnings
warnings.filterwarnings('ignore')
names = ["Age","Workclass","Education","Marital_status","Occupation","Gender","Capital_gain","Capital_loss","Hours_per_Week","Country","Income"]
df = pd.read_csv("KiBord-OlympicChallenge2.csv" , names = names)
df1 = pd.read_csv("KiBord-OlympicChallenge2.csv" , names = names)
df["Workclass"] = df["Workclass"].replace(" ?" , "Uncertain")
df1["Workclass"] = df1["Workclass"].replace(" ?" , "Uncertain")
df = df.drop(index = 0)
df = df.reset_index(drop = True)
df1 = df1.drop(index = 0)
df1 = df1.reset_index(drop = True)
le = LabelEncoder()
df.Workclass = le.fit_transform(df.Workclass)
df.Education = le.fit_transform(df.Education)
df.Marital_status = le.fit_transform(df.Marital_status)
df.Occupation = le.fit_transform(df.Occupation)
df.Gender = le.fit_transform(df.Gender)
df.Country = le.fit_transform(df.Country)
df.Income = le.fit_transform(df.Income)
x = df[["Age","Workclass","Education","Marital_status","Occupation","Gender","Capital_gain","Capital_loss","Hours_per_Week","Country"]]
y = df[["Income"]]
x_train , x_test , y_train , y_test = train_test_split(x , y , test_size = .3 , random_state = 12)
model_gini = DecisionTreeClassifier(criterion = "gini" , random_state = 0)
model_gini.fit(x_train, y_train)
model = DecisionTreeClassifier(criterion = "entropy" , random_state = 0)
model.fit(x_train, y_train)
scal = MinMaxScaler()
bn = df[["Hours_per_Week"]]
dat = scal.fit_transform(df)
s1 = list()
s2 = list()
s3 = list()
s4 = list()
s5 = list()
s6 = list()
s7 = list()
s8 = list()
s9 = list()
s10 = list()
s11 = list()
for i in dat: s1.append(i[0])
for i in dat: s2.append(i[1])
for i in dat: s3.append(i[2])
for i in dat: s4.append(i[3])
for i in dat: s5.append(i[4])
for i in dat: s6.append(i[5])
for i in dat: s7.append(i[6])
for i in dat: s8.append(i[7])
for i in dat: s9.append(i[8])
for i in dat: s10.append(i[9])
for i in dat: s11.append(i[10])
dfg = df[["Age","Workclass","Education","Marital_status","Occupation","Gender","Capital_gain","Capital_loss","Hours_per_Week","Country","Income"]]
dfg["Age"] = s1
dfg["Workclass"] = s2
dfg["Education"] = s3
dfg["Marital_status"] = s4
dfg["Occupation"] = s5
dfg["Gender"] = s6
dfg["Capital_gain"] = s7
dfg["Capital_loss"] = s8
dfg["Hours_per_Week"] = s9
dfg["Country"] = s10
dfg["Income"] = s11
x = dfg[["Age","Workclass","Education","Marital_status","Occupation","Gender","Capital_gain","Capital_loss","Hours_per_Week","Country"]]
y = dfg[["Income"]]
x_train , x_test , y_train , y_test = train_test_split(x , y , test_size = .3 , random_state = 12)
model2 = DecisionTreeClassifier(criterion = "entropy" , random_state = 0)
model2.fit(x_train, y_train)
clf = SVC(kernel = "poly")
clf.fit(x,y)
x = df[["Age","Workclass","Education","Marital_status","Occupation","Gender","Capital_gain","Capital_loss","Hours_per_Week","Country"]]
y = df[["Income"]]
x_train , x_test , y_train , y_test = train_test_split(x , y , test_size = .3 , random_state = 12)
y_pred = clf.predict(x_test)
workclass = list(set(list(df1["Workclass"])))
education = list(set(list(df1["Education"])))
marital_status = list(set(list(df1["Marital_status"])))
occupation = list(set(list(df1["Occupation"])))
gender = list(set(list(df1["Gender"])))
country = list(set(list(df1["Country"])))

workclass_l = le.fit_transform(workclass)
education_l = le.fit_transform(education)
marital_status_l = le.fit_transform(marital_status)
occupation_l = le.fit_transform(occupation)
gender_l = le.fit_transform(gender)
country_l = le.fit_transform(country)
ender = list()
while True:
    ager = int(input("Age: "))
    if 120 >= ager >= 0:
        ender.append(ager)
        break
system("cls")
for i in range(len(workclass)): print(f"{i+1} : {workclass[i]}")
while True:
    inp = int(input("Enter: "))
    if 1 <= inp <= 7:
        ender.append(workclass_l[inp - 1])
        break
print("\n\n\n")
system("cls")

for i in range(len(education)): print(f"{i+1} : {education[i]}")
while True:
    inp = int(input("Enter: "))
    if 1 <= inp <= 16:
        ender.append(education_l[inp - 1])
        break
print("\n\n\n")
system("cls")

for i in range(len(marital_status)): print(f"{i+1} : {marital_status[i]}")
while True:
    inp = int(input("Enter: "))
    if 1 <= inp <= 3:
        ender.append(marital_status_l[inp - 1])
        break
print("\n\n\n")
system("cls")

for i in range(len(occupation)): print(f"{i+1} : {occupation[i]}")
while True:
    inp = int(input("Enter: "))
    if 1 <= inp <= 15:
        ender.append(occupation_l[inp - 1])
        break
print("\n\n\n")
system("cls")

for i in range(len(gender)): print(f"{i+1} : {gender[i]}")
while True:
    inp = int(input("Enter: "))
    if 1 <= inp <= 2:
        ender.append(gender_l[inp - 1])
        break
print("\n\n\n")
system("cls")

while True:
    ager = int(input("Capital_gain: "))
    if ager >= 0:
        ender.append(ager)
        break
print("\n\n\n")
system("cls")

while True:
    ager = int(input("Capital_loss: "))
    if ager >= 0:
        ender.append(ager)
        break
print("\n\n\n")
system("cls")

while True:
    ager = int(input("Hours_per_Week: "))
    if ager >= 0:
        ender.append(ager)
        break
for i in range(len(country)): print(f"{i+1} : {country[i]}")
while True:
    inp = int(input("Enter: "))
    if 1 <= inp <= 42:
        ender.append(country_l[inp - 1])
        break
print("\n\n\n")
system("cls")
a1 = model.predict([ender])
a2 = model2.predict([ender])
a3 = clf.predict([ender])
bishtar = 0
kamtar = 0
if a1 == 0: kamtar += 1
else: bishtar += 1

if a2 == 0: kamtar += 1
else: bishtar += 1

if a3 == 0: kamtar += 1
else: bishtar += 1

if kamtar > bishtar: print("Your income is less than or equal to fifty thousand coins")
else: print("Your income is more than fifty thousand coins")
input("")