import launch
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode


def generate_launch_description():
    """Generate launch description with multiple components."""
    container = ComposableNodeContainer(
            node_name='phidget_container',
            node_namespace='',
            package='rclcpp_components',
            node_executable='component_container',
            composable_node_descriptions=[
                ComposableNode(
                    package='phidgets_digital_inputs',
                    node_plugin='phidgets::DigitalInputsRosI',
                    node_name='phidgets_digital_inputs',
                    parameters=[{'serial':-1,'hub_port':0,'is_hub_port_device':True,'publish_rate':0}],
                ),
            ],
            output='screen',
    )

    return launch.LaunchDescription([container])
