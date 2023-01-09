import pygame as pg
from enum import Enum


FPS = 60
CELL_SIZE = 100


class Cell(Enum): # способность создавать символические имена привязанные к конкретным константным значениям...
    VOID = 0
    CROSS = 1 # Крестики
    ZERO = 2 # Нолики


class Player():
    '''
    class of player, name and type of signs
    '''
    def __init__(self, name, cell_type) -> None:
        self.name = name
        self.cell_type = cell_type 


class GameField():
    def __init__(self) -> None:
        self.height = 3
        self.width = 3
        self.cells = [[Cell.VOID]*self.width for i in range(self.height)] # Крутецкий способ создать массив
   

class GameFieldView():
    '''
    виджет игрового поля, который отображает его на экране а также отображает место клика
    '''
    def __init__(self, field) -> None: # Передаем поле для отображения
        # загрузить картинки значков клеток
        # отобразить первичное поле
        self._field = field
        self._height = field.height * CELL_SIZE
        self._width = field.width * CELL_SIZE

    def draw(self):
        pass
    
    def check_coords_correct(self, x, y):
        return True  # TODO: учесть self.height

    def get_coords(self, x, y):
        return 0, 0 # TODO: реально вычислить клетку клика
        
    
class GameRoundManager():
    '''
    Иенеджер игры запускающий все процессы
    '''
    
    def __init__(self, player1: Player, player2: Player) -> None:
        self._players = [player1, player2]  # Нижним подчеркиваением сказали что свойство не публичное... 
        self._current_player = 0
        self.field = GameField()
        
    def handle_click(self, i, j): # обработчик клика
        player = self._players[self._current_player]
        print('click_handled', i, j)  # Игрок делает клик на поле


class GameWindow:
    '''
    Содержит в себе виджет поля, доп. кнопки. основной цикл и обработчик событий
    
    '''
    def __init__(self) -> None:
        # Инициализация pygame 
        pg.init()
        
        # параметры окна (Window)
        self._width = 600
        self._height = 600
        self._title = 'Крестики - нолики'
        self._screen = pg.display.set_mode((self._width, self._height)) #создание окна
        pg.display.set_caption(self._title) 
      
        player1 = Player('Петя', Cell.CROSS)
        player2 = Player('Вася', Cell.ZERO) # инициализация игроков, с указанием кто за кого играет
        self._game_menager = GameRoundManager(player1, player2) # создание менеджера с игроками
        self._field_widget = GameFieldView(self._game_menager.field) # создание экрана
        
    
    def main_loop(self): # Главный цикл
        finished = False 
        clock = pg.time.Clock()
        while not finished: 
            for event in pg.event.get():  # Проверка ивентов
                if event.type == pg.QUIT:  # Пробрасываем события
                    finished = True  # Если выход, то выход
                elif event.type == pg.MOUSEBUTTONDOWN:  # Игрок делает клик на поле
                    mouse_position = pg.mouse.get_pos()  # Считываем позицию мышки 
                    x, y = mouse_position  # Получаем х и у кординату клика мышки
                    if self._field_widget.check_coords_correct(x, y):  # Проверяет корректность введеных х и у, чтоб они попападали в окно 
                        i, j = self._field_widget.get_coords(x, y)  # Переводит х и у в координаты массива, чтоб этим не занимался game_manager
                    self._game_menager.handle_click(i, j)  # Передаем GameManager событие, чтоб он вытащил то что ему нужно
            pg.display.flip()  # Насколько понимаю работает как update
            clock.tick(FPS)  # Обновленние часиков 
        pg.quit()
        
        
def main():
    window = GameWindow()
    window.main_loop()
    print('Game over')
    
if __name__ == '__main__':
    main()