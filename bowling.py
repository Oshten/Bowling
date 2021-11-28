#! engoding = utf8

from errors import SumError

class PointsCounter:

    def __init__(self, game_resalt):
        self.sum_points = 0
        self.game_resalt = game_resalt

    def start_counter(self):
        self.game_resalt = self.game_resalt.replace('\'', '')
        if len(self.game_resalt.replace('X', '')) % 2 == 1:
            raise ValueError('Некорректный ввод: не хватает одного значения')
        sumbols = ''
        for sumbol in self.game_resalt:
            sumbols += sumbol
            if sumbols == 'X':
                self.sum_points += 20
                sumbols = ''
            elif len(sumbols) < 2:
                continue
            else:
                if 'X' in sumbols.upper() or sumbols[0] == '/':
                    raise SyntaxError('Некорректный ввод: пропущены значения')
                if sumbols[1] == '/':
                    self.sum_points += 15
                    sumbols = ''
                else:
                    sum_sumbols = 0
                    for points in sumbols.replace('-', ''):
                        try:
                            sum_sumbols += int(points)
                        except ValueError:
                            raise TypeError('Некорректный ввод: значения очков не цифры')
                    sumbols = ''
                    if sum_sumbols <= 9:
                        self.sum_points += sum_sumbols
                    else:
                        raise SumError('Некорректный ввод: сумма двух бросков больше 9 очков')
        return


# def get_score(game_resalt: str) -> int:
#     '''Определяет количество очков в боулинге'''
#     sum_points = 0
#     sumbols = ''
#     for sumbol in game_resalt:
#         sumbols += sumbol
#         if sumbols == 'X':
#             sum_points += 20
#             sumbols = ''
#         elif len(sumbols) < 2:
#             if game_resalt.index(sumbol) + 1 == len(game_resalt):
#                 raise ValueError('Некорректный ввод: не хватает одного значения')
#             else:
#                 continue
#         else:
#             if 'X' in sumbols.upper() or sumbols[0] == '/':
#                 raise SyntaxError('Некорректный ввод: пропущены значения')
#             if sumbols[1] == '/':
#                 sum_points += 15
#                 sumbols = ''
#             else:
#                 sum_sumbols = 0
#                 for points in sumbols.replace('-',''):
#                     try:
#                         sum_sumbols += int(points)
#                     except ValueError:
#                         raise TypeError('Некорректный ввод: значения очков не цифры')
#                 sumbols = ''
#                 if sum_sumbols <= 9:
#                     sum_points += sum_sumbols
#                 else:
#                     raise SumError('Некорректный ввод: сумма двух бросков больше 9 очков')
#     return sum_points
