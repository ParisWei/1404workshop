text = input("Enter a sentence:")
def num(s):
    list = s. split()
    dict = {}
    for item in list:
        if item in dict:
            dict[item] += 1
        else:
             dict[item] = 1
    return dict

word = text.strip()
out = num(word)

for key in out:
    print(key,":",out[key])
