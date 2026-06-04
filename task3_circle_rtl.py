from pymavlink import mavutil
import time
import math

print("CONNECTING")

master = mavutil.mavlink_connection('udpin:0.0.0.0:14551')

print("WAITING HEARTBEAT")
master.wait_heartbeat()

print("CONNECTED")

# Switch to GUIDED
master.set_mode_apm("GUIDED")
time.sleep(2)

# Arm
print("ARMING")
master.arducopter_arm()
master.motors_armed_wait()

print("ARMED")

# Takeoff
print("TAKING OFF")

master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
    0,
    0, 0, 0, 0, 0, 0, 5
)

# Wait to reach altitude
time.sleep(12)

print("STARTING CIRCLE")

speed = 1.0      # m/s
radius = 3.0     # m
omega = speed / radius

start = time.time()

while time.time() - start < 25:

    t = time.time() - start

    vx = -speed * math.sin(omega * t)
    vy =  speed * math.cos(omega * t)

    master.mav.set_position_target_local_ned_send(
        0,
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_FRAME_LOCAL_NED,
        0b0000111111000111,
        0, 0, 0,
        vx, vy, 0,
        0, 0, 0,
        0, 0
    )

    time.sleep(0.05)

print("RTL")

master.set_mode_apm("RTL")

print("DONE")
