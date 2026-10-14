#task 1
# import os
#
# lines = 0
# countsymbols = 0
# countwords = 0
# if os.path.exists("text.txt"):
#     with open("text.txt", "r", encoding="utf-8") as f:
#
#         for line in f.readlines():
#             clear_line = line.strip()
#             lines += 1
#             maxlenthline = 0
#             for i in line:
#                 if not i == " " and not i == "\n":
#                     countsymbols += 1
#             countwords += len(line.split(" "))
#             if len(clear_line) > maxlenthline:
#                 maxlenthline = len(clear_line)
# if os.path.exists("text.txt"):
#     with open("text.txt", "r", encoding="utf-8") as f:
#         max = 0
#         nummax = None
#         textmax = None
#         for number, line1 in enumerate(f):
#             clean_line2 = line1.strip()
#             if len(clean_line2) > max:
#                 max = len(clean_line2)
#                 nummax = number
#                 textmax = clean_line2
#
# print(f'Рядків: {lines}')
# print(f'Слів: {countwords}')
# print(f'Символів: {countsymbols}')
# print(f'Найдовший рядок:No{nummax}, {max}')
# print(f'Текст: {textmax}')
#task 2
with open