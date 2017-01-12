# xps_motion_controller
XPS-Q8 Motion Controller code

Requires XPS_Q8_drivers.py. See ftp://download.newport.com/MotionControl/Current/MotionControllers/XPS-Q/Drivers/python/

To move the motion controller use the move script:

python move.py -x 20. -y " -20." -z 30. -s " -30."

Note the required format for negative positions.

The following files are included in this repo:
XPS_Q8_drivers.py - obtained from ftp://download.newport.com/MotionControl/Current/MotionControllers/XPS-Q/Drivers/python/
core.py - Contains the XPS class which is used to control the motion controller.
example.py - Example script modified from the XPS programmers manual. 
move.py - Move the motion controller from the command line. 
xps_exception.py - Error handling
