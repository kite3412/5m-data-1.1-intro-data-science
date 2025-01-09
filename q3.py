def count_vowels(string):
    count = 0
    vowels = "aeiou"
    for i in string:
        if i.lower() in vowels:
            count += 1
    print(count)
    return

count_vowels("hello")
count_vowels("aeiou")

