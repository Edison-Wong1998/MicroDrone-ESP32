import time
from sensors import MPU6050, OV2640
from motor import ESCController

class MicroDrone:
    def __init__(self):
        self.imu = MPU6050()
        self.camera = OV2640()
        self.esc = ESCController(pins=[16,17,18,19])
        
    def start(self):
        """初始化设备"""
        self.imu.calibrate()
        self.esc.arm()
        print("Drone Ready!")
        
    def flight_loop(self):
        """主飞行循环"""
        try:
            while True:
                roll, pitch = self.imu.get_angles()
                self.esc.adjust_motors(roll, pitch)
                time.sleep(0.004)  # 250Hz频率
        except KeyboardInterrupt:
            self.esc.stop()

if __name__ == "__main__":
    drone = MicroDrone()
    drone.start()
    drone.flight_loop()