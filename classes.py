import pygame
import math


tram = pygame.image.load('tram.png')


class Line:
    """Class representing tram line

    :param list_of_stops: list of stops that belong to the line
    :type list_of_stops: list
    """
    def __init__(self, list_of_stops) -> None:
        self._stops = list_of_stops

    @property
    def stops(self):
        """Returns stops that belongs to the line"""
        return self._stops


class Stop:
    '''Class representing tram stop


    param: coordinates - coordinates of the stop
    type: list with 2 elements [x,y]
    '''
    def __init__(self, coordinates):
        self._coordinates = coordinates

    @property
    def coordinates(self):
        """Returns coordinates of the stop"""
        return self._coordinates


class Tram:
    """Class representing Tram

    param: line - line to which tram belongs to
    type: Line instance

    param: mother_stop - stop from which Tram begins his journey
    type: Stop instance
    """

    def __init__(self, line, mother_stop) -> None:

        self._line = line
        self.mother_stop = mother_stop
        mother_x, mother_y = self.mother_stop.coordinates
        self._graphic = tram.get_rect()
        self._graphic.topleft = (mother_x, mother_y)
        self.start_stop = None
        self.current_target = mother_stop
        self.waiting = 0

    @property
    def line(self):
        """Returns line to which tram belongs"""
        return self._line

    @property
    def graphic(self):
        """Returns Rectangle instance which keeps information about where the\
              tram is currently and the size of it"""
        return self._graphic

    @property
    def present_coordinates(self):
        """Returns tuple with current coordinates of the tram"""
        return (self._graphic.x, self._graphic.y)

    def set_target(self) -> tuple:
        """Changes coordinates of next stop(target)"""
        next_stop = None
        start_stop = self.current_target
        if start_stop in self.line.stops:
            start_stop_id = self.line.stops.index(start_stop)
            stop_list_length = len(self.line.stops)
            if start_stop_id < stop_list_length - 1:
                next_stop = self.line.stops[start_stop_id + 1]
            else:
                next_stop = self.line.stops[0]
            self.current_target = next_stop

    def find_y(self, x):
        """Finds Y coordinate of the tram according to the X cord."""
        x_diff = self.start_stop.coordinates[0] \
            - self.current_target.coordinates[0]
        y_diff = self.start_stop.coordinates[1]\
            - self.current_target.coordinates[1]
        if x_diff != 0:
            a = y_diff / x_diff
        else:
            if y_diff > 0:
                return self._graphic.y - 1
            else:
                return self._graphic.y + 1
        b = self.start_stop.coordinates[1]\
            - (a * self.start_stop.coordinates[0])
        y = a * x + b
        return y

    def move(self):
        """Changes coordinates of the tram so it \'moves\' to the next stop"""
        x_cord, y_cord = self.current_target.coordinates
        dx = x_cord - self.graphic.x
        dy = y_cord - self.graphic.y
        distance = math.sqrt(dx*dx + dy*dy)
        if distance > 1:
            if self._graphic.x < self.current_target.coordinates[0]:
                self._graphic.x += 1
            else:
                self._graphic.x -= 1
            self._graphic.y = self.find_y(self._graphic.x)
            return
        self._graphic.x, self._graphic.y = x_cord, y_cord

    def is_at_target_stop(self) -> (bool, Stop):
        """Checks whether the tram is at the target stop"""
        if self._graphic.x == self.current_target.coordinates[0]\
                and self._graphic.y == self.current_target.coordinates[1]:
            return True
        return False
