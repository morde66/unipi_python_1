import json
file = open("dictionary.txt", "r")
y = file.read()
diction = json.loads(y)
file.close()

key_freq = {}


def key_count(diction):
    for keys, value in diction.items():
        if type(value) is dict:
            key_count(value)
            if (keys in key_freq):
                key_freq[keys] += 1
            else:
                key_freq[keys]=1
        elif (keys in key_freq):
            key_freq[keys] += 1
        else:
            key_freq[keys] = 1
        if type(value) is list:
            for i in range(len(value)):
                if type(value[i]) is dict:
                    key_count(value[i])


key_count(diction)

smth = max(key_freq.items(), key=lambda x: x[1])
max_keys = list()
for key, value in key_freq.items():
    if value == smth[1]:
        max_keys.append(key)
print("The most frequent keys are: ", max_keys)