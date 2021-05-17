
all_students = []
all_scores = []
all_class = []
all_students_id = []


def classid(class_str):
    return all_class.index(class_str)


def studentsid(students_str):
    return all_students_id.index(students_str)


while True:
    origin = input().split(', ')
    if origin == ['END']:
        break
    if len(origin) == 2:
        all_students.append(origin)
    if len(origin) == 3:
        all_scores.append(origin)


for temp in all_scores:
    if temp[1] not in all_class:
        all_class.append(temp[1])
all_class.sort()
all_students.sort(key=lambda x: int(x[0]))
for temp in all_students:
    all_students_id.append(temp[0])

# print(all_scores)
# print(all_students)
# print(all_class)
# print(all_students_id)
# print(classid('Operating System'))
# print(studentsid('3180111435'))
table = [['' for i in range(len(all_students_id))]
         for i in range(len(all_class))]

for temp in all_scores:
    table[studentsid(temp[0])][classid(temp[1])] = temp[2]


# print(table)

print('student id, name, ', end='')
for temp in all_class:
    print(temp, end=', ')
print('average')

for i in range(len(all_students_id)):
    sum_n = 0
    sum = 0
    print(all_students_id[i]+', '+all_students[i][1]+', ', end='')
    for j in range(len(all_class)):
        if table[i][j] != '':
            print(str(round(float(table[i][j]), 1)), end=', ')
            sum_n += 1
            sum += float(table[i][j])
        else:
            print('', end=', ')
    if sum_n!=0:
        print(str(round(sum/sum_n, 1)))
    else:
        print('')
print(', , ', end='')
last = 0
for j in range(len(all_class)):
    sum = 0
    sum_n = 0
    for i in range(len(all_students_id)):
        if table[i][j] != '':
            sum_n += 1
            sum += float(table[i][j])
    last += sum/sum_n
    if sum_n!=0:
        print(str(round(sum/sum_n, 1)), end=', ')
    else:
        print('',end=', ')
if(len(all_class)!=0):
    print(str(round(last/len(all_class), 1)), end='')

