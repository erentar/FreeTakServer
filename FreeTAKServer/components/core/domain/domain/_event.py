from digitalpy.core.parsing.load_configuration import Configuration
from .model_constants import EventVariables as vars
import uuid
from datetime import datetime as dt
import datetime
from FreeTAKServer.components.core.abstract_component.cot_node import CoTNode
from FreeTAKServer.components.core.abstract_component.cot_property import CoTProperty
DATETIME_FMT = "%Y-%m-%dT%H:%M:%S.%fZ"

class Event(CoTNode):
    # TODO: fix emergency methods
    # Event.py
    """Python implementation of the Class Event
    # represents a TAK event: this class is instantiated with a standard set of
    #    values.
    # Generated by Enterprise Architect
    # Created on: 11-Feb-2020 11:08:07 AM
    # Original author: Corvo
    """

    # event as an XML
    # <?xml version="1.0" encoding="UTF-8" standalone="yes"?><event version="2.0" uid="Linux-ABC.server-ping" type="b-t-f" time="2020-02-14T20:32:31.444Z" start="2020-02-14T20:32:31.444Z" stale="2020-02-15T20:32:31.444Z" how="h-g-i-g-o">

    # default constructor

    def __init__(self, configuration: Configuration, model, registry = None, oid=None):
        attributes = {}
        self.__version = None
        self.__uid = None
        self.__type = None
        self.__how = None
        self.__stale = None
        self.__start = None
        self.__time = None
        self.__point = None
        self.__detail = None
        super().__init__(self.__class__.__name__, configuration, model, registry, attributes, oid)

        # flag to determin e if this event is a geo chcat if so, will be added as a
        # prefix to the uid

        # starting time when an event should be considered valid
        start = "%Y-%m-%dT%H:%M:%SZ"
        # basic event
        # Gives a hint about how the coordinates were generated

        # Schema version of this event instance (e.g.  2.0)

        # time stamp: when the event was generated
        time = "%Y-%m-%dT%H:%M:%SZ"

        # Hierarchically organized hint about event type (defaultis is 'a-f-G-I'
        # for infrastructure)

        # ending time when an event should no longer be considered valid
        stale = "%Y-%m-%dT%H:%M:%SZ"

        # Globally unique name for this information on this event can have
        # additional information attached.
        # e.g.  -ping means that this request is a ping

        # flag to determine if this event is a Ping, in this case append to the UID

    @CoTProperty
    def start(self):
        return self.__start

    @start.setter
    def start(self, start: str):
        DATETIME_FMT = "%Y-%m-%dT%H:%M:%S.%fZ"
        if start == None:
            timer = dt
            now = timer.utcnow()
            zulu = now.strftime(DATETIME_FMT)
            self.__start = zulu
        else:
            self.__start = start

    @CoTProperty
    def how(self):
        return self.__how

    @how.setter
    def how(self, how: str):
        self.__how = how

    @CoTProperty
    def uid(self):
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        if uid == None:
            self.uid = str(uuid.uuid1())

        else:
            self.__uid = uid

    @CoTProperty
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @CoTProperty
    def time(self):
        return self.__time

    @time.setter
    def time(self, time: str):
        DATETIME_FMT = "%Y-%m-%dT%H:%M:%S.%fZ"
        if time == None:
            timer = dt
            now = timer.utcnow()
            zulu = now.strftime(DATETIME_FMT)
            self.time = zulu
        else:
            self.__time = time

    @CoTProperty
    def stale(self):
        return self.__stale

    @stale.setter
    def stale(self, stale=None, staletime: dt = dt.utcnow().strftime(DATETIME_FMT)):
        if stale == None:
            DATETIME_FMT = "%Y-%m-%dT%H:%M:%S.%fZ"
            timer = dt
            now = timer.utcnow()
            zulu = now.strftime(DATETIME_FMT)
            add = datetime.timedelta(seconds=staletime)
            stale_part = dt.strptime(zulu, DATETIME_FMT) + add
            self.__stale = stale_part.strftime(DATETIME_FMT)
        else:
            self.__stale = stale

    @CoTProperty
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @CoTProperty
    def point(self):
        return self.__point

    @point.setter
    def point(self, point=None):
        self.__point = point

    @CoTProperty
    def detail(self):
        return self.__detail

    @detail.setter
    def detail(self, detail: detail):
        self.__detail = detail
