#!/usr/bin/env python

# Basic ros
import rospy

# Import msgs
from sensor_msgs.geometry_msgs import Vector3Stamped

def main():
    # init
    rospy.init_node('sim_noise_currents')

    count = 0

    pub = rospy.Publisher('current', Vector3Stamped, queue_size=10)

    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        msg = Vector3Stamped()
        msg.header.frame_id = 'sim_noise_currents'
        msg.header.stamp = rospy.Time.now()
        msg.header.seq = count
        msg.vector.x = 1.5
        msg.vector.y = 0.0
        msg.vector.z = 0.0
        pub.publish(msg)
        count += 1
        rate.sleep()


if __name__ == '__main__':
    main()

    
