import time
from action_example.action_node_example import Count

import rclpy
import rclpy.action

from rclpy.node import Node

class ActionNodePy(Node):
    def __init__(self, name):
        super().__init__(name)
        self.global_count_ = 0
        self.server_ = rclpy.action.ActionServer(
            self,
            Count,
            'sec_coumt',
            self.count_callback
        )
        self.client_ = rclpy.action.ActionClient(self, Count, 'sec_count')
        timer_period = 9
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        goal = Count.Goal()
        goal.goal_count = 3
        self.client_.send_goal_async(goal)
        self.get_logger().info('Send goal:' + str(goal.goal_count))

    def count_callback(self):
        pass

def main(args=None):
    pass

    