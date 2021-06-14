#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

class Rotator():
    def __init__(self):
        self._cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

    def rotate_forever(self):
        self.twist = Twist()

        r = rospy.Rate(10)
        while not rospy.is_shutdown():
            self.twist.angular.z = 0.1
            self._cmd_pub.publish(self.twist)
            rospy.loginfo("Rotating robot: %s", self.twist)
            r.sleep()

class Move():
    def __init__(self):
        self._cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

    def move_forever(self):
        self.twist = Twist()

        r = rospy.Rate(10)
        while not rospy.is_shutdown():
            self.twist.linear.x = 0.5
            self._cmd_pub.publish(self.twist)
            rospy.loginfo("Moving robot: %s", self.twist)
            r.sleep()
            
def main():
    rospy.init_node('rotate')
    try:
        mover = Move()
        mover.move_forever()
    except rospy.ROSInterruptException:
        pass

if __name__ == '__main__':
    main()