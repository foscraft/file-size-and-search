#!/usr/bin/python
# -*- coding: utf-8 -*-

import dsse_c
import pickle
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Provide at least one argument, please")
        sys.exit(1)

    client = dsse_c.DSSEClient()
    client.importkeys(pickle.load(open("keys", "rb")))

   

    token = client.SrchToken(sys.argv[1])
    print("Searching for keyword {}").format(sys.argv[1])