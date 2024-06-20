import serial
import time

# 設置串口名稱和波特率
serial_port = 'COM5'  # 對於 Windows，可能是 'COM3' 或其他
baud_rate = 9600
output_file = './sample30_g/.txt'

# 打開串口
ser = serial.Serial(serial_port, baud_rate)

try:
    # read capture setting
    while not ser.in_waiting : pass
    data_raw = ser.read_all()  
    data = data_raw.decode()
    print(data)

    with open(output_file, 'a') as file:
        file.write("aX,aY,aZ,gX,gY,gZ")
        while True:
            inputs = input("input something to start capture : ")
            ser.write(bytes(inputs, encoding='utf8'))
            # wait data reply  
            while not ser.in_waiting: pass
            # sleep a while for all data transmit finish
            time.sleep(2)
            # 讀取串口數據
            lines = ser.read_all().decode()
            lines.replace('\r\n', ',').strip(',')
            print(lines)  # 可選：打印到控制台
            file.write(lines)  # 保存到文件
except KeyboardInterrupt:
    # 關閉串口
    ser.close()
