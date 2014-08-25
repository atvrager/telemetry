import sqlite3
import time

class Database(object):
    def __init__(self, path):
        self.path = path
        self.conn = sqlite3.connect(self.path)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self.setupDatabase()

    def setupDatabase(self):
        version = self.getVersion()
        if version == 0:
            self.version1()

    def version1(self):
        self.cursor.execute('CREATE TABLE dbversion (version int);')
        self.cursor.execute('INSERT INTO dbversion VALUES(1);')
        self.cursor.execute('CREATE TABLE sessions (id integer PRIMARY KEY, carName text, driverName text, trackName text, trackConfig blob)')
        self.cursor.execute('CREATE TABLE data (session integer, timestamp integer, absEnabled boolean, absInAction boolean, accGf real, accGh real, accGv real, angular1 real, angular2 real, angular3 real, angular4 real, brake real, camber1 real, camber2 real, camber3 real, camber4 real, carCoordinatesX real, carCoordinatesY real, carCoordinatesZ real, carPosition real, carSlope real, cgHeight real, clutch real, contact1 real, contact2 real, contact3 real, contact4 real, dy1 real, dy2 real, dy3 real, dy4 real, gas real, gear integer, lapBest integer, lapCount integer, lapLast integer, lapTime integer, limiter boolean, load1 real, load2 real, load3 real, load4 real, loadedradius1 real, loadedradius2 real, loadedradius3 real, loadedradius4 real, mz1 real, mz2 real, mz3 real, mz4 real, ndslip1 real, ndslip2 real, ndslip3 real, ndslip4 real, pit boolean, rpm real, size_ integer, slipangle1 real, slipangle2 real, slipangle3 real, slipangle4 real, slipratio1 real, slipratio2 real, slipratio3 real, slipratio4 real, speedKmh real, speedMph real, speedMs real, steer real, suspension1 real, suspension2 real, suspension3 real, suspension4 real, tcEnabled boolean, tcInAction boolean, tyredirty1 real, tyredirty2 real, tyredirty3 real, tyredirty4 real, tyreradius1 real, tyreradius2 real, tyreradius3 real, tyreradius4 real, tyreslip1 real, tyreslip2 real, tyreslip3 real, tyreslip real)')
        self.conn.commit()

    def getVersion(self):
        try:
            self.cursor.execute('SELECT version from dbversion LIMIT 1;')
            version = self.cursor.fetchone()['version']
            return version
        except:
            return 0

    def newSession(self, session):
        self.cursor.execute('INSERT INTO sessions (carName, driverName, trackName, trackConfig) VALUES(?, ?, ?, ?)', (session.carName, session.driverName, session.trackName, session.trackConfig))
        self.conn.commit()
        return self.cursor.lastrowid

    def newData(self, data, sessionid):
        values = (sessionid, time.time()) + list(zip(*sorted(data.items())))[1]
        query = 'INSERT INTO data VALUES('
        for (i, _) in enumerate(values):
            if i < len(values)-1:
                query += '?, '
            else:
                query += '?'
        query += ');'
        self.cursor.execute(query, values)
        self.conn.commit()
