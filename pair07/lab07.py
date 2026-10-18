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

students = set()
studentsgrades = dict()
result = dict()
maxresultstudents = []
with open("grades.csv","r",encoding="utf-8") as f:
    g = f.readlines()
    for i in g:
        parts = i.split(";")
        students.add(parts[0])
    for i in students:
        for j in g:
            parts = j.split(";")
            if i == parts[0]:
                if i in studentsgrades:
                    studentsgrades[i].append(int(parts[2].strip()))
                else:
                    studentsgrades[i] = [int(parts[2].strip())]

sortedresult = sorted(studentsgrades.items(), key=lambda x:avarage(x[1]), reverse=True)
with open("report.txt","w",encoding="utf-8") as f:
    for i,value in sortedresult:
        print(f'{i} — Оцінок: {len(list(value))} — середній: {avarage(list(value))}')
        f.write(f'{i} — Оцінок: {len(list(value))} — середній: {avarage(list(value))}\n')
        result[i] = avarage(list(value))

maxresults = max(result.values())
for i in result:
    if result[i] == maxresults:
        maxresultstudents.append(i)

with open("report.txt","a",encoding="utf-8") as f:
    print("Найкращий результат: ", end="")
    f.write("Найкращий результат: ")

    lenght = len(maxresultstudents)
    if len(maxresultstudents) > 1:
        print(", ".join(maxresultstudents[:-1]) + " та " + maxresultstudents[-1], end="")
        f.write(", ".join(maxresultstudents[:-1]) + " та " + maxresultstudents[-1])
    elif len(maxresultstudents) == 1:
        print(maxresultstudents[0], end="")
        f.write(maxresultstudents[0])

    print(f' — {maxresults}',end="")
    f.write(f' — {maxresults}'  + "\n")

