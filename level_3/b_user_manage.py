"""
У нас есть класс UserManager, который содержит в себе спискок юзернэймов пользователей и может расширять этот список.

Задания:
    1. Создайте класс AdminManager, который будет наследником UserManager.
       У него должен быть свой уникальный метод ban_username, который по переданному в него юзернэйму будет удалять
       юзернэйм из списка. Если такого юзернэйма в списке нет - должно печататься сообщение: "Такого пользователя не существует."
    2. Создайте класс SuperAdminManager, который будет наследником AdminManager.
       У него должен быть свой уникальный метод ban_all_users, который будет удалять все юзернэймы из списка.
    3. Создайте экземпляры каждого из трех классов и у каждого экземпляра вызовите все возможные методы.
"""


class UserManager:
    def __init__(self):
        self.usernames = []

    def add_user(self, username):
        self.usernames.append(username)

    def get_users(self):
        return self.usernames


class AdminManager(UserManager):
    def ban_username(self, username):
        if username in self.usernames:
            self.usernames.remove(username)
        else:
            print('Такого пользователя не существует')


class SuperAdminManager(AdminManager):
    def ban_all_users(self):
        self.usernames.clear()


if __name__ == '__main__':
    instance_user = UserManager()
    instance_user.add_user(username='carrot')
    print(instance_user.get_users())

    instance_admin = AdminManager()
    instance_admin.add_user(username='cucumber')
    print(instance_admin.get_users())
    instance_admin.ban_username(username='cucumber')

    instance_super = SuperAdminManager()
    instance_super.add_user(username=524)
    print(instance_super.get_users())
    instance_super.ban_username(username='tomato')
    instance_super.ban_all_users()
    print(instance_super.get_users())

