#!/usr/bin/env python
import rospy
from rst_robot.msg import pwm_cmd , dist_wheels

class Robot :
    def __init__(self,id_rst) :
        self._batteryLevel = 100.0
        self._id = id_rst
        self._state = "free" 
        # if the robot has a mission state = "busy"
        # if the top is filled state = "Working"
        # if the top is empty ( returning ) state = "exiting" 
        self._Tables = []
        self._menu = []
        self._dist_wheels = [] # distance des roues
        self._pwm_cmd = [] # Commandes des moteurs
        self._current_dist_wheels = []
        self._previous_dist_wheels = []
        self._velocity_wheels = []

        self._name_node = "robot_" + str(self._id)
        rospy.init_node(self._name_node,anonymous=True)
        self._publisher_pwm_cmd = rospy.Publisher('/pwm_cmd',pwm_cmd,queue_size=10)
        rospy.Subscriber('/dist_wheels',dist_wheels,self.callback_dist_wheels)
        

    def callback_dist_wheels(self,dist_wheels):
        pass

    def fill_Table(self,clientId) :
        self._state = "Busy"
        # fill the Table with MarkersIds 

        # fill the Menu  Table

        pass
    
    def set_batteryLevel(self,value) :
        self._batteryLevel = value
    
    def set_RobotId(self):
        # check available IDs (saved in text file)
        pass


R1 = Robot(0)
rospy.spin()
