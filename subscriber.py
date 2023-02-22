#!/usr/bin/env python3
import rospy
import cv2
import numpy as np
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

def processer(img_msg):
    
    bridge=CvBridge()
    img=bridge.imgmsg_to_cv2(img_msg)
    img_blur=cv2.GaussianBlur(img, (3, 3), sigmaX=0, sigmaY=0)
    edge_img=cv2.Canny(img_blur, 100, 200)
    edge_img=cv2.cvtColor(edge_img, cv2.COLOR_GRAY2BGR)
    cv2.imshow("Original/Edge", np.hstack([img_blur, edge_img]))
    cv2.waitKey(1)
    
def main():
    rospy.init_node('subscriber')
    rospy.Subscriber('frames', Image, processer)
    rospy.spin()
    cv2.destroyAllWindows()

if __name__=='__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass