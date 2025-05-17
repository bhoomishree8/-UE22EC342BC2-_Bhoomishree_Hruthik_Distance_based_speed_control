import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import serial

class DistancePublisher(Node):
    def __init__(self):
        super().__init__('distance_publisher')
        self.publisher_ = self.create_publisher(Int32, 'distance', 10)
        # Update this line for ultrasonic sensor USB
        self.ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)  # Ultrasonic sensor connected here
        self.timer = self.create_timer(0.5, self.publish_distance)

    def publish_distance(self):
        if self.ser.in_waiting:
            line = self.ser.readline().decode().strip()
            if line.isdigit():
                msg = Int32()
                msg.data = int(line)
                self.publisher_.publish(msg)
                self.get_logger().info(f'Published: {msg.data} cm')

def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(DistancePublisher())
    rclpy.shutdown()
