#!/usr/bin/env python

import rospy
from visualization_msgs.msg import Marker

rospy.init_node('marker_message')

# marker = Marker(type=Marker.SPHERE, 
# 				color=[1, 1, 1, 1],
# 				# color.r=1,
# 				# color.g=1,  
# 				scale=[.1, .1, .1])
marker = Marker()

marker.header.frame_id = "odom"
marker.type = marker.SPHERE
marker.action = marker.ADD
marker.scale.x = 0.1
marker.scale.y = 0.1
marker.scale.z = 0.1
marker.color.r = 1.0
marker.color.g = 0.0
marker.color.b = 0.0
marker.color.a = 1.0
marker.pose.position.x=1
marker.pose.position.y=2
marker.pose.position.z=0


#Publish message
pub = rospy.Publisher("/my_marker", Marker, queue_size=10)
r = rospy.Rate(10)
while not rospy.is_shutdown():
	pub.publish(marker)
	r.sleep()