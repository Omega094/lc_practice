from datetime import datetime

def callBack():
    print datetime.now()

#callBack()

#Here is the single threaded version
"""
Problem:
    When one thread (T1) calles registerCallback, if isFired == False, then right after
    it finishes the check and about to put the callback into the callBackQueue,
    at this moment,another thread (T2)  calles triggerEvent and this function 
    finishes, which leaves the callBackQueue empty. 
    Then T1 append the callback to the callBackQueue, in this case, isFired is set to 
    True already but the callBackQueue still has one call back left. 
    
"""
isFired = False
callBackQueue = []

def registerCallback(cb):
    if isFired:
        cb()
    else:
        callBackQueue.append(cb)
    return

def triggerEvent():
    global isFired
    if isFired: return
    isFired = True
    while callBackQueue:
        cb = callBackQueue.pop(0)
        cb()
    return

"""
    Thread safe version V2
    Problem:
    Now this makes the two functions thread safe, however, when the excueting
    time of callback is long, this is still not efficient.  
"""

from threading import Thread, Lock
mutex = Lock()

def registerCallbackV2(cb):
    global isFired
    mutex.acquire()
    if isFired:
        cb()
    else:
        callBackQueue.append(cb)
    mutex.release()
    return

def triggerEventV2():
    global isFired
    mutex.acquire()
    isFired = True
    while callBackQueue:
        cb = callBackQueue.pop()
        cb()
    mutex.release()
    return

"""
    Thread safe version 3, with increasing the granularity of using mutex, 
    we can improve the efficiency to avoid the long time excueting of callback 
    function.
"""
#If the callback takes long time to excute, the register below 
#is more efficient. 

def registerCallbackV3(cb):
    global isFired
    mutex.acquire()
    if not isFired:
        callBackQueue.append(cb)
        mutex.release()
    else:
        mutex.release()
        cb()
    return 


def triggerEventV3():
    global isFired 
    mutex.acquire()
    while callBackQueue:
        cb = callBackQueue.pop(0)
        mutex.release()
        cb()
        mutex.acquire()
    isFired = True
    mutex.release()
    return

#test:

if __name__ == "__main__":
    for i in xrange(5):
        registerCallback(callBack)
    triggerEvent()
    print "Event is triggerred."
    registerCallback(callBack)

    print "/"*100
    print "Now test with V2: "
    isFired = False 
    for i in xrange(5):
        registerCallbackV2(callBack)
    triggerEventV2()
    print "Event is triggerred V2."
    registerCallbackV2(callBack)

    print "/"*100
    print "Now test with V3"
    isFired = False
    for i in xrange(5):
        registerCallbackV3(callBack)
    triggerEventV3()
    print "Event is triggerred V3"
    registerCallbackV3(callBack)

