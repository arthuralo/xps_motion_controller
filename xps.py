#!/usr/bin/env python
#
# core:
#
# XPS:
#
# Class used to control the xps motion controller.
#
# Author: James Waterfield
#         j.waterfield@sussex.ac.uk
#
# History:
# 2017/01/11: First instance.
#
#################################################
#################################################


import XPS_Q8_drivers
import xps_exception


class XPS():
    """ Initiate the XPS
    """

    def __init__(self):
        self._xps = XPS_Q8_drivers.XPS()
        self._socket_id = self._xps.TCP_ConnectToServer('192.168.0.254',
                                                        5001, 20)
        if self._socket_id == -1:
            raise xps_exception.XpsException(
                'Connection to XPS failed, check IP and port')

    def get_position(self, positioner):
        """
        """
        [err_code, cur_pos] = self._xps.GroupPositionCurrentGet(
            self._socket_id, positioner, 1)
        if err_code != 0:
            error_and_close(socket_id, err_code, 'GroupPositionCurrentGet')
        return cur_pos

    def check_position_spindle(self, position):
        """
        """
        positioner = 'Group4.Pos'
        cur_pos = self.get_position(positioner)
        if position != cur_pos:
            return False
        return True

    def check_position_x(self, position):
        """
        """
        positioner = 'Group2.Pos'
        cur_pos = self.get_position(positioner)
        if position != cur_pos:
            return False
        return True

    def check_position_y(self, position):
        """
        """
        positioner = 'Group3.Pos'
        cur_pos = self.get_position(positioner)
        if position != cur_pos:
            return False
        return True

    def check_position_z(self, position):
        """
        """
        positioner = 'Group1.Pos'
        cur_pos = self.get_position(positioner)
        if position != cur_pos:
            return False
        return True

    def get_position_spindle(self):
        """
        """
        positioner = 'Group4.Pos'
        return self.get_position(positioner)

    def get_position_x(self):
        """
        """
        positioner = 'Group2.Pos'
        return self.get_position(positioner)

    def get_position_y(self):
        """
        """
        positioner = 'Group3.Pos'
        return self.get_position(positioner)

    def get_position_z(self):
        """
        """
        positioner = 'Group1.Pos'
        return self.get_position(positioner)

    def home(self, group):
        """
        """
        [err_code, return_str] = self._xps.GroupHomeSearch(self._socket_id,
                                                           group)
        if err_code != 0:
            xps_exception.error_and_close(self, err_code, 'GroupHomeSearch')

    def initialise(self, group):
        """
        """
        [err_code, return_str] = self._xps.GroupInitialize(self._socket_id,
                                                           group)
        if err_code != 0:
            xps_exception.error_and_close(self, err_code, 'GroupInitialize')

    def initialise_all(self):
        """
        """
        self.initialise_spindle()
        self.initialise_x()
        self.initialise_y()
        self.initialise_z()

    def initialise_spindle(self):
        """
        """
        group = 'Group4'  # spindle
        self.kill(group)
        self.initialise(group)
        self.home(group)

    def initialise_x(self):
        """
        """
        group = 'Group2'  # x
        self.kill(group)
        self.initialise(group)
        self.home(group)

    def initialise_y(self):
        """
        """
        group = 'Group3'  # y
        self.kill(group)
        self.initialise(group)
        self.home(group)

    def initialise_z(self):
        """
        """
        group = 'Group1'  # z
        self.kill(group)
        self.initialise(group)
        self.home(group)

    def kill(self, group):
        """
        """
        [err_code, return_str] = self._xps.GroupKill(self._socket_id,
                                                     group)
        if err_code != 0:
            xps_exception.error_and_close(self, err_code, 'GroupKill')

    def move(self, positioner, position):
        """
        """
        [err_code, return_str] = self._xps.GroupMoveAbsolute(self._socket_id,
                                                             positioner,
                                                             [position])
        if err_code != 0:
            xps_exception.error_and_close(self, err_code, 'GroupMoveAbsolute')

    def move_spindle(self, position):
        """
        """
        positioner = 'Group4.Pos'
        self.move(positioner, position)

    def move_x(self, position):
        """
        """
        positioner = 'Group2.Pos'
        self.move(positioner, position)

    def move_y(self, position):
        """
        """
        positioner = 'Group3.Pos'
        self.move(positioner, position)

    def move_z(self, position):
        """
        """
        positioner = 'Group1.Pos'
        self.move(positioner, position)

    def print_position(self):
        """
        """
        print ("Current positon:: x: " + str(self.get_position_x()) +
               " y: " + str(self.get_position_y()) +
               " z: " + str(self.get_position_z()) +
               " spindle: " + str(self.get_position_spindle()))
