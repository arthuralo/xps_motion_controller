#!/usr/bin/env python
#
# xps_exception:
#
# XpsException
#
# Exceptions raised by the XPS Motion Controller
#
# Author: James Waterfield
#         j.waterfield@sussex.ac.uk
#
# History:
# 2017/01/11: First instance.
#
#################################################
#################################################


class XpsException(Exception):
    """Handles exceptions thrown by XPS motion controller
    """

    def __init__(self, error):
        Exception.__init__(self, error)


def error_and_close(xps,  err_code, API_name):
    """ Checks the error code and closes the socket.
    """
    if err_code != -2 and err_code != -108:
        [err_code2, err_str] = xps._xps.ErrorStringGet(xps._socket_id,
                                                       err_code)
        xps._xps.TCP_CloseSocket(xps._socket_id)
        raise XpsException(API_name + ': ' + err_str)
    else:
        if (err_code == -2):
            xps._xps.TCP_CloseSocket(xps._socket_id)
            raise XpsException(API_name + ': TCP timeout')
        if (err_code == -108):
            xps._xps.TCP_CloseSocket(xps._socket_id)
            raise XpsException(
                API_name + ': The TCP/IP connection was closed by an admin')
