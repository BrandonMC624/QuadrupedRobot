import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    model_path = os.path.join(
        get_package_share_directory('ensamble1_description'), 'urdf', 'ensamble1.xacro'
    )
    rviz_config_path = os.path.join(
        get_package_share_directory('ensamble1_description'), 'launch', 'urdf.rviz'
    )
    
    return LaunchDescription([
        DeclareLaunchArgument(
            name='gui',
            default_value='true',
            description='Flag to enable joint state publisher GUI'
        ),
        
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            condition=LaunchConfiguration('gui')
        ),
        
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': Command(['xacro ', model_path])}]
        ),
        
        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', rviz_config_path],
            output='screen'
        )
    ])