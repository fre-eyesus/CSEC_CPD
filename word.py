s = input()

upper = []
lower = []
for string1 in s:
    if string1.isupper():
        upper.append(string1)
    else:
        lower.append(string1)

if len(upper) == len(lower):
    s_equal = str(s).lower()
    print(s_equal)
elif len(upper) < len(lower):
     s_l = str(s).lower()
     print(s_l)
elif len(lower) < len(upper):
    s_u = str(s).upper()
    print(s_u)


