import ikpy
import numpy as np
import ikpy.utils.plot as plot_utils
from ikpy.chain import Chain
from ikpy.link import OriginLink, URDFLink
import matplotlib.pyplot
from mpl_toolkits.mplot3d import Axes3D



'''
    target = it will be a 4x4 matrix, we only need to give the trasport vector, so basically it will be [[1,0,0,x],[0,1,0,y],[0,0,1,z],[0,0,0,1]]

'''
class Robot(Chain):

    def __init__(self,name):

        super(Chain).__init__()
        self.name = name
        self.robot = self._create_robot_chain()
        self.links = self.robot.links

    def _create_robot_chain(self):
        
        my_arm_chain = Chain(name='arduino_robot',links=[
            OriginLink(),
            URDFLink(
                name="shoulderZ",
                bounds=(-1.57,1.57),
                origin_translation=[0,0,0],
                origin_orientation=[0,0,1.57],
                rotation=[0,0,1],
            ),
            URDFLink(
                name="shoulderY",
                bounds=(-1.57,1.57),
                origin_translation=[0,0,100],
                origin_orientation=[1.57,0,0],
                rotation=[0,0,1],
            ),
            URDFLink(
                name="elbow",
                bounds=(0,3.14),
                origin_translation=[0,120,0],
                origin_orientation=[0,0,0],
                rotation=[0,0,1],
            ),
            URDFLink(
                name="wristX",
                bounds=(-1.57,1.57),
                origin_translation=[0,80,0],
                origin_orientation=[0,1.57,1.57],
                rotation=[0,0,1]
            ),
            URDFLink(
                name="wristY",
                bounds=(-0.52,1.05),
                origin_translation=[0,0,30], #in metri
                origin_orientation=[-1.57,0,1.57],
                rotation=[0,0,1],
            ),
            URDFLink(
                name="handTool",
                origin_translation=[0,-80,0],
                origin_orientation=[-1.57,-1.57,-1.57],
                rotation=[0,0,0]
            ),
        ])
        return my_arm_chain
