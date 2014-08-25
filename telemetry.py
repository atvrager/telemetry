from database import Database
import packets
import pyuv
import signal

class Telemetry(object):
    def __init__(self, hostname, port):
        self.database = Database('telemetry.db')
        self.loop = pyuv.Loop.default_loop()
        self.hostname = hostname
        self.port = port
        self.session = -1

    def update_cb(self, handle, hostinfo, flags, data, error):
        sample = packets.CarInfo()
        sample.unpack(data)
        def insertData(handle):
            self.database.newData(sample.__dict__, self.session)
            self.asyncs.discard(handle)
        self.timeout.again()
        async = pyuv.Async(self.loop, insertData)
        self.asyncs.add(async)
        async.send()

    def handshake_cb(self, handle, hostinfo, flags, data, error):
        self.udp.stop_recv()
        resp = packets.HandshakeResp()
        resp.unpack(data)
        def startSession(handle):
            self.session = self.database.newSession(resp)
            self.asyncs.discard(handle)
        self.timeout.again()
        async = pyuv.Async(self.loop, startSession)
        self.asyncs.add(async)
        async.send()
        hs = packets.Handshake()
        hs.identifier = 2
        hs.version = 0
        hs.operationId = 1
        self.udp.send((self.hostname, self.port), hs.pack())
        self.udp.start_recv(self.update_cb)

    def timeout_cb(self, handle):
        self.udp.stop_recv()
        self.udp.start_recv(self.handshake_cb)
        hs = packets.Handshake()
        hs.identifier = 2
        hs.version = 0
        hs.operationId = 0
        self.udp.send((self.hostname, self.port), hs.pack())

    def sigint_cb(self, handle, signum):
        self.udp.stop_recv()
        hs = packets.Handshake()
        hs.identifier = 2
        hs.version = 0
        hs.operationId = 3
        self.udp.send((self.hostname, self.port), hs.pack())
        self.loop.stop()

    def main(self):
        self.asyncs = set()
        self.udp = pyuv.UDP(self.loop)
        self.udp.bind(("0.0.0.0", 9997))

        self.timeout = pyuv.Timer(self.loop)
        self.timeout.start(self.timeout_cb, 0, 10)

        self.sigint = pyuv.Signal(self.loop)
        self.sigint.start(self.sigint_cb, signal.SIGINT)


        self.loop.run(pyuv.UV_RUN_DEFAULT)

if __name__ == "__main__":
    Telemetry("127.0.0.1", 9996).main()
