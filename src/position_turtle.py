#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from turtlebot_koi_gelo.msg import hriks
from nav_msgs.msg import Odometry


class PositionTurtle:
    def __init__(self):
        rospy.init_node('position_turtle', anonymous=True)

        self.pub = rospy.Publisher('/turtle_pos_xy', String, queue_size=10)

        self.current_position = hriks()

        self.odom_sub = rospy.Subscriber('/odom', Odometry, self.odom_callback)

        self.publish_position()

    def odom_callback(self, msg):
        self.current_position.x = msg.pose.pose.position.x
        self.current_position.y = msg.pose.pose.position.y

    def publish_position(self):
        rate = rospy.Rate(0.2)  
        while not rospy.is_shutdown():

            position_str = "Current Position - x: {}, y: {}".format(self.current_position.x, self.current_position.y)
            
            rospy.loginfo(position_str)
            
            self.pub.publish(position_str)
            
            rate.sleep()

if __name__ == '__main__':

    PositionTurtle()