#!/usr/bin/env python
import rosbag
import matplotlib.pyplot as plt
bag = rosbag.Bag('2020-03-30-12-29-43.bag')

for topic, msg, t in bag.read_messages(topics=['/joint_states']):
    print(msg)
bag.close()