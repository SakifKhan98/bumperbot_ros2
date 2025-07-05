import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SimpleSubscriber(Node):
    def __init__(self):
        super().__init__("simple_subscriber")
        self.subscriber = self.create_subscription(
            String, "chatter", self.msgCallback, 10
        )
        self.get_logger().info("Simple Subscriber has been started.")

    def msgCallback(self, msg):
        self.get_logger().info(f'Received: "{msg.data}"')


def main():
    rclpy.init()
    simple_subscriber = SimpleSubscriber()
    rclpy.spin(simple_subscriber)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
