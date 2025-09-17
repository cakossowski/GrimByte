from abc import ABC, abstractmethod

class BaseState(ABC):
    def __init__(self, game):
        self.game = game

    @abstractmethod
    def enter(self):
        """ Executed when called """
        pass

    @abstractmethod
    def update_with_player_input(self, command):
        """ Handle player input via command and update current state """
        pass

    @abstractmethod
    def exit_state(self):
        """ Give signal to change state and execute everything that needs to be done on exiting current state"""
        pass

