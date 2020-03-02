import random


rand_list = [int(random.random() * 100) for i in range(10)]

# avg
avg_val = sum(rand_list) / len(rand_list)

# max
max_val = max(rand_list)

# min
min_val = min(rand_list)

# second max
snd_max_val = max([x for x in rand_list if x is not max(rand_list)])
# temp = list(rand_list)
# temp.remove(max(temp))
# snd_max_val = max(temp)

# second min
snd_min_val = min([x for x in rand_list if x is not min(rand_list)])
# temp = list(rand_list)
# temp.remove(min(temp))
# snd_min_val = min(temp)

# evens
evens_val = len([x for x in rand_list if x % 2 == 0])

print(rand_list)
print(f'{avg_val}\n{max_val}\n{min_val}\n{snd_max_val}\n{snd_min_val}\n{evens_val}\n')
