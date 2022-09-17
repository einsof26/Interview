from stack import Stack


def main(data):  #Принимает агрумент строку скобок
    stack = Stack([])  # Создает экземпляр класса Stack для решения задачи
    data_list = [elem for elem in data]  # Преобразует строку в список
    for elem in data_list:  # Перебираем элементы преобразованного списка
        if elem == '(' or elem == '[' or elem == '{':  # Если открывающие скобки, добавляем в стек
            stack.push(elem)
        # Если самый первый элемент закрывающая скобка, то точно несбалансирован
        elif (elem == ')' and stack.isEmpty() is True) or \
                (elem == ']' and stack.isEmpty() is True) \
                or (elem == '}' and stack.isEmpty() is True):
            return "Unbalanced"
        # Сравнивает элемент с последним в стеке.
        # Если взаимодополняющие, то удаляет этот последный элемент из стека
        # и  проверяет остались ли эл-ты в стеке.
        elif (elem == ')' and stack.peek() == '(') or \
                (elem == ']' and stack.peek() == '[') \
                or (elem == '}' and stack.peek() == '{'):
            stack.pop()
            if stack.size() == 0 and elem == data_list[-1]:
                # Если не осталось, и кончились элементы data_list, заканчивает программу - сбалансирован
                # print(stack.size())
                return "Balanced"
        else:  # Если нарушается условие взаимодополнения текущего эл-ты и последнего в стеке, то точно несбалансирован
            return "Unbalanced"


if __name__ == '__main__':
    print(main(data))
