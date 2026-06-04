from pymavlink import mavutil
import time

print("CONNECTING")

master = mavutil.mavlink_connection('udpin:0.0.0.0:14551')

print("WAITING HEARTBEAT")
master.wait_heartbeat()

print("CONNECTED")

# GUIDED mode
master.set_mode_apm("GUIDED")
time.sleep(2)

# Arm motors
print("ARMING")
master.arducopter_arm()
master.motors_armed_wait()

print("ARMED")

# Takeoff to 5 meters
print("TAKING OFF")

master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
    0,
    0, 0, 0, 0, 0, 0, 5
)

# Wait to reach altitude
time.sleep(10)

print("HOVERING")

# First 180° yaw rotation
print("ROTATING 180 DEGREES")

master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_CONDITION_YAW,
    0,
    180,    # angle
    20,     # yaw speed (deg/s)
    1,      # clockwise
    1,      # relative rotation
    0, 0, 0
)

time.sleep(10)

# Second 180° yaw rotation
print("ROTATING ANOTHER 180 DEGREES")

master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_CONDITION_YAW,
    0,
    180,
    20,
    1,
    1,
    0, 0, 0
)

time.sleep(10)

print("LANDING")

master.set_mode_apm("LAND")

print("DONE")
