# Drone Simulation Tasks using ArduPilot SITL and Gazebo

## Overview

This project demonstrates autonomous drone control in a simulated environment using ArduPilot SITL, Gazebo, MAVProxy, and PyMAVLink.

Three flight tasks were implemented and tested successfully:

1. Takeoff and Land
2. Hover and Yaw Rotation
3. Circular Flight and Return to Launch (RTL)

The objective was to control the drone through MAVLink commands and validate autonomous flight behaviors in simulation.

---

## Software Stack

* ArduPilot SITL
* Gazebo Simulation
* MAVProxy
* PyMAVLink
* Ubuntu 22.04 (WSL)

---

## Repository Structure

```text
.
├── README.md
├── task1_takeoff_land.py
├── task2_hover_yaw.py
└── task3_circle_rtl.py
```

---

## MAVLink Connection

The scripts communicate with the simulated vehicle through MAVProxy's forwarded MAVLink stream:

```python
master = mavutil.mavlink_connection('udpin:0.0.0.0:14551')
```

---

## Task 1 – Takeoff and Land

### Objective

* Arm the drone
* Take off to 5 meters altitude
* Hover briefly
* Land safely

### Result

The drone successfully performed autonomous takeoff and landing in the simulation environment.

---

## Task 2 – Hover and Yaw Rotation

### Objective

* Take off to 5 meters altitude
* Maintain hover
* Perform a complete 360° yaw rotation
* Land safely

### Result

The drone maintained altitude while executing two consecutive 180° yaw rotations, completing a full 360° turn before landing.

---

## Task 3 – Circular Flight and Return to Launch

### Objective

* Take off to 5 meters altitude
* Fly a circular trajectory
* Return to launch point

### Implementation

A velocity-based controller was implemented using PyMAVLink. The drone's velocity vector is continuously updated to generate circular motion.

```python
vx = -speed * math.sin(angle)
vy =  speed * math.cos(angle)
```

### Result

The drone successfully:

* Took off to the target altitude
* Executed a circular flight path
* Returned to launch (RTL)

---

## Execution

Start Gazebo and ArduPilot SITL, then run any task:

```bash
python3 task1_takeoff_land.py
```

```bash
python3 task2_hover_yaw.py
```

```bash
python3 task3_circle_rtl.py
```

---

## Demonstration

Screen recordings demonstrating successful execution of all three tasks are provided separately.

---

## Author

Shreya Singh
