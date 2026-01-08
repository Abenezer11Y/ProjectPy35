test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

print(f"The original dictionary as provided in the project is {test_dict}")

k = int(input("Enter the frequency you want to check: "))
res = 0

for key in test_dict:
    if test_dict[key] == k:
        res += 1

print(f"The frequency of {k} is {str(res)}")