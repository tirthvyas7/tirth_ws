import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy

class lidarfilter(Node):
    def __init__(self):
        super().__init__ ('lidarfilter')

        # qos_prof = QoSProfile(
        #         reliability=ReliabilityPolicy.BEST_EFFORT,
        #         durability=DurabilityPolicy.VOLATILE,
        #         history=HistoryPolicy.KEEP_LAST,
        #         depth=5
    # )

        self.rec=self.create_subscription(LaserScan,'/lidar/scan',self.fil,10)
        
        self.pub=self.create_publisher(LaserScan,"/filterscan",10)
        self.point=LaserScan()
        # self.timer=self.create_timer(0.05,self.fil(self.point))
        self.get_logger().info("Filtering......")
    def fil(self,point):
        
        self.point=point
        print(int(360*2.094/self.point.angle_max),len(self.point.ranges))
        for i in range (int(360*2.094/self.point.angle_max),360):
            self.point.ranges[i]=1000.0
        
            
        
        
        self.pub.publish(self.point)
        
           

def main(args=None):
    rclpy.init(args=args)
    Lidarfilter = lidarfilter()
    rclpy.spin(Lidarfilter)
    rclpy.shutdown()


if __name__ == '__main__':
    main()