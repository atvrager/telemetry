import struct
from struct import Struct

#struct handshaker{
#        int identifier;
#        int version;
#        int operationId;
#        };

class Handshake(Struct):
    def __init__(self):
        super().__init__('iii')
        self.identifier = -1
        self.version = -1
        self.operationId = -1

    def unpack(self, buffer):
        (self.identifier, self.version, self.operationId) = super().unpack(buffer)

    def pack(self):
        return super().pack(self.identifier, self.version, self.operationId)


#struct handshakerResponse{
#        char carName[50];
#        char driverName[50];
#        int identifier;
#        int version;
#        char trackName[50];
#        char trackConfig[50];
#        };

class HandshakeResp(Struct):
    def __init__(self):
        super().__init__('50s102sii50s50s')
        self.carName = b''
        self.driverName = b''
        self.identifier = -1
        self.version = -1
        self.trackName = b''
        self.trackConfig = b''

    def unpack(self, buffer):
        (self.carName, self.driverName, self.identifier, self.version, self.trackName, self.trackConfig) = super().unpack(buffer)

    def pack(self):
        return super().pack(self.carName, self.driverName, self.identifier, self.version, self.trackName, self.trackConfig)

#struct RTCarInfo
#{
#        char identifier;
#        int size;
#
#        float speed_Kmh;
#        float speed_Mph;
#        float speed_Ms;
#
#        bool isAbsEnabled;
#        bool isAbsInAction;
#        bool isTcInAction;
#        bool isTcEnabled;
#        bool isInPit;
#        bool isEngineLimiterOn;
#
#
#        float accG_vertical;
#        float accG_horizontal;
#        float accG_frontal;
#
#        int lapTime;
#        int lastLap;
#        int bestLap;
#        int lapCount;
#
#        float gas;
#        float brake;
#        float clutch;
#        float engineRPM;
#        float steer;
#        int gear;
#        float cgHeight;
#
#        float wheelAngularSpeed[4];
#        float slipAngle[4];
#        float slipAngle_ContactPatch[4];
#        float slipRatio[4];
#        float tyreSlip[4];
#        float ndSlip[4];
#        float load[4];
#        float Dy[4];
#        float Mz[4];
#        float tyreDirtyLevel[4];
#
#        float camberRAD[4];
#        float tyreRadius[4];
#        float tyreLoadedRadius[4];
#        float suspensionHeight[4];
#        float carPositionNormalized;
#        float carSlope;
#        float carCoordinates[3];
#
#} ;

