# task 1
# import os
#
# lines = 0
# countsymbols = 0
# countwords = 0
# if os.path.exists("text.txt"):
#     with open("text.txt", "r", encoding="utf-8") as f:
#         for line in f.readlines():
#             lines += 1
#             for i in line:
#                 if i != "\n":
#                     countsymbols += 1
#             countwords += len(line.split())
#     with open("text.txt", "r", encoding="utf-8") as f:
#         maxlen = 0
#         nummax = None
#         textmax = None
#         for number, line1 in enumerate(f, start=1):
#             clean_line2 = line1.strip()
#             if len(clean_line2) > maxlen:
#                 maxlen = len(clean_line2)
#                 nummax = number
#                 textmax = clean_line2
#
#     print(f'Рядків: {lines}')
#     print(f'Слів: {countwords}')
#     print(f'Символів: {countsymbols}')
#     print(f'Найдовший рядок:No{nummax}, {maxlen}')
#     print(f'Текст: {textmax}')
#task 2
# import os.path
#
# findline = input("Фрагмент: ")
#
# if os.path.exists("text.txt"):
#     with open("text.txt","r",encoding="utf-8") as file:
#         a = 0
#         for number,line in enumerate(file.readlines(), start=1):
#             if findline.strip().lower() in line.strip().lower():
#                 print(f'{number}: {line.strip()}')
#                 a += 1
#         if a == 0:
#             print("Збігів немає")
#task 3
# import os.path
# result = []
# if os.path.exists("students.txt"):
#     with open("students.txt","r", encoding="utf-8") as f:
#         for line in f:
#             student, score = line.strip().split(";")
#             if int(score) > 80:
#                 result.append([int(score), student])
# result=sorted(result, reverse=True)
# with open("result.txt","w", encoding="utf-8") as f:
#     for i in result:
#         f.write(f"{i[1]};{i[0]}\n")
#         f.write("\n")
# with open("result.txt","r", encoding="utf-8") as f:
#     print(f.readlines())
#task 4
def avarage(grades):
    if len(grades) > 0:
        return sum(grades) / len(grades)
    return 0

names = set()
scores = []
with open("grades.csv", 'r',encoding="utf-8") as f:
    for line in f:
        names.add(line.split(';')[0])
    print(names)
with open("grades.csv", 'r',encoding="utf-8") as f:
    lines = f.readlines()
    clear_lines = ""
    for line in lines:
        clear_line = line.strip()
        clear_lines += clear_line + "-"
    print(clear_lines)
    for n in names:
        s = []
        if n in clear_lines:
            parts = clear_line.split(';')
            print(parts)
            s.append(parts[2])
        print(n,s)
