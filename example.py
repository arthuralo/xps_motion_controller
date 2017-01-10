import XPS_Q8_drivers
import sys


def error_and_close(socket_id, err_code, API_name):
    if err_code != -2 and errCode != -108:
        [err_code2, err_str] = xps.ErrorStringGet(socket_id, err_code)
        if (error_code != 0):
            print API_name + ': ERROR ' + str(err_code)
        else:
            print API_name + ': ' + err_str
    else:
        if (err_code == -2):
            print API_name + ': TCP timeout'
        if (err_code == -108):
            print API_name + ': The TCP/IP connection was closed by an admin'
    xps.TCP_CloseSocket(socket_id)
    return

xps = XPS_Q8_drivers.XPS()
socket_id = xps.TCP_ConnectToServer('192.168.0.254', 5001, 20)
if socket_id == -1:
    print 'Connection to XPS failed, check IP and port'
    sys.exit()
else:
    print "Connected!"

# Define positioner
group = 'Group1'  # Forward/Backward (z)
positioner = group + '.Pos'

# Kill the group
[err_code, return_str] = xps.GroupKill(socket_id, group)
if err_code != 0:
    error_and_close(socket_id, err_code, 'GroupKill')
    sys.exit()

# Initialise the group
[err_code, return_str] = xps.GroupInitialize(socket_id, group)
if err_code != 0:
    error_and_close(socket_id, err_code, 'GroupInitialize')
    sys.exit()

# Home search
[err_code, return_str] = xps.GroupHomeSearch(socket_id, group)
if err_code != 0:
    error_and_close(socket_id, err_code, 'GroupHomeSearch')
    sys.exit()

# Make Some Movesss
for index in range(10):
    # Forward
    [err_code, return_str] = xps.GroupMoveAbsolute(socket_id, positioner,
                                                   [20.0])
    if err_code != 0:
        error_and_close(socket_id, err_code, 'GroupMoveAbsolute')
        sys.exit()
    [err_code, cur_pos] = xps.GroupPositionCurrentGet(socket_id, positioner, 1)
    if err_code != 0:
        error_and_close(socket_id, err_code, 'GroupPositionCurrentGet')
        sys.exit()
    else:
        print 'Positioner' + positioner + ' is in poisition ' + str(cur_pos)
    # Backward
    [err_code, return_str] = xps.GroupMoveAbsolute(socket_id, positioner,
                                                   [-20.0])
    if err_code != 0:
        error_and_close(socket_id, err_code, 'GroupMoveAbsolute')
        sys.exit()
    [err_code, cur_pos] = xps.GroupPositionCurrentGet(socket_id, positioner, 1)
    if err_code != 0:
        error_and_close(socket_id, err_code, 'GroupPositionCurrentGet')
        sys.exit()
    else:
        print 'Positioner' + positioner + ' is in poisition ' + str(cur_pos)

group = 'Group2'  # x 
positioner = group + '.Pos'

# Kill the group
[err_code, return_str] = xps.GroupKill(socket_id, group)
if err_code != 0:
    error_and_close(socket_id, err_code, 'GroupKill')
    sys.exit()

# Initialise the group
[err_code, return_str] = xps.GroupInitialize(socket_id, group)
if err_code != 0:
    error_and_close(socket_id, err_code, 'GroupInitialize')
    sys.exit()

# Home search
[err_code, return_str] = xps.GroupHomeSearch(socket_id, group)
if err_code != 0:
    error_and_close(socket_id, err_code, 'GroupHomeSearch')
    sys.exit()

# Make Some Movesss
for index in range(10):
    # Forward
    [err_code, return_str] = xps.GroupMoveAbsolute(socket_id, positioner,
                                                   [20.0])
    if err_code != 0:
        error_and_close(socket_id, err_code, 'GroupMoveAbsolute')
        sys.exit()
    [err_code, cur_pos] = xps.GroupPositionCurrentGet(socket_id, positioner, 1)
    if err_code != 0:
        error_and_close(socket_id, err_code, 'GroupPositionCurrentGet')
        sys.exit()
    else:
        print 'Positioner' + positioner + ' is in poisition ' + str(cur_pos)
    # Backward
    [err_code, return_str] = xps.GroupMoveAbsolute(socket_id, positioner,
                                                   [-20.0])
    if err_code != 0:
        error_and_close(socket_id, err_code, 'GroupMoveAbsolute')
        sys.exit()
    [err_code, cur_pos] = xps.GroupPositionCurrentGet(socket_id, positioner, 1)
    if err_code != 0:
        error_and_close(socket_id, err_code, 'GroupPositionCurrentGet')
        sys.exit()
    else:
        print 'Positioner' + positioner + ' is in poisition ' + str(cur_pos)


