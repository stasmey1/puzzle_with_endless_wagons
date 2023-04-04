import random


class Carriage:
    """Вагон"""
    numeric = -1

    @classmethod
    def numeric_instance(cls):
        cls.numeric += 1

    def __init__(self):
        self.light = random.choice([True, False])
        Carriage.numeric_instance()
        self.number = Carriage.numeric

    def off(self) -> None:
        """выключение света в вагоне"""
        self.light = False

    def on(self) -> None:
        """включение света в вагоне"""
        self.light = True

    def __repr__(self):
        return f'{self.number} - {self.light}'


class Train:
    """Поезд"""

    def __init__(self):
        '''устанавливаем количество вагонов от 10 до 1000'''
        self.carriages_list: list = [Carriage() for _ in range(random.randint(10, 1000))]

    def __repr__(self):
        return f'поезд из {len(self.carriages_list)} вагонов'


class Player:
    """Игрок"""

    def __init__(self):
        self.position: int = 0

    def step(self, direction: int) -> None:
        """позиция игрока меняется на шаг"""
        self.position += direction

    @staticmethod
    def light_off(carriage: Carriage) -> None:
        """выключение света в вагоне"""
        carriage.off()

    @staticmethod
    def light_on(carriage: Carriage) -> None:
        """включение света в вагоне"""
        carriage.on()

    @staticmethod
    def check_light(carriage: Carriage) -> bool:
        return carriage.light


class Solution:
    """Решение"""

    def __init__(self):
        self.player: Player = Player()
        self.train: Train = Train()

    def solution(self) -> int:
        """Метод возвращает количество вагонов"""

        """создаем новый вагон"""
        new_carriage = Carriage()
        """включаем в свет в новом вагоне"""
        new_carriage.light = True
        """ставим новый вагон первый в поезд"""
        self.train.carriages_list[0] = new_carriage
        """ставим его же (тот же объект) посленим в поезд"""
        self.train.carriages_list.append(new_carriage)

        while True:
            steps = 1
            for i in range(len(self.train.carriages_list) - 1):

                """Догора вперед"""
                for j in range(steps):
                    """игрк переходит на следующий вагон"""
                    self.player.step(1)
                    """определяем вагон в поезде по местонахождению игрока"""
                    carriage = self.train.carriages_list[self.player.position]
                    """если в вагоне горит свет - выключаем"""
                    if self.player.check_light(carriage):
                        carriage.off()

                """Догора назад"""
                for j in range(steps):
                    """игрок возвращается к началу поезда"""
                    self.player.step(-1)
                """если первый [0] вагон без света значит игрок выключил свет в последнем вагоне, 
                а первый ссылается на тот же объект, значит игррок сделал полный круг"""
                if self.train.carriages_list[0].light is False:
                    break
                else:
                    steps += 1
            break

        carriages_quantity = steps
        return carriages_quantity

    def show_solution(self):
        print(f'В ходе подсчета выяснилось что количество вагонов в поезде - {self.solution()}')


if __name__ == '__main__':
    example = Solution()
    example.show_solution()
