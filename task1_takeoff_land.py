from pymavlink import mavutil
import time

master = mavutil.mavlink_connection('udpin:0.0.0.0:14551')
master.wait_heartbeat()

print("Connected")

# GUIDED mode
master.set_mode_apm("GUIDED")
time.sleep(2)

# Arm
master.arducopter_arm()
master.motors_armed_wait()

print("Taking off")

master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
    0,
    0,0,0,0,0,0,5
)

time.sleep(15)

print("Landing")

master.set_mode_apm("LAND")
