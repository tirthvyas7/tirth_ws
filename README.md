# Mobile Robot
This repo Consists of a Mobile Robot with RGB Camera and Lidar Mounted on it. It is capable to be teleoperated using keyboard and can filter the data subscribled from Lidar Sensor to restrict its FOV to 120 Degrees.
## 1. bot_description
This repo contains of 3 launch files. 
1. rviz.launch.py- It spawns the robot urdf in rviz2 and it can be visualised.
2. spawn.launch.py- It spawns the bot into an empty world of Gazebo.
3. control.launch.py - Running this launch file will run the teleop__twist_keyboard which will help to operate the bot using keyboard keys.

## 2. bot_world
This repo contains of 1 launch files. 
1. world.launch.py- It spawns the robot in a custom gazebo wolrd.

## 3. bot_control
This repo contains of 1 launch file. 
1. filter.launch.py- It will spawn the robot in a custom gazebo world and start the filtering node which will filter the LaserScan data to 120 Degrees and also it launches Rviz2 to visualize it.


