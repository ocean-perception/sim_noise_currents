cmake_minimum_required(VERSION 2.8.3)
project(sim_noise_currents)

find_package(catkin REQUIRED COMPONENTS
  # ROS Dependencies
  geometry_msgs

  # COLA2 Dependencies
  smarty200_description
)

# Declare things to be passed to dependent projects
catkin_package()

