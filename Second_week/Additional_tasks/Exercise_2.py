def create_matrix(size):
    """
    Функция принимает на вход размер квадратной матрицы. Возвращает 'пустую' матрицу
    размером size x size, (все элементы матрицы имеют значение равное None).
    :param size: int > 0
    :return: list 
    """
    list_ = []
    for i in range(size) :
        strok = []
        for j in range(size) :
            strok.append(None)
        list_.append(strok)
    
    return list

def add_element(element, matrix) :
    
    # Если последний мы добавляем элемент на место первого стольца последний строки, то увеличиваем размер матрица на один
    if matrix[len(matrix)-2][len(matrix)-1] != None :
        
        # Переведем матрицу в одномерный массив
        mass = []
        for strok in matrix :
            for elemnt in strok :
                mass.append(elemnt)
        
        # Создадим новую матрицу большего размера
        new_matrix = []
        size_new_matrix = len(matrix)+1
        for i in range(size_new_matrix) :
            strok = []
            for j in range(size_new_matrix) :
                strok.append(None)
            new_matrix.append(strok) 
     

        
        # Запишем элементы массива в новую увеличенную матрицу
        i = 0
        for strok_ in range(size_new_matrix) :
            for elemnt_ in range(size_new_matrix) :
                try :
                    new_matrix[strok_][elemnt_] = mass[i]
                    i += 1
                except :
                    new_matrix[strok_][elemnt_] = None
                    
        # Теперь новая матрица это основная 
        matrix = new_matrix
        
    # Запишем новый элемент в матрицу
    size = len(matrix)
    flag = False
    for i in range(size):
        for elem in range(size) :
            if matrix[i][elem] == None :
                matrix[i][elem] = element
                flag = True
                break
        if flag :
            break
        
    return matrix
