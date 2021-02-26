#*******sys python文件*********
import _thread
from machine import UART
import utime
#*******sys python文件*********

#*******user python文件*********

class Uart2_Class():

    def __init__(self):
        self.uart2 = UART(UART.UART2, 115200, 8, 0, 1, 0)
        self.uart2_list = []               #串口数据缓存列表
        self.nema_line_str = ""            #存储NEMA LINE DATA
        self.get_gps_flag = 0
        self.gps_lat = "1111.1111"         #纬度
        self.gps_lon = "1111.1111"         #经度

    def Get_GPS_Location_Callback(self):
        print("GET GPS")
        if self.get_gps_flag == 1:
            print("Get Location: ", self.gps_lat, self.gps_lon)
        else:
            print("No Location")

    def recv_uart_buff(self):
        msgLen = self.uart2.any()
        if msgLen >= 1:
            msg = self.uart2.read(msgLen)
            for byte in msg:
                # print("byte: ",byte)
                # print("char: ",chr(byte))
                self.uart2_list.append(chr(byte))


    def Get_Nema_Line(self):
        nema_line_flag = False
        if len(self.uart2_list) >= 1:
            uart2_str = ''.join(self.uart2_list)
            index = uart2_str.find('\n')
            if index != -1:
                print("get nema line")
                self.nema_line_str = uart2_str[:index+1]
                print(self.nema_line_str)

                self.uart2_list.clear()
                nema_buff = uart2_str[index+1:]
                self.uart2_list.append(nema_buff)
                print("nema_buff: ",nema_buff)
                nema_line_flag = True

        if nema_line_flag == True:
            return True
        else:
            return False


    def Nema_Line_Prase(self):
        if self.nema_line_str.find("RMC") != -1:
            # print("get RMC")
            str_list = self.nema_line_str.split(',')
            if str_list[0].find("RMC") == -1:
                print("RMC data error")    #第一个列表对象没有RMC字符串
                return
            elif len(str_list) != 13:
                print("RMC data error")   #RMC DATA 数据长度错误
                return
            elif str_list[2] == 'A':
                self.get_gps_flag = 1
                self.gps_lat = str_list[3]
                self.gps_lon = str_list[5]
            else:
                self.get_gps_flag = 0
            self.Get_GPS_Location_Callback()
        else:
            print("no rmc line")

    def Read(self):
        while 1:
            utime.sleep_ms(1)
            self.recv_uart_buff()
            if self.Get_Nema_Line() == True:
                self.Nema_Line_Prase()

    def run(self):
        # 创建一个线程来监听接收uart消息
        _thread.start_new_thread(self.Read, ())





