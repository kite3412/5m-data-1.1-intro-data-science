def count_repeats(string):
    count = 0
    lst = list(string)
    for i in lst:
        occur = string.count(i)
        if occur > 1:
            count += 1
    print(count)
    return

count_repeats("hello")
count_repeats("aeiou")