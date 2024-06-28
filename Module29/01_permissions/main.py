from typing import Callable
import functools

user_permissions = ['admin']


def check_permission(user: str) -> Callable:
    def permission(func: Callable) -> Callable:
        """
        Функция - декоратор. Проверяет, входит ли логин пользователя в список разрешенных
        :param func: передаваемая функция
        :return:
        """
        @functools.wraps(permission)
        def _wrapped(*args, **kwargs):
            try:
                if user in user_permissions:
                    result = func(*args, **kwargs)
                    return result
                else:
                    raise PermissionError
            except PermissionError as exc:
                print(f"{exc}: У пользователя: {user} недостаточно прав, чтобы выполнить функцию {func.__name__}")

        return _wrapped
    return permission


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()

# зачет!
