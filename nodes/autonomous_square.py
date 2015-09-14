#!/usr/bin/env python

"""
Based on the teleop twist keyboard.
"""
import rospy
import time

from geometry_msgs.msg import Twist

import tty
import select
import sys
import termios

t_linear = 4400
t_angle =  1600

rospy.init_node('autonomous_square')

moveBindings = {
		'w':(1,0),
		'a':(0,1),
		'd':(0,-1),
		's':(-1,0),
		   }

speed = 1
turn = 1

def get_time():
	return int(round(time.time() * 1000))


if __name__=="__main__":
	cstart = get_time()
	settings = termios.tcgetattr(sys.stdin)
	pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
	r = rospy.Rate(10)
	
	x = 0
	th = 0
	status = 0

	try:
		while(1):
			key = getKey()

			
			t_elapsed = get_time() - cstart

			if (t_elapsed < t_linear):
				x = 1
				th = 0
			elif (t_elapsed < t_linear + t_angle):
				x = 0
				th = -1
			elif (t_elapsed > t_linear+t_angle):
				cstart = get_time()

			print "(x, th):", x, th

			twist = Twist()
			twist.linear.x = x*speed; twist.linear.y = 0; twist.linear.z = 0
			twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = th*turn
			pub.publish(twist)
	except Exception as e:
		print e

	finally:
		twist = Twist()
		twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
		twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
		pub.publish(twist)

		termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
	