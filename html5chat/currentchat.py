import sys
import time

print "Content-Type: text/event-stream\n\n"
sys.stdout.flush()
message = 'hi world'

count = 0
while count < 10:
    count+= 1
    print 'Data: '+ message + " \n\n"
    sys.stdout.flush()
    time.sleep(2)
