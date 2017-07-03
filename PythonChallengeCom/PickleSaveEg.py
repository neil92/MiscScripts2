#!/usr/bin/python

import pickle

colordic = { "lion":"yellow", "fox":"orange" }

pickle.dump(colordic, open("pickledum.p", "wb"))