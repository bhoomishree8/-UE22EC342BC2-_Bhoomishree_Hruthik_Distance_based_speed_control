import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import serial

class StatusSubscriber(Node):
    def __init__(self):
        super().__init__('status_subscriber')
        # Update this line for LCD USB
        self.ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)  # LCD connected here
        self.subscription = self.create_subscription(
            Int32,
            'distance',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        if msg.data < 10:
            self.ser.write(b'Too close!\n')
        else:
            self.ser.write(b'Distance fine\n')
        self.get_logger().info(f'Sent to LCD: {msg.data} cm')

def main(args=None):
    rclpy.init(args=args)
    rclpy.spin(StatusSubscriber())
    rclpy.shutdown()
