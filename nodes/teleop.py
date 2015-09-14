#!/usr/bin/env python

"""
Based on the teleop twist keyboard.
"""
import rospy
from geometry_msgs.msg import Twist

import tty
import select
import sys
import termios

msg = """
Reading from the keyboard  and Publishing to Twist!
---------------------------
Moving around:
		w	 
   a		 d
		s	

space: stop

CTRL-C to quit
"""

rospy.init_node('teleop')

moveBindings = {
		'w':(1,0),
		'a':(0,1),
		'd':(0,-1),
		's':(-1,0),
		   }

speed = 1
turn = 1

def getKey():
		tty.setraw(sys.stdin.fileno())
		select.select([sys.stdin], [], [], 0)
		key = sys.stdin.read(1)
		termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
		return key

settings = termios.tcgetattr(sys.stdin)
key = None

if __name__=="__main__":
	settings = termios.tcgetattr(sys.stdin)
	
	pub = rospy.Publisher('cmd_vel', Twist)

	x = 0
	th = 0
	status = 0

	try:
		print msg
		while(1):
			key = getKey()
			print "\"" + key + "\""

			if key in moveBindings.keys():
				x = moveBindings[key][0]
				print "x", x
				th = moveBindings[key][1]
				print "th", th
			else:
				x = 0
				th = 0
				if (key == '\x03'):
					break

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
	