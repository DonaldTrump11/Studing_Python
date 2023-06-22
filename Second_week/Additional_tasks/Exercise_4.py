from collections import namedtuple
from collections import defaultdict
from functools import wraps

# Дано по заданию
statistics = defaultdict(list)
Order = namedtuple('Order', ['success', 'portions'])

# Декоратор возвращает ту же функцию, что и получает. При этом добавляет необходимые данные из этой функции в словарь
def collect_statistics(statistics):
    def inner(my_func):
        @wraps(my_func)
        def wrapper(*args, **kwargs) :
            result = my_func(*args, **kwargs)
            success = result[0]
            portions = args[1]-result[1] if result[0]==0 else result[1]
            statistics[args[0]].append(Order(success, portions))
            return result
        return wrapper
    return inner

#recipes = {'Бутерброд с ветчиной': {'Хлеб': 50, 'Ветчина': 20, 'Сыр': 20}, 'Салат Витаминный': {'Помидоры': 50, 'Огурцы': 20, 'Лук': 20, 'Майонез': 50, 'Зелень': 20}}
#store = {'Хлеб': 250, 'Ветчина': 120, 'Сыр': 120, 'Помидоры': 50, 'Огурцы': 20, 'Лук': 20, 'Майонез': 500, 'Зелень': 20}


@collect_statistics(statistics)
def check_portions(food, count, new_recipes=recipes, new_store=store):
    # Проверим, есть ли блюдо в списке с рецептами. Если нет, то запишем новый рецепт в словарь. 
    if food not in recipes :
        try :
            recipes[food] = new_recipes
            
        except:
            return (0, 0)
    
    
    # Проверим, сколько у нас продуктов для приготовления
    
    # Введем счетчик количества ингредиентов 
    i = 0
    quantity_needed_products = [] # будут храниться числа, показывающие во склько раз имеющихся продуктов больше, чем требуется
    for key_recipes in recipes[food]:
        for key_store in store :
            if key_recipes == key_store :
                # Счетчик ингридиентов увеличивается на 1, когда необходимый продукт есть на складе
                i += 1
                
                quantity_needed_products.append(store[key_store] // recipes[food][key_recipes])
    
    # Если счетчик ингридиентов меньше колличества необходимых продуктов - приготовить блюдо НЕ можем
    if len(recipes[food]) > i:
        return (0, 0)
    
    # Сколько порций можем приготовить
    max_can_cook = min(quantity_needed_products)
    
    # Можем ли мы приготовить заказ
    result = 1 if max_can_cook>=count else 0
    
    # Вывод
    
    if result == 1:
        return (result, count)
    elif result == 0:
        return (result, max_can_cook)

