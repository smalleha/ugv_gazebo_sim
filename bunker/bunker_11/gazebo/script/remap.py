import sys
import rospy
from moveit_commander import MoveGroupCommander, roscpp_initialize
import moveit_commander

# remap again
joint_state_topic = ['joint_states:=/aubo_i5/joint_states']
moveit_commander.roscpp_initialize(joint_state_topic)
rospy.init_node('foo', anonymous=False)
roscpp_initialize(sys.argv)

aubo_i5 = MoveGroupCommander('aubo_i5')
print right_arm.get_current_pose()