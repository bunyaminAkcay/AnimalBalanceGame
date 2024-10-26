from core.clock import Clock
from core.UIText import UIText

class Timer(UIText):
    
    def __init__(self, textString, x, y, fontSize, layer, fontColor, time, board, resultScreen, fontBackground=None, visibility=True):
        super().__init__(textString, x, y, fontSize, layer, fontColor, fontBackground, visibility)
        self.time = time
        self.board = board
        self.resultScreen = resultScreen

    def init(self):
        super().init()
        self.interval = 100
        self.clock = Clock(self.interval)
        self.time = float(self.time)

    def update(self):

        if self.time < 10:
            self.fontColor = (255, 0, 0)

        if self.time <= 0:
            self.time = 0
            minutes = int( self.time // 60)
            remaining_seconds = self.time % 60
            formattedTime = f"{minutes}:{remaining_seconds:.1f}"
            self.setText(formattedTime)
            self.end()
        elif self.clock.getTicks() > 0:
            self.time -= self.interval/1000
            minutes = int( self.time // 60)
            remaining_seconds = self.time % 60
            formattedTime = f"{minutes}:{remaining_seconds:.1f}"
            self.setText(formattedTime)
    
    def end(self):
        self.board.stop = True
        self.resultScreen.showResults()
        