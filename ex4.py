strData = "person&long&long&0022ff&0022ff&./airport.mp4"
print("string : ", strData)
mappingName = strData.split("&")
mappingName = mappingName[len(mappingName)-1]
mappingName = mappingName.split(".")
mappingName= mappingName[1].split("/")[1]
print (mappingName[1].split("/")[1])
'''from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
from tensorflow.python.client import device_lib


print(device_lib.list_local_devices())
tf.debugging.set_log_device_placement(True)'''

'''
import tensorflow as tf

tf.debugging.set_log_device_placement(True)

# 텐서 생성
a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
c = tf.matmul(a, b)

print(c)
'''
'''
import torch

print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))'''