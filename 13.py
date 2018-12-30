#!/usr/bin/env python -w

import xmlrpc.client

with xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php") as proxy:
    print(proxy.system.listMethods())
    print(proxy.system.methodHelp('phone'))
    print(proxy.phone('Bert'))
    # print("3 is even: %s" % str(proxy.is_even(3)))
    # print("100 is even: %s" % str(proxy.is_even(100)))http://www.pythonchallenge.com/pc/phonebook.php

# solution: calling it with 'Bert' gave '555-ITALY' 555-48259