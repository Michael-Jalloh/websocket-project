from websocket import create_connection
ws = create_connection('ws://127.0.0.1:9001')
print 'Type "QUIT"  to cancel'

while 1:
	msg = raw_input('Enter your msg: ')
	if msg =='QUIT':
		break
	ws.send(msg)
	msg = ws.recv()
	print 'Reply: {}'.format(msg)

ws.close()
