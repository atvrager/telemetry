import packets
import pyuv
import signal

class Telemetry(object):
    def __init__(self, hostname, port):
        self.loop = pyuv.Loop.default_loop()
        self.hostname = hostname
        self.port = port

    def update_cb(self, handle, hostinfo, flags, data, error):
        sample = packets.CarInfo()
        sample.unpack(data)
        print(sample.__dict__)

    def handshake_cb(self, handle, hostinfo, flags, data, error):
        self.udp.stop_recv()
        resp = packets.HandshakeResp()
        resp.unpack(data)
        hs = packets.Handshake()
        hs.identifier = 2
        hs.version = 0
        hs.operationId = 1
        self.udp.send((self.hostname, self.port), hs.pack())
        self.udp.start_recv(self.update_cb)

    def sigint_cb(self, handle, signum):
        self.udp.stop_recv()
        hs = packets.Handshake()
        hs.identifier = 2
        hs.version = 0
        hs.operationId = 3
        self.udp.send((self.hostname, self.port), hs.pack())
        self.loop.stop()

    def main(self):
        self.udp = pyuv.UDP(self.loop)
        self.udp.bind(("0.0.0.0", 9997))
        self.udp.start_recv(self.handshake_cb)

        self.sigint = pyuv.Signal(self.loop)
        self.sigint.start(self.sigint_cb, signal.SIGINT)

        hs = packets.Handshake()
        hs.identifier = 2
        hs.version = 0
        hs.operationId = 0

        self.udp.send((self.hostname, self.port), hs.pack())

        self.loop.run(pyuv.UV_RUN_DEFAULT)

if __name__ == "__main__":
    Telemetry("127.0.0.1", 9996).main()
