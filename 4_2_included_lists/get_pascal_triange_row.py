''''''
def get_pascal_triangle(rows_ammount):
    pascal_triangle = []
    length_of_lst = 1 # Кол. эл в списке = уровню списка в треугольнике

    # Формирование шаблона треугольника Паскаля (Только 1)
    for _ in range(rows_ammount):
        inner_lst = [1 for _ in range(length_of_lst)]
        pascal_triangle.append(inner_lst)
        length_of_lst += 1
    # print_pascal_triangle(pascal_triangle)

    # Заполнение внутренних эл. треугольника Паскаля
    # необходимо посчитать сумму эл в списке уровнем выше
    # По индексам, на 1 меньше и равного индексу текущего эл.

    if rows_ammount > 2:
        # Проход по уровням треугольника начиная с 3 (указано 2, т.к. нумерация с 0)
        for level in range(2, rows_ammount):
            # Проход по внутренним элементам текущего уровня треугольника
            for el in range(1, len(pascal_triangle[level]) - 1): 
                pascal_triangle[level][el] = (pascal_triangle[level-1][el-1] + pascal_triangle[level-1][el])
            
    return pascal_triangle

def print_pascal_triangle(pascal_triangle):
    for level in pascal_triangle: # По вложенным спискам
        for el in level: # По эл. вложенных списков
            print(str(el) + " ", end="")
        print() # Для переноса строки

############################

# Вывод треугольника Паскаля # step 11

rows_ammount = int(input()) # Введите число строк треугольника Паскаля: 
pascal_triangle = []

pascal_triangle = get_pascal_triangle(rows_ammount + 1)
print(pascal_triangle[rows_ammount])
