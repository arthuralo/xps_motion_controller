#!/usr/bin/env python
#
# move:
#
# moves the XPS Motion Controller
#
# Author: James Waterfield
#         j.waterfield@sussex.ac.uk
#
# History:
# 2017/01/11: First instance.
#
#################################################
#################################################

import argparse
import xps


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-x', dest='xPos', type=float, help='x position')
    parser.add_argument('-y', dest='yPos', type=float, help='y position')
    parser.add_argument('-z', dest='zPos', type=float, help='z position')
    parser.add_argument('-s', dest='spindle', type=float,
                        help='spindle position')
    args = parser.parse_args()
    my_xps = xps.XPS()
    my_xps.initialise_all()
    my_xps.move_x(args.xPos)
    my_xps.move_y(args.yPos)
    my_xps.move_z(args.zPos)
    my_xps.move_spindle(args.spindle)
    my_xps.print_position()
    if not my_xps.check_position_x(args.xPos):
        my_xps.move_x(args.xPos)
        print "Adjusted", my_xps.print_position()
    if not my_xps.check_position_y(args.yPos):
        my_xps.move_y(args.yPos)
        print "Adjusted", my_xps.print_position()
    if not my_xps.check_position_z(args.zPos):
        my_xps.move_z(args.zPos)
        print "Adjusted", my_xps.print_position()
    if not my_xps.check_position_spindle(args.spindle):
        my_xps.move_spindle(args.spindle)
        print "Adjusted", my_xps.print_position()
