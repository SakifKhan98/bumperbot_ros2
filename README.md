# bumperbot_ros2

A ROS 2 package for controlling and simulating a simple bumper robot. This project provides launch files, nodes, and configuration for running the bumperbot in a ROS 2 environment.

## Features

- ROS 2 nodes for robot control and sensor feedback
- Simulation support (e.g., Gazebo)
- Example launch files
- Basic collision detection and response

## Requirements

- ROS 2 (Humble, Iron, or later)
- Python 3.8+
- Gazebo (optional, for simulation)

## Installation

Clone the repository into your ROS 2 workspace:

```bash
cd ~/ros2_ws/src
git clone https://github.com/yourusername/bumperbot_ros2.git
cd ~/ros2_ws
colcon build
source install/setup.bash
```

## Usage

To launch the bumperbot simulation:

```bash
ros2 launch bumperbot_ros2 bumperbot_sim.launch.py
```

To run the bumperbot control node:

```bash
ros2 run bumperbot_ros2 bumperbot_controller
```

## Contributing

Contributions are welcome! Please open issues or submit pull requests.

## License

This project is licensed under the MIT License.
