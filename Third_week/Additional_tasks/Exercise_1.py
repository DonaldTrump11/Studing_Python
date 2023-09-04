class Matrix:
    MAX_SIZE = 1000  
    
    @staticmethod
    def create_matrix(size = 1):
        ''' Статический метод, создающий матрицу(двойной массив) нужного размера(по умолчанию 1)'''
        matrix = []
        for line in range(size):
            temporary_list = []
            for element in range(size):
                temporary_list.append(None)
            matrix.append(temporary_list)
        return matrix
    
    def __init__(self, max_size=None, matrix=None):
        if max_size == None:
            self.max_size = 1000
        else:
            self.max_size = int(max_size)
        
        try:
            if matrix != None :
                self.matrix = matrix
            else :
                self.matrix = self.create_matrix()
        except:
            self.matrix = self.create_matrix()

    def append(self, element=None):
        ''' Добавляем новый элемент в матрицу. При необходимости увеличиваем её размер.'''
        matrix = self.matrix
        max_size = int(self.max_size)
        size = len(matrix)
        
        # Проверим, является ли элемент None
        if element == None:
            return matrix
        
        # Проверим, нужно ли увеличивать размер матрицы для добавления элемента
        add_new_element = matrix[size-2][size-1] # Место последнего элемента в предпоследней строке
        
        # Если матрица размером 1, то увеличиваем её:
        if size == 1:
            add_new_element = "Увеличиваем"
        
        # Если размер матрицы равен максимально возможному размеру - не увеличиваем
        if size > max_size :
            raise IndexError("Матрица больше, чем может быть")
        elif size == max_size:
            add_new_element = None
        
        if add_new_element != None:
            new_matrix = self.create_matrix(size+1) # создадим новуюмтрицу
            temporary_list = [] # временный список
            
            # Переносим значения из старой матрицы во временный список
            for line_old_matrix in matrix:
                for elem_old_matrix in line_old_matrix:
                    if elem_old_matrix != None:
                        temporary_list.append(elem_old_matrix)
                         
            
            # Заполняем новую матрицу элементами из временного списка
            i = 0
            for line_new_matrix in range(size+1):
                for elem_new_matrix in range(size+1):
                    try:
                        new_matrix[line_new_matrix][elem_new_matrix] = temporary_list[i]
                        i+=1
                    except:
                        new_matrix[line_new_matrix][elem_new_matrix] = None
            matrix = new_matrix # Присваиваем переменной matrix матрицу new_matrix
            size = len(matrix)
            
        # Добавляем элемент к матрице
        flag = False
        for line_num in range(size):
            if flag:
                break
            for elem_num in range(size):
                if matrix[line_num][elem_num] == None:
                    matrix[line_num][elem_num] = element
                    flag = True
                    break
        if flag ==  False:
            raise IndexError("list assignment index out of range))")
        self.__init__(max_size, matrix)
        return matrix
                    

    def pop(self):
        ''' В данном методе удаляется последний значимый элемент из матрицы. 
            При возможности уменьшается размер этой матрицы'''
        
        matrix = self.matrix
        max_size = self.max_size
        size = len(matrix)
        
        # Если размер матрицы 1, то метод не работает
        if size <= 1:
            raise IndexError("Размер матрицы = 1. Её нельзя уменьшить((")
        
        # Удалим последний элемент
        flag = False
        for line in range(size):
            if flag :
                break
            for element in range(size):
                if matrix[line][element] == None and element!=0:
                    pop_element = matrix[line][element-1]
                    matrix[line][element-1] = None
                    flaf = True
                    break
                elif matrix[line][element] == None and element == 0:
                    pop_element = matrix[line-1][size-1]
                    matrix[line-1][size-1] = None                        
                    flaf = True
                    break
        if flag == False:
            pop_element = matrix[size-1][size-1]
            matrix[size-1][size-1] = None
            
        # Проверим, нужно ли уменьшать размер матрицы 
    
        # Переведем матрицу(двумерный массив) в временный список(одномерный массив)
        temporary_list = []
        
        for old_line in matrix:
            for old_elem in old_line:
                if old_elem != None:
                    temporary_list.append(old_elem)
        
        quantity_elemements = len(temporary_list) # Количество элементов в исходной матрице
        elements_for_decrease = (size-1)**2 - (size-1)  # Количество элементов необходимое для уменьшения
        
        # Уменьшаем разиер матрицы
        if quantity_elemements <= elements_for_decrease:
            
            # Создаем новую матрицу меньшего размера
            new_matrix = self.create_matrix(size-1)
            new_size = len(new_matrix)
            
            # Заполняем новую матрицу
            i = 0
            for new_line in range(new_size):
                for new_elem in range(new_size):
                    try:
                        new_matrix[new_line][new_elem] = temporary_list[i]
                    except:
                        new_matrix[new_line][new_elem] = None
                    i += 1
            matrix = new_matrix
        
        self.__init__(max_size, matrix)
        return pop_element

    def __str__(self):
        ''' Переводим матрицу из вида массивов в строковый вид'''
        matrix = self.matrix
        size = len(matrix)
        matrix_string = ""
        
        for line in matrix:
            for elem in line:
                if matrix_string[-1:] == "\n":
                    matrix_string = matrix_string + str(elem)
                else:
                    matrix_string = matrix_string + " " + str(elem)
            matrix_string = matrix_string + "\n"
        return matrix_string[1:]
        

    @classmethod
    def from_iter(cls, iter_obj, max_size=None):
        if max_size == None:
            max_size = 1000 
        
        try:
            iter(iter_obj)
        except:
            raise TypeError ("Неитерируемый объект")
            
        a = Matrix(max_size=max_size)
            
        for element in iter_obj:
            if element == None:
                continue
            a.append(element)
        
        
        return a
        
-------------------------------------------------------------
-------------------------------------------------------------
raise TypeError ("Тут еще тесты)))")

-------------------------------------------------------------


----------------------------------------------------------------
--------------------------------------------------------------


m = Matrix(max_size = 2)
for i in range(1,5):
    m.append(i)
    print(m)
    print("*"*20)
print("="*30)
print("="*30)
for i in range(1,5):
    m.pop()
    print(m)
    print("*"*20)
