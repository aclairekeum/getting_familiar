#!/usr/bin/env python


# Transfrom frames odom >< base_link

import rospy
import roslib
import math
import tf
import geometry_msgs.msg
from visualization_msgs.msg import Marker

rospy.init_node('marker_message_v2')

# Listen for transforms
listener = tf.TransformListener()
rate = rospy.Rate(10)

# Create marker
marker = Marker()

marker.header.frame_id = "base_link"
marker.type = marker.SPHERE
marker.action = marker.ADD
marker.scale.x = 0.1
marker.scale.y = 0.1
marker.scale.z = 0.1
marker.color.r = 1.0
marker.color.g = 0.0
marker.color.b = 0.0
marker.color.a = 1.0
marker.pose.position.z=0
marker.pose.position.x = 1 
marker.pose.position.y = 2


#Publish message
pub = rospy.Publisher("/my_marker", Marker, queue_size=10)
r = rospy.Rate(10)
while not rospy.is_shutdown():
	print "test"
	try:
		(trans,rot) = listener.lookupTransform('/odom', '/base_link', rospy.Time(0))
	except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
		print "EXCEPT"
		(trans, rot) = (1, 1)
		continue

	print (trans, rot)
	# marker.pose.position.x = 1 + trans[0]
	# marker.pose.position.y = 2 + trans[1]

	pub.publish(marker)
	r.sleep()