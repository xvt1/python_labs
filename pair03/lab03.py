#task 1
# inp = input("Ведіть рядок: ")
# print("Символів: ", len(inp))
# vowels = "аеєиіїоуюяaeiou" # не зряяяя документацію перечитую)))) воно мені буде требааа)))) дякуююю за доккументаціююю
# chars = 0
# digits = 0
# space = 0
# vowels_in_inp = 0
# for char in inp:
#     if(char.isalpha()):
#         chars += 1
#     if(char.isdigit()):
#         digits += 1
#     if(char == " "):
#         space += 1
#     if(char.lower() in vowels):
#         vowels_in_inp += 1
# print("Літер: ", chars)
# print("Цифр: ", digits)
# print("Пробілів: ", space)
# print("Голосних: ", vowels_in_inp)
# print("Слів: ",len(inp.split()))

#task 2
# inp = input("Напишіть ПІБ: ").strip().title()
#
# words = inp.split()
# if (len(words) == 3):
#     print(words[0],words[1][0] +"."+ words[2][0]+".")
# else:
#     print("ПІБ має складатися з трьох слів")

#task 3
# word1 = input("Ведіть слово 1: ").strip().lower().replace(" ", "")
# word2 = input("Ведіть слово 2: ").strip().lower().replace(" ", "")
#
# print("Слово 1: " + word1)
# print("Слово 2: " + word2)
#
# if sorted(word1) == sorted(word2):
#     print("Рядки є анаграмами.")
# else:
#     print("Рядки не є анаграмами.")
#task 4

# inp = input("Ведіть рядок ")

#task 4
def analyze(sentence):
    words = sentence.split()
    if not words:
        print("Речення порожнє")
        return

    max_len = max(len(w) for w in words)
    min_len = min(len(w) for w in words)

    longest = []
    shortest = []
    for w in words:
        if len(w) == max_len and w not in longest:
            longest.append(w)
        if len(w) == min_len and w not in shortest:
            shortest.append(w)

    unique = len(set(w.lower() for w in words))

    print("Найдовші:", ", ".join(longest))
    print("Найкоротші:", ", ".join(shortest))
    print("Унікальних слів:", unique)


sentence = input("Введіть речення: ")
analyze(sentence)

old_word = input("Введіть слово, яке потрібно замінити: ")
new_word = input("Введіть нове слово: ")

new_words = []
for w in sentence.split():
    if w.lower() == old_word.lower():
        new_words.append(new_word)
    else:
        new_words.append(w)

print("Після заміни:", " ".join(new_words))