import smbus

class MPU6050:
    def __init__(self, bus=1, address=0x68):
        self.bus = smbus.SMBus(bus)
        self.address = address
        self._setup()
    
    def _setup(self):
        self.bus.write_byte_data(self.address, 0x6B, 0x00)  # 唤醒设备
    
    def get_angles(self):
        """获取简化版姿态角 (roll, pitch)"""
        data = self.bus.read_i2c_block_data(self.address, 0x3B, 4)
        roll = (data[0] << 8) | data[1]
        pitch = (data[2] << 8) | data[3]
        return roll/16384.0, pitch/16384.0  # 转换为角度值

class OV2640:
    def capture_frame(self):
        """模拟摄像头捕获"""
        return bytearray(640*480)  # 伪数据