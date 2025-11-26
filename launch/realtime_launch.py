"""启动gscam2，使用低延迟RTMP参数"""

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    config_dir = os.path.join(get_package_share_directory("gscam2"), "cfg")
    params_file = os.path.join(config_dir, "realtime_param.yaml")

    node = Node(
        package="gscam2",
        executable="gscam_main",
        name="gscam_publisher",
        output="screen",
        parameters=[params_file],
    )

    return LaunchDescription([node])


