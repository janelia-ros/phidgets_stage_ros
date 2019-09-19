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
                    node_name='phidgets_digital_inputs1',
                    parameters=[{'serial':-1,'hub_port':1,'is_hub_port_device':True,'publish_rate':0}],
                ),
                ComposableNode(
                    package='phidgets_digital_inputs',
                    node_plugin='phidgets::DigitalInputsRosI',
                    node_name='phidgets_digital_inputs3',
                    parameters=[{'serial':-1,'hub_port':3,'is_hub_port_device':True,'publish_rate':0}],
                ),
                # ComposableNode(
                #     package='phidgets_motors',
                #     node_plugin='phidgets::MotorsRosI',
                #     node_name='phidgets_motors',
                #     parameters=[{'serial':-1,'hub_port':0,'braking_strength':0.0,'data_interval_ms':250,'publish_rate':0}],
                # ),
            ],
            output='screen',
    )

    return launch.LaunchDescription([container])
