#!/usr/bin/env python3
import rospy
import cv2
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image

def main():
    rospy.init_node('image_publisher')
    bridge=CvBridge()
    cap=cv2.VideoCapture('/home/ingenio/catkin_ws/src/mrt_assignment/scripts/F1Onboards480.mp4')

    pub=rospy.Publisher('frames', Image, queue_size=10)
    rate=rospy.Rate(30)

    while not rospy.is_shutdown():
        ret, frame=cap.read()
        try:
            img_msg=bridge.cv2_to_imgmsg(frame)
        except CvBridgeError as e:
            rospy.logerr('CvBridgeError: {}'.format(e))
            continue
        pub.publish(img_msg)
        rate.sleep()     
    cap.release()

if __name__=='__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass