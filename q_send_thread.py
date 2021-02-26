from usr import q_msg_queue
import utime
import _thread
from usr import q_mqtt

class send_thread_class():

    def send_thread_func(self,thread_name, thread_id):
        while 1:
            utime.sleep_ms(1)
            if len(q_msg_queue.pack_msg_queue.list_id) > 0:
                msg = q_msg_queue.pack_msg_queue.get_queue()
                #do something
                print("send msg:",msg)
                #send msg by mqtt
                q_mqtt.mqtt.put_msg(msg)

    def run(self):
        _thread.start_new_thread(self.send_thread_func, ("send_thread", 4))


send_thread = send_thread_class()