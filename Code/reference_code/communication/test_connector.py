
# event_but_muster -> universal komunikationsstracke
# möglicher einspung: https://github.com/seanpar203/event-bus -> soll als singelton

from time import sleep
from threading import Thread
from instance_x import Instance_X

instance_1 = Instance_X('instance_1')
instance_2 = Instance_X('instance_2')

instance_1.sender.add_listener(instance_2.resiver)
instance_2.sender.add_listener(instance_1.resiver)

Thread(target=instance_2.run).start()
sleep(3)
instance_1.send()
sleep(3)
instance_1.send(message={"name":"Pong", "info":"Hallo zurück"})

