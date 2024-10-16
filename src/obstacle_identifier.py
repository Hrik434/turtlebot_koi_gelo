#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan

class ObstacleIdentifier:
    def __init__(self):
        rospy.init_node('obstacle_identifier', anonymous=True)

        self.pub = rospy.Publisher('/obstacle', String, queue_size=10)

        self.scan_sub = rospy.Subscriber('/scan', LaserScan, self.scan_callback)

        self.detected=False


    def scan_callback(self, msg):
        
        self.found=False

        for distance in msg.ranges:
            if distance > 0 and distance < 30.0:
                self.found = True
                break

        if self.detected==False and self.found==True:
            self.publish_obstacle_message()
            self.detected=True
        elif self.found==False:
            self.detected=False



    def publish_obstacle_message(self):
        
        obstacle_message = "Obstacle Found"
        rospy.loginfo(obstacle_message)  
        self.pub.publish(obstacle_message)  

if __name__ == '__main__':
    
    ObstacleIdentifier()
    rospy.spin()  
    
