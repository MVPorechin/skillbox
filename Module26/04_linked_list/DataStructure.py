from typing import Any, Optional


class Node:
    """
    Класс описывающий узел
    Args:
       :param data: данные помещаемые в узел
       :param next_node: ссылка на следующий элемент списка
    """

    def __init__(self, data: Optional[Any] = None, next_node: Optional['Node'] = None) -> None:
        self.data = data
        self.next_node = next_node

    def __str__(self) -> str:
        return 'Node [{data}]'.format(
            data=str(self.data)
        )


class LinkedList:
    """
    Класс описывающий односвязный список
    """

    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.length = 0

    def append(self, value: Any) -> None:
        """
        Метод добавляет узел в связный список
        :param value: данные помещаемые в новый узел
        :return: None
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next_node:
            last = last.next_node
        last.next_node = new_node
        self.length += 1

    def get(self, index: int) -> Any:
        """
        Метод возвращает значение по индексу
        :param index: int
        :return: Any
        """
        current_node = self.head
        current_index = 0
        if self.length == 0 or self.length <= index:
            raise IndexError

        while current_node is not None:
            if current_index == index:
                return current_node.data
            current_node = current_node.next_node
            current_index += 1


    def check_data(self, value: Any) -> bool:
        lastnode = self.head
        while lastnode:
            if value == lastnode.data:
                return True
            else:
                lastnode = lastnode.next_node
        return False

    def remove(self, index: int) -> None:
        """
        Метод удаляет узел из списка по индексу узла
        :param index: индекс узла из связного списка
        :return: None
        """
        current_node = self.head
        current_index = 0
        if self.length == 0 or self.length <= index:
            raise IndexError

        if current_node is not None:
            if index == 0:
                self.head = current_node.next_node
                self.length -= 1
                return

        while current_node is not None:
            if current_index == index:
                break
            previous = current_node
            current_node = current_node.next_node
            current_index += 1

        previous.next_node = current_node.next_node
        self.length -= 1