class CarInfo(Struct):
    def __init__(self):
        super().__init__('ci3f2?2???3f4i3fffif4f4f4f4f4f4f4f4f4f4f4f4f4f4fff3f')
        self.size_ = -1
        self.speedKmh = -1
        self.speedMph = -1
        self.speedMs = -1
        self.absEnabled = False
        self.absInAction = False
        self.tcInAction = False
        self.tcEnabled = False
        self.pit = False
        self.limiter = False
        self.accGv = -1
        self.accGh = -1
        self.accGf = -1
        self.lapTime = -1
        self.lapLast = -1
        self.lapBest = -1
        self.lapCount = -1
        self.gas = -1
        self.brake = -1
        self.clutch = -1
        self.rpm = -1
        self.steer = -1
        self.gear = -1
        self.cgHeight = -1
        self.angular1 = -1
        self.angular2 = -1
        self.angular3 = -1
        self.angular4 = -1
        self.slipangle1 = -1
        self.slipangle2 = -1
        self.slipangle3 = -1
        self.slipangle4 = -1
        self.contact1 = -1
        self.contact2 = -1
        self.contact3 = -1
        self.contact4 = -1
        self.slipratio1 = -1
        self.slipratio2 = -1
        self.slipratio3 = -1
        self.slipratio4 = -1
        self.tyreslip1 = -1
        self.tyreslip2 = -1
        self.tyreslip3 = -1
        self.tyreslip4 = -1
        self.ndslip1 = -1
        self.ndslip2 = -1
        self.ndslip3 = -1
        self.ndslip4 = -1
        self.load1 = -1
        self.load2 = -1
        self.load3 = -1
        self.load4 = -1
        self.dy1 = -1
        self.dy2 = -1
        self.dy3 = -1
        self.dy4 = -1
        self.mz1 = -1
        self.mz2 = -1
        self.mz3 = -1
        self.mz4 = -1
        self.tyredirty1 = -1
        self.tyredirty2 = -1
        self.tyredirty3 = -1
        self.tyredirty4 = -1
        self.camber1 = -1
        self.camber2 = -1
        self.camber3 = -1
        self.camber4 = -1
        self.tyreradius1 = -1
        self.tyreradius2 = -1
        self.tyreradius3 = -1
        self.tyreradius4 = -1
        self.loadedradius1 = -1
        self.loadedradius2 = -1
        self.loadedradius3 = -1
        self.loadedradius4 = -1
        self.suspension1 = -1
        self.suspension2 = -1
        self.suspension3 = -1
        self.suspension4 = -1
        self.carPosition = -1
        self.carSlope = -1
        self.carCoordinatesX = -1
        self.carCoordinatesY = -1
        self.carCoordinatesZ = -1

    def pack(self):
        return super().pack(b'a', self.size_, self.speedKmh, self.speedMph, self.speedMs, self.absEnabled, self.absInAction, self.tcInAction, self.tcEnabled, self.pit, self.limiter, self.accGv, self.accGh, self.accGf, self.lapTime, self.lapLast, self.lapBest, self.lapCount, self.gas, self.brake, self.clutch, self.rpm, self.steer, self.gear, self.cgHeight, self.angular1, self.angular2, self.angular3, self.angular4, self.slipangle1, self.slipangle2, self.slipangle3, self.slipangle4, self.contact1, self.contact2, self.contact3, self.contact4, self.slipratio1, self.slipratio2, self.slipratio3, self.slipratio4, self.tyreslip1, self.tyreslip2, self.tyreslip3, self.tyreslip4, self.ndslip1, self.ndslip2, self.ndslip3, self.ndslip4, self.load1, self.load2, self.load3, self.load4, self.dy1, self.dy2, self.dy3, self.dy4, self.mz1, self.mz2, self.mz3, self.mz4, self.tyredirty1, self.tyredirty2, self.tyredirty3, self.tyredirty4, self.camber1, self.camber2, self.camber3, self.camber4, self.tyreradius1, self.tyreradius2, self.tyreradius3, self.tyreradius4, self.loadedradius1, self.loadedradius2, self.loadedradius3, self.loadedradius4, self.suspension1, self.suspension2, self.suspension3, self.suspension4, self.carPosition, self.carSlope, self.carCoordinatesX, self.carCoordinatesY, self.carCoordinatesZ)

    def unpack(self, buffer):
        (_, self.size_, self.speedKmh, self.speedMph, self.speedMs, self.absEnabled, self.absInAction, self.tcInAction, self.tcEnabled, self.pit, self.limiter, self.accGv, self.accGh, self.accGf, self.lapTime, self.lapLast, self.lapBest, self.lapCount, self.gas, self.brake, self.clutch, self.rpm, self.steer, self.gear, self.cgHeight, self.angular1, self.angular2, self.angular3, self.angular4, self.slipangle1, self.slipangle2, self.slipangle3, self.slipangle4, self.contact1, self.contact2, self.contact3, self.contact4, self.slipratio1, self.slipratio2, self.slipratio3, self.slipratio4, self.tyreslip1, self.tyreslip2, self.tyreslip3, self.tyreslip4, self.ndslip1, self.ndslip2, self.ndslip3, self.ndslip4, self.load1, self.load2, self.load3, self.load4, self.dy1, self.dy2, self.dy3, self.dy4, self.mz1, self.mz2, self.mz3, self.mz4, self.tyredirty1, self.tyredirty2, self.tyredirty3, self.tyredirty4, self.camber1, self.camber2, self.camber3, self.camber4, self.tyreradius1, self.tyreradius2, self.tyreradius3, self.tyreradius4, self.loadedradius1, self.loadedradius2, self.loadedradius3, self.loadedradius4, self.suspension1, self.suspension2, self.suspension3, self.suspension4, self.carPosition, self.carSlope, self.carCoordinatesX, self.carCoordinatesY, self.carCoordinatesZ) = super().unpack(buffer)

#struct RTLap
#{
#        int carIdentifierNumber;
#        int lap;
#        char driverName[50];
#        char carName[50];
#        int time;
#        };
class LapInfo(Struct):
    def __init__(self):
        super().__init__('ii50s50si')
        self.carIdentifierNumber = -1
        self.lap = -1
        self.driverName = b''
        self.carName = b''
        self.time = -1

    def pack(self):
        return super().pack(self.carIdentifierNumber, self.lap, self.driverName, self.carName, self.time)

    def unpack(self, buffer):
        (self.carIdentifierNumber, self.lap, self.driverName, self.carName, self.time) = super().unpack(buffer)
