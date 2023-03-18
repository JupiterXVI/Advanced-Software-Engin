
# event_but_muster -> universal komunikationsstracke
# möglicher einspung: https://github.com/seanpar203/event-bus -> soll als singelton

from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.join(sys_path[0], '..'))

from time import sleep
from threading import Thread
from communication import Sender, Resiver
from communication import Runner


test_sender = Sender()
test_resiver = Resiver()
runner = Runner()

runner.sender.add_listener(test_resiver)
test_sender.add_listener(runner.resiver)

info_packet1 = {
    'function':'myprint',
    'parameter':'Hallo Word'
}

info_packet2 = {
    'function':'byebye',
    'parameter':''
}



Thread(target=runner.run).start()
sleep(3)
test_sender.set_event(name='print_message', info=info_packet1)
test_sender.send()
sleep(3)
test_sender.set_event(name='print_message', info=info_packet2)
test_sender.send()
#instance_1.send(message={"name":"Pong", "info":"Hallo zurück"})