group = 'Group3'  # y 
positioner = group + '.Pos'

# Kill the group
[err_code, return_str] = xps.GroupKill(socket_id, group)
if err_code != 0:
    error_and_close(socket_id, err_code, 'GroupKill')
    sys.exit()

# Initialise the group
[err_code, return_str] = xps.GroupInitialize(socket_id, group)
if err_code != 0:
    error_and_close(socket_id, err_code, 'GroupInitialize')
    sys.exit()

# Home search
[err_code, return_str] = xps.GroupHomeSearch(socket_id, group)
if err_code != 0:
    error_and_close(socket_id, err_code, 'GroupHomeSearch')
    sys.exit()

# Make Some Movesss
for index in range(10):
    # Forward
    [err_code, return_str] = xps.GroupMoveAbsolute(socket_id, positioner,
                                                   [20.0])
    if err_code != 0:
        error_and_close(socket_id, err_code, 'GroupMoveAbsolute')
        sys.exit()
    [err_code, cur_pos] = xps.GroupPositionCurrentGet(socket_id, positioner, 1)
    if err_code != 0:
        error_and_close(socket_id, err_code, 'GroupPositionCurrentGet')
        sys.exit()
    else:
        print 'Positioner' + positioner + ' is in poisition ' + str(cur_pos)
    # Backward
    [err_code, return_str] = xps.GroupMoveAbsolute(socket_id, positioner,
                                                   [-20.0])
    if err_code != 0:
        error_and_close(socket_id, err_code, 'GroupMoveAbsolute')
        sys.exit()
    [err_code, cur_pos] = xps.GroupPositionCurrentGet(socket_id, positioner, 1)
    if err_code != 0:
        error_and_close(socket_id, err_code, 'GroupPositionCurrentGet')
        sys.exit()
    else:
        print 'Positioner' + positioner + ' is in poisition ' + str(cur_pos)

group = 'Group4'  # spindle 
positioner = group + '.Pos'

# Kill the group
[err_code, return_str] = xps.GroupKill(socket_id, group)
if err_code != 0:
    error_and_close(socket_id, err_code, 'GroupKill')
    sys.exit()

# Initialise the group
[err_code, return_str] = xps.GroupInitialize(socket_id, group)
if err_code != 0:
    error_and_close(socket_id, err_code, 'GroupInitialize')
    sys.exit()

# Home search
[err_code, return_str] = xps.GroupHomeSearch(socket_id, group)
if err_code != 0:
    error_and_close(socket_id, err_code, 'GroupHomeSearch')
    sys.exit()

# Make Some Movesss
for index in range(3):
    # Forward
    [err_code, return_str] = xps.GroupMoveAbsolute(socket_id, positioner,
                                                   [20.0])
    if err_code != 0:
        error_and_close(socket_id, err_code, 'GroupMoveAbsolute')
        sys.exit()
    [err_code, cur_pos] = xps.GroupPositionCurrentGet(socket_id, positioner, 1)
    if err_code != 0:
        error_and_close(socket_id, err_code, 'GroupPositionCurrentGet')
        sys.exit()
    else:
        print 'Positioner' + positioner + ' is in poisition ' + str(cur_pos)
    # Backward
    [err_code, return_str] = xps.GroupMoveAbsolute(socket_id, positioner,
                                                   [-20.0])
    if err_code != 0:
        error_and_close(socket_id, err_code, 'GroupMoveAbsolute')
        sys.exit()
    [err_code, cur_pos] = xps.GroupPositionCurrentGet(socket_id, positioner, 1)
    if err_code != 0:
        error_and_close(socket_id, err_code, 'GroupPositionCurrentGet')
        sys.exit()
    else:
        print 'Positioner' + positioner + ' is in poisition ' + str(cur_pos)

xps.TCP_CloseSocket(socket_id)

