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
import core


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-x', dest='xPos', type=float, help='x position')
    parser.add_argument('-y', dest='yPos', type=float, help='y position')
    parser.add_argument('-z', dest='zPos', type=float, help='z position')
    parser.add_argument('-s', dest='spindle', type=float,
                        help='spindle position')
    args = parser.parse_args()
    xps = core.XPS()
    xps.initialise_all()
    xps.move_x(args.xPos)
    xps.move_y(args.yPos)
    xps.move_z(args.zPos)
    xps.move_spindle(args.spindle)
    xps.print_position()
    if not xps.check_position_x(args.xPos):
        xps.move_x(args.xPos)
        print "Adjusted", xps.print_position()
    if not xps.check_position_y(args.yPos):
        xps.move_y(args.yPos)
        print "Adjusted", xps.print_position()
    if not xps.check_position_z(args.zPos):
        xps.move_z(args.zPos)
        print "Adjusted", xps.print_position()
    if not xps.check_position_spindle(args.spindle):
        xps.move_spindle(args.spindle)
        print "Adjusted", xps.print_position()
