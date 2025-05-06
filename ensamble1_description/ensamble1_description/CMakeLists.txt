cmake_minimum_required(VERSION 3.8)
project(ensamble1_description)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)

# Install launch files
install(DIRECTORY launch/
  DESTINATION share/${PROJECT_NAME}/
)

# Install URDF and Xacro files
install(DIRECTORY urdf/
  DESTINATION share/${PROJECT_NAME}/
)

# Install config files if applicable
install(DIRECTORY config/
  DESTINATION share/${PROJECT_NAME}/
)

# If there are C++ nodes, uncomment and modify accordingly
# add_executable(my_cpp_node src/my_cpp_node.cpp)
# ament_target_dependencies(my_cpp_node rclcpp)
# install(TARGETS my_cpp_node
#   DESTINATION lib/${PROJECT_NAME})

# Export package dependencies
ament_package()