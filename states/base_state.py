from abc import ABC, abstractmethod

class BaseState(ABC):
    def __init__(self, game):
        self.game = game

    @abstractmethod
    def on_enter(self):
        """ Executed when called"""
        pass

    @abstractmethod
    def handle_input(self):
        pass

