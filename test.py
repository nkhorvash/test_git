import pandas as pd


dir = 'C://users/nkhor/PycharmProjects/data/'
text = dir + 'test_3.txt'

with open(text, 'r') as file:
    print(file.read())

test1 = pd.read_excel('C://users/nkhor/PycharmProjects/data/test_1.xlsx')

print(test1)