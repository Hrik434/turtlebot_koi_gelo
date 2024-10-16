#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

class command_history:
    def __init__(self) -> None:
        rospy.init_node('Command_history', anonymous=True)

        self.sub=rospy.Subscriber("/sending_command_topic", String, self.history_callback)

        self.history = []


    def history_callback(self,data):
        command = data.data
        self.history.append(command)
        rospy.loginfo("Command received: {}".format(command))
        rospy.loginfo("current history: {}".format(self.history))


if __name__=='__main__':
    command_history()
    rospy.spin()

