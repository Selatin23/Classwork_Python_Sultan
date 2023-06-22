'''first = [3523, 23, 235552, 2123, 5324]
first.append(12342)
print(first)

second = [23, 5, 235, 12, 23]
second.extend(first)
print(second)

second.insert(2, 9000000000000000)
print(second)

second.remove(5)
print(second)

second.pop(1)
print(second)

group216 = ["A", "S", "D", "F", "G"]
group216.remove("A")
group216_lost = group216.pop(-1)
print(group216)
print(group216_lost)
group216.clear()
print(group216)'''

'''letters = ['Q', 'W', 'E', 'R', 'T', 'Y']
index = letters.index('R')
count = letters.count('R')
sort_letters = letters.sort(reverse=True)
print(index)
print(count)
print(sort_letters)
print(letters)

def get_lenght(text):
    return len(text)

def get_second_symbol(text):
    return text[1]

letters = ['QA', 'WS', 'ED', 'RF', 'TG', 'YH']
letters.sort()
print(letters)
letters.sort(key=get_lenght)
print(letters)
letters.sort(key=get_second_symbol, reverse=True)
print(letters)

iterm = letters.pop(-2)
print(letters)
print(iterm)'''

'''letters = ['QA', 'WS', 'ED', 'RF', 'TG', 'YH']
letters.reverse()
print(letters)
letters2 = letters.copy()
letters2.pop(-1)
print(letters2)
print(letters)

table = [
    [10, 14, 87],
    [34, 20, 17],
    [57, 40, 19]
]

other_table = table.copy()
other_table [1] = 0
other_table [2] [2] = 100
print(table)
print(other_table)'''

leap_years = [x + 2000 for x in range(0, 30, 4)]
print(leap_years)