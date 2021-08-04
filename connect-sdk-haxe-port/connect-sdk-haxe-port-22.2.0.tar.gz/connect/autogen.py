import sys

import math as python_lib_Math
import math as Math
from os import path as python_lib_os_Path
import inspect as python_lib_Inspect
import sys as python_lib_Sys
import builtins as python_lib_Builtins
import functools as python_lib_Functools
import json as python_lib_Json
try:
    import msvcrt as python_lib_Msvcrt
except:
    pass
import os as python_lib_Os
import random as python_lib_Random
import re as python_lib_Re
import shutil as python_lib_Shutil
import subprocess as python_lib_Subprocess
try:
    import termios as python_lib_Termios
except:
    pass
import time as python_lib_Time
import timeit as python_lib_Timeit
import traceback as python_lib_Traceback
try:
    import tty as python_lib_Tty
except:
    pass
from datetime import datetime as python_lib_datetime_Datetime
from datetime import timedelta as python_lib_datetime_Timedelta
from datetime import tzinfo as python_lib_datetime_Tzinfo
from datetime import timezone as python_lib_datetime_Timezone
from io import IOBase as python_lib_io_IOBase
from io import BufferedIOBase as python_lib_io_BufferedIOBase
from io import RawIOBase as python_lib_io_RawIOBase
from io import FileIO as python_lib_io_FileIO
from io import TextIOBase as python_lib_io_TextIOBase
from io import StringIO as python_lib_io_StringIO
from json import JSONEncoder as python_lib_json_JSONEncoder
from time import struct_time as python_lib_time_StructTime
import urllib.parse as python_lib_urllib_Parse


class _hx_AnonObject:
    _hx_disable_getattr = False
    def __init__(self, fields):
        self.__dict__ = fields
    def __repr__(self):
        return repr(self.__dict__)
    def __contains__(self, item):
        return item in self.__dict__
    def __getitem__(self, item):
        return self.__dict__[item]
    def __getattr__(self, name):
        if (self._hx_disable_getattr):
            raise AttributeError('field does not exist')
        else:
            return None
    def _hx_hasattr(self,field):
        self._hx_disable_getattr = True
        try:
            getattr(self, field)
            self._hx_disable_getattr = False
            return True
        except AttributeError:
            self._hx_disable_getattr = False
            return False



_hx_classes = {}


class Enum:
    _hx_class_name = "Enum"
    __slots__ = ("tag", "index", "params")
    _hx_fields = ["tag", "index", "params"]
    _hx_methods = ["__str__"]

    def __init__(self,tag,index,params):
        self.tag = tag
        self.index = index
        self.params = params

    def __str__(self):
        if (self.params is None):
            return self.tag
        else:
            return self.tag + '(' + (', '.join(str(v) for v in self.params)) + ')'

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.tag = None
        _hx_o.index = None
        _hx_o.params = None
Enum._hx_class = Enum
_hx_classes["Enum"] = Enum


class Class: pass


class Connect:
    _hx_class_name = "Connect"
    __slots__ = ()
    _hx_statics = ["main"]

    @staticmethod
    def main():
        pass
Connect._hx_class = Connect
_hx_classes["Connect"] = Connect


class Date:
    _hx_class_name = "Date"
    __slots__ = ("date", "dateUTC")
    _hx_fields = ["date", "dateUTC"]
    _hx_methods = ["getTime", "getHours", "getMinutes", "getSeconds", "getFullYear", "getMonth", "getDate", "getDay", "getUTCHours", "getUTCMinutes", "getUTCSeconds", "getUTCFullYear", "getUTCMonth", "getUTCDate", "getUTCDay", "getTimezoneOffset", "toString"]
    _hx_statics = ["now", "fromTime", "makeLocal", "UTC", "fromString"]

    def __init__(self,year,month,day,hour,_hx_min,sec):
        self.dateUTC = None
        if (year < python_lib_datetime_Datetime.min.year):
            year = python_lib_datetime_Datetime.min.year
        if (day == 0):
            day = 1
        self.date = Date.makeLocal(python_lib_datetime_Datetime(year,(month + 1),day,hour,_hx_min,sec,0))
        self.dateUTC = self.date.astimezone(python_lib_datetime_Timezone.utc)

    def getTime(self):
        return (self.date.timestamp() * 1000)

    def getHours(self):
        return self.date.hour

    def getMinutes(self):
        return self.date.minute

    def getSeconds(self):
        return self.date.second

    def getFullYear(self):
        return self.date.year

    def getMonth(self):
        return (self.date.month - 1)

    def getDate(self):
        return self.date.day

    def getDay(self):
        return HxOverrides.mod(self.date.isoweekday(), 7)

    def getUTCHours(self):
        return self.dateUTC.hour

    def getUTCMinutes(self):
        return self.dateUTC.minute

    def getUTCSeconds(self):
        return self.dateUTC.second

    def getUTCFullYear(self):
        return self.dateUTC.year

    def getUTCMonth(self):
        return (self.dateUTC.month - 1)

    def getUTCDate(self):
        return self.dateUTC.day

    def getUTCDay(self):
        return HxOverrides.mod(self.dateUTC.isoweekday(), 7)

    def getTimezoneOffset(self):
        x = (self.date.utcoffset() / python_lib_datetime_Timedelta(0,60))
        tmp = None
        try:
            tmp = int(x)
        except BaseException as _g:
            None
            tmp = None
        return -tmp

    def toString(self):
        return self.date.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def now():
        d = Date(2000,0,1,0,0,0)
        d.date = Date.makeLocal(python_lib_datetime_Datetime.now())
        d.dateUTC = d.date.astimezone(python_lib_datetime_Timezone.utc)
        return d

    @staticmethod
    def fromTime(t):
        d = Date(2000,0,1,0,0,0)
        d.date = Date.makeLocal(python_lib_datetime_Datetime.fromtimestamp((t / 1000.0)))
        d.dateUTC = d.date.astimezone(python_lib_datetime_Timezone.utc)
        return d

    @staticmethod
    def makeLocal(date):
        try:
            return date.astimezone()
        except BaseException as _g:
            None
            tzinfo = python_lib_datetime_Datetime.now(python_lib_datetime_Timezone.utc).astimezone().tzinfo
            return date.replace(**python__KwArgs_KwArgs_Impl_.fromT(_hx_AnonObject({'tzinfo': tzinfo})))

    @staticmethod
    def UTC(year,month,day,hour,_hx_min,sec):
        return (python_lib_datetime_Datetime(year,(month + 1),day,hour,_hx_min,sec,0,python_lib_datetime_Timezone.utc).timestamp() * 1000)

    @staticmethod
    def fromString(s):
        _g = len(s)
        if (_g == 8):
            k = s.split(":")
            return Date.fromTime((((Std.parseInt((k[0] if 0 < len(k) else None)) * 3600000.) + ((Std.parseInt((k[1] if 1 < len(k) else None)) * 60000.))) + ((Std.parseInt((k[2] if 2 < len(k) else None)) * 1000.))))
        elif (_g == 10):
            k = s.split("-")
            return Date(Std.parseInt((k[0] if 0 < len(k) else None)),(Std.parseInt((k[1] if 1 < len(k) else None)) - 1),Std.parseInt((k[2] if 2 < len(k) else None)),0,0,0)
        elif (_g == 19):
            k = s.split(" ")
            _this = (k[0] if 0 < len(k) else None)
            y = _this.split("-")
            _this = (k[1] if 1 < len(k) else None)
            t = _this.split(":")
            return Date(Std.parseInt((y[0] if 0 < len(y) else None)),(Std.parseInt((y[1] if 1 < len(y) else None)) - 1),Std.parseInt((y[2] if 2 < len(y) else None)),Std.parseInt((t[0] if 0 < len(t) else None)),Std.parseInt((t[1] if 1 < len(t) else None)),Std.parseInt((t[2] if 2 < len(t) else None)))
        else:
            raise haxe_Exception.thrown(("Invalid date format : " + ("null" if s is None else s)))

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.date = None
        _hx_o.dateUTC = None
Date._hx_class = Date
_hx_classes["Date"] = Date


class EReg:
    _hx_class_name = "EReg"
    __slots__ = ("pattern", "matchObj", "_hx_global")
    _hx_fields = ["pattern", "matchObj", "global"]
    _hx_methods = ["match", "matched", "matchedLeft", "matchedRight", "matchedPos", "matchSub", "split", "replace", "map"]
    _hx_statics = ["escape"]

    def __init__(self,r,opt):
        self.matchObj = None
        self._hx_global = False
        options = 0
        _g = 0
        _g1 = len(opt)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            c = (-1 if ((i >= len(opt))) else ord(opt[i]))
            if (c == 109):
                options = (options | python_lib_Re.M)
            if (c == 105):
                options = (options | python_lib_Re.I)
            if (c == 115):
                options = (options | python_lib_Re.S)
            if (c == 117):
                options = (options | python_lib_Re.U)
            if (c == 103):
                self._hx_global = True
        self.pattern = python_lib_Re.compile(r,options)

    def match(self,s):
        self.matchObj = python_lib_Re.search(self.pattern,s)
        return (self.matchObj is not None)

    def matched(self,n):
        return self.matchObj.group(n)

    def matchedLeft(self):
        return HxString.substr(self.matchObj.string,0,self.matchObj.start())

    def matchedRight(self):
        return HxString.substr(self.matchObj.string,self.matchObj.end(),None)

    def matchedPos(self):
        return _hx_AnonObject({'pos': self.matchObj.start(), 'len': (self.matchObj.end() - self.matchObj.start())})

    def matchSub(self,s,pos,_hx_len = None):
        if (_hx_len is None):
            _hx_len = -1
        if (_hx_len != -1):
            self.matchObj = self.pattern.search(s,pos,(pos + _hx_len))
        else:
            self.matchObj = self.pattern.search(s,pos)
        return (self.matchObj is not None)

    def split(self,s):
        if self._hx_global:
            ret = []
            lastEnd = 0
            x = python_HaxeIterator(python_lib_Re.finditer(self.pattern,s))
            while x.hasNext():
                x1 = x.next()
                x2 = HxString.substring(s,lastEnd,x1.start())
                ret.append(x2)
                lastEnd = x1.end()
            x = HxString.substr(s,lastEnd,None)
            ret.append(x)
            return ret
        else:
            self.matchObj = python_lib_Re.search(self.pattern,s)
            if (self.matchObj is None):
                return [s]
            else:
                return [HxString.substring(s,0,self.matchObj.start()), HxString.substr(s,self.matchObj.end(),None)]

    def replace(self,s,by):
        _this = by.split("$$")
        by = "_hx_#repl#__".join([python_Boot.toString1(x1,'') for x1 in _this])
        def _hx_local_0(x):
            res = by
            g = x.groups()
            _g = 0
            _g1 = len(g)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                gs = g[i]
                if (gs is None):
                    continue
                delimiter = ("$" + HxOverrides.stringOrNull(str((i + 1))))
                _this = (list(res) if ((delimiter == "")) else res.split(delimiter))
                res = gs.join([python_Boot.toString1(x1,'') for x1 in _this])
            _this = res.split("_hx_#repl#__")
            res = "$".join([python_Boot.toString1(x1,'') for x1 in _this])
            return res
        replace = _hx_local_0
        return python_lib_Re.sub(self.pattern,replace,s,(0 if (self._hx_global) else 1))

    def map(self,s,f):
        buf_b = python_lib_io_StringIO()
        pos = 0
        right = s
        cur = self
        while (pos < len(s)):
            if (self.matchObj is None):
                self.matchObj = python_lib_Re.search(self.pattern,s)
            else:
                self.matchObj = self.matchObj.re.search(s,pos)
            if (self.matchObj is None):
                break
            pos1 = self.matchObj.end()
            curPos_pos = cur.matchObj.start()
            curPos_len = (cur.matchObj.end() - cur.matchObj.start())
            buf_b.write(Std.string(HxString.substr(HxString.substr(cur.matchObj.string,0,cur.matchObj.start()),pos,None)))
            buf_b.write(Std.string(f(cur)))
            right = HxString.substr(cur.matchObj.string,cur.matchObj.end(),None)
            if (not self._hx_global):
                buf_b.write(Std.string(right))
                return buf_b.getvalue()
            if (curPos_len == 0):
                buf_b.write(Std.string(("" if (((pos1 < 0) or ((pos1 >= len(s))))) else s[pos1])))
                right = HxString.substr(right,1,None)
                pos = (pos1 + 1)
            else:
                pos = pos1
        buf_b.write(Std.string(right))
        return buf_b.getvalue()

    @staticmethod
    def escape(s):
        return python_lib_Re.escape(s)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.pattern = None
        _hx_o.matchObj = None
        _hx_o._hx_global = None
EReg._hx_class = EReg
_hx_classes["EReg"] = EReg


class _EnumValue_EnumValue_Impl_:
    _hx_class_name = "_EnumValue.EnumValue_Impl_"
    __slots__ = ()
    _hx_statics = ["match"]

    @staticmethod
    def match(this1,pattern):
        return False
_EnumValue_EnumValue_Impl_._hx_class = _EnumValue_EnumValue_Impl_
_hx_classes["_EnumValue.EnumValue_Impl_"] = _EnumValue_EnumValue_Impl_


class IntIterator:
    _hx_class_name = "IntIterator"
    __slots__ = ("min", "max")
    _hx_fields = ["min", "max"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,_hx_min,_hx_max):
        self.min = _hx_min
        self.max = _hx_max

    def hasNext(self):
        return (self.min < self.max)

    def next(self):
        def _hx_local_3():
            def _hx_local_2():
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.min
                _hx_local_0.min = (_hx_local_1 + 1)
                return _hx_local_1
            return _hx_local_2()
        return _hx_local_3()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.min = None
        _hx_o.max = None
IntIterator._hx_class = IntIterator
_hx_classes["IntIterator"] = IntIterator


class Lambda:
    _hx_class_name = "Lambda"
    __slots__ = ()
    _hx_statics = ["array", "list", "map", "mapi", "flatten", "flatMap", "has", "exists", "foreach", "iter", "filter", "fold", "foldi", "count", "empty", "indexOf", "find", "findIndex", "concat"]

    @staticmethod
    def array(it):
        a = list()
        i = HxOverrides.iterator(it)
        while i.hasNext():
            i1 = i.next()
            a.append(i1)
        return a

    @staticmethod
    def list(it):
        l = haxe_ds_List()
        i = HxOverrides.iterator(it)
        while i.hasNext():
            i1 = i.next()
            l.add(i1)
        return l

    @staticmethod
    def map(it,f):
        _g = []
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            x2 = f(x1)
            _g.append(x2)
        return _g

    @staticmethod
    def mapi(it,f):
        i = 0
        _g = []
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            x2 = i
            i = (i + 1)
            x3 = f(x2,x1)
            _g.append(x3)
        return _g

    @staticmethod
    def flatten(it):
        _g = []
        e = HxOverrides.iterator(it)
        while e.hasNext():
            e1 = e.next()
            x = HxOverrides.iterator(e1)
            while x.hasNext():
                x1 = x.next()
                _g.append(x1)
        return _g

    @staticmethod
    def flatMap(it,f):
        _g = []
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            x2 = f(x1)
            _g.append(x2)
        _g1 = []
        e = HxOverrides.iterator(_g)
        while e.hasNext():
            e1 = e.next()
            x = HxOverrides.iterator(e1)
            while x.hasNext():
                x1 = x.next()
                _g1.append(x1)
        return _g1

    @staticmethod
    def has(it,elt):
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            if HxOverrides.eq(x1,elt):
                return True
        return False

    @staticmethod
    def exists(it,f):
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            if f(x1):
                return True
        return False

    @staticmethod
    def foreach(it,f):
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            if (not f(x1)):
                return False
        return True

    @staticmethod
    def iter(it,f):
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            f(x1)

    @staticmethod
    def filter(it,f):
        _g = []
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            if f(x1):
                _g.append(x1)
        return _g

    @staticmethod
    def fold(it,f,first):
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            first = f(x1,first)
        return first

    @staticmethod
    def foldi(it,f,first):
        i = 0
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            first = f(x1,first,i)
            i = (i + 1)
        return first

    @staticmethod
    def count(it,pred = None):
        n = 0
        if (pred is None):
            _ = HxOverrides.iterator(it)
            while _.hasNext():
                _1 = _.next()
                n = (n + 1)
        else:
            x = HxOverrides.iterator(it)
            while x.hasNext():
                x1 = x.next()
                if pred(x1):
                    n = (n + 1)
        return n

    @staticmethod
    def empty(it):
        return (not HxOverrides.iterator(it).hasNext())

    @staticmethod
    def indexOf(it,v):
        i = 0
        v2 = HxOverrides.iterator(it)
        while v2.hasNext():
            v21 = v2.next()
            if HxOverrides.eq(v,v21):
                return i
            i = (i + 1)
        return -1

    @staticmethod
    def find(it,f):
        v = HxOverrides.iterator(it)
        while v.hasNext():
            v1 = v.next()
            if f(v1):
                return v1
        return None

    @staticmethod
    def findIndex(it,f):
        i = 0
        v = HxOverrides.iterator(it)
        while v.hasNext():
            v1 = v.next()
            if f(v1):
                return i
            i = (i + 1)
        return -1

    @staticmethod
    def concat(a,b):
        l = list()
        x = HxOverrides.iterator(a)
        while x.hasNext():
            x1 = x.next()
            l.append(x1)
        x = HxOverrides.iterator(b)
        while x.hasNext():
            x1 = x.next()
            l.append(x1)
        return l
Lambda._hx_class = Lambda
_hx_classes["Lambda"] = Lambda


class Reflect:
    _hx_class_name = "Reflect"
    __slots__ = ()
    _hx_statics = ["hasField", "field", "setField", "getProperty", "setProperty", "callMethod", "fields", "isFunction", "compare", "isClosure", "compareMethods", "isObject", "isEnumValue", "deleteField", "copy", "makeVarArgs"]

    @staticmethod
    def hasField(o,field):
        return python_Boot.hasField(o,field)

    @staticmethod
    def field(o,field):
        return python_Boot.field(o,field)

    @staticmethod
    def setField(o,field,value):
        setattr(o,(("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field)),value)

    @staticmethod
    def getProperty(o,field):
        if (o is None):
            return None
        if (field in python_Boot.keywords):
            field = ("_hx_" + field)
        elif ((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95))):
            field = ("_hx_" + field)
        if isinstance(o,_hx_AnonObject):
            return Reflect.field(o,field)
        tmp = Reflect.field(o,("get_" + ("null" if field is None else field)))
        if ((tmp is not None) and callable(tmp)):
            return tmp()
        else:
            return Reflect.field(o,field)

    @staticmethod
    def setProperty(o,field,value):
        field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
        if isinstance(o,_hx_AnonObject):
            setattr(o,field1,value)
        elif hasattr(o,("set_" + ("null" if field1 is None else field1))):
            getattr(o,("set_" + ("null" if field1 is None else field1)))(value)
        else:
            setattr(o,field1,value)

    @staticmethod
    def callMethod(o,func,args):
        if callable(func):
            return func(*args)
        else:
            return None

    @staticmethod
    def fields(o):
        return python_Boot.fields(o)

    @staticmethod
    def isFunction(f):
        if (not ((python_lib_Inspect.isfunction(f) or python_lib_Inspect.ismethod(f)))):
            return python_Boot.hasField(f,"func_code")
        else:
            return True

    @staticmethod
    def compare(a,b):
        if ((a is None) and ((b is None))):
            return 0
        if (a is None):
            return 1
        elif (b is None):
            return -1
        elif HxOverrides.eq(a,b):
            return 0
        elif (a > b):
            return 1
        else:
            return -1

    @staticmethod
    def isClosure(v):
        return isinstance(v,python_internal_MethodClosure)

    @staticmethod
    def compareMethods(f1,f2):
        if HxOverrides.eq(f1,f2):
            return True
        if (isinstance(f1,python_internal_MethodClosure) and isinstance(f2,python_internal_MethodClosure)):
            m1 = f1
            m2 = f2
            if HxOverrides.eq(m1.obj,m2.obj):
                return (m1.func == m2.func)
            else:
                return False
        if ((not Reflect.isFunction(f1)) or (not Reflect.isFunction(f2))):
            return False
        return False

    @staticmethod
    def isObject(v):
        _g = Type.typeof(v)
        tmp = _g.index
        if (tmp == 4):
            return True
        elif (tmp == 6):
            _g1 = _g.params[0]
            return True
        else:
            return False

    @staticmethod
    def isEnumValue(v):
        if not HxOverrides.eq(v,Enum):
            return isinstance(v,Enum)
        else:
            return False

    @staticmethod
    def deleteField(o,field):
        if (field in python_Boot.keywords):
            field = ("_hx_" + field)
        elif ((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95))):
            field = ("_hx_" + field)
        if (not python_Boot.hasField(o,field)):
            return False
        o.__delattr__(field)
        return True

    @staticmethod
    def copy(o):
        if (o is None):
            return None
        o2 = _hx_AnonObject({})
        _g = 0
        _g1 = python_Boot.fields(o)
        while (_g < len(_g1)):
            f = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            value = Reflect.field(o,f)
            setattr(o2,(("_hx_" + f) if ((f in python_Boot.keywords)) else (("_hx_" + f) if (((((len(f) > 2) and ((ord(f[0]) == 95))) and ((ord(f[1]) == 95))) and ((ord(f[(len(f) - 1)]) != 95)))) else f)),value)
        return o2

    @staticmethod
    def makeVarArgs(f):
        def _hx_local_0(*v):
            this1 = v
            return f((list(this1) if ((not Std.isOfType(this1,list))) else this1))
        return _hx_local_0
Reflect._hx_class = Reflect
_hx_classes["Reflect"] = Reflect


class Std:
    _hx_class_name = "Std"
    __slots__ = ()
    _hx_statics = ["downcast", "instance", "isMetaType", "is", "isOfType", "string", "int", "parseInt", "shortenPossibleNumber", "parseFloat", "random"]

    @staticmethod
    def downcast(value,c):
        try:
            tmp = None
            if (not isinstance(value,c)):
                if c._hx_is_interface:
                    cls = c
                    loop = None
                    def _hx_local_1(intf):
                        f = (intf._hx_interfaces if (hasattr(intf,"_hx_interfaces")) else [])
                        if (f is not None):
                            _g = 0
                            while (_g < len(f)):
                                i = (f[_g] if _g >= 0 and _g < len(f) else None)
                                _g = (_g + 1)
                                if (i == cls):
                                    return True
                                else:
                                    l = loop(i)
                                    if l:
                                        return True
                            return False
                        else:
                            return False
                    loop = _hx_local_1
                    currentClass = value.__class__
                    result = False
                    while (currentClass is not None):
                        if loop(currentClass):
                            result = True
                            break
                        currentClass = python_Boot.getSuperClass(currentClass)
                    tmp = result
                else:
                    tmp = False
            else:
                tmp = True
            if tmp:
                return value
            else:
                return None
        except BaseException as _g:
            None
            return None

    @staticmethod
    def instance(value,c):
        return Std.downcast(value,c)

    @staticmethod
    def isMetaType(v,t):
        return (v == t)

    @staticmethod
    def _hx_is(v,t):
        return Std.isOfType(v,t)

    @staticmethod
    def isOfType(v,t):
        if ((v is None) and ((t is None))):
            return False
        if (t is None):
            return False
        if (t == Dynamic):
            return (v is not None)
        isBool = isinstance(v,bool)
        if ((t == Bool) and isBool):
            return True
        if ((((not isBool) and (not (t == Bool))) and (t == Int)) and isinstance(v,int)):
            return True
        vIsFloat = isinstance(v,float)
        tmp = None
        tmp1 = None
        if (((not isBool) and vIsFloat) and (t == Int)):
            f = v
            tmp1 = (((f != Math.POSITIVE_INFINITY) and ((f != Math.NEGATIVE_INFINITY))) and (not python_lib_Math.isnan(f)))
        else:
            tmp1 = False
        if tmp1:
            tmp1 = None
            try:
                tmp1 = int(v)
            except BaseException as _g:
                None
                tmp1 = None
            tmp = (v == tmp1)
        else:
            tmp = False
        if ((tmp and ((v <= 2147483647))) and ((v >= -2147483648))):
            return True
        if (((not isBool) and (t == Float)) and isinstance(v,(float, int))):
            return True
        if (t == str):
            return isinstance(v,str)
        isEnumType = (t == Enum)
        if ((isEnumType and python_lib_Inspect.isclass(v)) and hasattr(v,"_hx_constructs")):
            return True
        if isEnumType:
            return False
        isClassType = (t == Class)
        if ((((isClassType and (not isinstance(v,Enum))) and python_lib_Inspect.isclass(v)) and hasattr(v,"_hx_class_name")) and (not hasattr(v,"_hx_constructs"))):
            return True
        if isClassType:
            return False
        tmp = None
        try:
            tmp = isinstance(v,t)
        except BaseException as _g:
            None
            tmp = False
        if tmp:
            return True
        if python_lib_Inspect.isclass(t):
            cls = t
            loop = None
            def _hx_local_1(intf):
                f = (intf._hx_interfaces if (hasattr(intf,"_hx_interfaces")) else [])
                if (f is not None):
                    _g = 0
                    while (_g < len(f)):
                        i = (f[_g] if _g >= 0 and _g < len(f) else None)
                        _g = (_g + 1)
                        if (i == cls):
                            return True
                        else:
                            l = loop(i)
                            if l:
                                return True
                    return False
                else:
                    return False
            loop = _hx_local_1
            currentClass = v.__class__
            result = False
            while (currentClass is not None):
                if loop(currentClass):
                    result = True
                    break
                currentClass = python_Boot.getSuperClass(currentClass)
            return result
        else:
            return False

    @staticmethod
    def string(s):
        return python_Boot.toString1(s,"")

    @staticmethod
    def int(x):
        try:
            return int(x)
        except BaseException as _g:
            None
            return None

    @staticmethod
    def parseInt(x):
        if (x is None):
            return None
        try:
            return int(x)
        except BaseException as _g:
            None
            base = 10
            _hx_len = len(x)
            foundCount = 0
            sign = 0
            firstDigitIndex = 0
            lastDigitIndex = -1
            previous = 0
            _g = 0
            _g1 = _hx_len
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                c = (-1 if ((i >= len(x))) else ord(x[i]))
                if (((c > 8) and ((c < 14))) or ((c == 32))):
                    if (foundCount > 0):
                        return None
                    continue
                else:
                    c1 = c
                    if (c1 == 43):
                        if (foundCount == 0):
                            sign = 1
                        elif (not (((48 <= c) and ((c <= 57))))):
                            if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                                break
                    elif (c1 == 45):
                        if (foundCount == 0):
                            sign = -1
                        elif (not (((48 <= c) and ((c <= 57))))):
                            if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                                break
                    elif (c1 == 48):
                        if (not (((foundCount == 0) or (((foundCount == 1) and ((sign != 0))))))):
                            if (not (((48 <= c) and ((c <= 57))))):
                                if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                                    break
                    elif ((c1 == 120) or ((c1 == 88))):
                        if ((previous == 48) and ((((foundCount == 1) and ((sign == 0))) or (((foundCount == 2) and ((sign != 0))))))):
                            base = 16
                        elif (not (((48 <= c) and ((c <= 57))))):
                            if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                                break
                    elif (not (((48 <= c) and ((c <= 57))))):
                        if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                            break
                if (((foundCount == 0) and ((sign == 0))) or (((foundCount == 1) and ((sign != 0))))):
                    firstDigitIndex = i
                foundCount = (foundCount + 1)
                lastDigitIndex = i
                previous = c
            if (firstDigitIndex <= lastDigitIndex):
                digits = HxString.substring(x,firstDigitIndex,(lastDigitIndex + 1))
                try:
                    return (((-1 if ((sign == -1)) else 1)) * int(digits,base))
                except BaseException as _g:
                    return None
            return None

    @staticmethod
    def shortenPossibleNumber(x):
        r = ""
        _g = 0
        _g1 = len(x)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            c = ("" if (((i < 0) or ((i >= len(x))))) else x[i])
            _g2 = HxString.charCodeAt(c,0)
            if (_g2 is None):
                break
            else:
                _g3 = _g2
                if (((((((((((_g3 == 57) or ((_g3 == 56))) or ((_g3 == 55))) or ((_g3 == 54))) or ((_g3 == 53))) or ((_g3 == 52))) or ((_g3 == 51))) or ((_g3 == 50))) or ((_g3 == 49))) or ((_g3 == 48))) or ((_g3 == 46))):
                    r = (("null" if r is None else r) + ("null" if c is None else c))
                else:
                    break
        return r

    @staticmethod
    def parseFloat(x):
        try:
            return float(x)
        except BaseException as _g:
            None
            if (x is not None):
                r1 = Std.shortenPossibleNumber(x)
                if (r1 != x):
                    return Std.parseFloat(r1)
            return Math.NaN

    @staticmethod
    def random(x):
        if (x <= 0):
            return 0
        else:
            return int((python_lib_Random.random() * x))
Std._hx_class = Std
_hx_classes["Std"] = Std


class Float: pass


class Int: pass


class Bool: pass


class Dynamic: pass


class StringBuf:
    _hx_class_name = "StringBuf"
    __slots__ = ("b",)
    _hx_fields = ["b"]
    _hx_methods = ["get_length", "add", "add1", "addChar", "addSub", "toString"]

    def __init__(self):
        self.b = python_lib_io_StringIO()

    def get_length(self):
        pos = self.b.tell()
        self.b.seek(0,2)
        _hx_len = self.b.tell()
        self.b.seek(pos,0)
        return _hx_len

    def add(self,x):
        s = Std.string(x)
        self.b.write(s)

    def add1(self,s):
        self.b.write(s)

    def addChar(self,c):
        s = "".join(map(chr,[c]))
        self.b.write(s)

    def addSub(self,s,pos,_hx_len = None):
        s1 = (HxString.substr(s,pos,None) if ((_hx_len is None)) else HxString.substr(s,pos,_hx_len))
        self.b.write(s1)

    def toString(self):
        return self.b.getvalue()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.b = None
StringBuf._hx_class = StringBuf
_hx_classes["StringBuf"] = StringBuf


class haxe_SysTools:
    _hx_class_name = "haxe.SysTools"
    __slots__ = ()
    _hx_statics = ["winMetaCharacters", "quoteUnixArg", "quoteWinArg"]

    @staticmethod
    def quoteUnixArg(argument):
        if (argument == ""):
            return "''"
        _this = EReg("[^a-zA-Z0-9_@%+=:,./-]","")
        _this.matchObj = python_lib_Re.search(_this.pattern,argument)
        if (_this.matchObj is None):
            return argument
        return (("'" + HxOverrides.stringOrNull(StringTools.replace(argument,"'","'\"'\"'"))) + "'")

    @staticmethod
    def quoteWinArg(argument,escapeMetaCharacters):
        _this = EReg("^[^ \t\\\\\"]+$","")
        _this.matchObj = python_lib_Re.search(_this.pattern,argument)
        if (_this.matchObj is None):
            result_b = python_lib_io_StringIO()
            needquote = None
            startIndex = None
            if (((argument.find(" ") if ((startIndex is None)) else HxString.indexOfImpl(argument," ",startIndex))) == -1):
                startIndex = None
                needquote = (((argument.find("\t") if ((startIndex is None)) else HxString.indexOfImpl(argument,"\t",startIndex))) != -1)
            else:
                needquote = True
            needquote1 = (needquote or ((argument == "")))
            if needquote1:
                result_b.write("\"")
            bs_buf = StringBuf()
            _g = 0
            _g1 = len(argument)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                _g2 = HxString.charCodeAt(argument,i)
                if (_g2 is None):
                    c = _g2
                    if (bs_buf.get_length() > 0):
                        result_b.write(Std.string(bs_buf.b.getvalue()))
                        bs_buf = StringBuf()
                    result_b.write("".join(map(chr,[c])))
                else:
                    _g3 = _g2
                    if (_g3 == 34):
                        bs = bs_buf.b.getvalue()
                        result_b.write(Std.string(bs))
                        result_b.write(Std.string(bs))
                        bs_buf = StringBuf()
                        result_b.write("\\\"")
                    elif (_g3 == 92):
                        bs_buf.b.write("\\")
                    else:
                        c1 = _g2
                        if (bs_buf.get_length() > 0):
                            result_b.write(Std.string(bs_buf.b.getvalue()))
                            bs_buf = StringBuf()
                        result_b.write("".join(map(chr,[c1])))
            result_b.write(Std.string(bs_buf.b.getvalue()))
            if needquote1:
                result_b.write(Std.string(bs_buf.b.getvalue()))
                result_b.write("\"")
            argument = result_b.getvalue()
        if escapeMetaCharacters:
            result_b = python_lib_io_StringIO()
            _g = 0
            _g1 = len(argument)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                c = HxString.charCodeAt(argument,i)
                if (python_internal_ArrayImpl.indexOf(haxe_SysTools.winMetaCharacters,c,None) >= 0):
                    result_b.write("".join(map(chr,[94])))
                result_b.write("".join(map(chr,[c])))
            return result_b.getvalue()
        else:
            return argument
haxe_SysTools._hx_class = haxe_SysTools
_hx_classes["haxe.SysTools"] = haxe_SysTools


class StringTools:
    _hx_class_name = "StringTools"
    __slots__ = ()
    _hx_statics = ["urlEncode", "urlDecode", "htmlEscape", "htmlUnescape", "contains", "startsWith", "endsWith", "isSpace", "ltrim", "rtrim", "trim", "lpad", "rpad", "replace", "hex", "fastCodeAt", "unsafeCodeAt", "iterator", "keyValueIterator", "isEof", "quoteUnixArg", "winMetaCharacters", "quoteWinArg"]

    @staticmethod
    def urlEncode(s):
        return python_lib_urllib_Parse.quote(s,"")

    @staticmethod
    def urlDecode(s):
        return python_lib_urllib_Parse.unquote(s)

    @staticmethod
    def htmlEscape(s,quotes = None):
        buf_b = python_lib_io_StringIO()
        _g_offset = 0
        _g_s = s
        while (_g_offset < len(_g_s)):
            index = _g_offset
            _g_offset = (_g_offset + 1)
            code = ord(_g_s[index])
            code1 = code
            if (code1 == 34):
                if quotes:
                    buf_b.write("&quot;")
                else:
                    buf_b.write("".join(map(chr,[code])))
            elif (code1 == 38):
                buf_b.write("&amp;")
            elif (code1 == 39):
                if quotes:
                    buf_b.write("&#039;")
                else:
                    buf_b.write("".join(map(chr,[code])))
            elif (code1 == 60):
                buf_b.write("&lt;")
            elif (code1 == 62):
                buf_b.write("&gt;")
            else:
                buf_b.write("".join(map(chr,[code])))
        return buf_b.getvalue()

    @staticmethod
    def htmlUnescape(s):
        _this = s.split("&gt;")
        _this1 = ">".join([python_Boot.toString1(x1,'') for x1 in _this])
        _this = _this1.split("&lt;")
        _this1 = "<".join([python_Boot.toString1(x1,'') for x1 in _this])
        _this = _this1.split("&quot;")
        _this1 = "\"".join([python_Boot.toString1(x1,'') for x1 in _this])
        _this = _this1.split("&#039;")
        _this1 = "'".join([python_Boot.toString1(x1,'') for x1 in _this])
        _this = _this1.split("&amp;")
        return "&".join([python_Boot.toString1(x1,'') for x1 in _this])

    @staticmethod
    def contains(s,value):
        startIndex = None
        return (((s.find(value) if ((startIndex is None)) else HxString.indexOfImpl(s,value,startIndex))) != -1)

    @staticmethod
    def startsWith(s,start):
        return s.startswith(start)

    @staticmethod
    def endsWith(s,end):
        return s.endswith(end)

    @staticmethod
    def isSpace(s,pos):
        if (((len(s) == 0) or ((pos < 0))) or ((pos >= len(s)))):
            return False
        c = HxString.charCodeAt(s,pos)
        if (not (((c > 8) and ((c < 14))))):
            return (c == 32)
        else:
            return True

    @staticmethod
    def ltrim(s):
        l = len(s)
        r = 0
        while ((r < l) and StringTools.isSpace(s,r)):
            r = (r + 1)
        if (r > 0):
            return HxString.substr(s,r,(l - r))
        else:
            return s

    @staticmethod
    def rtrim(s):
        l = len(s)
        r = 0
        while ((r < l) and StringTools.isSpace(s,((l - r) - 1))):
            r = (r + 1)
        if (r > 0):
            return HxString.substr(s,0,(l - r))
        else:
            return s

    @staticmethod
    def trim(s):
        return StringTools.ltrim(StringTools.rtrim(s))

    @staticmethod
    def lpad(s,c,l):
        if (len(c) <= 0):
            return s
        buf = StringBuf()
        l = (l - len(s))
        while (buf.get_length() < l):
            s1 = Std.string(c)
            buf.b.write(s1)
        s1 = Std.string(s)
        buf.b.write(s1)
        return buf.b.getvalue()

    @staticmethod
    def rpad(s,c,l):
        if (len(c) <= 0):
            return s
        buf = StringBuf()
        s1 = Std.string(s)
        buf.b.write(s1)
        while (buf.get_length() < l):
            s = Std.string(c)
            buf.b.write(s)
        return buf.b.getvalue()

    @staticmethod
    def replace(s,sub,by):
        _this = (list(s) if ((sub == "")) else s.split(sub))
        return by.join([python_Boot.toString1(x1,'') for x1 in _this])

    @staticmethod
    def hex(n,digits = None):
        s = ""
        hexChars = "0123456789ABCDEF"
        while True:
            index = (n & 15)
            s = (HxOverrides.stringOrNull((("" if (((index < 0) or ((index >= len(hexChars))))) else hexChars[index]))) + ("null" if s is None else s))
            n = HxOverrides.rshift(n, 4)
            if (not ((n > 0))):
                break
        if ((digits is not None) and ((len(s) < digits))):
            diff = (digits - len(s))
            _g = 0
            _g1 = diff
            while (_g < _g1):
                _ = _g
                _g = (_g + 1)
                s = ("0" + ("null" if s is None else s))
        return s

    @staticmethod
    def fastCodeAt(s,index):
        if (index >= len(s)):
            return -1
        else:
            return ord(s[index])

    @staticmethod
    def unsafeCodeAt(s,index):
        return ord(s[index])

    @staticmethod
    def iterator(s):
        return haxe_iterators_StringIterator(s)

    @staticmethod
    def keyValueIterator(s):
        return haxe_iterators_StringKeyValueIterator(s)

    @staticmethod
    def isEof(c):
        return (c == -1)

    @staticmethod
    def quoteUnixArg(argument):
        if (argument == ""):
            return "''"
        else:
            _this = EReg("[^a-zA-Z0-9_@%+=:,./-]","")
            _this.matchObj = python_lib_Re.search(_this.pattern,argument)
            if (_this.matchObj is None):
                return argument
            else:
                return (("'" + HxOverrides.stringOrNull(StringTools.replace(argument,"'","'\"'\"'"))) + "'")

    @staticmethod
    def quoteWinArg(argument,escapeMetaCharacters):
        argument1 = argument
        _this = EReg("^[^ \t\\\\\"]+$","")
        _this.matchObj = python_lib_Re.search(_this.pattern,argument1)
        if (_this.matchObj is None):
            result_b = python_lib_io_StringIO()
            needquote = None
            startIndex = None
            if (((argument1.find(" ") if ((startIndex is None)) else HxString.indexOfImpl(argument1," ",startIndex))) == -1):
                startIndex = None
                needquote = (((argument1.find("\t") if ((startIndex is None)) else HxString.indexOfImpl(argument1,"\t",startIndex))) != -1)
            else:
                needquote = True
            needquote1 = (needquote or ((argument1 == "")))
            if needquote1:
                result_b.write("\"")
            bs_buf = StringBuf()
            _g = 0
            _g1 = len(argument1)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                _g2 = HxString.charCodeAt(argument1,i)
                if (_g2 is None):
                    c = _g2
                    if (bs_buf.get_length() > 0):
                        result_b.write(Std.string(bs_buf.b.getvalue()))
                        bs_buf = StringBuf()
                    result_b.write("".join(map(chr,[c])))
                else:
                    _g3 = _g2
                    if (_g3 == 34):
                        bs = bs_buf.b.getvalue()
                        result_b.write(Std.string(bs))
                        result_b.write(Std.string(bs))
                        bs_buf = StringBuf()
                        result_b.write("\\\"")
                    elif (_g3 == 92):
                        bs_buf.b.write("\\")
                    else:
                        c1 = _g2
                        if (bs_buf.get_length() > 0):
                            result_b.write(Std.string(bs_buf.b.getvalue()))
                            bs_buf = StringBuf()
                        result_b.write("".join(map(chr,[c1])))
            result_b.write(Std.string(bs_buf.b.getvalue()))
            if needquote1:
                result_b.write(Std.string(bs_buf.b.getvalue()))
                result_b.write("\"")
            argument1 = result_b.getvalue()
        if escapeMetaCharacters:
            result_b = python_lib_io_StringIO()
            _g = 0
            _g1 = len(argument1)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                c = HxString.charCodeAt(argument1,i)
                if (python_internal_ArrayImpl.indexOf(haxe_SysTools.winMetaCharacters,c,None) >= 0):
                    result_b.write("".join(map(chr,[94])))
                result_b.write("".join(map(chr,[c])))
            return result_b.getvalue()
        else:
            return argument1
StringTools._hx_class = StringTools
_hx_classes["StringTools"] = StringTools


class sys_FileSystem:
    _hx_class_name = "sys.FileSystem"
    __slots__ = ()
    _hx_statics = ["exists", "stat", "rename", "fullPath", "absolutePath", "isDirectory", "createDirectory", "deleteFile", "deleteDirectory", "readDirectory"]

    @staticmethod
    def exists(path):
        return python_lib_os_Path.exists(path)

    @staticmethod
    def stat(path):
        s = python_lib_Os.stat(path)
        return _hx_AnonObject({'gid': s.st_gid, 'uid': s.st_uid, 'atime': Date.fromTime((1000 * s.st_atime)), 'mtime': Date.fromTime((1000 * s.st_mtime)), 'ctime': Date.fromTime((1000 * s.st_ctime)), 'size': s.st_size, 'dev': s.st_dev, 'ino': s.st_ino, 'nlink': s.st_nlink, 'rdev': getattr(s,"st_rdev",0), 'mode': s.st_mode})

    @staticmethod
    def rename(path,newPath):
        python_lib_Os.rename(path,newPath)

    @staticmethod
    def fullPath(relPath):
        return python_lib_os_Path.realpath(relPath)

    @staticmethod
    def absolutePath(relPath):
        if haxe_io_Path.isAbsolute(relPath):
            return relPath
        return haxe_io_Path.join([Sys.getCwd(), relPath])

    @staticmethod
    def isDirectory(path):
        return python_lib_os_Path.isdir(path)

    @staticmethod
    def createDirectory(path):
        python_lib_Os.makedirs(path,511,True)

    @staticmethod
    def deleteFile(path):
        python_lib_Os.remove(path)

    @staticmethod
    def deleteDirectory(path):
        python_lib_Os.rmdir(path)

    @staticmethod
    def readDirectory(path):
        return python_lib_Os.listdir(path)
sys_FileSystem._hx_class = sys_FileSystem
_hx_classes["sys.FileSystem"] = sys_FileSystem


class Sys:
    _hx_class_name = "Sys"
    __slots__ = ()
    _hx_statics = ["environ", "get_environ", "time", "exit", "print", "println", "args", "getEnv", "putEnv", "environment", "sleep", "setTimeLocale", "getCwd", "setCwd", "systemName", "command", "cpuTime", "executablePath", "_programPath", "programPath", "getChar", "stdin", "stdout", "stderr"]
    environ = None

    @staticmethod
    def get_environ():
        _g = Sys.environ
        if (_g is None):
            environ = haxe_ds_StringMap()
            env = python_lib_Os.environ
            key = python_HaxeIterator(iter(env.keys()))
            while key.hasNext():
                key1 = key.next()
                value = env.get(key1,None)
                environ.h[key1] = value
            def _hx_local_1():
                def _hx_local_0():
                    Sys.environ = environ
                    return Sys.environ
                return _hx_local_0()
            return _hx_local_1()
        else:
            env = _g
            return env

    @staticmethod
    def time():
        return python_lib_Time.time()

    @staticmethod
    def exit(code):
        python_lib_Sys.exit(code)

    @staticmethod
    def print(v):
        python_Lib.printString(Std.string(v))

    @staticmethod
    def println(v):
        _hx_str = Std.string(v)
        python_Lib.printString((("" + ("null" if _hx_str is None else _hx_str)) + HxOverrides.stringOrNull(python_Lib.lineEnd)))

    @staticmethod
    def args():
        argv = python_lib_Sys.argv
        return argv[1:None]

    @staticmethod
    def getEnv(s):
        return Sys.get_environ().h.get(s,None)

    @staticmethod
    def putEnv(s,v):
        python_lib_Os.putenv(s,v)
        Sys.get_environ().h[s] = v

    @staticmethod
    def environment():
        return Sys.get_environ()

    @staticmethod
    def sleep(seconds):
        python_lib_Time.sleep(seconds)

    @staticmethod
    def setTimeLocale(loc):
        return False

    @staticmethod
    def getCwd():
        return python_lib_Os.getcwd()

    @staticmethod
    def setCwd(s):
        python_lib_Os.chdir(s)

    @staticmethod
    def systemName():
        _g = python_lib_Sys.platform
        x = _g
        if x.startswith("linux"):
            return "Linux"
        else:
            _g1 = _g
            _hx_local_0 = len(_g1)
            if (_hx_local_0 == 5):
                if (_g1 == "win32"):
                    return "Windows"
                else:
                    raise haxe_Exception.thrown("not supported platform")
            elif (_hx_local_0 == 6):
                if (_g1 == "cygwin"):
                    return "Windows"
                elif (_g1 == "darwin"):
                    return "Mac"
                else:
                    raise haxe_Exception.thrown("not supported platform")
            else:
                raise haxe_Exception.thrown("not supported platform")

    @staticmethod
    def command(cmd,args = None):
        if (args is None):
            return python_lib_Subprocess.call(cmd,**python__KwArgs_KwArgs_Impl_.fromT(_hx_AnonObject({'shell': True})))
        else:
            return python_lib_Subprocess.call(([cmd] + args))

    @staticmethod
    def cpuTime():
        return python_lib_Timeit.default_timer()

    @staticmethod
    def executablePath():
        return python_internal_ArrayImpl._get(python_lib_Sys.argv, 0)

    @staticmethod
    def programPath():
        return Sys._programPath

    @staticmethod
    def getChar(echo):
        ch = None
        _g = Sys.systemName()
        _g1 = _g
        _hx_local_0 = len(_g1)
        if (_hx_local_0 == 5):
            if (_g1 == "Linux"):
                fd = python_lib_Sys.stdin.fileno()
                old = python_lib_Termios.tcgetattr(fd)
                fileNo = fd
                when = python_lib_Termios.TCSADRAIN
                settings = old
                def _hx_local_1():
                    python_lib_Termios.tcsetattr(fileNo,when,settings)
                restore = _hx_local_1
                try:
                    python_lib_Tty.setraw(fd)
                    x = python_lib_Sys.stdin.read(1)
                    restore()
                    ch = HxString.charCodeAt(x,0)
                except BaseException as _g1:
                    None
                    e = haxe_Exception.caught(_g1).unwrap()
                    restore()
                    raise haxe_Exception.thrown(e)
            else:
                x = _g
                raise haxe_Exception.thrown((("platform " + ("null" if x is None else x)) + " not supported"))
        elif (_hx_local_0 == 3):
            if (_g1 == "Mac"):
                fd = python_lib_Sys.stdin.fileno()
                old = python_lib_Termios.tcgetattr(fd)
                fileNo = fd
                when = python_lib_Termios.TCSADRAIN
                settings = old
                def _hx_local_2():
                    python_lib_Termios.tcsetattr(fileNo,when,settings)
                restore = _hx_local_2
                try:
                    python_lib_Tty.setraw(fd)
                    x = python_lib_Sys.stdin.read(1)
                    restore()
                    ch = HxString.charCodeAt(x,0)
                except BaseException as _g1:
                    None
                    e = haxe_Exception.caught(_g1).unwrap()
                    restore()
                    raise haxe_Exception.thrown(e)
            else:
                x = _g
                raise haxe_Exception.thrown((("platform " + ("null" if x is None else x)) + " not supported"))
        elif (_hx_local_0 == 7):
            if (_g1 == "Windows"):
                ch = HxString.charCodeAt(python_lib_Msvcrt.getwch(),0)
            else:
                x = _g
                raise haxe_Exception.thrown((("platform " + ("null" if x is None else x)) + " not supported"))
        else:
            x = _g
            raise haxe_Exception.thrown((("platform " + ("null" if x is None else x)) + " not supported"))
        if echo:
            python_Lib.printString(Std.string("".join(map(chr,[ch]))))
        return ch

    @staticmethod
    def stdin():
        return python_io_IoTools.createFileInputFromText(python_lib_Sys.stdin)

    @staticmethod
    def stdout():
        return python_io_IoTools.createFileOutputFromText(python_lib_Sys.stdout)

    @staticmethod
    def stderr():
        return python_io_IoTools.createFileOutputFromText(python_lib_Sys.stderr)
Sys._hx_class = Sys
_hx_classes["Sys"] = Sys

class ValueType(Enum):
    __slots__ = ()
    _hx_class_name = "ValueType"
    _hx_constructs = ["TNull", "TInt", "TFloat", "TBool", "TObject", "TFunction", "TClass", "TEnum", "TUnknown"]

    @staticmethod
    def TClass(c):
        return ValueType("TClass", 6, (c,))

    @staticmethod
    def TEnum(e):
        return ValueType("TEnum", 7, (e,))
ValueType.TNull = ValueType("TNull", 0, ())
ValueType.TInt = ValueType("TInt", 1, ())
ValueType.TFloat = ValueType("TFloat", 2, ())
ValueType.TBool = ValueType("TBool", 3, ())
ValueType.TObject = ValueType("TObject", 4, ())
ValueType.TFunction = ValueType("TFunction", 5, ())
ValueType.TUnknown = ValueType("TUnknown", 8, ())
ValueType._hx_class = ValueType
_hx_classes["ValueType"] = ValueType


class Type:
    _hx_class_name = "Type"
    __slots__ = ()
    _hx_statics = ["getClass", "getEnum", "getSuperClass", "getClassName", "getEnumName", "resolveClass", "resolveEnum", "createInstance", "createEmptyInstance", "createEnum", "createEnumIndex", "getInstanceFields", "getClassFields", "getEnumConstructs", "typeof", "asEnumImpl", "enumEq", "enumConstructor", "enumParameters", "enumIndex", "allEnums"]

    @staticmethod
    def getClass(o):
        if (o is None):
            return None
        o1 = o
        if ((o1 is not None) and ((HxOverrides.eq(o1,str) or python_lib_Inspect.isclass(o1)))):
            return None
        if isinstance(o,_hx_AnonObject):
            return None
        if hasattr(o,"_hx_class"):
            return o._hx_class
        if hasattr(o,"__class__"):
            return o.__class__
        else:
            return None

    @staticmethod
    def getEnum(o):
        if (o is None):
            return None
        return o.__class__

    @staticmethod
    def getSuperClass(c):
        return python_Boot.getSuperClass(c)

    @staticmethod
    def getClassName(c):
        if hasattr(c,"_hx_class_name"):
            return c._hx_class_name
        else:
            if (c == list):
                return "Array"
            if (c == Math):
                return "Math"
            if (c == str):
                return "String"
            try:
                return c.__name__
            except BaseException as _g:
                None
                return None

    @staticmethod
    def getEnumName(e):
        return e._hx_class_name

    @staticmethod
    def resolveClass(name):
        if (name == "Array"):
            return list
        if (name == "Math"):
            return Math
        if (name == "String"):
            return str
        cl = _hx_classes.get(name,None)
        tmp = None
        if (cl is not None):
            o = cl
            tmp = (not (((o is not None) and ((HxOverrides.eq(o,str) or python_lib_Inspect.isclass(o))))))
        else:
            tmp = True
        if tmp:
            return None
        return cl

    @staticmethod
    def resolveEnum(name):
        if (name == "Bool"):
            return Bool
        o = Type.resolveClass(name)
        if hasattr(o,"_hx_constructs"):
            return o
        else:
            return None

    @staticmethod
    def createInstance(cl,args):
        return cl(*args)

    @staticmethod
    def createEmptyInstance(cl):
        i = cl.__new__(cl)
        callInit = None
        def _hx_local_0(cl):
            sc = Type.getSuperClass(cl)
            if (sc is not None):
                callInit(sc)
            if hasattr(cl,"_hx_empty_init"):
                cl._hx_empty_init(i)
        callInit = _hx_local_0
        callInit(cl)
        return i

    @staticmethod
    def createEnum(e,constr,params = None):
        f = Reflect.field(e,constr)
        if (f is None):
            raise haxe_Exception.thrown(("No such constructor " + ("null" if constr is None else constr)))
        if Reflect.isFunction(f):
            if (params is None):
                raise haxe_Exception.thrown((("Constructor " + ("null" if constr is None else constr)) + " need parameters"))
            return Reflect.callMethod(e,f,params)
        if ((params is not None) and ((len(params) != 0))):
            raise haxe_Exception.thrown((("Constructor " + ("null" if constr is None else constr)) + " does not need parameters"))
        return f

    @staticmethod
    def createEnumIndex(e,index,params = None):
        c = python_internal_ArrayImpl._get(e._hx_constructs, index)
        if (c is None):
            raise haxe_Exception.thrown((Std.string(index) + " is not a valid enum constructor index"))
        return Type.createEnum(e,c,params)

    @staticmethod
    def getInstanceFields(c):
        return python_Boot.getInstanceFields(c)

    @staticmethod
    def getClassFields(c):
        return python_Boot.getClassFields(c)

    @staticmethod
    def getEnumConstructs(e):
        if hasattr(e,"_hx_constructs"):
            x = e._hx_constructs
            return list(x)
        else:
            return []

    @staticmethod
    def typeof(v):
        if (v is None):
            return ValueType.TNull
        elif isinstance(v,bool):
            return ValueType.TBool
        elif isinstance(v,int):
            return ValueType.TInt
        elif isinstance(v,float):
            return ValueType.TFloat
        elif isinstance(v,str):
            return ValueType.TClass(str)
        elif isinstance(v,list):
            return ValueType.TClass(list)
        elif (isinstance(v,_hx_AnonObject) or python_lib_Inspect.isclass(v)):
            return ValueType.TObject
        elif isinstance(v,Enum):
            return ValueType.TEnum(v.__class__)
        elif (isinstance(v,type) or hasattr(v,"_hx_class")):
            return ValueType.TClass(v.__class__)
        elif callable(v):
            return ValueType.TFunction
        else:
            return ValueType.TUnknown

    @staticmethod
    def asEnumImpl(x):
        return x

    @staticmethod
    def enumEq(a,b):
        if HxOverrides.eq(a,b):
            return True
        try:
            if ((b is None) and (not HxOverrides.eq(a,b))):
                return False
            if (a.tag != b.tag):
                return False
            p1 = a.params
            p2 = b.params
            if (len(p1) != len(p2)):
                return False
            _g = 0
            _g1 = len(p1)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                if (not Type.enumEq(p1[i],p2[i])):
                    return False
            if (a._hx_class != b._hx_class):
                return False
        except BaseException as _g:
            None
            return False
        return True

    @staticmethod
    def enumConstructor(e):
        return e.tag

    @staticmethod
    def enumParameters(e):
        return list(e.params)

    @staticmethod
    def enumIndex(e):
        return e.index

    @staticmethod
    def allEnums(e):
        ctors = Type.getEnumConstructs(e)
        ret = []
        _g = 0
        while (_g < len(ctors)):
            ctor = (ctors[_g] if _g >= 0 and _g < len(ctors) else None)
            _g = (_g + 1)
            v = Reflect.field(e,ctor)
            if Std.isOfType(v,e):
                ret.append(v)
        return ret
Type._hx_class = Type
_hx_classes["Type"] = Type


class connect_Base:
    _hx_class_name = "connect.Base"
    __slots__ = ()
    _hx_methods = ["__getattr__", "__setattr__", "__eq__"]

    def __getattr__(self,key):
        class_ = Type.getClass(self)
        fields = python_Boot.getInstanceFields(class_)
        camelized = connect_Inflection.toCamelCase(key)
        if (python_internal_ArrayImpl.indexOf(fields,camelized,None) > -1):
            return python_lib_Builtins.getattr(self,camelized)
        else:
            className = Type.getClassName(class_)
            raise haxe_Exception.thrown(AttributeError((((("'" + ("null" if className is None else className)) + "' object has no attribute '") + ("null" if key is None else key)) + "'")))

    def __setattr__(self,key,value):
        class_ = Type.getClass(self)
        fields = python_Boot.getInstanceFields(class_)
        camelized = connect_Inflection.toCamelCase(key)
        if ((python_internal_ArrayImpl.indexOf(fields,key,None) == -1) and ((python_internal_ArrayImpl.indexOf(fields,camelized,None) > -1))):
            key = camelized
        return super().__setattr__(key, value)

    def __eq__(self,other):
        thisType = type(self)
        otherType = type(other)
        if (thisType == otherType):
            return (Std.string(self) == Std.string(other))
        else:
            return False

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
connect_Base._hx_class = connect_Base
_hx_classes["connect.Base"] = connect_Base


class connect_Config(connect_Base):
    _hx_class_name = "connect.Config"
    __slots__ = ("apiUrl", "apiKey", "products", "data")
    _hx_fields = ["apiUrl", "apiKey", "products", "data"]
    _hx_methods = ["getApiUrl", "getApiKey", "hasProduct", "getProductsString", "getData"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_Base


    def __init__(self,apiUrl,apiKey,products,data):
        index = (len(apiUrl) - 1)
        self.apiUrl = (apiUrl if (((("" if (((index < 0) or ((index >= len(apiUrl))))) else apiUrl[index])) == "/")) else (("null" if apiUrl is None else apiUrl) + "/"))
        startIndex = None
        self.apiKey = (apiKey if ((((apiKey.find("ApiKey ") if ((startIndex is None)) else HxString.indexOfImpl(apiKey,"ApiKey ",startIndex))) == 0)) else ("ApiKey " + ("null" if apiKey is None else apiKey)))
        self.products = (products.copy() if ((products is not None)) else connect_util_Collection())
        self.data = (data if ((data is not None)) else connect_util_Dictionary())

    def getApiUrl(self):
        return self.apiUrl

    def getApiKey(self):
        return self.apiKey

    def hasProduct(self,productId):
        return (self.products.indexOf(productId) > -1)

    def getProductsString(self):
        return self.products.join(",")

    def getData(self,key):
        return self.data.get(key)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.apiUrl = None
        _hx_o.apiKey = None
        _hx_o.products = None
        _hx_o.data = None
connect_Config._hx_class = connect_Config
_hx_classes["connect.Config"] = connect_Config


class connect_util_Dictionary(connect_Base):
    _hx_class_name = "connect.util.Dictionary"
    __slots__ = ("map",)
    _hx_fields = ["map"]
    _hx_methods = ["clear", "copy", "exists", "get", "getBool", "getInt", "getFloat", "getString", "iterator", "keys", "isEmpty", "remove", "set", "setBool", "setInt", "setFloat", "setString", "toString", "toObject"]
    _hx_statics = ["fromObject", "toObject_r", "fromObject_r"]
    _hx_interfaces = []
    _hx_super = connect_Base


    def __init__(self):
        self.map = haxe_ds_StringMap()

    def clear(self):
        self.map.h.clear()

    def copy(self):
        cp = connect_util_Dictionary()
        key = self.keys()
        while key.hasNext():
            key1 = key.next()
            cp.set(key1,self.get(key1))
        return cp

    def exists(self,key):
        return (key in self.map.h)

    def get(self,key):
        return self.map.h.get(key,None)

    def getBool(self,key):
        if self.exists(key):
            return self.get(key)
        else:
            return False

    def getInt(self,key):
        if self.exists(key):
            return self.get(key)
        else:
            return 0

    def getFloat(self,key):
        if self.exists(key):
            return self.get(key)
        else:
            return 0.0

    def getString(self,key):
        if self.exists(key):
            return self.get(key)
        else:
            return ""

    def iterator(self):
        return self.map.iterator()

    def keys(self):
        return self.map.keys()

    def isEmpty(self):
        if (self.map.keys() is not None):
            return (not self.map.keys().hasNext())
        else:
            return True

    def remove(self,key):
        return self.map.remove(key)

    def set(self,key,value):
        self.map.h[key] = value
        return self

    def setBool(self,key,x):
        return self.set(key,x)

    def setInt(self,key,x):
        return self.set(key,x)

    def setFloat(self,key,x):
        return self.set(key,x)

    def setString(self,key,x):
        return self.set(key,x)

    def toString(self):
        return haxe_format_JsonPrinter.print(self.toObject(),None,None)

    def toObject(self):
        return connect_util_Dictionary.toObject_r(self)

    @staticmethod
    def fromObject(obj):
        if isinstance(obj, dict):
            obj = python_Lib.dictToAnon(obj)
        return connect_util_Dictionary.fromObject_r(obj)

    @staticmethod
    def toObject_r(x):
        _g = Type.typeof(x)
        if (_g.index == 6):
            _g1 = _g.params[0]
            if (_g1 == connect_util_Collection):
                col = x
                arr = list()
                elem = col.iterator()
                while elem.hasNext():
                    elem1 = elem.next()
                    x1 = connect_util_Dictionary.toObject_r(elem1)
                    arr.append(x1)
                return arr
            elif (_g1 == connect_util_Dictionary):
                _hx_dict = x
                obj = _hx_AnonObject({})
                keys = _hx_dict.keys()
                key = keys
                while key.hasNext():
                    key1 = key.next()
                    value = connect_util_Dictionary.toObject_r(_hx_dict.get(key1))
                    setattr(obj,(("_hx_" + key1) if ((key1 in python_Boot.keywords)) else (("_hx_" + key1) if (((((len(key1) > 2) and ((ord(key1[0]) == 95))) and ((ord(key1[1]) == 95))) and ((ord(key1[(len(key1) - 1)]) != 95)))) else key1)),value)
                return obj
            else:
                classObj = Type.getClass(x)
                instanceFields = (python_Boot.getInstanceFields(classObj) if ((classObj is not None)) else [])
                hasToObject = (python_internal_ArrayImpl.indexOf(instanceFields,"toObject",None) > -1)
                if hasToObject:
                    return Reflect.field(x,"toObject")()
                else:
                    return x
        else:
            classObj = Type.getClass(x)
            instanceFields = (python_Boot.getInstanceFields(classObj) if ((classObj is not None)) else [])
            hasToObject = (python_internal_ArrayImpl.indexOf(instanceFields,"toObject",None) > -1)
            if hasToObject:
                return Reflect.field(x,"toObject")()
            else:
                return x

    @staticmethod
    def fromObject_r(x):
        _g = Type.typeof(x)
        tmp = _g.index
        if (tmp == 4):
            _hx_dict = connect_util_Dictionary()
            fields = python_Boot.fields(x)
            _g1 = 0
            while (_g1 < len(fields)):
                field = (fields[_g1] if _g1 >= 0 and _g1 < len(fields) else None)
                _g1 = (_g1 + 1)
                _hx_dict.set(field,connect_util_Dictionary.fromObject_r(Reflect.field(x,field)))
            return _hx_dict
        elif (tmp == 6):
            if (_g.params[0] == list):
                arr = x
                col = connect_util_Collection()
                _g = 0
                while (_g < len(arr)):
                    elem = (arr[_g] if _g >= 0 and _g < len(arr) else None)
                    _g = (_g + 1)
                    col.push(connect_util_Dictionary.fromObject_r(elem))
                return col
            else:
                if isinstance(x, dict):
                    return connect_util_Dictionary.fromObject_r(python_Lib.dictToAnon(x))
                return x
        else:
            if isinstance(x, dict):
                return connect_util_Dictionary.fromObject_r(python_Lib.dictToAnon(x))
            return x

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.map = None
connect_util_Dictionary._hx_class = connect_util_Dictionary
_hx_classes["connect.util.Dictionary"] = connect_util_Dictionary


class haxe_IMap:
    _hx_class_name = "haxe.IMap"
    __slots__ = ()
    _hx_methods = ["get", "set", "exists", "remove", "keys", "iterator", "keyValueIterator", "copy", "toString", "clear"]
haxe_IMap._hx_class = haxe_IMap
_hx_classes["haxe.IMap"] = haxe_IMap


class haxe_ds_StringMap:
    _hx_class_name = "haxe.ds.StringMap"
    __slots__ = ("h",)
    _hx_fields = ["h"]
    _hx_methods = ["set", "get", "exists", "remove", "keys", "iterator", "keyValueIterator", "copy", "toString", "clear"]
    _hx_interfaces = [haxe_IMap]

    def __init__(self):
        self.h = dict()

    def set(self,key,value):
        self.h[key] = value

    def get(self,key):
        return self.h.get(key,None)

    def exists(self,key):
        return (key in self.h)

    def remove(self,key):
        has = (key in self.h)
        if has:
            del self.h[key]
        return has

    def keys(self):
        return python_HaxeIterator(iter(self.h.keys()))

    def iterator(self):
        return python_HaxeIterator(iter(self.h.values()))

    def keyValueIterator(self):
        return haxe_iterators_MapKeyValueIterator(self)

    def copy(self):
        copied = haxe_ds_StringMap()
        key = self.keys()
        while key.hasNext():
            key1 = key.next()
            value = self.h.get(key1,None)
            copied.h[key1] = value
        return copied

    def toString(self):
        s_b = python_lib_io_StringIO()
        s_b.write("{")
        it = self.keys()
        i = it
        while i.hasNext():
            i1 = i.next()
            s_b.write(Std.string(i1))
            s_b.write(" => ")
            s_b.write(Std.string(Std.string(self.h.get(i1,None))))
            if it.hasNext():
                s_b.write(", ")
        s_b.write("}")
        return s_b.getvalue()

    def clear(self):
        self.h.clear()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.h = None
haxe_ds_StringMap._hx_class = haxe_ds_StringMap
_hx_classes["haxe.ds.StringMap"] = haxe_ds_StringMap


class connect_Env(connect_Base):
    _hx_class_name = "connect.Env"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = []
    _hx_statics = ["config", "loggers", "defaultQuery", "apiClient", "fulfillmentApi", "usageApi", "tierApi", "generalApi", "marketplaceApi", "subscriptionsApi", "ROOT_LOGGER", "initConfig", "loadConfig", "isConfigInitialized", "initLogger", "getLoggerForRequest", "isLoggerInitialized", "initDefaultQuery", "isDefaultQueryInitialized", "getConfig", "getLogger", "getApiClient", "getFulfillmentApi", "getUsageApi", "getTierApi", "getGeneralApi", "getSubscriptionsApi", "getMarketplaceApi", "_reset", "_getDefaultQuery"]
    _hx_interfaces = []
    _hx_super = connect_Base

    config = None
    defaultQuery = None
    apiClient = None
    fulfillmentApi = None
    usageApi = None
    tierApi = None
    generalApi = None
    marketplaceApi = None
    subscriptionsApi = None

    @staticmethod
    def initConfig(apiUrl,apiKey,products):
        if (connect_Env.config is None):
            connect_Env.config = connect_Config(apiUrl,apiKey,products,None)
        else:
            raise haxe_Exception.thrown("Config instance is already initialized.")

    @staticmethod
    def loadConfig(filename):
        if (connect_Env.config is None):
            content = sys_io_File.getContent(filename)
            _hx_dict = connect_util_Dictionary.fromObject(python_lib_Json.loads(content,**python__KwArgs_KwArgs_Impl_.fromT(_hx_AnonObject({'object_hook': python_Lib.dictToAnon}))))
            apiUrl = _hx_dict.get("apiEndpoint")
            apiKey = _hx_dict.get("apiKey")
            configProducts = _hx_dict.get("products")
            products = (configProducts if (Std.isOfType(configProducts,connect_util_Collection)) else (connect_util_Collection._fromArray([configProducts]) if (Std.isOfType(configProducts,str)) else None))
            _hx_dict.remove("apiEndpoint")
            _hx_dict.remove("apiKey")
            _hx_dict.remove("products")
            connect_Env.config = connect_Config(apiUrl,apiKey,products,_hx_dict)
        else:
            raise haxe_Exception.thrown("Config instance is already initialized.")

    @staticmethod
    def isConfigInitialized():
        return (connect_Env.config is not None)

    @staticmethod
    def initLogger(config):
        if (not connect_Env.loggers.exists("root")):
            connect_Env.loggers.set("root",connect_logger_Logger(config))
        else:
            raise haxe_Exception.thrown("Logger instance is already initialized.")

    @staticmethod
    def getLoggerForRequest(request):
        if (not connect_Env.loggers.exists("root")):
            connect_Env.loggers.set("root",connect_logger_Logger(None))
        if ((request is not None) and ((Reflect.field(request,"id") is not None))):
            if (not connect_Env.loggers.exists(request.id)):
                def _hx_local_1():
                    _hx_local_0 = connect_Env.loggers.get("root")
                    if (Std.isOfType(_hx_local_0,connect_logger_Logger) or ((_hx_local_0 is None))):
                        _hx_local_0
                    else:
                        raise "Class cast error"
                    return _hx_local_0
                connect_Env.loggers.set(request.id,(_hx_local_1()).copy(request))
            return connect_Env.loggers.get(request.id)
        else:
            return connect_Env.loggers.get("root")

    @staticmethod
    def isLoggerInitialized():
        return connect_Env.loggers.exists("root")

    @staticmethod
    def initDefaultQuery(query):
        if (connect_Env.defaultQuery is None):
            connect_Env.defaultQuery = query.copy()
        else:
            raise haxe_Exception.thrown("Default Query instance in already initialized.")

    @staticmethod
    def isDefaultQueryInitialized():
        return (connect_Env.defaultQuery is not None)

    @staticmethod
    def getConfig():
        if (not connect_Env.isConfigInitialized()):
            connect_Env.loadConfig("config.json")
        return connect_Env.config

    @staticmethod
    def getLogger():
        if (not connect_Env.isLoggerInitialized()):
            connect_Env.initLogger(None)
        return connect_Env.loggers.get("root")

    @staticmethod
    def getApiClient():
        if (connect_Env.apiClient is None):
            connect_Env.apiClient = connect_api_impl_ApiClientImpl()
        return connect_Env.apiClient

    @staticmethod
    def getFulfillmentApi():
        if (connect_Env.fulfillmentApi is None):
            connect_Env.fulfillmentApi = connect_api_FulfillmentApi()
        return connect_Env.fulfillmentApi

    @staticmethod
    def getUsageApi():
        if (connect_Env.usageApi is None):
            connect_Env.usageApi = connect_api_UsageApi()
        return connect_Env.usageApi

    @staticmethod
    def getTierApi():
        if (connect_Env.tierApi is None):
            connect_Env.tierApi = connect_api_TierApi()
        return connect_Env.tierApi

    @staticmethod
    def getGeneralApi():
        if (connect_Env.generalApi is None):
            connect_Env.generalApi = connect_api_GeneralApi()
        return connect_Env.generalApi

    @staticmethod
    def getSubscriptionsApi():
        if (connect_Env.subscriptionsApi is None):
            connect_Env.subscriptionsApi = connect_api_SubscriptionsApi()
        return connect_Env.subscriptionsApi

    @staticmethod
    def getMarketplaceApi():
        if (connect_Env.marketplaceApi is None):
            connect_Env.marketplaceApi = connect_api_MarketplaceApi()
        return connect_Env.marketplaceApi

    @staticmethod
    def _reset(client = None):
        connect_Env.config = None
        connect_Env.loggers = connect_util_Dictionary()
        connect_Env.defaultQuery = None
        connect_Env.apiClient = client
        connect_Env.fulfillmentApi = None
        connect_Env.usageApi = None
        connect_Env.tierApi = None
        connect_Env.generalApi = None
        connect_Env.marketplaceApi = None
        connect_Env.subscriptionsApi = None

    @staticmethod
    def _getDefaultQuery():
        return connect_Env.defaultQuery
connect_Env._hx_class = connect_Env
_hx_classes["connect.Env"] = connect_Env


class connect_flow_FlowExecutorDelegate:
    _hx_class_name = "connect.flow.FlowExecutorDelegate"
    __slots__ = ()
    _hx_methods = ["onStepBegin", "onStepEnd", "onStepFail", "onStepSkip", "onStepAbort"]
connect_flow_FlowExecutorDelegate._hx_class = connect_flow_FlowExecutorDelegate
_hx_classes["connect.flow.FlowExecutorDelegate"] = connect_flow_FlowExecutorDelegate


class connect_Flow(connect_Base):
    _hx_class_name = "connect.Flow"
    __slots__ = ("filterFunc", "skipRequestOnPendingMigration", "executor", "logger", "request", "data", "lastRequestState")
    _hx_fields = ["filterFunc", "skipRequestOnPendingMigration", "executor", "logger", "request", "data", "lastRequestState"]
    _hx_methods = ["getClassName", "setStoreRequestOnFailure", "storesRequestOnFailure", "setStoreNumAttempts", "storesNumAttempts", "setSkipRequestOnPendingMigration", "skipsRequestOnPendingMigration", "setup", "step", "getAssetRequest", "getListing", "getTierConfigRequest", "getUsageFile", "setData", "setVolatileData", "getData", "getDataKeys", "approveByTemplate", "approveByTile", "fail", "inquire", "pend", "skip", "abort", "_run", "filterRequests", "callRequestFilter", "runRequest", "prepareRequest", "processSetup", "getCurrentAttempt", "onStepBegin", "onStepEnd", "onStepFail", "onStepSkip", "onStepAbort"]
    _hx_statics = ["SKIP_MSG"]
    _hx_interfaces = [connect_flow_FlowExecutorDelegate]
    _hx_super = connect_Base


    def __init__(self,filterFunc):
        self.lastRequestState = None
        self.data = None
        self.request = None
        self.logger = None
        self.executor = None
        self.filterFunc = filterFunc
        self.skipRequestOnPendingMigration = True
        self.executor = connect_flow_FlowExecutor(self,self)
        self.logger = connect_flow_FlowLogger(self.getClassName())
        self.request = None
        self.data = connect_util_Dictionary()
        self.lastRequestState = None

    def getClassName(self):
        return type(self).__name__

    def setStoreRequestOnFailure(self,enable):
        pass

    def storesRequestOnFailure(self):
        return False

    def setStoreNumAttempts(self,enable):
        pass

    def storesNumAttempts(self):
        return False

    def setSkipRequestOnPendingMigration(self,enable):
        self.skipRequestOnPendingMigration = enable

    def skipsRequestOnPendingMigration(self):
        return self.skipRequestOnPendingMigration

    def setup(self):
        pass

    def step(self,description,func):
        self.executor.addStep(description,func)
        return self

    def getAssetRequest(self):
        return connect_flow_RequestCaster.castAssetRequest(self.request)

    def getListing(self):
        return connect_flow_RequestCaster.castListing(self.request)

    def getTierConfigRequest(self):
        return connect_flow_RequestCaster.castTierConfigRequest(self.request)

    def getUsageFile(self):
        return connect_flow_RequestCaster.castUsageFile(self.request)

    def setData(self,key,value):
        self.data.set(key,value)
        return self

    def setVolatileData(self,key,value):
        return self.setData(key,value)

    def getData(self,key):
        return self.data.get(key)

    def getDataKeys(self):
        _g = []
        key = self.data.keys()
        while key.hasNext():
            key1 = key.next()
            _g.append(key1)
        return connect_util_Collection._fromArray(_g)

    def approveByTemplate(self,id):
        request = self.getAssetRequest()
        tcr = self.getTierConfigRequest()
        if (request is not None):
            request.update(None)
            request.approveByTemplate(id)
            self.abort("")
        elif (tcr is not None):
            tcr.update(None)
            tcr.approveByTemplate(id)
            self.abort("")

    def approveByTile(self,text):
        request = self.getAssetRequest()
        if (request is not None):
            request.update(None)
            request.approveByTile(text)
            self.abort("")

    def fail(self,reason):
        request = self.getAssetRequest()
        tcr = self.getTierConfigRequest()
        if (request is not None):
            request.update(None)
            request.fail(reason)
            self.abort("Failing request")
        elif (tcr is not None):
            tcr.update(None)
            tcr.fail(reason)
            self.abort("Failing request")

    def inquire(self,templateId,params):
        request = self.getAssetRequest()
        tcr = self.getTierConfigRequest()
        if (request is not None):
            request.update(params)
            request.inquire(templateId)
            self.abort("Inquiring request")
        elif (tcr is not None):
            tcr.update(params)
            tcr.inquire()
            self.abort("Inquiring request")

    def pend(self):
        request = self.getAssetRequest()
        tcr = self.getTierConfigRequest()
        if (request is not None):
            request.update(None)
            request.pend()
            self.abort("Pending request")
        elif (tcr is not None):
            tcr.update(None)
            tcr.pend()
            self.abort("Pending request")

    def skip(self):
        self.executor.abort()

    def abort(self,message):
        self.executor.abort((message if ((message is not None)) else ""))

    def _run(self,_hx_list):
        _gthis = self
        self.logger.openFlowSection()
        filteredList = self.filterRequests(_hx_list)
        def _hx_local_2(model):
            def _hx_local_1():
                _hx_local_0 = model
                if (Std.isOfType(_hx_local_0,connect_models_IdModel) or ((_hx_local_0 is None))):
                    _hx_local_0
                else:
                    raise "Class cast error"
                return _hx_local_0
            _gthis.runRequest(_hx_local_1())
        Lambda.iter(filteredList,_hx_local_2)
        self.logger.closeFlowSection()

    def filterRequests(self,_hx_list):
        if (self.filterFunc is not None):
            return connect_util_Collection._fromArray(list(filter(self.callRequestFilter,_hx_list.toArray())))
        else:
            return _hx_list

    def callRequestFilter(self,m):
        def _hx_local_2():
            def _hx_local_1():
                _hx_local_0 = m
                if (Std.isOfType(_hx_local_0,connect_models_IdModel) or ((_hx_local_0 is None))):
                    _hx_local_0
                else:
                    raise "Class cast error"
                return _hx_local_0
            return self.filterFunc(_hx_local_1())
        return _hx_local_2()

    def runRequest(self,request):
        connect_api_ConnectHelper.setLogger(connect_Env.getLoggerForRequest(request))
        self.logger.openRequestSection(request)
        if (self.prepareRequest(request) and self.processSetup()):
            self.executor.executeRequest(request,0)
        else:
            self.logger.writeMigrationMessage(request)
        self.logger.closeRequestSection()
        connect_api_ConnectHelper.setLogger(connect_Env.getLogger())

    def prepareRequest(self,request):
        self.request = request
        self.data = connect_util_Dictionary()
        self.lastRequestState = connect_flow_ProcessedRequestInfo(None,None)
        assetRequest = self.getAssetRequest()
        if (not ((((assetRequest is None) or (not assetRequest.needsMigration())) or (not self.skipsRequestOnPendingMigration())))):
            return (assetRequest.type != "purchase")
        else:
            return True

    def processSetup(self):
        self.logger.openSetupSection()
        ok = True
        try:
            self.executor.reset()
            self.setup()
        except BaseException as _g:
            None
            ex = haxe_Exception.caught(_g).unwrap()
            self.logger.writeException(connect_flow_FlowExecutor.getStackTrace(ex))
            if (self.getAssetRequest() is not None):
                self.getAssetRequest()._updateConversation((HxOverrides.stringOrNull(connect_Flow.SKIP_MSG) + HxOverrides.stringOrNull(connect_flow_FlowExecutor.getExceptionMessage(ex))))
            ok = False
        self.logger.closeSetupSection()
        return ok

    def getCurrentAttempt(self):
        return 0

    def onStepBegin(self,request,step,index):
        self.logger.openStepSection(index,step.getDescription())
        self.logger.writeStepInfo(connect_flow_ProcessedRequestInfo(self.request,self.data),self.lastRequestState)

    def onStepEnd(self,request,step,index):
        self.logger.closeStepSection(index)

    def onStepFail(self,request,step,index,msg):
        self.logger.writeStepError(connect_flow_ProcessedRequestInfo(self.request,self.data),self.lastRequestState)
        self.logger.writeException(msg)
        if (self.getAssetRequest() is not None):
            self.getAssetRequest()._updateConversation((HxOverrides.stringOrNull(connect_Flow.SKIP_MSG) + ("null" if msg is None else msg)))
        self.logger.closeStepSection(index)

    def onStepSkip(self,request,step,index):
        self.logger.writeStepSkip()
        self.logger.closeStepSection(index)

    def onStepAbort(self,request,step,index,msg):
        if (msg != ""):
            self.logger.writeException(msg)
        self.logger.closeStepSection(index)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.filterFunc = None
        _hx_o.skipRequestOnPendingMigration = None
        _hx_o.executor = None
        _hx_o.logger = None
        _hx_o.request = None
        _hx_o.data = None
        _hx_o.lastRequestState = None
connect_Flow._hx_class = connect_Flow
_hx_classes["connect.Flow"] = connect_Flow


class connect_Inflection:
    _hx_class_name = "connect.Inflection"
    __slots__ = ()
    _hx_statics = ["toCamelCase", "toSingular", "toSnakeCase"]

    @staticmethod
    def toCamelCase(text,capitalizeFirst = None):
        if (capitalizeFirst is None):
            capitalizeFirst = False
        buffer_b = python_lib_io_StringIO()
        lastWasUnderscore = capitalizeFirst
        _g = 0
        _g1 = len(text)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            char = (("" if (((i < 0) or ((i >= len(text))))) else text[i]).upper() if lastWasUnderscore else ("" if (((i < 0) or ((i >= len(text))))) else text[i]))
            if (char != "_"):
                buffer_b.write(Std.string(char))
                lastWasUnderscore = False
            else:
                lastWasUnderscore = True
        return buffer_b.getvalue()

    @staticmethod
    def toSingular(text):
        index = (len(text) - 1)
        if ((("" if (((index < 0) or ((index >= len(text))))) else text[index])) == "s"):
            return HxString.substr(text,0,(len(text) - 1))
        else:
            return text

    @staticmethod
    def toSnakeCase(text):
        r1 = EReg("(.)([A-Z][a-z]+)","g")
        r2 = EReg("([a-z0-9])([A-Z])","g")
        s1 = r1.replace(text,"$1_$2")
        return r2.replace(s1,"$1_$2").lower()
connect_Inflection._hx_class = connect_Inflection
_hx_classes["connect.Inflection"] = connect_Inflection


class connect_Processor(connect_Base):
    _hx_class_name = "connect.Processor"
    __slots__ = ("flows",)
    _hx_fields = ["flows"]
    _hx_methods = ["flow", "processAssetRequests", "processListings", "processTierConfigRequests", "processUsageFiles", "run"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_Base


    def __init__(self):
        self.flows = []

    def flow(self,flow):
        _this = self.flows
        _this.append(flow)
        return self

    def processAssetRequests(self,filters):
        self.run(connect_models_AssetRequest,filters)

    def processListings(self,filters):
        self.run(connect_models_Listing,filters)

    def processTierConfigRequests(self,filters):
        self.run(connect_models_TierConfigRequest,filters)

    def processUsageFiles(self,filters):
        self.run(connect_models_UsageFile,filters)

    def run(self,modelClass,filters):
        _g = Type.typeof(modelClass)
        if (_g.index == 6):
            if (_g.params[0] == str):
                def _hx_local_1():
                    _hx_local_0 = modelClass
                    if (Std.isOfType(_hx_local_0,str) or ((_hx_local_0 is None))):
                        _hx_local_0
                    else:
                        raise "Class cast error"
                    return _hx_local_0
                modelClass = Type.resolveClass(_hx_local_1())
        prevLogName = connect_Env.getLogger().getFilename()
        connect_Env.getLogger().setFilename(None)
        connect_Env.getLogger().openSection(("Running Processor on " + Std.string(connect_util_DateTime.now())))
        try:
            connect_Env.getLogger().openSection(("Listing requests on " + Std.string(connect_util_DateTime.now())))
            listMethod = Reflect.field(modelClass,"list")
            _hx_list = Reflect.callMethod(modelClass,listMethod,[filters])
            connect_Env.getLogger().closeSection()
            _g = 0
            _g1 = self.flows
            while (_g < len(_g1)):
                flow = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                _g = (_g + 1)
                flow._run(_hx_list)
        except BaseException as _g:
            None
            ex = haxe_Exception.caught(_g).unwrap()
            connect_Env.getLogger().writeCodeBlock(connect_logger_Logger.LEVEL_ERROR,Std.string(ex),"")
            connect_Env.getLogger().closeSection()
        connect_Env.getLogger().closeSection()
        connect_Env.getLogger().setFilename(prevLogName)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.flows = None
connect_Processor._hx_class = connect_Processor
_hx_classes["connect.Processor"] = connect_Processor


class connect_api_ConnectHelper:
    _hx_class_name = "connect.api.ConnectHelper"
    __slots__ = ()
    _hx_statics = ["logger", "setLogger", "getLogger", "get", "put", "post", "postFile", "delete", "connectSyncRequest", "parsePath", "getHeaders", "checkResponse"]
    logger = None

    @staticmethod
    def setLogger(logger):
        connect_api_ConnectHelper.logger = logger

    @staticmethod
    def getLogger():
        if (connect_api_ConnectHelper.logger is None):
            connect_api_ConnectHelper.logger = connect_Env.getLogger()
        return connect_api_ConnectHelper.logger

    @staticmethod
    def get(resource,id = None,suffix = None,params = None,rqlParams = None,logLevel = None):
        if (rqlParams is None):
            rqlParams = False
        return connect_api_ConnectHelper.checkResponse(connect_api_ConnectHelper.connectSyncRequest("GET",connect_api_ConnectHelper.parsePath(resource,id,suffix),connect_api_ConnectHelper.getHeaders(),params,rqlParams,None,None,None,None,logLevel))

    @staticmethod
    def put(resource,id,suffix,body,logLevel = None):
        return connect_api_ConnectHelper.checkResponse(connect_api_ConnectHelper.connectSyncRequest("PUT",connect_api_ConnectHelper.parsePath(resource,id,suffix),connect_api_ConnectHelper.getHeaders(),None,False,body,None,None,None,logLevel))

    @staticmethod
    def post(resource,id = None,suffix = None,body = None,logLevel = None):
        return connect_api_ConnectHelper.checkResponse(connect_api_ConnectHelper.connectSyncRequest("POST",connect_api_ConnectHelper.parsePath(resource,id,suffix),connect_api_ConnectHelper.getHeaders(),None,False,body,None,None,None,logLevel))

    @staticmethod
    def postFile(resource,id = None,suffix = None,fileArg = None,fileName = None,fileContents = None,logLevel = None):
        return connect_api_ConnectHelper.checkResponse(connect_api_ConnectHelper.connectSyncRequest("POST",connect_api_ConnectHelper.parsePath(resource,id,suffix),connect_api_ConnectHelper.getHeaders(False),None,False,None,fileArg,fileName,fileContents,logLevel))

    @staticmethod
    def delete(resource,id,suffix = None,logLevel = None):
        return connect_api_ConnectHelper.checkResponse(connect_api_ConnectHelper.connectSyncRequest("DELETE",connect_api_ConnectHelper.parsePath(resource,id,suffix),connect_api_ConnectHelper.getHeaders(),None,False,None,None,None,None,logLevel))

    @staticmethod
    def connectSyncRequest(method,path,headers,params,rqlParams,data,fileArg,fileName,fileContent,logLevel):
        paramsStr = ((params.toString() if rqlParams else params.toPlain()) if ((params is not None)) else "")
        url = ((HxOverrides.stringOrNull(connect_Env.getConfig().getApiUrl()) + ("null" if path is None else path)) + ("null" if paramsStr is None else paramsStr))
        return connect_Env.getApiClient().syncRequestWithLogger(method,url,headers,data,fileArg,fileName,fileContent,None,connect_api_ConnectHelper.getLogger(),logLevel)

    @staticmethod
    def parsePath(resource,id = None,suffix = None):
        return ((("null" if resource is None else resource) + HxOverrides.stringOrNull(((("/" + ("null" if id is None else id)) if (((id is not None) and ((id != "")))) else "")))) + HxOverrides.stringOrNull(((("/" + ("null" if suffix is None else suffix)) if (((suffix is not None) and ((suffix != "")))) else ""))))

    @staticmethod
    def getHeaders(addContentType = None):
        if (addContentType is None):
            addContentType = True
        headers = connect_util_Dictionary()
        headers.set("Authorization",connect_Env.getConfig().getApiKey())
        if addContentType:
            headers.set("Content-Type","application/json")
        else:
            headers.set("Accept","application/json")
        return headers

    @staticmethod
    def checkResponse(response):
        if (response.status < 400):
            return response.text
        else:
            raise haxe_Exception.thrown(response.text)
connect_api_ConnectHelper._hx_class = connect_api_ConnectHelper
_hx_classes["connect.api.ConnectHelper"] = connect_api_ConnectHelper


class connect_api_FulfillmentApi(connect_Base):
    _hx_class_name = "connect.api.FulfillmentApi"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["listRequests", "getRequest", "createRequest", "updateRequest", "changeRequestStatus", "assignRequest", "renderTemplate", "listAssets", "getAsset", "getAssetRequests"]
    _hx_statics = ["REQUESTS_PATH", "TEMPLATES_PATH", "ASSETS_PATH"]
    _hx_interfaces = []
    _hx_super = connect_Base


    def __init__(self):
        pass

    def listRequests(self,filters):
        return connect_api_ConnectHelper.get(connect_api_FulfillmentApi.REQUESTS_PATH,None,None,filters,False,connect_logger_Logger.LEVEL_DEBUG)

    def getRequest(self,id):
        return connect_api_ConnectHelper.get(connect_api_FulfillmentApi.REQUESTS_PATH,id)

    def createRequest(self,body):
        return connect_api_ConnectHelper.post(connect_api_FulfillmentApi.REQUESTS_PATH,None,None,body)

    def updateRequest(self,id,request):
        return connect_api_ConnectHelper.put(connect_api_FulfillmentApi.REQUESTS_PATH,id,None,request)

    def changeRequestStatus(self,id,status,data):
        return connect_api_ConnectHelper.post(connect_api_FulfillmentApi.REQUESTS_PATH,id,status,data)

    def assignRequest(self,id,assignee):
        return connect_api_ConnectHelper.post(connect_api_FulfillmentApi.REQUESTS_PATH,id,("assign/" + ("null" if assignee is None else assignee)))

    def renderTemplate(self,id,requestId):
        return connect_api_ConnectHelper.get(connect_api_FulfillmentApi.TEMPLATES_PATH,id,"render",connect_api_Query().equal("request_id",requestId))

    def listAssets(self,filters):
        return connect_api_ConnectHelper.get(connect_api_FulfillmentApi.ASSETS_PATH,None,None,filters,True)

    def getAsset(self,id):
        return connect_api_ConnectHelper.get(connect_api_FulfillmentApi.ASSETS_PATH,id)

    def getAssetRequests(self,id):
        return connect_api_ConnectHelper.get(connect_api_FulfillmentApi.ASSETS_PATH,id,"requests")

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
connect_api_FulfillmentApi._hx_class = connect_api_FulfillmentApi
_hx_classes["connect.api.FulfillmentApi"] = connect_api_FulfillmentApi


class connect_api_GeneralApi(connect_Base):
    _hx_class_name = "connect.api.GeneralApi"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["listAccounts", "createAccount", "getAccount", "listAccountUsers", "getAccountUser", "listConversations", "createConversation", "getConversation", "createConversationMessage", "listProducts", "getProduct", "listProductActions", "getProductAction", "getProductActionLink", "getProductConnections", "listProductItems", "listProductParameters", "getProductParameter", "createProductParameter", "updateProductParameter", "deleteProductParameter", "getProductTemplates", "getProductVersions", "getProductVersion", "getProductVersionActions", "getProductVersionAction", "getProductVersionActionLink", "getProductVersionItems", "getProductVersionParameters", "getProductVersionTemplates", "listProductConfigurations", "setProductConfigurationParam", "listProductAgreements", "listProductMedia", "createProductMedia", "getProductMedia", "updateProductMedia", "deleteProductMedia", "listCategories", "getCategory"]
    _hx_statics = ["ACCOUNTS_PATH", "CONVERSATIONS_PATH", "PRODUCTS_PATH", "CATEGORIES_PATH"]
    _hx_interfaces = []
    _hx_super = connect_Base


    def __init__(self):
        pass

    def listAccounts(self,filters):
        return connect_api_ConnectHelper.get(connect_api_GeneralApi.ACCOUNTS_PATH,None,None,filters,False,connect_logger_Logger.LEVEL_DEBUG)

    def createAccount(self):
        return connect_api_ConnectHelper.post(connect_api_GeneralApi.ACCOUNTS_PATH)

    def getAccount(self,id):
        return connect_api_ConnectHelper.get(connect_api_GeneralApi.ACCOUNTS_PATH,id)

    def listAccountUsers(self,id):
        return connect_api_ConnectHelper.get(connect_api_GeneralApi.ACCOUNTS_PATH,id,"users",None,False,connect_logger_Logger.LEVEL_DEBUG)

    def getAccountUser(self,id,userId):
        return connect_api_ConnectHelper.get(connect_api_GeneralApi.ACCOUNTS_PATH,id,("users/" + ("null" if userId is None else userId)))

    def listConversations(self,filters):
        return connect_api_ConnectHelper.get(connect_api_GeneralApi.CONVERSATIONS_PATH,None,None,filters,False,connect_logger_Logger.LEVEL_DEBUG)

    def createConversation(self,data):
        return connect_api_ConnectHelper.post(connect_api_GeneralApi.CONVERSATIONS_PATH,None,None,data,connect_logger_Logger.LEVEL_DEBUG)

    def getConversation(self,id):
        return connect_api_ConnectHelper.get(connect_api_GeneralApi.CONVERSATIONS_PATH,id,None,None,False,connect_logger_Logger.LEVEL_DEBUG)

    def createConversationMessage(self,id,data):
        return connect_api_ConnectHelper.post(connect_api_GeneralApi.CONVERSATIONS_PATH,id,"messages",data,connect_logger_Logger.LEVEL_DEBUG)

    def listProducts(self,filters):
        return connect_api_ConnectHelper.get(connect_api_GeneralApi.PRODUCTS_PATH,None,None,filters,True,connect_logger_Logger.LEVEL_DEBUG)

    def getProduct(self,id):
        return connect_api_ConnectHelper.get(connect_api_GeneralApi.PRODUCTS_PATH,id)

    def listProductActions(self,id,filters):
        return connect_api_ConnectHelper.get(connect_api_GeneralApi.PRODUCTS_PATH,id,"actions",filters,False,connect_logger_Logger.LEVEL_DEBUG)

    def getProductAction(self,id,actionId):
        return connect_api_ConnectHelper.get(connect_api_GeneralApi.PRODUCTS_PATH,id,("actions/" + ("null" if actionId is None else actionId)))

    def getProductActionLink(self,id,actionId):
        response = python_lib_Json.loads(connect_api_ConnectHelper.get(connect_api_GeneralApi.PRODUCTS_PATH,id,(("actions/" + ("null" if actionId is None else actionId)) + "/actionLink")),**python__KwArgs_KwArgs_Impl_.fromT(_hx_AnonObject({'object_hook': python_Lib.dictToAnon})))
        return response.link

    def getProductConnections(self,id):
        return connect_api_ConnectHelper.get(connect_api_GeneralApi.PRODUCTS_PATH,id,"connections")

    def listProductItems(self,id,filters):
        return connect_api_ConnectHelper.get(connect_api_GeneralApi.PRODUCTS_PATH,id,"items",filters,False,connect_logger_Logger.LEVEL_DEBUG)

    def listProductParameters(self,id,filters):
        return connect_api_ConnectHelper.get(connect_api_GeneralApi.PRODUCTS_PATH,id,"parameters",filters,False,connect_logger_Logger.LEVEL_DEBUG)

    def getProductParameter(self,id,paramId):
        return connect_api_ConnectHelper.get(connect_api_GeneralApi.PRODUCTS_PATH,id,("parameters/" + ("null" if paramId is None else paramId)))

    def createProductParameter(self,id,data):
        return connect_api_ConnectHelper.post(connect_api_GeneralApi.PRODUCTS_PATH,id,"parameters",data)

    def updateProductParameter(self,id,paramId,data):
        return connect_api_ConnectHelper.put(connect_api_GeneralApi.PRODUCTS_PATH,id,("parameters/" + ("null" if paramId is None else paramId)),data)

    def deleteProductParameter(self,id,paramId):
        connect_api_ConnectHelper.delete(connect_api_GeneralApi.PRODUCTS_PATH,id,("parameters/" + ("null" if paramId is None else paramId)))

    def getProductTemplates(self,id):
        return connect_api_ConnectHelper.get(connect_api_GeneralApi.PRODUCTS_PATH,id,"templates")

    def getProductVersions(self,id):
        return connect_api_ConnectHelper.get(connect_api_GeneralApi.PRODUCTS_PATH,id,"versions")

    def getProductVersion(self,id,version):
        return connect_api_ConnectHelper.get(connect_api_GeneralApi.PRODUCTS_PATH,id,("versions/" + Std.string(version)))

    def getProductVersionActions(self,id,version):
        return connect_api_ConnectHelper.get(connect_api_GeneralApi.PRODUCTS_PATH,id,(("versions/" + Std.string(version)) + "/actions"))

    def getProductVersionAction(self,id,version,actionId):
        return connect_api_ConnectHelper.get(connect_api_GeneralApi.PRODUCTS_PATH,id,((("versions/" + Std.string(version)) + "/actions/") + ("null" if actionId is None else actionId)))

    def getProductVersionActionLink(self,id,version,actionId):
        response = python_lib_Json.loads(connect_api_ConnectHelper.get(connect_api_GeneralApi.PRODUCTS_PATH,id,(((("versions/" + Std.string(version)) + "/actions/") + ("null" if actionId is None else actionId)) + "/actionLink")),**python__KwArgs_KwArgs_Impl_.fromT(_hx_AnonObject({'object_hook': python_Lib.dictToAnon})))
        return response.link

    def getProductVersionItems(self,id,version):
        return connect_api_ConnectHelper.get(connect_api_GeneralApi.PRODUCTS_PATH,id,(("versions/" + Std.string(version)) + "/items"))

    def getProductVersionParameters(self,id,version):
        return connect_api_ConnectHelper.get(connect_api_GeneralApi.PRODUCTS_PATH,id,(("versions/" + Std.string(version)) + "/parameters"))

    def getProductVersionTemplates(self,id,version):
        return connect_api_ConnectHelper.get(connect_api_GeneralApi.PRODUCTS_PATH,id,(("versions/" + Std.string(version)) + "/templates"))

    def listProductConfigurations(self,id,filters):
        return connect_api_ConnectHelper.get(connect_api_GeneralApi.PRODUCTS_PATH,id,"configurations",filters)

    def setProductConfigurationParam(self,id,param):
        return connect_api_ConnectHelper.post(connect_api_GeneralApi.PRODUCTS_PATH,id,"configurations",param)

    def listProductAgreements(self,id,filters):
        return connect_api_ConnectHelper.get(connect_api_GeneralApi.PRODUCTS_PATH,id,"agreements",filters,False,connect_logger_Logger.LEVEL_DEBUG)

    def listProductMedia(self,id,filters):
        return connect_api_ConnectHelper.get(connect_api_GeneralApi.PRODUCTS_PATH,id,"media",filters,False,connect_logger_Logger.LEVEL_DEBUG)

    def createProductMedia(self,id):
        return connect_api_ConnectHelper.post(connect_api_GeneralApi.PRODUCTS_PATH,id,"media")

    def getProductMedia(self,id,mediaId):
        return connect_api_ConnectHelper.get(connect_api_GeneralApi.PRODUCTS_PATH,id,("media/" + ("null" if mediaId is None else mediaId)))

    def updateProductMedia(self,id,mediaId,media):
        return connect_api_ConnectHelper.put(connect_api_GeneralApi.PRODUCTS_PATH,((("" + ("null" if id is None else id)) + "/media/") + ("null" if mediaId is None else mediaId)),None,media)

    def deleteProductMedia(self,id,mediaId):
        return connect_api_ConnectHelper.delete(connect_api_GeneralApi.PRODUCTS_PATH,id,("media/" + ("null" if mediaId is None else mediaId)))

    def listCategories(self,filters):
        return connect_api_ConnectHelper.get(connect_api_GeneralApi.CATEGORIES_PATH,None,None,filters,False,connect_logger_Logger.LEVEL_DEBUG)

    def getCategory(self,id):
        return connect_api_ConnectHelper.get(connect_api_GeneralApi.CATEGORIES_PATH,id)

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
connect_api_GeneralApi._hx_class = connect_api_GeneralApi
_hx_classes["connect.api.GeneralApi"] = connect_api_GeneralApi


class connect_api_IApiClient:
    _hx_class_name = "connect.api.IApiClient"
    __slots__ = ()
    _hx_methods = ["syncRequest", "syncRequestWithLogger"]
connect_api_IApiClient._hx_class = connect_api_IApiClient
_hx_classes["connect.api.IApiClient"] = connect_api_IApiClient


class connect_api_MarketplaceApi:
    _hx_class_name = "connect.api.MarketplaceApi"
    __slots__ = ()
    _hx_methods = ["listAgreements", "createAgreement", "getAgreement", "updateAgreement", "removeAgreement", "listAgreementVersions", "newAgreementVersion", "getAgreementVersion", "removeAgreementVersion", "listAgreementSubAgreements", "createAgreementSubAgreement", "listListings", "getListing", "putListing", "listListingRequests", "getListingRequest", "createListingRequest", "assignListingRequest", "unassignListingRequest", "changeListingRequestToDraft", "changeListingRequestToDeploying", "changeListingRequestToCompleted", "changeListingRequestToCanceled", "changeListingRequestToReviewing", "listMarketplaces", "createMarketplace", "getMarketplace", "updateMarketplace", "setMarketplaceIcon", "deleteMarketplace"]
    _hx_statics = ["AGREEMENTS_PATH", "LISTINGS_PATH", "LISTINGREQUESTS_PATH", "MARKETPLACES_PATH"]

    def __init__(self):
        pass

    def listAgreements(self,filters):
        return connect_api_ConnectHelper.get(connect_api_MarketplaceApi.AGREEMENTS_PATH,None,None,filters,False,connect_logger_Logger.LEVEL_DEBUG)

    def createAgreement(self,body):
        return connect_api_ConnectHelper.post(connect_api_MarketplaceApi.AGREEMENTS_PATH,None,None,body)

    def getAgreement(self,id):
        return connect_api_ConnectHelper.get(connect_api_MarketplaceApi.AGREEMENTS_PATH,id)

    def updateAgreement(self,id,body):
        return connect_api_ConnectHelper.put(connect_api_MarketplaceApi.AGREEMENTS_PATH,id,None,body)

    def removeAgreement(self,id):
        connect_api_ConnectHelper.delete(connect_api_MarketplaceApi.AGREEMENTS_PATH,id)

    def listAgreementVersions(self,id):
        return connect_api_ConnectHelper.get(connect_api_MarketplaceApi.AGREEMENTS_PATH,id,"versions",None,False,connect_logger_Logger.LEVEL_DEBUG)

    def newAgreementVersion(self,id,body):
        return connect_api_ConnectHelper.post(connect_api_MarketplaceApi.AGREEMENTS_PATH,id,"versions",body)

    def getAgreementVersion(self,id,version):
        return connect_api_ConnectHelper.get(connect_api_MarketplaceApi.AGREEMENTS_PATH,id,("version/" + ("null" if version is None else version)))

    def removeAgreementVersion(self,id,version):
        connect_api_ConnectHelper.delete(connect_api_MarketplaceApi.AGREEMENTS_PATH,id,("version/" + ("null" if version is None else version)))

    def listAgreementSubAgreements(self,id):
        return connect_api_ConnectHelper.get(connect_api_MarketplaceApi.AGREEMENTS_PATH,id,connect_api_MarketplaceApi.AGREEMENTS_PATH,None,False,connect_logger_Logger.LEVEL_DEBUG)

    def createAgreementSubAgreement(self,id,body):
        return connect_api_ConnectHelper.post(connect_api_MarketplaceApi.AGREEMENTS_PATH,id,connect_api_MarketplaceApi.AGREEMENTS_PATH,body)

    def listListings(self,filters):
        return connect_api_ConnectHelper.get(connect_api_MarketplaceApi.LISTINGS_PATH,None,None,filters,False,connect_logger_Logger.LEVEL_DEBUG)

    def getListing(self,id):
        return connect_api_ConnectHelper.get(connect_api_MarketplaceApi.LISTINGS_PATH,id)

    def putListing(self,id,body):
        return connect_api_ConnectHelper.put(connect_api_MarketplaceApi.LISTINGS_PATH,id,None,body)

    def listListingRequests(self,filters):
        return connect_api_ConnectHelper.get(connect_api_MarketplaceApi.LISTINGREQUESTS_PATH,None,None,filters,False,connect_logger_Logger.LEVEL_DEBUG)

    def getListingRequest(self,id):
        return connect_api_ConnectHelper.get(connect_api_MarketplaceApi.LISTINGREQUESTS_PATH,id)

    def createListingRequest(self,body):
        return connect_api_ConnectHelper.post(connect_api_MarketplaceApi.LISTINGREQUESTS_PATH,None,None,body)

    def assignListingRequest(self,id):
        connect_api_ConnectHelper.post(connect_api_MarketplaceApi.LISTINGREQUESTS_PATH,id,"assign")

    def unassignListingRequest(self,id):
        connect_api_ConnectHelper.post(connect_api_MarketplaceApi.LISTINGREQUESTS_PATH,id,"unassign")

    def changeListingRequestToDraft(self,id):
        connect_api_ConnectHelper.post(connect_api_MarketplaceApi.LISTINGREQUESTS_PATH,id,"refine")

    def changeListingRequestToDeploying(self,id):
        connect_api_ConnectHelper.post(connect_api_MarketplaceApi.LISTINGREQUESTS_PATH,id,"deploy")

    def changeListingRequestToCompleted(self,id):
        connect_api_ConnectHelper.post(connect_api_MarketplaceApi.LISTINGREQUESTS_PATH,id,"complete")

    def changeListingRequestToCanceled(self,id):
        connect_api_ConnectHelper.post(connect_api_MarketplaceApi.LISTINGREQUESTS_PATH,id,"cancel")

    def changeListingRequestToReviewing(self,id):
        connect_api_ConnectHelper.post(connect_api_MarketplaceApi.LISTINGREQUESTS_PATH,id,"submit")

    def listMarketplaces(self,filters):
        return connect_api_ConnectHelper.get(connect_api_MarketplaceApi.MARKETPLACES_PATH,None,None,filters,False,connect_logger_Logger.LEVEL_DEBUG)

    def createMarketplace(self,body):
        return connect_api_ConnectHelper.post(connect_api_MarketplaceApi.MARKETPLACES_PATH,None,None,body)

    def getMarketplace(self,id):
        return connect_api_ConnectHelper.get(connect_api_MarketplaceApi.MARKETPLACES_PATH,id)

    def updateMarketplace(self,id,body):
        return connect_api_ConnectHelper.put(connect_api_MarketplaceApi.MARKETPLACES_PATH,id,None,body)

    def setMarketplaceIcon(self,id,data):
        connect_api_ConnectHelper.postFile(connect_api_MarketplaceApi.MARKETPLACES_PATH,id,"icon","name","marketplace.png",data)

    def deleteMarketplace(self,id):
        connect_api_ConnectHelper.delete(connect_api_MarketplaceApi.MARKETPLACES_PATH,id)

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
connect_api_MarketplaceApi._hx_class = connect_api_MarketplaceApi
_hx_classes["connect.api.MarketplaceApi"] = connect_api_MarketplaceApi


class connect_api_Query(connect_Base):
    _hx_class_name = "connect.api.Query"
    __slots__ = ("in__", "out_", "limit_", "orderBy_", "offset_", "ordering_", "like_", "ilike_", "select_", "relOps", "forceRql_")
    _hx_fields = ["in__", "out_", "limit_", "orderBy_", "offset_", "ordering_", "like_", "ilike_", "select_", "relOps", "forceRql_"]
    _hx_methods = ["copy", "default_", "in_", "out", "limit", "orderBy", "offset", "ordering", "like", "ilike", "select", "equal", "notEqual", "greater", "greaterOrEqual", "lesser", "lesserOrEqual", "toString", "toPlain", "toObject", "toJson", "forceRql", "addRelOp"]
    _hx_statics = ["fromObject", "fromJson", "stringMapToObject", "valueToObject", "arrayToObject", "sortStringArray"]
    _hx_interfaces = []
    _hx_super = connect_Base


    def __init__(self):
        self.select_ = None
        self.ordering_ = None
        self.offset_ = None
        self.orderBy_ = None
        self.limit_ = None
        self.in__ = haxe_ds_StringMap()
        self.out_ = haxe_ds_StringMap()
        self.like_ = haxe_ds_StringMap()
        self.ilike_ = haxe_ds_StringMap()
        self.relOps = haxe_ds_StringMap()
        self.forceRql_ = False

    def copy(self):
        copy = connect_api_Query()
        _g = haxe_ds_StringMap()
        k = self.in__.keys()
        while k.hasNext():
            k1 = k.next()
            value = list(self.in__.h.get(k1,None))
            _g.h[k1] = value
        copy.in__ = _g
        _g = haxe_ds_StringMap()
        k = self.out_.keys()
        while k.hasNext():
            k1 = k.next()
            value = list(self.out_.h.get(k1,None))
            _g.h[k1] = value
        copy.out_ = _g
        copy.limit_ = self.limit_
        copy.orderBy_ = self.orderBy_
        copy.offset_ = self.offset_
        copy.ordering_ = (list(self.ordering_) if ((self.ordering_ is not None)) else None)
        copy.like_ = self.like_.copy()
        copy.ilike_ = self.ilike_.copy()
        copy.select_ = (list(self.select_) if ((self.select_ is not None)) else None)
        _g = haxe_ds_StringMap()
        k = self.relOps.keys()
        while k.hasNext():
            k1 = k.next()
            _g1 = []
            _g2 = 0
            _g3 = self.relOps.h.get(k1,None)
            while (_g2 < len(_g3)):
                kv = (_g3[_g2] if _g2 >= 0 and _g2 < len(_g3) else None)
                _g2 = (_g2 + 1)
                x = connect_api__Query_KeyValue(kv.key,kv.value)
                _g1.append(x)
            _g.h[k1] = _g1
        copy.relOps = _g
        return copy

    def default_(self):
        _gthis = self
        _hx_def = connect_Env._getDefaultQuery()
        _g = []
        k = _hx_def.in__.keys()
        while k.hasNext():
            k1 = k.next()
            _g.append(k1)
        def _hx_local_0(k):
            if (not (k in _gthis.in__.h)):
                _this = _gthis.in__
                value = list(_hx_def.in__.h.get(k,None))
                _this.h[k] = value
        Lambda.iter(_g,_hx_local_0)
        _g = []
        k = _hx_def.out_.keys()
        while k.hasNext():
            k1 = k.next()
            _g.append(k1)
        def _hx_local_1(k):
            if (not (k in _gthis.out_.h)):
                _this = _gthis.out_
                value = list(_hx_def.out_.h.get(k,None))
                _this.h[k] = value
        Lambda.iter(_g,_hx_local_1)
        if (self.limit_ is None):
            self.limit_ = _hx_def.limit_
        if (self.orderBy_ is None):
            self.orderBy_ = _hx_def.orderBy_
        if (self.offset_ is None):
            self.offset_ = _hx_def.offset_
        if (_hx_def.ordering_ is not None):
            if (self.ordering_ is None):
                self.ordering_ = []
            def _hx_local_2(e):
                if (python_internal_ArrayImpl.indexOf(_gthis.ordering_,e,None) == -1):
                    _this = _gthis.ordering_
                    _this.append(e)
            Lambda.iter(_hx_def.ordering_,_hx_local_2)
        _g = []
        k = _hx_def.like_.keys()
        while k.hasNext():
            k1 = k.next()
            _g.append(k1)
        def _hx_local_3(k):
            if (not (k in _gthis.like_.h)):
                _this = _gthis.like_
                value = _hx_def.like_.h.get(k,None)
                _this.h[k] = value
        Lambda.iter(_g,_hx_local_3)
        _g = []
        k = _hx_def.ilike_.keys()
        while k.hasNext():
            k1 = k.next()
            _g.append(k1)
        def _hx_local_4(k):
            if (not (k in _gthis.ilike_.h)):
                _this = _gthis.ilike_
                value = _hx_def.ilike_.h.get(k,None)
                _this.h[k] = value
        Lambda.iter(_g,_hx_local_4)
        if (_hx_def.select_ is not None):
            if (self.select_ is None):
                self.select_ = []
            def _hx_local_5(e):
                if (python_internal_ArrayImpl.indexOf(_gthis.select_,e,None) == -1):
                    _this = _gthis.select_
                    _this.append(e)
            Lambda.iter(_hx_def.select_,_hx_local_5)
        _g = []
        k = _hx_def.relOps.keys()
        while k.hasNext():
            k1 = k.next()
            _g.append(k1)
        def _hx_local_10(k):
            if (k in _gthis.relOps.h):
                thisK = _gthis.relOps.h.get(k,None)
                _g = 0
                _g1 = _hx_def.relOps.h.get(k,None)
                while (_g < len(_g1)):
                    kv = [(_g1[_g] if _g >= 0 and _g < len(_g1) else None)]
                    _g = (_g + 1)
                    def _hx_local_8(kv):
                        def _hx_local_7(thisKV):
                            return thisKV.equals((kv[0] if 0 < len(kv) else None))
                        return _hx_local_7
                    if (Lambda.find(thisK,_hx_local_8(kv)) is None):
                        x = connect_api__Query_KeyValue((kv[0] if 0 < len(kv) else None).key,(kv[0] if 0 < len(kv) else None).value)
                        thisK.append(x)
            else:
                _this = _gthis.relOps
                _g = []
                _g1 = 0
                _g2 = _hx_def.relOps.h.get(k,None)
                while (_g1 < len(_g2)):
                    kv1 = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
                    _g1 = (_g1 + 1)
                    x = connect_api__Query_KeyValue(kv1.key,kv1.value)
                    _g.append(x)
                _this.h[k] = _g
        Lambda.iter(_g,_hx_local_10)
        return self

    def in_(self,property,array):
        _this = self.in__
        value = list(array.toArray())
        _this.h[property] = value
        return self

    def out(self,property,array):
        _this = self.out_
        value = list(array.toArray())
        _this.h[property] = value
        return self

    def limit(self,amount):
        self.limit_ = amount
        return self

    def orderBy(self,property):
        self.orderBy_ = property
        return self

    def offset(self,page):
        self.offset_ = page
        return self

    def ordering(self,propertyList):
        self.ordering_ = list(propertyList.toArray())
        return self

    def like(self,property,pattern):
        self.like_.h[property] = pattern
        return self

    def ilike(self,property,pattern):
        self.ilike_.h[property] = pattern
        return self

    def select(self,attributes):
        self.select_ = list(attributes.toArray())
        return self

    def equal(self,property,value):
        return self.addRelOp("eq",property,value)

    def notEqual(self,property,value):
        return self.addRelOp("ne",property,value)

    def greater(self,property,value):
        return self.addRelOp("gt",property,value)

    def greaterOrEqual(self,property,value):
        return self.addRelOp("ge",property,value)

    def lesser(self,property,value):
        return self.addRelOp("lt",property,value)

    def lesserOrEqual(self,property,value):
        return self.addRelOp("le",property,value)

    def toString(self):
        rql = list()
        if (self.select_ is not None):
            _this = self.select_
            x = (("select(" + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in _this]))) + ")")
            rql.append(x)
        _g = []
        k = self.like_.keys()
        while k.hasNext():
            k1 = k.next()
            _g.append(k1)
        likeKeys = connect_api_Query.sortStringArray(_g)
        _g = 0
        while (_g < len(likeKeys)):
            key = (likeKeys[_g] if _g >= 0 and _g < len(likeKeys) else None)
            _g = (_g + 1)
            x = (((("like(" + ("null" if key is None else key)) + ",") + HxOverrides.stringOrNull(self.like_.h.get(key,None))) + ")")
            rql.append(x)
        _g = []
        k = self.ilike_.keys()
        while k.hasNext():
            k1 = k.next()
            _g.append(k1)
        ilikeKeys = connect_api_Query.sortStringArray(_g)
        _g = 0
        while (_g < len(ilikeKeys)):
            key = (ilikeKeys[_g] if _g >= 0 and _g < len(ilikeKeys) else None)
            _g = (_g + 1)
            x = (((("ilike(" + ("null" if key is None else key)) + ",") + HxOverrides.stringOrNull(self.ilike_.h.get(key,None))) + ")")
            rql.append(x)
        _g = []
        k = self.in__.keys()
        while k.hasNext():
            k1 = k.next()
            _g.append(k1)
        inKeys = connect_api_Query.sortStringArray(_g)
        _g = 0
        while (_g < len(inKeys)):
            key = (inKeys[_g] if _g >= 0 and _g < len(inKeys) else None)
            _g = (_g + 1)
            _this = self.in__.h.get(key,None)
            x = (((("in(" + ("null" if key is None else key)) + ",(") + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in _this]))) + "))")
            rql.append(x)
        _g = []
        k = self.out_.keys()
        while k.hasNext():
            k1 = k.next()
            _g.append(k1)
        outKeys = connect_api_Query.sortStringArray(_g)
        _g = 0
        while (_g < len(outKeys)):
            key = (outKeys[_g] if _g >= 0 and _g < len(outKeys) else None)
            _g = (_g + 1)
            _this = self.out_.h.get(key,None)
            x = (((("out(" + ("null" if key is None else key)) + ",(") + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in _this]))) + "))")
            rql.append(x)
        _g = []
        k = self.relOps.keys()
        while k.hasNext():
            k1 = k.next()
            _g.append(k1)
        relOpsKeys = connect_api_Query.sortStringArray(_g)
        _g = 0
        while (_g < len(relOpsKeys)):
            relOp = (relOpsKeys[_g] if _g >= 0 and _g < len(relOpsKeys) else None)
            _g = (_g + 1)
            arguments = self.relOps.h.get(relOp,None)
            _g1 = 0
            while (_g1 < len(arguments)):
                argument = (arguments[_g1] if _g1 >= 0 and _g1 < len(arguments) else None)
                _g1 = (_g1 + 1)
                x = (((((("" + ("null" if relOp is None else relOp)) + "(") + HxOverrides.stringOrNull(argument.key)) + ",") + HxOverrides.stringOrNull(argument.value)) + ")")
                rql.append(x)
        if (self.ordering_ is not None):
            _this = self.ordering_
            x = (("ordering(" + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in _this]))) + ")")
            rql.append(x)
        if (self.limit_ is not None):
            x = ("limit=" + Std.string(self.limit_))
            rql.append(x)
        if (self.orderBy_ is not None):
            x = ("order_by=" + HxOverrides.stringOrNull(self.orderBy_))
            rql.append(x)
        if (self.offset_ is not None):
            x = ("offset=" + Std.string(self.offset_))
            rql.append(x)
        if (len(rql) > 0):
            return ("?" + HxOverrides.stringOrNull("&".join([python_Boot.toString1(x1,'') for x1 in rql])))
        else:
            return ""

    def toPlain(self):
        if (not self.forceRql_):
            rql = list()
            if ("eq" in self.relOps.h):
                arguments = self.relOps.h.get("eq",None)
                _g = 0
                while (_g < len(arguments)):
                    argument = (arguments[_g] if _g >= 0 and _g < len(arguments) else None)
                    _g = (_g + 1)
                    x = ((("" + HxOverrides.stringOrNull(argument.key)) + "=") + HxOverrides.stringOrNull(argument.value))
                    rql.append(x)
            if (self.limit_ is not None):
                x = ("limit=" + Std.string(self.limit_))
                rql.append(x)
            if (self.orderBy_ is not None):
                x = ("order_by=" + HxOverrides.stringOrNull(self.orderBy_))
                rql.append(x)
            if (self.offset_ is not None):
                x = ("offset=" + Std.string(self.offset_))
                rql.append(x)
            if (self.ordering_ is not None):
                _this = self.ordering_
                x = (("ordering(" + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in _this]))) + ")")
                rql.append(x)
            if (len(rql) > 0):
                return ("?" + HxOverrides.stringOrNull("&".join([python_Boot.toString1(x1,'') for x1 in rql])))
            else:
                return ""
        else:
            return self.toString()

    def toObject(self):
        obj = _hx_AnonObject({'_hx_in': connect_api_Query.stringMapToObject(self.in__), 'out': connect_api_Query.stringMapToObject(self.out_), 'limit': self.limit_, 'orderBy': self.orderBy_, 'offset': self.offset_, 'ordering': self.ordering_, 'like': connect_api_Query.stringMapToObject(self.like_), 'ilike': connect_api_Query.stringMapToObject(self.ilike_), 'select': self.select_, 'relOps': connect_api_Query.stringMapToObject(self.relOps)})
        def _hx_local_0(field):
            value = Reflect.field(obj,field)
            keys = Type.typeof(value).index
            if (keys == 0):
                return False
            elif (keys == 4):
                return (len(python_Boot.fields(value)) > 0)
            else:
                return True
        keys = list(filter(_hx_local_0,python_Boot.fields(obj)))
        out = _hx_AnonObject({})
        _g = 0
        _g1 = len(keys)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            field = (keys[i] if i >= 0 and i < len(keys) else None)
            value = Reflect.field(obj,(keys[i] if i >= 0 and i < len(keys) else None))
            setattr(out,(("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field)),value)
        return out

    def toJson(self):
        return haxe_format_JsonPrinter.print(self.toObject(),None,None)

    def forceRql(self,force):
        self.forceRql_ = force
        return self

    def addRelOp(self,op,property,value):
        if (not (op in self.relOps.h)):
            _this = self.relOps
            value1 = list()
            _this.h[op] = value1
        _this = self.relOps.h.get(op,None)
        x = connect_api__Query_KeyValue(property,value)
        _this.append(x)
        return self

    @staticmethod
    def fromObject(obj):
        select = Reflect.field(obj,"select")
        like = Reflect.field(obj,"like")
        ilike = Reflect.field(obj,"ilike")
        in_ = Reflect.field(obj,"in")
        out = Reflect.field(obj,"out")
        relOps = Reflect.field(obj,"relOps")
        ordering = Reflect.field(obj,"ordering")
        limit = Reflect.field(obj,"limit")
        orderBy = Reflect.field(obj,"orderBy")
        offset = Reflect.field(obj,"offset")
        rql = connect_api_Query()
        if (select is not None):
            rql.select_ = select
        if (like is not None):
            fields = python_Boot.fields(like)
            def _hx_local_0(field):
                _this = rql.like_
                value = Reflect.field(like,field)
                _this.h[field] = value
            Lambda.iter(fields,_hx_local_0)
        if (ilike is not None):
            fields = python_Boot.fields(ilike)
            def _hx_local_1(field):
                _this = rql.ilike_
                value = Reflect.field(ilike,field)
                _this.h[field] = value
            Lambda.iter(fields,_hx_local_1)
        if (in_ is not None):
            fields = python_Boot.fields(in_)
            def _hx_local_2(field):
                _this = rql.in__
                value = Reflect.field(in_,field)
                _this.h[field] = value
            Lambda.iter(fields,_hx_local_2)
        if (out is not None):
            fields = python_Boot.fields(out)
            def _hx_local_3(field):
                _this = rql.out_
                value = Reflect.field(out,field)
                _this.h[field] = value
            Lambda.iter(fields,_hx_local_3)
        if (relOps is not None):
            fields = python_Boot.fields(relOps)
            def _hx_local_5(field):
                array = Reflect.field(relOps,field)
                _this = rql.relOps
                def _hx_local_4(kv):
                    return connect_api__Query_KeyValue(kv.key,kv.value)
                value = list(map(_hx_local_4,array))
                _this.h[field] = value
            Lambda.iter(fields,_hx_local_5)
        if (ordering is not None):
            rql.ordering_ = ordering
        if (limit is not None):
            rql.limit_ = limit
        if (orderBy is not None):
            rql.orderBy_ = orderBy
        if (offset is not None):
            rql.offset_ = offset
        return rql

    @staticmethod
    def fromJson(json):
        return connect_api_Query.fromObject(python_lib_Json.loads(json,**python__KwArgs_KwArgs_Impl_.fromT(_hx_AnonObject({'object_hook': python_Lib.dictToAnon}))))

    @staticmethod
    def stringMapToObject(_hx_map):
        obj = _hx_AnonObject({})
        _g = []
        k = _hx_map.keys()
        while k.hasNext():
            k1 = k.next()
            _g.append(k1)
        fields = _g
        def _hx_local_0(f):
            value = connect_api_Query.valueToObject(_hx_map.h.get(f,None))
            setattr(obj,(("_hx_" + f) if ((f in python_Boot.keywords)) else (("_hx_" + f) if (((((len(f) > 2) and ((ord(f[0]) == 95))) and ((ord(f[1]) == 95))) and ((ord(f[(len(f) - 1)]) != 95)))) else f)),value)
        Lambda.iter(fields,_hx_local_0)
        return obj

    @staticmethod
    def valueToObject(value):
        _g = Type.typeof(value)
        if (_g.index == 6):
            _g1 = _g.params[0]
            if (_g1 == list):
                return connect_api_Query.arrayToObject(value)
            elif (_g1 == connect_api__Query_KeyValue):
                return Reflect.field(value,"toObject")()
            else:
                return value
        else:
            return value

    @staticmethod
    def arrayToObject(arr):
        _g = []
        _g_current = 0
        _g_array = arr
        while (_g_current < len(_g_array)):
            x = _g_current
            _g_current = (_g_current + 1)
            x1 = (_g_array[x] if x >= 0 and x < len(_g_array) else None)
            x2 = connect_api_Query.valueToObject(x1)
            _g.append(x2)
        return _g

    @staticmethod
    def sortStringArray(arr):
        def _hx_local_0(a,b):
            return Reflect.compare(a,b)
        haxe_ds_ArraySort.sort(arr,_hx_local_0)
        return arr

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.in__ = None
        _hx_o.out_ = None
        _hx_o.limit_ = None
        _hx_o.orderBy_ = None
        _hx_o.offset_ = None
        _hx_o.ordering_ = None
        _hx_o.like_ = None
        _hx_o.ilike_ = None
        _hx_o.select_ = None
        _hx_o.relOps = None
        _hx_o.forceRql_ = None
connect_api_Query._hx_class = connect_api_Query
_hx_classes["connect.api.Query"] = connect_api_Query


class connect_api__Query_KeyValue:
    _hx_class_name = "connect.api._Query.KeyValue"
    __slots__ = ("key", "value")
    _hx_fields = ["key", "value"]
    _hx_methods = ["equals", "toObject"]

    def __init__(self,key,value):
        self.key = key
        self.value = value

    def equals(self,other):
        if (self.key == other.key):
            return (self.value == other.value)
        else:
            return False

    def toObject(self):
        return _hx_AnonObject({'key': self.key, 'value': self.value})

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.key = None
        _hx_o.value = None
connect_api__Query_KeyValue._hx_class = connect_api__Query_KeyValue
_hx_classes["connect.api._Query.KeyValue"] = connect_api__Query_KeyValue


class connect_api_Response(connect_Base):
    _hx_class_name = "connect.api.Response"
    __slots__ = ("status", "text", "data")
    _hx_fields = ["status", "text", "data"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_Base


    def __init__(self,status,text,data):
        self.status = status
        self.text = text
        self.data = data

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.status = None
        _hx_o.text = None
        _hx_o.data = None
connect_api_Response._hx_class = connect_api_Response
_hx_classes["connect.api.Response"] = connect_api_Response


class connect_api_SubscriptionsApi(connect_Base):
    _hx_class_name = "connect.api.SubscriptionsApi"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["listRecurringAssets", "getRecurringAsset", "listBillingRequests", "getBillingRequest", "createBillingRequest", "updateBillingRequestAttributes"]
    _hx_statics = ["ASSETS_PATH", "REQUESTS_PATH"]
    _hx_interfaces = []
    _hx_super = connect_Base


    def __init__(self):
        pass

    def listRecurringAssets(self,filters):
        return connect_api_ConnectHelper.get(connect_api_SubscriptionsApi.ASSETS_PATH,None,None,filters,True,connect_logger_Logger.LEVEL_DEBUG)

    def getRecurringAsset(self,id):
        return connect_api_ConnectHelper.get(connect_api_SubscriptionsApi.ASSETS_PATH,id)

    def listBillingRequests(self,filters):
        return connect_api_ConnectHelper.get(connect_api_SubscriptionsApi.REQUESTS_PATH,None,None,filters,True,connect_logger_Logger.LEVEL_DEBUG)

    def getBillingRequest(self,id):
        return connect_api_ConnectHelper.get(connect_api_SubscriptionsApi.REQUESTS_PATH,id)

    def createBillingRequest(self,data,currentRequest):
        return connect_api_ConnectHelper.post(connect_api_SubscriptionsApi.REQUESTS_PATH,None,None,data)

    def updateBillingRequestAttributes(self,id,data):
        return connect_api_ConnectHelper.put(connect_api_SubscriptionsApi.REQUESTS_PATH,id,"attributes",data)

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
connect_api_SubscriptionsApi._hx_class = connect_api_SubscriptionsApi
_hx_classes["connect.api.SubscriptionsApi"] = connect_api_SubscriptionsApi


class connect_api_TierApi(connect_Base):
    _hx_class_name = "connect.api.TierApi"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["listTierConfigRequests", "createTierConfigRequest", "getTierConfigRequest", "updateTierConfigRequest", "pendTierConfigRequest", "inquireTierConfigRequest", "approveTierConfigRequest", "failTierConfigRequest", "assignTierConfigRequest", "unassignTierConfigRequest", "listTierAccounts", "getTierAccount", "listTierConfigs", "getTierConfig"]
    _hx_statics = ["TCR_PATH", "TA_PATH", "TC_PATH"]
    _hx_interfaces = []
    _hx_super = connect_Base


    def __init__(self):
        pass

    def listTierConfigRequests(self,filters):
        return connect_api_ConnectHelper.get(connect_api_TierApi.TCR_PATH,None,None,filters,True,connect_logger_Logger.LEVEL_DEBUG)

    def createTierConfigRequest(self,body):
        return connect_api_ConnectHelper.post(connect_api_TierApi.TCR_PATH,None,None,body)

    def getTierConfigRequest(self,id):
        return connect_api_ConnectHelper.get(connect_api_TierApi.TCR_PATH,id)

    def updateTierConfigRequest(self,id,tcr):
        return connect_api_ConnectHelper.put(connect_api_TierApi.TCR_PATH,id,None,tcr)

    def pendTierConfigRequest(self,id):
        connect_api_ConnectHelper.post(connect_api_TierApi.TCR_PATH,id,"pend")

    def inquireTierConfigRequest(self,id):
        connect_api_ConnectHelper.post(connect_api_TierApi.TCR_PATH,id,"inquire")

    def approveTierConfigRequest(self,id,data):
        return connect_api_ConnectHelper.post(connect_api_TierApi.TCR_PATH,id,"approve",data)

    def failTierConfigRequest(self,id,data):
        connect_api_ConnectHelper.post(connect_api_TierApi.TCR_PATH,id,"fail",data)

    def assignTierConfigRequest(self,id):
        connect_api_ConnectHelper.post(connect_api_TierApi.TCR_PATH,id,"assign")

    def unassignTierConfigRequest(self,id):
        connect_api_ConnectHelper.post(connect_api_TierApi.TCR_PATH,id,"unassign")

    def listTierAccounts(self,filters):
        return connect_api_ConnectHelper.get(connect_api_TierApi.TA_PATH,None,None,filters)

    def getTierAccount(self,id):
        return connect_api_ConnectHelper.get(connect_api_TierApi.TA_PATH,id)

    def listTierConfigs(self,filters):
        return connect_api_ConnectHelper.get(connect_api_TierApi.TC_PATH,None,None,filters,True)

    def getTierConfig(self,id):
        return connect_api_ConnectHelper.get(connect_api_TierApi.TC_PATH,id)

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
connect_api_TierApi._hx_class = connect_api_TierApi
_hx_classes["connect.api.TierApi"] = connect_api_TierApi


class connect_api_UsageApi(connect_Base):
    _hx_class_name = "connect.api.UsageApi"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["listUsageFiles", "createUsageFile", "getUsageFile", "updateUsageFile", "deleteUsageFile", "uploadUsageFile", "submitUsageFileAction", "acceptUsageFileAction", "rejectUsageFileAction", "closeUsageFileAction", "getProductSpecificUsageFileTemplate", "uploadReconciliationFileFromProvider", "reprocessProcessedFile", "listUsageRecords", "getUsageRecord", "updateUsageRecord", "closeUsageRecord"]
    _hx_statics = ["USAGE_FILES_PATH", "USAGE_PRODUCTS_PATH", "USAGE_RECORDS_PATH"]
    _hx_interfaces = []
    _hx_super = connect_Base


    def __init__(self):
        pass

    def listUsageFiles(self,filters):
        return connect_api_ConnectHelper.get(connect_api_UsageApi.USAGE_FILES_PATH,None,None,filters,True,connect_logger_Logger.LEVEL_DEBUG)

    def createUsageFile(self,body):
        return connect_api_ConnectHelper.post(connect_api_UsageApi.USAGE_FILES_PATH,None,None,body)

    def getUsageFile(self,id):
        return connect_api_ConnectHelper.get(connect_api_UsageApi.USAGE_FILES_PATH,id)

    def updateUsageFile(self,id,body):
        return connect_api_ConnectHelper.put(connect_api_UsageApi.USAGE_FILES_PATH,id,None,body)

    def deleteUsageFile(self,id):
        connect_api_ConnectHelper.post(connect_api_UsageApi.USAGE_FILES_PATH,id,"delete")

    def uploadUsageFile(self,id,file):
        return connect_api_ConnectHelper.postFile(connect_api_UsageApi.USAGE_FILES_PATH,id,"upload","usage_file","usage_file.xlsx",file)

    def submitUsageFileAction(self,id):
        return connect_api_ConnectHelper.post(connect_api_UsageApi.USAGE_FILES_PATH,id,"submit")

    def acceptUsageFileAction(self,id,note):
        return connect_api_ConnectHelper.post(connect_api_UsageApi.USAGE_FILES_PATH,id,"accept",haxe_format_JsonPrinter.print(_hx_AnonObject({'acceptance_note': note}),None,None))

    def rejectUsageFileAction(self,id,note):
        return connect_api_ConnectHelper.post(connect_api_UsageApi.USAGE_FILES_PATH,id,"reject",haxe_format_JsonPrinter.print(_hx_AnonObject({'rejection_note': note}),None,None))

    def closeUsageFileAction(self,id):
        return connect_api_ConnectHelper.post(connect_api_UsageApi.USAGE_FILES_PATH,id,"close")

    def getProductSpecificUsageFileTemplate(self,productId):
        return connect_api_ConnectHelper.get(connect_api_UsageApi.USAGE_PRODUCTS_PATH,productId,"template")

    def uploadReconciliationFileFromProvider(self,id,file):
        return connect_api_ConnectHelper.postFile(connect_api_UsageApi.USAGE_FILES_PATH,id,"reconciliation","reconciliation_file","reconciliation_file.xlsx",file)

    def reprocessProcessedFile(self,id):
        return connect_api_ConnectHelper.post(connect_api_UsageApi.USAGE_FILES_PATH,id,"reprocess")

    def listUsageRecords(self,filters):
        return connect_api_ConnectHelper.get(connect_api_UsageApi.USAGE_RECORDS_PATH,None,None,filters)

    def getUsageRecord(self,id):
        return connect_api_ConnectHelper.get(connect_api_UsageApi.USAGE_RECORDS_PATH,id)

    def updateUsageRecord(self,id,record):
        return connect_api_ConnectHelper.put(connect_api_UsageApi.USAGE_RECORDS_PATH,id,None,record)

    def closeUsageRecord(self,id,record):
        return connect_api_ConnectHelper.post(connect_api_UsageApi.USAGE_RECORDS_PATH,id,"close",record)

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
connect_api_UsageApi._hx_class = connect_api_UsageApi
_hx_classes["connect.api.UsageApi"] = connect_api_UsageApi


class connect_api_impl_ApiClientImpl(connect_Base):
    _hx_class_name = "connect.api.impl.ApiClientImpl"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["syncRequest", "syncRequestWithLogger"]
    _hx_statics = ["syncRequestPython", "logRequest", "getHeadersTable", "maskHeaders", "getFormattedData"]
    _hx_interfaces = [connect_api_IApiClient]
    _hx_super = connect_Base


    def __init__(self):
        pass

    def syncRequest(self,method,url,headers,body,fileArg,fileName,fileContent,certificate):
        return self.syncRequestWithLogger(method,url,headers,body,fileArg,fileName,fileContent,certificate,None,None)

    def syncRequestWithLogger(self,method,url,headers,body,fileArg,fileName,fileContent,certificate,logger,logLevel):
        response = connect_api_impl_ApiClientImpl.syncRequestPython(method,url,headers,body,fileArg,fileName,fileContent,certificate)
        if (logger is None):
            logger = connect_Env.getLogger()
        if (logLevel is None):
            logLevel = (connect_logger_Logger.LEVEL_ERROR if (((response.status >= 400) or ((response.status == -1)))) else connect_logger_Logger.LEVEL_INFO)
        connect_api_impl_ApiClientImpl.logRequest(logLevel,method,url,headers,body,response,logger)
        if (response.status != -1):
            return response
        else:
            raise haxe_Exception.thrown(response.text)

    @staticmethod
    def syncRequestPython(method,url,headers,body,fileArg,fileName,fileContent,certificate):
        try:
            return connect_native_PythonRequest.request(method,url,headers,body,fileArg,fileName,fileContent,300,certificate)
        except BaseException as _g:
            None
            ex = haxe_Exception.caught(_g).unwrap()
            return connect_api_Response(-1,Std.string(ex),None)

    @staticmethod
    def logRequest(level,method,url,headers,body,response,logger = None):
        firstMessage = ((("Http " + HxOverrides.stringOrNull(method.upper())) + " request to ") + ("null" if url is None else url))
        handler = logger.getHandlers().iterator()
        while handler.hasNext():
            handler1 = handler.next()
            fmt = handler1.formatter
            requestList = connect_util_Collection()
            if (headers is not None):
                requestList.push(("Headers:\n" + HxOverrides.stringOrNull(connect_api_impl_ApiClientImpl.getHeadersTable(headers,fmt))))
            if (body is not None):
                requestList.push(connect_api_impl_ApiClientImpl.getFormattedData(body,"Body",fmt))
            if (response.status != -1):
                requestList.push(("Status: " + Std.string(response.status)))
                requestList.push(connect_api_impl_ApiClientImpl.getFormattedData(response.text,"Response",fmt))
            else:
                requestList.push(connect_api_impl_ApiClientImpl.getFormattedData(response.text,"Exception",fmt))
            requestLogger = (logger if ((logger is not None)) else connect_Env.getLogger())
            requestLogger._writeToHandler(level,fmt.formatBlock(level,((("" + ("null" if firstMessage is None else firstMessage)) + "\n") + HxOverrides.stringOrNull(fmt.formatList(level,requestList)))),handler1)

    @staticmethod
    def getHeadersTable(headers,fmt):
        fixedHeaders = (headers if ((connect_Env.getLogger().getLevel() == connect_logger_Logger.LEVEL_DEBUG)) else connect_api_impl_ApiClientImpl.maskHeaders(headers))
        _g = []
        key = fixedHeaders.keys()
        while key.hasNext():
            key1 = key.next()
            _g.append(key1)
        headerKeys = _g
        headersCol = connect_util_Collection().push(connect_util_Collection().push("Name").push("Value"))
        def _hx_local_0(key):
            headersCol.push(connect_util_Collection().push(key).push(fixedHeaders.get(key)))
        Lambda.iter(headerKeys,_hx_local_0)
        return fmt.formatTable(connect_Env.getLogger().getLevel(),headersCol)

    @staticmethod
    def maskHeaders(headers):
        return connect_util_Dictionary.fromObject(connect_util_Masker.maskFields(headers.toObject()))

    @staticmethod
    def getFormattedData(data,title,fmt):
        if connect_util_Util.isJson(data):
            maskedData = (connect_util_Masker.maskString(data) if ((connect_Env.getLogger().getLevel() != connect_logger_Logger.LEVEL_DEBUG)) else data)
            prefix = (("" + ("null" if title is None else title)) + ":\n")
            block = fmt.formatCodeBlock(connect_Env.getLogger().getLevel(),maskedData,"json")
            return (("" + ("null" if prefix is None else prefix)) + ("null" if block is None else block))
        else:
            return ((("" + ("null" if title is None else title)) + ": ") + ("null" if data is None else data))

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
connect_api_impl_ApiClientImpl._hx_class = connect_api_impl_ApiClientImpl
_hx_classes["connect.api.impl.ApiClientImpl"] = connect_api_impl_ApiClientImpl


class connect_flow_FlowExecutor:
    _hx_class_name = "connect.flow.FlowExecutor"
    __slots__ = ("flow", "delegate", "steps", "abortRequested", "abortMessage")
    _hx_fields = ["flow", "delegate", "steps", "abortRequested", "abortMessage"]
    _hx_methods = ["addStep", "reset", "executeRequest", "processSteps", "processStep", "callStepFunc", "processAbortOrEnd", "abort"]
    _hx_statics = ["getExceptionMessage", "getStackTrace"]

    def __init__(self,flow,delegate):
        self.flow = flow
        self.delegate = delegate
        self.steps = []
        self.abortRequested = False
        self.abortMessage = None

    def addStep(self,description,func):
        _this = self.steps
        x = connect_flow_Step(description,func)
        _this.append(x)

    def reset(self):
        self.abortRequested = False
        self.abortMessage = None

    def executeRequest(self,request,firstIndex):
        _g = []
        _g1 = firstIndex
        _g2 = len(self.steps)
        while (_g1 < _g2):
            i = _g1
            _g1 = (_g1 + 1)
            x = (self.steps[i] if i >= 0 and i < len(self.steps) else None)
            _g.append(x)
        steps = _g
        self.processSteps(request,steps,firstIndex)

    def processSteps(self,request,steps,firstIndex):
        _gthis = self
        def _hx_local_0(step,shouldContinue,index):
            if shouldContinue:
                return _gthis.processStep(request,step,(index + firstIndex))
            else:
                return False
        Lambda.foldi(steps,_hx_local_0,True)

    def processStep(self,request,step,index):
        if (self.delegate is not None):
            self.delegate.onStepBegin(request,step,index)
        self.callStepFunc(request,step,index)
        return self.processAbortOrEnd(request,step,index)

    def callStepFunc(self,request,step,index):
        try:
            step.getFunc()(self.flow)
        except BaseException as _g:
            None
            ex = haxe_Exception.caught(_g).unwrap()
            if (self.delegate is not None):
                self.delegate.onStepFail(request,step,index,connect_flow_FlowExecutor.getExceptionMessage(ex))
            self.abort()

    def processAbortOrEnd(self,request,step,index):
        if self.abortRequested:
            if (self.delegate is not None):
                if (self.abortMessage is None):
                    self.delegate.onStepSkip(request,step,index)
                else:
                    self.delegate.onStepAbort(request,step,index,self.abortMessage)
            self.abortRequested = False
            return False
        else:
            if (self.delegate is not None):
                self.delegate.onStepEnd(request,step,index)
            return True

    def abort(self,message = None):
        self.abortRequested = True
        self.abortMessage = message

    @staticmethod
    def getExceptionMessage(ex):
        return str(ex)

    @staticmethod
    def getStackTrace(ex):
        import traceback
        return traceback.format_exc()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.flow = None
        _hx_o.delegate = None
        _hx_o.steps = None
        _hx_o.abortRequested = None
        _hx_o.abortMessage = None
connect_flow_FlowExecutor._hx_class = connect_flow_FlowExecutor
_hx_classes["connect.flow.FlowExecutor"] = connect_flow_FlowExecutor


class connect_flow_FlowLogger:
    _hx_class_name = "connect.flow.FlowLogger"
    __slots__ = ("flowName", "logger")
    _hx_fields = ["flowName", "logger"]
    _hx_methods = ["openFlowSection", "closeFlowSection", "openRequestSection", "closeRequestSection", "openSetupSection", "closeSetupSection", "openStepSection", "closeStepSection", "writeStepInfo", "writeStepError", "writeStep", "getFormattedRequest", "getFormattedData", "getDataTable", "writeStepSkip", "writeMigrationMessage", "writeException"]

    def __init__(self,flowName):
        self.flowName = flowName
        self.logger = connect_Env.getLogger()

    def openFlowSection(self):
        self.logger.openSection(((("Running " + HxOverrides.stringOrNull(self.flowName)) + " on ") + Std.string(connect_util_DateTime.now())))

    def closeFlowSection(self):
        self.logger.closeSection()
        self.logger = connect_Env.getLogger()

    def openRequestSection(self,request):
        self.logger = connect_Env.getLoggerForRequest(request)
        self.logger.openSection(((("Processing request \"" + HxOverrides.stringOrNull(request.id)) + "\" on ") + Std.string(connect_util_DateTime.now())))

    def closeRequestSection(self):
        self.logger.closeSection()
        self.logger = connect_Env.getLogger()

    def openSetupSection(self):
        self.logger.openSection("Setup")

    def closeSetupSection(self):
        self.logger.closeSection()

    def openStepSection(self,index,description):
        self.logger.openSection(((("" + Std.string(((index + 1)))) + ". ") + ("null" if description is None else description)))

    def closeStepSection(self,index):
        self.logger.closeSection()

    def writeStepInfo(self,requestInfo,prevRequestInfo):
        self.writeStep(connect_logger_Logger.LEVEL_INFO,requestInfo,prevRequestInfo)

    def writeStepError(self,requestInfo,prevRequestInfo):
        if (self.logger.getLevel() == connect_logger_Logger.LEVEL_ERROR):
            self.writeStep(connect_logger_Logger.LEVEL_ERROR,requestInfo,prevRequestInfo)

    def writeStep(self,level,requestInfo,prevRequestInfo):
        handler = self.logger.getHandlers().iterator()
        while handler.hasNext():
            handler1 = handler.next()
            _hx_list = connect_util_Collection().push(self.getFormattedRequest(requestInfo.getRequestString(),prevRequestInfo.getRequestString(),handler1.formatter)).push(self.getFormattedData(requestInfo.getDataString(),prevRequestInfo.getDataString(),requestInfo.getData(),handler1.formatter))
            self.logger._writeToHandler(level,handler1.formatter.formatList(level,_hx_list),handler1)

    def getFormattedRequest(self,request,lastRequest,fmt):
        if (request != lastRequest):
            if (self.logger.getLevel() == connect_logger_Logger.LEVEL_DEBUG):
                lastRequestObj = (python_lib_Json.loads(lastRequest,**python__KwArgs_KwArgs_Impl_.fromT(_hx_AnonObject({'object_hook': python_Lib.dictToAnon}))) if (connect_util_Util.isJsonObject(lastRequest)) else None)
                requestObj = (python_lib_Json.loads(request,**python__KwArgs_KwArgs_Impl_.fromT(_hx_AnonObject({'object_hook': python_Lib.dictToAnon}))) if ((connect_util_Util.isJsonObject(request) and ((lastRequestObj is not None)))) else None)
                diff = (connect_util_Util.createObjectDiff(requestObj,lastRequestObj) if (((lastRequestObj is not None) and ((requestObj is not None)))) else None)
                requestStr = (request if ((diff is None)) else (connect_util_Masker.maskObject(diff) if ((connect_Env.getLogger().getLevel() != connect_logger_Logger.LEVEL_DEBUG)) else haxe_format_JsonPrinter.print(diff,None,None)))
                requestTitle = ("Request (changes):" if ((diff is not None)) else "Request:")
                return (("" + ("null" if requestTitle is None else requestTitle)) + HxOverrides.stringOrNull(fmt.formatCodeBlock(self.logger.getLevel(),Std.string(requestStr),"json")))
            else:
                return ("Request (id): " + ("null" if request is None else request))
        else:
            return "Request: Same as in previous step."

    def getFormattedData(self,data,lastData,dataDict,fmt):
        if (data != "{}"):
            if (data != lastData):
                if (self.logger.getLevel() == connect_logger_Logger.LEVEL_DEBUG):
                    return ("Data:" + HxOverrides.stringOrNull(self.getDataTable(dataDict,fmt)))
                else:
                    _g = []
                    key = dataDict.keys()
                    while key.hasNext():
                        key1 = key.next()
                        _g.append(key1)
                    keysStr = ", ".join([python_Boot.toString1(x1,'') for x1 in _g])
                    return (("Data (keys): " + ("null" if keysStr is None else keysStr)) + ".")
            else:
                return "Data: Same as in previous step."
        else:
            return "Data: Empty."

    def getDataTable(self,data,fmt):
        _g = []
        key = data.keys()
        while key.hasNext():
            key1 = key.next()
            _g.append(key1)
        dataKeys = _g
        dataCol = connect_util_Collection().push(connect_util_Collection().push("Key").push("Value"))
        def _hx_local_0(key):
            dataCol.push(connect_util_Collection().push(key).push(data.get(key)))
        Lambda.iter(dataKeys,_hx_local_0)
        return fmt.formatTable(self.logger.getLevel(),dataCol)

    def writeStepSkip(self):
        self.logger.write(connect_logger_Logger.LEVEL_INFO,"Skipping request.")

    def writeMigrationMessage(self,request):
        self.logger.write(connect_logger_Logger.LEVEL_INFO,"Skipping request because it is pending migration.")

    def writeException(self,message):
        self.logger.writeCodeBlock(connect_logger_Logger.LEVEL_ERROR,message,"")

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.flowName = None
        _hx_o.logger = None
connect_flow_FlowLogger._hx_class = connect_flow_FlowLogger
_hx_classes["connect.flow.FlowLogger"] = connect_flow_FlowLogger


class connect_flow_ProcessedRequestInfo:
    _hx_class_name = "connect.flow.ProcessedRequestInfo"
    __slots__ = ("request", "data", "requestStr", "dataStr")
    _hx_fields = ["request", "data", "requestStr", "dataStr"]
    _hx_methods = ["getRequest", "getData", "getRequestString", "getDataString"]
    _hx_statics = ["requestToString", "dataToString"]

    def __init__(self,request,data):
        self.request = request
        self.data = data
        self.requestStr = connect_flow_ProcessedRequestInfo.requestToString(request)
        self.dataStr = connect_flow_ProcessedRequestInfo.dataToString(data)

    def getRequest(self):
        return self.request

    def getData(self):
        return self.data

    def getRequestString(self):
        return self.requestStr

    def getDataString(self):
        return self.dataStr

    @staticmethod
    def requestToString(request):
        if (request is not None):
            if (connect_Env.getLogger().getLevel() != connect_logger_Logger.LEVEL_DEBUG):
                return connect_util_Masker.maskObject(request.toObject())
            else:
                return haxe_format_JsonPrinter.print(request.toObject(),None,None)
        else:
            return ""

    @staticmethod
    def dataToString(data):
        if (data is not None):
            return Std.string(data)
        else:
            return "{}"

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.request = None
        _hx_o.data = None
        _hx_o.requestStr = None
        _hx_o.dataStr = None
connect_flow_ProcessedRequestInfo._hx_class = connect_flow_ProcessedRequestInfo
_hx_classes["connect.flow.ProcessedRequestInfo"] = connect_flow_ProcessedRequestInfo


class connect_flow_RequestCaster:
    _hx_class_name = "connect.flow.RequestCaster"
    __slots__ = ()
    _hx_statics = ["castAssetRequest", "castListing", "castTierConfigRequest", "castUsageFile"]

    @staticmethod
    def castAssetRequest(request):
        def _hx_local_2():
            def _hx_local_1():
                _hx_local_0 = request
                if (Std.isOfType(_hx_local_0,connect_models_AssetRequest) or ((_hx_local_0 is None))):
                    _hx_local_0
                else:
                    raise "Class cast error"
                return _hx_local_0
            return _hx_local_1()
        try:
            return _hx_local_2()
        except BaseException as _g:
            None
            return None

    @staticmethod
    def castListing(request):
        def _hx_local_2():
            def _hx_local_1():
                _hx_local_0 = request
                if (Std.isOfType(_hx_local_0,connect_models_Listing) or ((_hx_local_0 is None))):
                    _hx_local_0
                else:
                    raise "Class cast error"
                return _hx_local_0
            return _hx_local_1()
        try:
            return _hx_local_2()
        except BaseException as _g:
            None
            return None

    @staticmethod
    def castTierConfigRequest(request):
        def _hx_local_2():
            def _hx_local_1():
                _hx_local_0 = request
                if (Std.isOfType(_hx_local_0,connect_models_TierConfigRequest) or ((_hx_local_0 is None))):
                    _hx_local_0
                else:
                    raise "Class cast error"
                return _hx_local_0
            return _hx_local_1()
        try:
            return _hx_local_2()
        except BaseException as _g:
            None
            return None

    @staticmethod
    def castUsageFile(request):
        def _hx_local_2():
            def _hx_local_1():
                _hx_local_0 = request
                if (Std.isOfType(_hx_local_0,connect_models_UsageFile) or ((_hx_local_0 is None))):
                    _hx_local_0
                else:
                    raise "Class cast error"
                return _hx_local_0
            return _hx_local_1()
        try:
            return _hx_local_2()
        except BaseException as _g:
            None
            return None
connect_flow_RequestCaster._hx_class = connect_flow_RequestCaster
_hx_classes["connect.flow.RequestCaster"] = connect_flow_RequestCaster


class connect_flow_Step:
    _hx_class_name = "connect.flow.Step"
    __slots__ = ("description", "func")
    _hx_fields = ["description", "func"]
    _hx_methods = ["getDescription", "getFunc"]

    def __init__(self,description,func):
        self.description = description
        self.func = func

    def getDescription(self):
        return self.description

    def getFunc(self):
        return self.func

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.description = None
        _hx_o.func = None
connect_flow_Step._hx_class = connect_flow_Step
_hx_classes["connect.flow.Step"] = connect_flow_Step


class connect_logger_ILoggerWriter:
    _hx_class_name = "connect.logger.ILoggerWriter"
    __slots__ = ()
    _hx_methods = ["setFilename", "getFilename", "writeLine", "copy"]
connect_logger_ILoggerWriter._hx_class = connect_logger_ILoggerWriter
_hx_classes["connect.logger.ILoggerWriter"] = connect_logger_ILoggerWriter


class connect_logger_FileLoggerWriter(connect_Base):
    _hx_class_name = "connect.logger.FileLoggerWriter"
    __slots__ = ("filename", "file")
    _hx_fields = ["filename", "file"]
    _hx_methods = ["setFilename", "getFilename", "writeLine", "getFile", "copy"]
    _hx_statics = []
    _hx_interfaces = [connect_logger_ILoggerWriter]
    _hx_super = connect_Base


    def __init__(self):
        self.filename = None
        self.file = None

    def setFilename(self,filename):
        currentFilename = self.filename
        self.filename = filename
        if ((filename != currentFilename) and ((self.file is not None))):
            self.file.close()
            self.file = None
            return True
        else:
            return False

    def getFilename(self):
        return self.filename

    def writeLine(self,level,line):
        lineStr = Std.string(line)
        if (self.getFile() is not None):
            self.getFile().writeString((("null" if lineStr is None else lineStr) + "\n"))
            self.getFile().flush()
        try:
            _hx_str = Std.string(lineStr)
            python_Lib.printString((("" + ("null" if _hx_str is None else _hx_str)) + HxOverrides.stringOrNull(python_Lib.lineEnd)))
        except BaseException as _g:
            None

    def getFile(self):
        if ((self.file is None) and ((self.filename is not None))):
            path = haxe_io_Path.directory(self.filename)
            if ((path != "") and (not sys_FileSystem.exists(path))):
                sys_FileSystem.createDirectory(path)
            self.file = sys_io_File.append(self.filename)
        return self.file

    def copy(self,request):
        newCopy = connect_logger_FileLoggerWriter()
        newCopy.setFilename(self.getFilename())
        return newCopy

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.filename = None
        _hx_o.file = None
connect_logger_FileLoggerWriter._hx_class = connect_logger_FileLoggerWriter
_hx_classes["connect.logger.FileLoggerWriter"] = connect_logger_FileLoggerWriter


class connect_logger_ILoggerFormatter:
    _hx_class_name = "connect.logger.ILoggerFormatter"
    __slots__ = ()
    _hx_methods = ["formatSection", "formatBlock", "formatCodeBlock", "formatList", "formatTable", "formatLine", "getFileExtension", "copy"]
connect_logger_ILoggerFormatter._hx_class = connect_logger_ILoggerFormatter
_hx_classes["connect.logger.ILoggerFormatter"] = connect_logger_ILoggerFormatter


class connect_logger_Logger(connect_Base):
    _hx_class_name = "connect.logger.Logger"
    __slots__ = ("path", "level", "handlers", "sections", "maskedFields", "maskedParams", "regexMaskingList", "defaultFilename", "initialConfig")
    _hx_fields = ["path", "level", "handlers", "sections", "maskedFields", "maskedParams", "regexMaskingList", "defaultFilename", "initialConfig"]
    _hx_methods = ["getInitialConfig", "getPath", "getLevel", "isBeautified", "isCompact", "setFilename", "setFilenameForRequest", "getFilename", "getHandlers", "openSection", "closeSection", "writeBlock", "writeCodeBlock", "writeList", "writeTable", "write", "getMaskedFields", "getMaskedParams", "addRegExMask", "_getRegExMaskingList", "log", "debug", "info", "notice", "warning", "error", "critical", "alert", "emergency", "_writeToHandler", "writeSections", "copy"]
    _hx_statics = ["LEVEL_ERROR", "LEVEL_WARNING", "LEVEL_INFO", "LEVEL_DEBUG"]
    _hx_interfaces = []
    _hx_super = connect_Base


    def __init__(self,config):
        self.defaultFilename = None
        if (config is None):
            config = connect_logger_LoggerConfig()
        self.initialConfig = config
        _this = config.path_
        index = (len(config.path_) - 1)
        self.path = (config.path_ if (((("" if (((index < 0) or ((index >= len(_this))))) else _this[index])) == "/")) else (HxOverrides.stringOrNull(config.path_) + "/"))
        a = config.level_
        b = connect_logger_Logger.LEVEL_ERROR
        a1 = (a if (python_lib_Math.isnan(a)) else (b if (python_lib_Math.isnan(b)) else max(a,b)))
        b = connect_logger_Logger.LEVEL_DEBUG
        x = (a1 if (python_lib_Math.isnan(a1)) else (b if (python_lib_Math.isnan(b)) else min(a1,b)))
        tmp = None
        try:
            tmp = int(x)
        except BaseException as _g:
            None
            tmp = None
        self.level = tmp
        self.handlers = config.handlers_.copy()
        self.sections = []
        self.maskedFields = config.maskedFields_.copy()
        self.maskedParams = config.maskedParams_.copy()
        self.regexMaskingList = config.regexMaskingList_.copy()
        if (self.maskedFields.indexOf("Authorization") == -1):
            self.maskedFields.push("Authorization")
        self.defaultFilename = None

    def getInitialConfig(self):
        return self.initialConfig

    def getPath(self):
        return self.path

    def getLevel(self):
        return self.level

    def isBeautified(self):
        return False

    def isCompact(self):
        return False

    def setFilename(self,filename):
        if ((self.defaultFilename is None) and ((filename is not None))):
            self.defaultFilename = filename
        fullname = ((HxOverrides.stringOrNull(self.path) + ("null" if filename is None else filename)) if (((self.path is not None) and ((filename is not None)))) else ((HxOverrides.stringOrNull(self.path) + HxOverrides.stringOrNull(self.defaultFilename)) if ((self.path is not None)) else None))
        def _hx_local_0(handler,last):
            fullnameWithExt = (((("" + ("null" if fullname is None else fullname)) + ".") + HxOverrides.stringOrNull(handler.formatter.getFileExtension())) if ((fullname is not None)) else None)
            if last:
                return handler.writer.setFilename(fullnameWithExt)
            else:
                return False
        setFilenameResult = Lambda.fold(self.handlers,_hx_local_0,True)
        if (setFilenameResult and ((fullname is not None))):
            _g = 0
            _g1 = self.sections
            while (_g < len(_g1)):
                section = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                _g = (_g + 1)
                section.written = False

    def setFilenameForRequest(self,request):
        defaultProvider = "provider"
        defaultHub = "hub"
        defaultMarketplace = "marketplace"
        defaultProduct = "product"
        defaultTierAccount = "tierAccount"
        if Std.isOfType(request,connect_models_Asset):
            def _hx_local_1():
                _hx_local_0 = request
                if (Std.isOfType(_hx_local_0,connect_models_Asset) or ((_hx_local_0 is None))):
                    _hx_local_0
                else:
                    raise "Class cast error"
                return _hx_local_0
            asset = _hx_local_1()
            provider = (asset.connection.provider.id if ((asset.connection.provider is not None)) else defaultProvider)
            hub = (asset.connection.hub.id if ((asset.connection.hub is not None)) else defaultHub)
            marketplace = (asset.marketplace.id if ((asset.marketplace is not None)) else defaultMarketplace)
            product = (asset.product.id if ((asset.product is not None)) else defaultProduct)
            tierAccount = (asset.tiers.customer.id if ((asset.tiers.customer is not None)) else defaultTierAccount)
            self.setFilename(((((((((("" + ("null" if provider is None else provider)) + "/") + ("null" if hub is None else hub)) + "/") + ("null" if marketplace is None else marketplace)) + "/") + ("null" if product is None else product)) + "/") + ("null" if tierAccount is None else tierAccount)))
        if Std.isOfType(request,connect_models_AssetRequest):
            def _hx_local_3():
                _hx_local_2 = request
                if (Std.isOfType(_hx_local_2,connect_models_AssetRequest) or ((_hx_local_2 is None))):
                    _hx_local_2
                else:
                    raise "Class cast error"
                return _hx_local_2
            assetRequest = _hx_local_3()
            provider = (assetRequest.asset.connection.provider.id if ((assetRequest.asset.connection.provider is not None)) else defaultProvider)
            hub = (assetRequest.asset.connection.hub.id if ((assetRequest.asset.connection.hub is not None)) else defaultHub)
            marketplace = (assetRequest.marketplace.id if ((assetRequest.marketplace is not None)) else defaultMarketplace)
            product = (assetRequest.asset.product.id if ((assetRequest.asset.product is not None)) else defaultProduct)
            tierAccount = (assetRequest.asset.tiers.customer.id if ((assetRequest.asset.tiers.customer is not None)) else defaultTierAccount)
            self.setFilename(((((((((("" + ("null" if provider is None else provider)) + "/") + ("null" if hub is None else hub)) + "/") + ("null" if marketplace is None else marketplace)) + "/") + ("null" if product is None else product)) + "/") + ("null" if tierAccount is None else tierAccount)))
        if Std.isOfType(request,connect_models_TierConfigRequest):
            def _hx_local_5():
                _hx_local_4 = request
                if (Std.isOfType(_hx_local_4,connect_models_TierConfigRequest) or ((_hx_local_4 is None))):
                    _hx_local_4
                else:
                    raise "Class cast error"
                return _hx_local_4
            tierRequest = _hx_local_5()
            provider = (tierRequest.configuration.connection.provider.id if ((tierRequest.configuration.connection.provider is not None)) else defaultProvider)
            hub = (tierRequest.configuration.connection.hub.id if ((tierRequest.configuration.connection.hub is not None)) else defaultHub)
            marketplace = (tierRequest.configuration.marketplace.id if ((tierRequest.configuration.marketplace is not None)) else defaultMarketplace)
            product = (tierRequest.configuration.product.id if ((tierRequest.configuration.product is not None)) else defaultProduct)
            tierAccount = (tierRequest.configuration.account.id if ((tierRequest.configuration.account is not None)) else defaultTierAccount)
            self.setFilename(((((((((("" + ("null" if provider is None else provider)) + "/") + ("null" if hub is None else hub)) + "/") + ("null" if marketplace is None else marketplace)) + "/") + ("null" if product is None else product)) + "/") + ("null" if tierAccount is None else tierAccount)))
        if Std.isOfType(request,connect_models_Listing):
            def _hx_local_7():
                _hx_local_6 = request
                if (Std.isOfType(_hx_local_6,connect_models_Listing) or ((_hx_local_6 is None))):
                    _hx_local_6
                else:
                    raise "Class cast error"
                return _hx_local_6
            listingRequest = _hx_local_7()
            provider = (listingRequest.provider.id if ((listingRequest.provider is not None)) else defaultProvider)
            marketplace = (listingRequest.contract.marketplace.id if ((listingRequest.contract.marketplace is not None)) else defaultMarketplace)
            self.setFilename(((("usage/" + ("null" if provider is None else provider)) + "/") + ("null" if marketplace is None else marketplace)))
        if Std.isOfType(request,connect_models_UsageFile):
            def _hx_local_9():
                _hx_local_8 = request
                if (Std.isOfType(_hx_local_8,connect_models_UsageFile) or ((_hx_local_8 is None))):
                    _hx_local_8
                else:
                    raise "Class cast error"
                return _hx_local_8
            usageRequest = _hx_local_9()
            provider = (usageRequest.provider.id if ((usageRequest.provider is not None)) else defaultProvider)
            marketplace = (usageRequest.marketplace.id if ((usageRequest.marketplace.id is not None)) else defaultMarketplace)
            self.setFilename(((("usage/" + ("null" if provider is None else provider)) + "/") + ("null" if marketplace is None else marketplace)))

    def getFilename(self):
        firstHandler = (self.handlers.get(0) if ((self.handlers.length() > 0)) else None)
        if (firstHandler is not None):
            filename = firstHandler.writer.getFilename()
            ext = firstHandler.formatter.getFileExtension()
            noPathFilename = None
            if (filename is not None):
                _hx_str = self.path
                startIndex = None
                noPathFilename = (((filename.find(_hx_str) if ((startIndex is None)) else HxString.indexOfImpl(filename,_hx_str,startIndex))) == 0)
            else:
                noPathFilename = False
            noPathFilename1 = (HxString.substr(filename,len(self.path),None) if noPathFilename else filename)
            noExtFilename = (HxString.substr(noPathFilename1,0,((len(noPathFilename1) - len(ext)) - 1)) if ((((noPathFilename1 is not None) and ((ext is not None))) and ((len(ext) > 0)))) else noPathFilename1)
            return noExtFilename
        else:
            return None

    def getHandlers(self):
        return self.handlers

    def openSection(self,name):
        _this = self.sections
        x = connect_logger__Logger_LoggerSection(name)
        _this.append(x)

    def closeSection(self):
        _this = self.sections
        if (len(_this) != 0):
            _this.pop()

    def writeBlock(self,level,block):
        output = self.handlers.iterator()
        while output.hasNext():
            output1 = output.next()
            self._writeToHandler(level,output1.formatter.formatBlock(level,block),output1)

    def writeCodeBlock(self,level,code,language):
        output = self.handlers.iterator()
        while output.hasNext():
            output1 = output.next()
            self._writeToHandler(level,output1.formatter.formatCodeBlock(level,Std.string(code),language),output1)

    def writeList(self,level,_hx_list):
        output = self.handlers.iterator()
        while output.hasNext():
            output1 = output.next()
            self._writeToHandler(level,output1.formatter.formatList(level,_hx_list),output1)

    def writeTable(self,level,table):
        output = self.handlers.iterator()
        while output.hasNext():
            output1 = output.next()
            self._writeToHandler(level,output1.formatter.formatTable(level,table),output1)

    def write(self,level,message):
        output = self.handlers.iterator()
        while output.hasNext():
            output1 = output.next()
            self._writeToHandler(level,message,output1)

    def getMaskedFields(self):
        return self.maskedFields

    def getMaskedParams(self):
        return self.maskedParams

    def addRegExMask(self,expression):
        self.regexMaskingList.push(connect_util_Util.toRegEx(expression))

    def _getRegExMaskingList(self):
        return self.regexMaskingList

    def log(self,message):
        self.error(message)

    def debug(self,message):
        self.write(connect_logger_Logger.LEVEL_DEBUG,message)

    def info(self,message):
        self.write(connect_logger_Logger.LEVEL_INFO,message)

    def notice(self,message):
        self.info(message)

    def warning(self,message):
        self.write(connect_logger_Logger.LEVEL_WARNING,message)

    def error(self,message):
        self.write(connect_logger_Logger.LEVEL_ERROR,message)

    def critical(self,message):
        self.error(message)

    def alert(self,message):
        self.error(message)

    def emergency(self,message):
        self.error(message)

    def _writeToHandler(self,level,message,handler):
        if (self.level >= level):
            self.writeSections(level)
            handler.writer.writeLine(level,handler.formatter.formatLine(level,message))

    def writeSections(self,level):
        _g = 0
        _g1 = len(self.sections)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if (not (self.sections[i] if i >= 0 and i < len(self.sections) else None).written):
                output = self.handlers.iterator()
                while output.hasNext():
                    output1 = output.next()
                    section = output1.formatter.formatSection(level,(i + 1),(self.sections[i] if i >= 0 and i < len(self.sections) else None).name)
                    output1.writer.writeLine(level,section)
                (self.sections[i] if i >= 0 and i < len(self.sections) else None).written = True

    def copy(self,request):
        handlers = connect_util_Collection()
        handler = self.handlers.iterator()
        while handler.hasNext():
            handler1 = handler.next()
            handlers.push(connect_logger_LoggerHandler(handler1.formatter.copy(request),handler1.writer.copy(request)))
        config = connect_logger_LoggerConfig().path(self.path).level(self.level).handlers(handlers).maskedFields(self.maskedFields).maskedParams(self.maskedParams)
        logger = connect_logger_Logger(config)
        value = list(self.sections)
        setattr(logger,(("_hx_" + "sections") if (("sections" in python_Boot.keywords)) else (("_hx_" + "sections") if (((((len("sections") > 2) and ((ord("sections"[0]) == 95))) and ((ord("sections"[1]) == 95))) and ((ord("sections"[(len("sections") - 1)]) != 95)))) else "sections")),value)
        value = self.regexMaskingList.copy()
        setattr(logger,(("_hx_" + "regexMaskingList") if (("regexMaskingList" in python_Boot.keywords)) else (("_hx_" + "regexMaskingList") if (((((len("regexMaskingList") > 2) and ((ord("regexMaskingList"[0]) == 95))) and ((ord("regexMaskingList"[1]) == 95))) and ((ord("regexMaskingList"[(len("regexMaskingList") - 1)]) != 95)))) else "regexMaskingList")),value)
        value = self.defaultFilename
        setattr(logger,(("_hx_" + "defaultFilename") if (("defaultFilename" in python_Boot.keywords)) else (("_hx_" + "defaultFilename") if (((((len("defaultFilename") > 2) and ((ord("defaultFilename"[0]) == 95))) and ((ord("defaultFilename"[1]) == 95))) and ((ord("defaultFilename"[(len("defaultFilename") - 1)]) != 95)))) else "defaultFilename")),value)
        value = self.initialConfig
        setattr(logger,(("_hx_" + "initialConfig") if (("initialConfig" in python_Boot.keywords)) else (("_hx_" + "initialConfig") if (((((len("initialConfig") > 2) and ((ord("initialConfig"[0]) == 95))) and ((ord("initialConfig"[1]) == 95))) and ((ord("initialConfig"[(len("initialConfig") - 1)]) != 95)))) else "initialConfig")),value)
        logger.setFilenameForRequest(request)
        return logger

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.path = None
        _hx_o.level = None
        _hx_o.handlers = None
        _hx_o.sections = None
        _hx_o.maskedFields = None
        _hx_o.maskedParams = None
        _hx_o.regexMaskingList = None
        _hx_o.defaultFilename = None
        _hx_o.initialConfig = None
connect_logger_Logger._hx_class = connect_logger_Logger
_hx_classes["connect.logger.Logger"] = connect_logger_Logger


class connect_logger__Logger_LoggerSection:
    _hx_class_name = "connect.logger._Logger.LoggerSection"
    __slots__ = ("name", "written")
    _hx_fields = ["name", "written"]

    def __init__(self,name):
        self.name = name
        self.written = False

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.name = None
        _hx_o.written = None
connect_logger__Logger_LoggerSection._hx_class = connect_logger__Logger_LoggerSection
_hx_classes["connect.logger._Logger.LoggerSection"] = connect_logger__Logger_LoggerSection


class haxe_ds__Map_Map_Impl_:
    _hx_class_name = "haxe.ds._Map.Map_Impl_"
    __slots__ = ()
    _hx_statics = ["set", "get", "exists", "remove", "keys", "iterator", "keyValueIterator", "copy", "toString", "clear", "arrayWrite", "toStringMap", "toIntMap", "toEnumValueMapMap", "toObjectMap", "fromStringMap", "fromIntMap", "fromObjectMap"]

    @staticmethod
    def set(this1,key,value):
        this1.set(key,value)

    @staticmethod
    def get(this1,key):
        return this1.get(key)

    @staticmethod
    def exists(this1,key):
        return this1.exists(key)

    @staticmethod
    def remove(this1,key):
        return this1.remove(key)

    @staticmethod
    def keys(this1):
        return this1.keys()

    @staticmethod
    def iterator(this1):
        return this1.iterator()

    @staticmethod
    def keyValueIterator(this1):
        return this1.keyValueIterator()

    @staticmethod
    def copy(this1):
        return this1.copy()

    @staticmethod
    def toString(this1):
        return this1.toString()

    @staticmethod
    def clear(this1):
        this1.clear()

    @staticmethod
    def arrayWrite(this1,k,v):
        this1.set(k,v)
        return v

    @staticmethod
    def toStringMap(t):
        return haxe_ds_StringMap()

    @staticmethod
    def toIntMap(t):
        return haxe_ds_IntMap()

    @staticmethod
    def toEnumValueMapMap(t):
        return haxe_ds_EnumValueMap()

    @staticmethod
    def toObjectMap(t):
        return haxe_ds_ObjectMap()

    @staticmethod
    def fromStringMap(_hx_map):
        return _hx_map

    @staticmethod
    def fromIntMap(_hx_map):
        return _hx_map

    @staticmethod
    def fromObjectMap(_hx_map):
        return _hx_map
haxe_ds__Map_Map_Impl_._hx_class = haxe_ds__Map_Map_Impl_
_hx_classes["haxe.ds._Map.Map_Impl_"] = haxe_ds__Map_Map_Impl_


class connect_logger_LoggerConfig(connect_Base):
    _hx_class_name = "connect.logger.LoggerConfig"
    __slots__ = ("path_", "level_", "handlers_", "maskedFields_", "maskedParams_", "regexMaskingList_")
    _hx_fields = ["path_", "level_", "handlers_", "maskedFields_", "maskedParams_", "regexMaskingList_"]
    _hx_methods = ["path", "level", "levelName", "handlers", "maskedFields", "maskedParams", "beautify", "regexMasks", "markdown"]
    _hx_statics = ["levelTranslation"]
    _hx_interfaces = []
    _hx_super = connect_Base


    def __init__(self):
        self.path_ = "logs"
        self.level_ = connect_logger_Logger.LEVEL_INFO
        self.handlers_ = connect_util_Collection().push(connect_logger_LoggerHandler(connect_logger_PlainLoggerFormatter(),connect_logger_FileLoggerWriter()))
        self.maskedFields_ = connect_util_Collection()
        self.maskedParams_ = connect_util_Collection()
        self.regexMaskingList_ = connect_util_Collection()

    def path(self,path):
        self.path_ = path
        return self

    def level(self,level):
        self.level_ = level
        return self

    def levelName(self,level):
        if (level in connect_logger_LoggerConfig.levelTranslation.h):
            self.level_ = connect_logger_LoggerConfig.levelTranslation.h.get(level,None)
        return self

    def handlers(self,handlers):
        self.handlers_ = handlers.copy()
        return self

    def maskedFields(self,maskedFields):
        self.maskedFields_ = maskedFields
        return self

    def maskedParams(self,maskedParams):
        self.maskedParams_ = maskedParams
        return self

    def beautify(self,enable):
        return self

    def regexMasks(self,expressions):
        expression = expressions.iterator()
        while expression.hasNext():
            expression1 = expression.next()
            self.regexMaskingList_.push(connect_util_Util.toRegEx(expression1))
        return self

    def markdown(self,enable):
        return self

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.path_ = None
        _hx_o.level_ = None
        _hx_o.handlers_ = None
        _hx_o.maskedFields_ = None
        _hx_o.maskedParams_ = None
        _hx_o.regexMaskingList_ = None
connect_logger_LoggerConfig._hx_class = connect_logger_LoggerConfig
_hx_classes["connect.logger.LoggerConfig"] = connect_logger_LoggerConfig


class connect_logger_LoggerHandler:
    _hx_class_name = "connect.logger.LoggerHandler"
    __slots__ = ("formatter", "writer")
    _hx_fields = ["formatter", "writer"]

    def __init__(self,formatter,writer):
        self.formatter = formatter
        self.writer = writer

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.formatter = None
        _hx_o.writer = None
connect_logger_LoggerHandler._hx_class = connect_logger_LoggerHandler
_hx_classes["connect.logger.LoggerHandler"] = connect_logger_LoggerHandler


class connect_logger_PlainLoggerFormatter(connect_Base):
    _hx_class_name = "connect.logger.PlainLoggerFormatter"
    __slots__ = ("currentRequest",)
    _hx_fields = ["currentRequest"]
    _hx_methods = ["formatSection", "formatPrefix", "formatBlock", "getPrefixedLines", "getUnprefixedLines", "formatCodeBlock", "formatList", "formatTable", "formatLine", "getFileExtension", "copy"]
    _hx_statics = ["NO_REQUEST", "formatDate", "formatLevel", "removePrefix", "isPrefixed"]
    _hx_interfaces = [connect_logger_ILoggerFormatter]
    _hx_super = connect_Base


    def __init__(self):
        self.currentRequest = connect_logger_PlainLoggerFormatter.NO_REQUEST

    def formatSection(self,level,sectionLevel,text):
        hashes = StringTools.rpad("","#",sectionLevel)
        prefix = ((("null" if hashes is None else hashes) + " ") if ((hashes != "")) else "")
        textStr = Std.string(text)
        return ((("" + HxOverrides.stringOrNull(self.formatPrefix(level))) + ("null" if prefix is None else prefix)) + ("null" if textStr is None else textStr))

    def formatPrefix(self,level):
        return (((((("" + HxOverrides.stringOrNull(connect_logger_PlainLoggerFormatter.formatDate())) + "  ") + HxOverrides.stringOrNull(connect_logger_PlainLoggerFormatter.formatLevel(level))) + "   ") + HxOverrides.stringOrNull(self.currentRequest)) + " - ")

    def formatBlock(self,level,text):
        _this = self.getPrefixedLines(level,text)
        return "\n".join([python_Boot.toString1(x1,'') for x1 in _this])

    def getPrefixedLines(self,level,text):
        prefix = self.formatPrefix(level)
        def _hx_local_1():
            def _hx_local_0(l):
                return (("" + ("null" if prefix is None else prefix)) + ("null" if l is None else l))
            return list(map(_hx_local_0,self.getUnprefixedLines(level,text)))
        return _hx_local_1()

    def getUnprefixedLines(self,level,text):
        def _hx_local_1():
            def _hx_local_0(l):
                return connect_logger_PlainLoggerFormatter.removePrefix(l)
            return list(map(_hx_local_0,connect_util_Util.getLines(text)))
        return _hx_local_1()

    def formatCodeBlock(self,level,text,language):
        _this = self.getPrefixedLines(level,text)
        return "\n".join([python_Boot.toString1(x1,'') for x1 in _this])

    def formatList(self,level,_hx_list):
        _gthis = self
        if (_hx_list.length() > 0):
            prefix = self.formatPrefix(level)
            def _hx_local_0(text):
                lines = _gthis.getPrefixedLines(level,text)
                python_internal_ArrayImpl._set(lines, 0, ((("" + ("null" if prefix is None else prefix)) + "* ") + HxOverrides.stringOrNull(connect_logger_PlainLoggerFormatter.removePrefix((lines[0] if 0 < len(lines) else None)))))
                return "\n".join([python_Boot.toString1(x1,'') for x1 in lines])
            _this = list(map(_hx_local_0,_hx_list.toArray()))
            formatted = "\n".join([python_Boot.toString1(x1,'') for x1 in _this])
            return formatted
        else:
            return ""

    def formatTable(self,level,table):
        if (table.length() > 0):
            prefix = self.formatPrefix(level)
            _g = []
            row = table.iterator()
            while row.hasNext():
                row1 = row.next()
                x = (((("" + ("null" if prefix is None else prefix)) + "| ") + HxOverrides.stringOrNull(row1.join(" | "))) + " |")
                _g.append(x)
            rows = _g
            header = (rows[0] if 0 < len(rows) else None)
            rest = rows[1:None]
            return ((("" + ("null" if header is None else header)) + "\n") + HxOverrides.stringOrNull("\n".join([python_Boot.toString1(x1,'') for x1 in rest])))
        else:
            return ""

    def formatLine(self,level,text):
        _this = self.getPrefixedLines(level,text)
        return "\n".join([python_Boot.toString1(x1,'') for x1 in _this])

    def getFileExtension(self):
        return "log"

    def copy(self,request):
        formatter = connect_logger_PlainLoggerFormatter()
        formatter.currentRequest = (request.id if ((request is not None)) else connect_logger_PlainLoggerFormatter.NO_REQUEST)
        return formatter

    @staticmethod
    def formatDate():
        date = connect_util_DateTime.now().toString()
        return StringTools.replace(HxOverrides.arrayGet(date.split("+"), 0),"T"," ")

    @staticmethod
    def formatLevel(level):
        levelNames = ["ERROR", "WARNING", "INFO", "DEBUG"]
        if ((level >= 0) and ((level < len(levelNames)))):
            return (levelNames[level] if level >= 0 and level < len(levelNames) else None)
        else:
            return ("LEVEL:" + Std.string(level))

    @staticmethod
    def removePrefix(text):
        lines = connect_util_Util.getLines(text)
        def _hx_local_0(l):
            if connect_logger_PlainLoggerFormatter.isPrefixed(l):
                _this = l.split("- ")[1:None]
                return "- ".join([python_Boot.toString1(x1,'') for x1 in _this])
            else:
                return l
        fixedLines = list(map(_hx_local_0,lines))
        return "\n".join([python_Boot.toString1(x1,'') for x1 in fixedLines])

    @staticmethod
    def isPrefixed(text):
        _this = Std.string(text)
        datePrefix = python_internal_ArrayImpl._get(_this.split(" "), 0)
        return (connect_util_DateTime.fromString(datePrefix) is not None)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.currentRequest = None
connect_logger_PlainLoggerFormatter._hx_class = connect_logger_PlainLoggerFormatter
_hx_classes["connect.logger.PlainLoggerFormatter"] = connect_logger_PlainLoggerFormatter


class connect_models_Model(connect_Base):
    _hx_class_name = "connect.models.Model"
    __slots__ = ("_footprint", "fieldClassNames")
    _hx_fields = ["_footprint", "fieldClassNames"]
    _hx_methods = ["toObject", "toString", "_setFieldClassNames", "_toDiff", "_toDiffString", "getFieldClassName"]
    _hx_statics = ["parse", "parseArray", "_parse", "_parseArray"]
    _hx_interfaces = []
    _hx_super = connect_Base


    def __init__(self):
        self.fieldClassNames = None
        self._footprint = None

    def toObject(self):
        obj = _hx_AnonObject({})
        fields = python_Boot.getInstanceFields(Type.getClass(self))
        _g = 0
        while (_g < len(fields)):
            field = (fields[_g] if _g >= 0 and _g < len(fields) else None)
            _g = (_g + 1)
            if (field != "_footprint"):
                value = Reflect.field(self,field)
                if ((field != "fieldClassNames") and ((value is not None))):
                    _g1 = Type.typeof(value)
                    tmp = _g1.index
                    if (tmp == 5):
                        pass
                    elif (tmp == 6):
                        _g2 = _g1.params[0]
                        _g3 = _g2
                        if (_g3 == str):
                            field1 = connect_Inflection.toSnakeCase(field)
                            value1 = Std.string(value)
                            setattr(obj,(("_hx_" + field1) if ((field1 in python_Boot.keywords)) else (("_hx_" + field1) if (((((len(field1) > 2) and ((ord(field1[0]) == 95))) and ((ord(field1[1]) == 95))) and ((ord(field1[(len(field1) - 1)]) != 95)))) else field1)),value1)
                        elif (_g3 == connect_util_DateTime):
                            field2 = connect_Inflection.toSnakeCase(field)
                            value2 = value.toString()
                            setattr(obj,(("_hx_" + field2) if ((field2 in python_Boot.keywords)) else (("_hx_" + field2) if (((((len(field2) > 2) and ((ord(field2[0]) == 95))) and ((ord(field2[1]) == 95))) and ((ord(field2[(len(field2) - 1)]) != 95)))) else field2)),value2)
                        elif (_g3 == connect_util_Dictionary):
                            field3 = connect_Inflection.toSnakeCase(field)
                            value3 = value.toObject()
                            setattr(obj,(("_hx_" + field3) if ((field3 in python_Boot.keywords)) else (("_hx_" + field3) if (((((len(field3) > 2) and ((ord(field3[0]) == 95))) and ((ord(field3[1]) == 95))) and ((ord(field3[(len(field3) - 1)]) != 95)))) else field3)),value3)
                        else:
                            class_ = _g2
                            className = Type.getClassName(class_)
                            startIndex = None
                            if (((className.find("connect.util.Collection") if ((startIndex is None)) else HxString.indexOfImpl(className,"connect.util.Collection",startIndex))) == 0):
                                def _hx_local_2():
                                    _hx_local_1 = value
                                    if (Std.isOfType(_hx_local_1,connect_util_Collection) or ((_hx_local_1 is None))):
                                        _hx_local_1
                                    else:
                                        raise "Class cast error"
                                    return _hx_local_1
                                col = _hx_local_2()
                                arr = list()
                                elem = col.iterator()
                                while elem.hasNext():
                                    elem1 = elem.next()
                                    elemClassName = Type.getClassName(Type.getClass(elem1))
                                    startIndex1 = None
                                    if (((elemClassName.find("connect.models.") if ((startIndex1 is None)) else HxString.indexOfImpl(elemClassName,"connect.models.",startIndex1))) == 0):
                                        x = elem1.toObject()
                                        arr.append(x)
                                    else:
                                        arr.append(elem1)
                                if (len(arr) > 0):
                                    field4 = connect_Inflection.toSnakeCase(field)
                                    setattr(obj,(("_hx_" + field4) if ((field4 in python_Boot.keywords)) else (("_hx_" + field4) if (((((len(field4) > 2) and ((ord(field4[0]) == 95))) and ((ord(field4[1]) == 95))) and ((ord(field4[(len(field4) - 1)]) != 95)))) else field4)),arr)
                            else:
                                startIndex2 = None
                                if (((className.find("connect.models.") if ((startIndex2 is None)) else HxString.indexOfImpl(className,"connect.models.",startIndex2))) == 0):
                                    def _hx_local_4():
                                        _hx_local_3 = value
                                        if (Std.isOfType(_hx_local_3,connect_models_Model) or ((_hx_local_3 is None))):
                                            _hx_local_3
                                        else:
                                            raise "Class cast error"
                                        return _hx_local_3
                                    model = (_hx_local_4()).toObject()
                                    if (len(python_Boot.fields(model)) != 0):
                                        field5 = connect_Inflection.toSnakeCase(field)
                                        setattr(obj,(("_hx_" + field5) if ((field5 in python_Boot.keywords)) else (("_hx_" + field5) if (((((len(field5) > 2) and ((ord(field5[0]) == 95))) and ((ord(field5[1]) == 95))) and ((ord(field5[(len(field5) - 1)]) != 95)))) else field5)),model)
                                else:
                                    field6 = connect_Inflection.toSnakeCase(field)
                                    setattr(obj,(("_hx_" + field6) if ((field6 in python_Boot.keywords)) else (("_hx_" + field6) if (((((len(field6) > 2) and ((ord(field6[0]) == 95))) and ((ord(field6[1]) == 95))) and ((ord(field6[(len(field6) - 1)]) != 95)))) else field6)),value)
                    else:
                        field7 = connect_Inflection.toSnakeCase(field)
                        setattr(obj,(("_hx_" + field7) if ((field7 in python_Boot.keywords)) else (("_hx_" + field7) if (((((len(field7) > 2) and ((ord(field7[0]) == 95))) and ((ord(field7[1]) == 95))) and ((ord(field7[(len(field7) - 1)]) != 95)))) else field7)),value)
        return obj

    def toString(self):
        return haxe_format_JsonPrinter.print(self.toObject(),None,None)

    def _setFieldClassNames(self,_hx_map):
        if (self.fieldClassNames is None):
            self.fieldClassNames = _hx_map

    def _toDiff(self):
        prevObj = python_lib_Json.loads(self._footprint,**python__KwArgs_KwArgs_Impl_.fromT(_hx_AnonObject({'object_hook': python_Lib.dictToAnon})))
        return connect_util_Util.createObjectDiff(self.toObject(),prevObj)

    def _toDiffString(self):
        return haxe_format_JsonPrinter.print(self._toDiff(),None,None)

    def getFieldClassName(self,field):
        if ((self.fieldClassNames is not None) and (field in self.fieldClassNames.h)):
            nameInField = self.fieldClassNames.h.get(field,None)
            exceptions = ["DateTime", "Dictionary", "String"]
            if (python_internal_ArrayImpl.indexOf(exceptions,nameInField,None) == -1):
                return ("connect.models." + ("null" if nameInField is None else nameInField))
            else:
                return nameInField
        else:
            return None

    @staticmethod
    def parse(modelClass,body):
        obj = python_lib_Json.loads(body,**python__KwArgs_KwArgs_Impl_.fromT(_hx_AnonObject({'object_hook': python_Lib.dictToAnon})))
        if Std.isOfType(obj,list):
            raise haxe_Exception.thrown("Model.parse cannot parse a Json that contains an array.")
        return connect_models_Model._parse(modelClass,obj)

    @staticmethod
    def parseArray(modelClass,body):
        array = python_lib_Json.loads(body,**python__KwArgs_KwArgs_Impl_.fromT(_hx_AnonObject({'object_hook': python_Lib.dictToAnon})))
        if (not Std.isOfType(array,list)):
            raise haxe_Exception.thrown("Model.parseArray can only parse a Json that contains an array.")
        return connect_models_Model._parseArray(modelClass,array)

    @staticmethod
    def _parse(modelClass,obj):
        instance = modelClass(*[])
        def _hx_local_1():
            _hx_local_0 = instance
            if (Std.isOfType(_hx_local_0,connect_models_Model) or ((_hx_local_0 is None))):
                _hx_local_0
            else:
                raise "Class cast error"
            return _hx_local_0
        model = _hx_local_1()
        _g = 0
        _g1 = python_Boot.getInstanceFields(modelClass)
        while (_g < len(_g1)):
            field = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            snakeField = connect_Inflection.toSnakeCase(field)
            camelField = connect_Inflection.toCamelCase(field,True)
            if python_Boot.hasField(obj,snakeField):
                val = Reflect.field(obj,snakeField)
                _g2 = Type.typeof(val)
                tmp = _g2.index
                if (tmp == 4):
                    fieldClassName = model.getFieldClassName(field)
                    className = (("connect.models." + ("null" if camelField is None else camelField)) if ((fieldClassName is None)) else fieldClassName)
                    classObj = Type.resolveClass(className)
                    if (classObj is not None):
                        if (className != "String"):
                            value = connect_models_Model._parse(classObj,val)
                            setattr(model,(("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field)),value)
                        else:
                            value1 = haxe_format_JsonPrinter.print(val,None,None)
                            setattr(model,(("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field)),value1)
                    elif (className == "Dictionary"):
                        value2 = connect_util_Dictionary.fromObject(val)
                        setattr(model,(("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field)),value2)
                    else:
                        raise haxe_Exception.thrown((("Cannot find class \"" + ("null" if className is None else className)) + "\""))
                elif (tmp == 6):
                    if (_g2.params[0] == list):
                        fieldClassName1 = model.getFieldClassName(field)
                        className1 = (connect_Inflection.toSingular(("connect.models." + ("null" if camelField is None else camelField))) if ((fieldClassName1 is None)) else fieldClassName1)
                        classObj1 = Type.resolveClass(className1)
                        value3 = connect_models_Model._parseArray(classObj1,val)
                        setattr(model,(("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field)),value3)
                    else:
                        fieldClassName2 = model.getFieldClassName(field)
                        if ((fieldClassName2 == "DateTime") and ((val is not None))):
                            value4 = connect_util_DateTime.fromString(val)
                            setattr(model,(("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field)),value4)
                        else:
                            try:
                                setattr(model,(("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field)),val)
                            except BaseException as _g3:
                                None
                else:
                    fieldClassName3 = model.getFieldClassName(field)
                    if ((fieldClassName3 == "DateTime") and ((val is not None))):
                        value5 = connect_util_DateTime.fromString(val)
                        setattr(model,(("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field)),value5)
                    else:
                        try:
                            setattr(model,(("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field)),val)
                        except BaseException as _g4:
                            None
        model._footprint = model.toString()
        return instance

    @staticmethod
    def _parseArray(modelClass,array):
        result = connect_util_Collection()
        _g = 0
        while (_g < len(array)):
            obj = (array[_g] if _g >= 0 and _g < len(array) else None)
            _g = (_g + 1)
            if (modelClass is not None):
                result.push(connect_models_Model._parse(modelClass,obj))
            else:
                result.push(obj)
        return result

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o._footprint = None
        _hx_o.fieldClassNames = None
connect_models_Model._hx_class = connect_models_Model
_hx_classes["connect.models.Model"] = connect_models_Model


class connect_models_IdModel(connect_models_Model):
    _hx_class_name = "connect.models.IdModel"
    __slots__ = ("id",)
    _hx_fields = ["id"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_Model


    def __init__(self):
        self.id = None
        super().__init__()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.id = None
connect_models_IdModel._hx_class = connect_models_IdModel
_hx_classes["connect.models.IdModel"] = connect_models_IdModel


class connect_models_Account(connect_models_IdModel):
    _hx_class_name = "connect.models.Account"
    __slots__ = ("name", "type", "events", "brand", "externalId", "sourcing")
    _hx_fields = ["name", "type", "events", "brand", "externalId", "sourcing"]
    _hx_methods = ["listUsers", "getUser"]
    _hx_statics = ["list", "create", "get"]
    _hx_interfaces = []
    _hx_super = connect_models_IdModel


    def __init__(self):
        self.sourcing = None
        self.externalId = None
        self.brand = None
        self.events = None
        self.type = None
        self.name = None
        super().__init__()

    def listUsers(self):
        users = connect_Env.getGeneralApi().listAccountUsers(self.id)
        return connect_models_Model.parseArray(connect_models_User,users)

    def getUser(self,userId):
        def _hx_local_0(user):
            return (user.id == userId)
        users = list(filter(_hx_local_0,self.listUsers().toArray()))
        if (len(users) > 0):
            return (users[0] if 0 < len(users) else None)
        else:
            return None

    @staticmethod
    def list(filters):
        accounts = connect_Env.getGeneralApi().listAccounts(filters)
        return connect_models_Model.parseArray(connect_models_Account,accounts)

    @staticmethod
    def create():
        account = connect_Env.getGeneralApi().createAccount()
        return connect_models_Model.parse(connect_models_Account,account)

    @staticmethod
    def get(id):
        try:
            account = connect_Env.getGeneralApi().getAccount(id)
            return connect_models_Model.parse(connect_models_Account,account)
        except BaseException as _g:
            None
            return None

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.name = None
        _hx_o.type = None
        _hx_o.events = None
        _hx_o.brand = None
        _hx_o.externalId = None
        _hx_o.sourcing = None
connect_models_Account._hx_class = connect_models_Account
_hx_classes["connect.models.Account"] = connect_models_Account


class connect_models_Action(connect_models_IdModel):
    _hx_class_name = "connect.models.Action"
    __slots__ = ("name", "action", "type", "description", "scope", "events")
    _hx_fields = ["name", "action", "type", "description", "scope", "events"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_IdModel


    def __init__(self):
        self.events = None
        self.scope = None
        self.description = None
        self.type = None
        self.action = None
        self.name = None
        super().__init__()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.name = None
        _hx_o.action = None
        _hx_o.type = None
        _hx_o.description = None
        _hx_o.scope = None
        _hx_o.events = None
connect_models_Action._hx_class = connect_models_Action
_hx_classes["connect.models.Action"] = connect_models_Action


class connect_models_Activation(connect_models_Model):
    _hx_class_name = "connect.models.Activation"
    __slots__ = ("link", "message", "date")
    _hx_fields = ["link", "message", "date"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_Model


    def __init__(self):
        self.date = None
        self.message = None
        self.link = None
        super().__init__()
        _g = haxe_ds_StringMap()
        _g.h["date"] = "DateTime"
        self._setFieldClassNames(_g)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.link = None
        _hx_o.message = None
        _hx_o.date = None
connect_models_Activation._hx_class = connect_models_Activation
_hx_classes["connect.models.Activation"] = connect_models_Activation


class connect_models_Agreement(connect_models_IdModel):
    _hx_class_name = "connect.models.Agreement"
    __slots__ = ("type", "title", "description", "created", "updated", "owner", "stats", "author", "version", "active", "link", "versionCreated", "versionContracts", "agreements", "parent", "marketplace", "name")
    _hx_fields = ["type", "title", "description", "created", "updated", "owner", "stats", "author", "version", "active", "link", "versionCreated", "versionContracts", "agreements", "parent", "marketplace", "name"]
    _hx_methods = ["register", "update", "remove", "listVersions", "registerVersion", "getVersion", "removeVersion", "listSubAgreements", "registerSubAgreement"]
    _hx_statics = ["list", "get"]
    _hx_interfaces = []
    _hx_super = connect_models_IdModel


    def __init__(self):
        self.name = None
        self.marketplace = None
        self.parent = None
        self.agreements = None
        self.versionContracts = None
        self.versionCreated = None
        self.link = None
        self.active = None
        self.version = None
        self.author = None
        self.stats = None
        self.owner = None
        self.updated = None
        self.created = None
        self.description = None
        self.title = None
        self.type = None
        super().__init__()
        _g = haxe_ds_StringMap()
        _g.h["created"] = "DateTime"
        _g.h["updated"] = "DateTime"
        _g.h["owner"] = "Account"
        _g.h["stats"] = "AgreementStats"
        _g.h["author"] = "User"
        _g.h["versionCreated"] = "DateTime"
        _g.h["parent"] = "Agreement"
        self._setFieldClassNames(_g)

    def register(self):
        try:
            agreement = connect_Env.getMarketplaceApi().createAgreement(self.toString())
            return connect_models_Model.parse(connect_models_Agreement,agreement)
        except BaseException as _g:
            None
            return None

    def update(self):
        try:
            diff = self._toDiff()
            hasModifiedFields = (len(python_Boot.fields(diff)) > 1)
            if hasModifiedFields:
                agreement = connect_Env.getMarketplaceApi().updateAgreement(self.id,haxe_format_JsonPrinter.print(diff,None,None))
                return connect_models_Model.parse(connect_models_Agreement,agreement)
            else:
                return self
        except BaseException as _g:
            None
            return None

    def remove(self):
        try:
            connect_Env.getMarketplaceApi().removeAgreement(self.id)
            return True
        except BaseException as _g:
            None
            return False

    def listVersions(self):
        versions = connect_Env.getMarketplaceApi().listAgreementVersions(self.id)
        return connect_models_Model.parseArray(connect_models_Agreement,versions)

    def registerVersion(self):
        try:
            version = connect_Env.getMarketplaceApi().newAgreementVersion(self.id,self.toString())
            return connect_models_Model.parse(connect_models_Agreement,version)
        except BaseException as _g:
            None
            return None

    def getVersion(self,version):
        try:
            version1 = connect_Env.getMarketplaceApi().getAgreementVersion(self.id,Std.string(version))
            return connect_models_Model.parse(connect_models_Agreement,version1)
        except BaseException as _g:
            None
            return None

    def removeVersion(self,version):
        try:
            connect_Env.getMarketplaceApi().removeAgreementVersion(self.id,Std.string(version))
            return True
        except BaseException as _g:
            None
            return False

    def listSubAgreements(self):
        agreements = connect_Env.getMarketplaceApi().listAgreementSubAgreements(self.id)
        return connect_models_Model.parseArray(connect_models_Agreement,agreements)

    def registerSubAgreement(self,agreement):
        try:
            agreement1 = connect_Env.getMarketplaceApi().createAgreementSubAgreement(self.id,agreement.toString())
            return connect_models_Model.parse(connect_models_Agreement,agreement1)
        except BaseException as _g:
            None
            return None

    @staticmethod
    def list(filters):
        agreements = connect_Env.getMarketplaceApi().listAgreements(filters)
        return connect_models_Model.parseArray(connect_models_Agreement,agreements)

    @staticmethod
    def get(id):
        try:
            agreement = connect_Env.getMarketplaceApi().getAgreement(id)
            return connect_models_Model.parse(connect_models_Agreement,agreement)
        except BaseException as _g:
            None
            return None

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.type = None
        _hx_o.title = None
        _hx_o.description = None
        _hx_o.created = None
        _hx_o.updated = None
        _hx_o.owner = None
        _hx_o.stats = None
        _hx_o.author = None
        _hx_o.version = None
        _hx_o.active = None
        _hx_o.link = None
        _hx_o.versionCreated = None
        _hx_o.versionContracts = None
        _hx_o.agreements = None
        _hx_o.parent = None
        _hx_o.marketplace = None
        _hx_o.name = None
connect_models_Agreement._hx_class = connect_models_Agreement
_hx_classes["connect.models.Agreement"] = connect_models_Agreement


class connect_models_AgreementStats(connect_models_Model):
    _hx_class_name = "connect.models.AgreementStats"
    __slots__ = ("contracts", "versions")
    _hx_fields = ["contracts", "versions"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_Model


    def __init__(self):
        self.versions = None
        self.contracts = None
        super().__init__()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.contracts = None
        _hx_o.versions = None
connect_models_AgreementStats._hx_class = connect_models_AgreementStats
_hx_classes["connect.models.AgreementStats"] = connect_models_AgreementStats


class connect_models_Asset(connect_models_IdModel):
    _hx_class_name = "connect.models.Asset"
    __slots__ = ("status", "externalId", "externalUid", "externalName", "product", "connection", "contract", "marketplace", "params", "tiers", "items", "configuration", "events")
    _hx_fields = ["status", "externalId", "externalUid", "externalName", "product", "connection", "contract", "marketplace", "params", "tiers", "items", "configuration", "events"]
    _hx_methods = ["getRequests", "getNewItems", "getChangedItems", "getRemovedItems", "getParamById", "getItemById", "getItemByMpn", "getItemByGlobalId", "getCustomerConfig", "getTier1Config", "getTier2Config"]
    _hx_statics = ["list", "get"]
    _hx_interfaces = []
    _hx_super = connect_models_IdModel


    def __init__(self):
        self.events = None
        self.configuration = None
        self.items = None
        self.tiers = None
        self.params = None
        self.marketplace = None
        self.contract = None
        self.connection = None
        self.product = None
        self.externalName = None
        self.externalUid = None
        self.externalId = None
        self.status = None
        super().__init__()

    def getRequests(self):
        requests = connect_Env.getFulfillmentApi().getAssetRequests(self.id)
        return connect_models_Model.parseArray(connect_models_AssetRequest,requests)

    def getNewItems(self):
        def _hx_local_1():
            def _hx_local_0(item):
                if (Std.parseInt(item.quantity) > 0):
                    return (Std.parseInt(item.oldQuantity) == 0)
                else:
                    return False
            return connect_util_Collection._fromArray(list(filter(_hx_local_0,self.items.toArray())))
        return _hx_local_1()

    def getChangedItems(self):
        def _hx_local_1():
            def _hx_local_0(item):
                if (Std.parseInt(item.quantity) > 0):
                    return (Std.parseInt(item.oldQuantity) > 0)
                else:
                    return False
            return connect_util_Collection._fromArray(list(filter(_hx_local_0,self.items.toArray())))
        return _hx_local_1()

    def getRemovedItems(self):
        def _hx_local_1():
            def _hx_local_0(item):
                if (Std.parseInt(item.quantity) == 0):
                    return (Std.parseInt(item.oldQuantity) > 0)
                else:
                    return False
            return connect_util_Collection._fromArray(list(filter(_hx_local_0,self.items.toArray())))
        return _hx_local_1()

    def getParamById(self,paramId):
        def _hx_local_0(param):
            return (param.id == paramId)
        params = list(filter(_hx_local_0,self.params.toArray()))
        if (len(params) > 0):
            return (params[0] if 0 < len(params) else None)
        else:
            return None

    def getItemById(self,itemId):
        def _hx_local_0(item):
            return (item.id == itemId)
        items = list(filter(_hx_local_0,self.items.toArray()))
        if (len(items) > 0):
            return (items[0] if 0 < len(items) else None)
        else:
            return None

    def getItemByMpn(self,mpn):
        def _hx_local_0(item):
            return (item.mpn == mpn)
        items = list(filter(_hx_local_0,self.items.toArray()))
        if (len(items) > 0):
            return (items[0] if 0 < len(items) else None)
        else:
            return None

    def getItemByGlobalId(self,globalId):
        def _hx_local_0(item):
            return (item.globalId == globalId)
        items = list(filter(_hx_local_0,self.items.toArray()))
        if (len(items) > 0):
            return (items[0] if 0 < len(items) else None)
        else:
            return None

    def getCustomerConfig(self):
        if ((self.tiers.customer is not None) and ((self.product is not None))):
            return self.tiers.customer.getTierConfig(self.product.id,0)
        else:
            return None

    def getTier1Config(self):
        if ((self.tiers.tier1 is not None) and ((self.product is not None))):
            return self.tiers.tier1.getTierConfig(self.product.id,1)
        else:
            return None

    def getTier2Config(self):
        if ((self.tiers.tier2 is not None) and ((self.product is not None))):
            return self.tiers.tier2.getTierConfig(self.product.id,2)
        else:
            return None

    @staticmethod
    def list(filters):
        assets = connect_Env.getFulfillmentApi().listAssets(filters)
        return connect_models_Model.parseArray(connect_models_Asset,assets)

    @staticmethod
    def get(id):
        try:
            asset = connect_Env.getFulfillmentApi().getAsset(id)
            return connect_models_Model.parse(connect_models_Asset,asset)
        except BaseException as _g:
            None
            return None

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.status = None
        _hx_o.externalId = None
        _hx_o.externalUid = None
        _hx_o.externalName = None
        _hx_o.product = None
        _hx_o.connection = None
        _hx_o.contract = None
        _hx_o.marketplace = None
        _hx_o.params = None
        _hx_o.tiers = None
        _hx_o.items = None
        _hx_o.configuration = None
        _hx_o.events = None
connect_models_Asset._hx_class = connect_models_Asset
_hx_classes["connect.models.Asset"] = connect_models_Asset


class connect_models_AssetRequest(connect_models_IdModel):
    _hx_class_name = "connect.models.AssetRequest"
    __slots__ = ("type", "created", "updated", "status", "paramsFormUrl", "activationKey", "reason", "note", "asset", "contract", "marketplace", "assignee")
    _hx_fields = ["type", "created", "updated", "status", "paramsFormUrl", "activationKey", "reason", "note", "asset", "contract", "marketplace", "assignee"]
    _hx_methods = ["register", "update", "addValueToParams", "approveByTemplate", "approveByTile", "fail", "inquire", "pend", "assign", "needsMigration", "getConversation", "_updateConversation"]
    _hx_statics = ["list", "get"]
    _hx_interfaces = []
    _hx_super = connect_models_IdModel


    def __init__(self):
        self.assignee = None
        self.marketplace = None
        self.contract = None
        self.asset = None
        self.note = None
        self.reason = None
        self.activationKey = None
        self.paramsFormUrl = None
        self.status = None
        self.updated = None
        self.created = None
        self.type = None
        super().__init__()
        _g = haxe_ds_StringMap()
        _g.h["created"] = "DateTime"
        _g.h["updated"] = "DateTime"
        _g.h["assignee"] = "String"
        self._setFieldClassNames(_g)

    def register(self):
        try:
            request = connect_Env.getFulfillmentApi().createRequest(self.toString())
            return connect_models_Model.parse(connect_models_AssetRequest,request)
        except BaseException as _g:
            None
            return None

    def update(self,params):
        try:
            if (params is None):
                diff = self._toDiff()
                hasModifiedFields = (len(python_Boot.fields(diff)) > 1)
                if hasModifiedFields:
                    request = connect_Env.getFulfillmentApi().updateRequest(self.id,haxe_format_JsonPrinter.print(self.addValueToParams(diff),None,None))
                    return connect_models_Model.parse(connect_models_AssetRequest,request)
                else:
                    return self
            else:
                if (params.length() > 0):
                    connect_Env.getFulfillmentApi().updateRequest(self.id,(("{\"asset\":{\"params\":" + HxOverrides.stringOrNull(params.toString())) + "}}"))
                return self
        except BaseException as _g:
            None
            return None

    def addValueToParams(self,obj):
        _gthis = self
        asset = Reflect.field(obj,"asset")
        params = (Reflect.field(asset,"params") if ((asset is not None)) else None)
        if (params is not None):
            def _hx_local_0(p):
                if (not python_Boot.hasField(p,"value")):
                    value = _gthis.asset.getParamById(Reflect.field(p,"id")).value
                    setattr(p,(("_hx_" + "value") if (("value" in python_Boot.keywords)) else (("_hx_" + "value") if (((((len("value") > 2) and ((ord("value"[0]) == 95))) and ((ord("value"[1]) == 95))) and ((ord("value"[(len("value") - 1)]) != 95)))) else "value")),value)
            Lambda.iter(params,_hx_local_0)
        return obj

    def approveByTemplate(self,id):
        request = connect_Env.getFulfillmentApi().changeRequestStatus(self.id,"approve",haxe_format_JsonPrinter.print(_hx_AnonObject({'template_id': id}),None,None))
        self._updateConversation((("Request approved using template " + ("null" if id is None else id)) + "."))
        return connect_models_Model.parse(connect_models_AssetRequest,request)

    def approveByTile(self,text):
        request = connect_Env.getFulfillmentApi().changeRequestStatus(self.id,"approve",haxe_format_JsonPrinter.print(_hx_AnonObject({'activation_tile': text}),None,None))
        self._updateConversation("Request approved using custom activation tile.")
        return connect_models_Model.parse(connect_models_AssetRequest,request)

    def fail(self,reason):
        request = connect_Env.getFulfillmentApi().changeRequestStatus(self.id,"fail",haxe_format_JsonPrinter.print(_hx_AnonObject({'reason': reason}),None,None))
        self._updateConversation((("Request failed: " + ("null" if reason is None else reason)) + "."))
        return connect_models_Model.parse(connect_models_AssetRequest,request)

    def inquire(self,templateId):
        body = (_hx_AnonObject({'template_id': templateId}) if ((templateId is not None)) else _hx_AnonObject({}))
        request = connect_Env.getFulfillmentApi().changeRequestStatus(self.id,"inquire",haxe_format_JsonPrinter.print(body,None,None))
        self._updateConversation("Request inquired.")
        return connect_models_Model.parse(connect_models_AssetRequest,request)

    def pend(self):
        request = connect_Env.getFulfillmentApi().changeRequestStatus(self.id,"pend","{}")
        self._updateConversation("Request pended.")
        return connect_models_Model.parse(connect_models_AssetRequest,request)

    def assign(self,assigneeId):
        request = connect_Env.getFulfillmentApi().assignRequest(self.id,assigneeId)
        self._updateConversation((("Request assigned to " + ("null" if assigneeId is None else assigneeId)) + "."))
        return connect_models_Model.parse(connect_models_AssetRequest,request)

    def needsMigration(self,key = None):
        if (key is None):
            key = "migration_info"
        param = self.asset.getParamById(key)
        result = (((param is not None) and ((param.value is not None))) and ((param.value != "")))
        if result:
            return True
        elif (key == "migration_info"):
            return self.needsMigration("migration_info_object")
        else:
            return False

    def getConversation(self):
        convs = connect_models_Conversation.list(connect_api_Query().equal("instance_id",self.id))
        conv = (convs.get(0) if ((convs.length() > 0)) else None)
        if (((conv is not None) and ((conv.id is not None))) and ((conv.id != ""))):
            return connect_models_Conversation.get(conv.id)
        else:
            return None

    def _updateConversation(self,message):
        conversation = self.getConversation()
        if (conversation is not None):
            try:
                conversation.createMessage(message)
            except BaseException as _g:
                None
                connect_Env.getLogger().write(connect_logger_Logger.LEVEL_ERROR,((("Error updating conversation for request " + HxOverrides.stringOrNull(self.id)) + ": ") + ("null" if message is None else message)))

    @staticmethod
    def list(filters):
        requests = connect_Env.getFulfillmentApi().listRequests(filters)
        return connect_models_Model.parseArray(connect_models_AssetRequest,requests)

    @staticmethod
    def get(id):
        try:
            request = connect_Env.getFulfillmentApi().getRequest(id)
            return connect_models_Model.parse(connect_models_AssetRequest,request)
        except BaseException as _g:
            None
            return None

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.type = None
        _hx_o.created = None
        _hx_o.updated = None
        _hx_o.status = None
        _hx_o.paramsFormUrl = None
        _hx_o.activationKey = None
        _hx_o.reason = None
        _hx_o.note = None
        _hx_o.asset = None
        _hx_o.contract = None
        _hx_o.marketplace = None
        _hx_o.assignee = None
connect_models_AssetRequest._hx_class = connect_models_AssetRequest
_hx_classes["connect.models.AssetRequest"] = connect_models_AssetRequest


class connect_models_BillingAnniversary(connect_models_Model):
    _hx_class_name = "connect.models.BillingAnniversary"
    __slots__ = ("day", "month")
    _hx_fields = ["day", "month"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_Model


    def __init__(self):
        self.month = None
        self.day = None
        super().__init__()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.day = None
        _hx_o.month = None
connect_models_BillingAnniversary._hx_class = connect_models_BillingAnniversary
_hx_classes["connect.models.BillingAnniversary"] = connect_models_BillingAnniversary


class connect_models_BillingInfo(connect_models_Model):
    _hx_class_name = "connect.models.BillingInfo"
    __slots__ = ("stats", "period", "nextDate", "anniversary")
    _hx_fields = ["stats", "period", "nextDate", "anniversary"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_Model


    def __init__(self):
        self.anniversary = None
        self.nextDate = None
        self.period = None
        self.stats = None
        super().__init__()
        _g = haxe_ds_StringMap()
        _g.h["stats"] = "BillingStats"
        _g.h["nextDate"] = "DateTime"
        _g.h["anniversary"] = "BillingAnniversary"
        self._setFieldClassNames(_g)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.stats = None
        _hx_o.period = None
        _hx_o.nextDate = None
        _hx_o.anniversary = None
connect_models_BillingInfo._hx_class = connect_models_BillingInfo
_hx_classes["connect.models.BillingInfo"] = connect_models_BillingInfo


class connect_models_BillingStats(connect_models_Model):
    _hx_class_name = "connect.models.BillingStats"
    __slots__ = ("vendor", "provider")
    _hx_fields = ["vendor", "provider"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_Model


    def __init__(self):
        self.provider = None
        self.vendor = None
        super().__init__()
        _g = haxe_ds_StringMap()
        _g.h["vendor"] = "BillingStatsInfo"
        _g.h["provider"] = "BillingStatsInfo"
        self._setFieldClassNames(_g)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.vendor = None
        _hx_o.provider = None
connect_models_BillingStats._hx_class = connect_models_BillingStats
_hx_classes["connect.models.BillingStats"] = connect_models_BillingStats


class connect_models_BillingStatsInfo(connect_models_Model):
    _hx_class_name = "connect.models.BillingStatsInfo"
    __slots__ = ("lastRequest", "count")
    _hx_fields = ["lastRequest", "count"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_Model


    def __init__(self):
        self.count = None
        self.lastRequest = None
        super().__init__()
        _g = haxe_ds_StringMap()
        _g.h["lastRequest"] = "BillingStatsRequest"
        self._setFieldClassNames(_g)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.lastRequest = None
        _hx_o.count = None
connect_models_BillingStatsInfo._hx_class = connect_models_BillingStatsInfo
_hx_classes["connect.models.BillingStatsInfo"] = connect_models_BillingStatsInfo


class connect_models_BillingStatsRequest(connect_models_IdModel):
    _hx_class_name = "connect.models.BillingStatsRequest"
    __slots__ = ("type", "period")
    _hx_fields = ["type", "period"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_IdModel


    def __init__(self):
        self.period = None
        self.type = None
        super().__init__()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.type = None
        _hx_o.period = None
connect_models_BillingStatsRequest._hx_class = connect_models_BillingStatsRequest
_hx_classes["connect.models.BillingStatsRequest"] = connect_models_BillingStatsRequest


class connect_models_Category(connect_models_IdModel):
    _hx_class_name = "connect.models.Category"
    __slots__ = ("name", "parent", "children", "family")
    _hx_fields = ["name", "parent", "children", "family"]
    _hx_methods = []
    _hx_statics = ["list", "get"]
    _hx_interfaces = []
    _hx_super = connect_models_IdModel


    def __init__(self):
        self.family = None
        self.children = None
        self.parent = None
        self.name = None
        super().__init__()
        _g = haxe_ds_StringMap()
        _g.h["parent"] = "Category"
        _g.h["children"] = "Category"
        self._setFieldClassNames(_g)

    @staticmethod
    def list(filters):
        categories = connect_Env.getGeneralApi().listCategories(filters)
        return connect_models_Model.parseArray(connect_models_Category,categories)

    @staticmethod
    def get(id):
        try:
            category = connect_Env.getGeneralApi().getCategory(id)
            return connect_models_Model.parse(connect_models_Category,category)
        except BaseException as _g:
            None
            return None

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.name = None
        _hx_o.parent = None
        _hx_o.children = None
        _hx_o.family = None
connect_models_Category._hx_class = connect_models_Category
_hx_classes["connect.models.Category"] = connect_models_Category


class connect_models_Choice(connect_models_Model):
    _hx_class_name = "connect.models.Choice"
    __slots__ = ("value", "label")
    _hx_fields = ["value", "label"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_Model


    def __init__(self):
        self.label = None
        self.value = None
        super().__init__()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.value = None
        _hx_o.label = None
connect_models_Choice._hx_class = connect_models_Choice
_hx_classes["connect.models.Choice"] = connect_models_Choice


class connect_models_Configuration(connect_models_Model):
    _hx_class_name = "connect.models.Configuration"
    __slots__ = ("params",)
    _hx_fields = ["params"]
    _hx_methods = ["getParamById"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_Model


    def __init__(self):
        self.params = None
        super().__init__()

    def getParamById(self,paramId):
        def _hx_local_0(param):
            return (param.id == paramId)
        params = list(filter(_hx_local_0,self.params.toArray()))
        if (len(params) > 0):
            return (params[0] if 0 < len(params) else None)
        else:
            return None

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.params = None
connect_models_Configuration._hx_class = connect_models_Configuration
_hx_classes["connect.models.Configuration"] = connect_models_Configuration


class connect_models_Configurations(connect_models_Model):
    _hx_class_name = "connect.models.Configurations"
    __slots__ = ("suspendResumeSupported", "requiresResellerInformation")
    _hx_fields = ["suspendResumeSupported", "requiresResellerInformation"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_Model


    def __init__(self):
        self.requiresResellerInformation = None
        self.suspendResumeSupported = None
        super().__init__()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.suspendResumeSupported = None
        _hx_o.requiresResellerInformation = None
connect_models_Configurations._hx_class = connect_models_Configurations
_hx_classes["connect.models.Configurations"] = connect_models_Configurations


class connect_models_Connection(connect_models_IdModel):
    _hx_class_name = "connect.models.Connection"
    __slots__ = ("type", "provider", "vendor", "product", "hub", "status", "createdAt")
    _hx_fields = ["type", "provider", "vendor", "product", "hub", "status", "createdAt"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_IdModel


    def __init__(self):
        self.createdAt = None
        self.status = None
        self.hub = None
        self.product = None
        self.vendor = None
        self.provider = None
        self.type = None
        super().__init__()
        _g = haxe_ds_StringMap()
        _g.h["provider"] = "Account"
        _g.h["vendor"] = "Account"
        _g.h["createdAt"] = "DateTime"
        self._setFieldClassNames(_g)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.type = None
        _hx_o.provider = None
        _hx_o.vendor = None
        _hx_o.product = None
        _hx_o.hub = None
        _hx_o.status = None
        _hx_o.createdAt = None
connect_models_Connection._hx_class = connect_models_Connection
_hx_classes["connect.models.Connection"] = connect_models_Connection


class connect_models_Constraints(connect_models_Model):
    _hx_class_name = "connect.models.Constraints"
    __slots__ = ("required", "hidden", "unique", "reconciliation", "shared", "minLength", "maxLength", "choices")
    _hx_fields = ["required", "hidden", "unique", "reconciliation", "shared", "minLength", "maxLength", "choices"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_Model


    def __init__(self):
        self.choices = None
        self.maxLength = None
        self.minLength = None
        self.shared = None
        self.reconciliation = None
        self.unique = None
        self.hidden = None
        self.required = None
        super().__init__()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.required = None
        _hx_o.hidden = None
        _hx_o.unique = None
        _hx_o.reconciliation = None
        _hx_o.shared = None
        _hx_o.minLength = None
        _hx_o.maxLength = None
        _hx_o.choices = None
connect_models_Constraints._hx_class = connect_models_Constraints
_hx_classes["connect.models.Constraints"] = connect_models_Constraints


class connect_models_Contact(connect_models_Model):
    _hx_class_name = "connect.models.Contact"
    __slots__ = ("firstName", "lastName", "email", "phoneNumber")
    _hx_fields = ["firstName", "lastName", "email", "phoneNumber"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_Model


    def __init__(self):
        self.phoneNumber = None
        self.email = None
        self.lastName = None
        self.firstName = None
        super().__init__()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.firstName = None
        _hx_o.lastName = None
        _hx_o.email = None
        _hx_o.phoneNumber = None
connect_models_Contact._hx_class = connect_models_Contact
_hx_classes["connect.models.Contact"] = connect_models_Contact


class connect_models_ContactInfo(connect_models_Model):
    _hx_class_name = "connect.models.ContactInfo"
    __slots__ = ("addressLine1", "addressLine2", "country", "state", "city", "postalCode", "contact")
    _hx_fields = ["addressLine1", "addressLine2", "country", "state", "city", "postalCode", "contact"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_Model


    def __init__(self):
        self.contact = None
        self.postalCode = None
        self.city = None
        self.state = None
        self.country = None
        self.addressLine2 = None
        self.addressLine1 = None
        super().__init__()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.addressLine1 = None
        _hx_o.addressLine2 = None
        _hx_o.country = None
        _hx_o.state = None
        _hx_o.city = None
        _hx_o.postalCode = None
        _hx_o.contact = None
connect_models_ContactInfo._hx_class = connect_models_ContactInfo
_hx_classes["connect.models.ContactInfo"] = connect_models_ContactInfo


class connect_models_Contract(connect_models_IdModel):
    _hx_class_name = "connect.models.Contract"
    __slots__ = ("name", "version", "type", "status", "agreement", "marketplace", "owner", "creator", "created", "updated", "enrolled", "versionCreated", "activation", "signee")
    _hx_fields = ["name", "version", "type", "status", "agreement", "marketplace", "owner", "creator", "created", "updated", "enrolled", "versionCreated", "activation", "signee"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_IdModel


    def __init__(self):
        self.signee = None
        self.activation = None
        self.versionCreated = None
        self.enrolled = None
        self.updated = None
        self.created = None
        self.creator = None
        self.owner = None
        self.marketplace = None
        self.agreement = None
        self.status = None
        self.type = None
        self.version = None
        self.name = None
        super().__init__()
        _g = haxe_ds_StringMap()
        _g.h["created"] = "DateTime"
        _g.h["updated"] = "DateTime"
        _g.h["enrolled"] = "DateTime"
        _g.h["versionCreated"] = "DateTime"
        _g.h["owner"] = "Account"
        _g.h["creator"] = "User"
        _g.h["signee"] = "User"
        self._setFieldClassNames(_g)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.name = None
        _hx_o.version = None
        _hx_o.type = None
        _hx_o.status = None
        _hx_o.agreement = None
        _hx_o.marketplace = None
        _hx_o.owner = None
        _hx_o.creator = None
        _hx_o.created = None
        _hx_o.updated = None
        _hx_o.enrolled = None
        _hx_o.versionCreated = None
        _hx_o.activation = None
        _hx_o.signee = None
connect_models_Contract._hx_class = connect_models_Contract
_hx_classes["connect.models.Contract"] = connect_models_Contract


class connect_models_Conversation(connect_models_IdModel):
    _hx_class_name = "connect.models.Conversation"
    __slots__ = ("instanceId", "created", "topic", "messages", "creator")
    _hx_fields = ["instanceId", "created", "topic", "messages", "creator"]
    _hx_methods = ["createMessage"]
    _hx_statics = ["list", "create", "get"]
    _hx_interfaces = []
    _hx_super = connect_models_IdModel


    def __init__(self):
        self.creator = None
        self.messages = None
        self.topic = None
        self.created = None
        self.instanceId = None
        super().__init__()
        _g = haxe_ds_StringMap()
        _g.h["created"] = "DateTime"
        _g.h["creator"] = "User"
        self._setFieldClassNames(_g)

    def createMessage(self,text):
        msg = connect_Env.getGeneralApi().createConversationMessage(self.id,haxe_format_JsonPrinter.print(_hx_AnonObject({'text': text}),None,None))
        message = connect_models_Model.parse(connect_models_Message,msg)
        if (self.messages is None):
            self.messages = connect_util_Collection()
        self.messages.push(message)
        return message

    @staticmethod
    def list(filters):
        convs = connect_Env.getGeneralApi().listConversations(filters)
        return connect_models_Model.parseArray(connect_models_Conversation,convs)

    @staticmethod
    def create(instanceId,topic):
        conv = connect_Env.getGeneralApi().createConversation(haxe_format_JsonPrinter.print(_hx_AnonObject({'instance_id': instanceId, 'topic': topic}),None,None))
        return connect_models_Model.parse(connect_models_Conversation,conv)

    @staticmethod
    def get(id):
        try:
            conv = connect_Env.getGeneralApi().getConversation(id)
            return connect_models_Model.parse(connect_models_Conversation,conv)
        except BaseException as _g:
            None
            return None

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.instanceId = None
        _hx_o.created = None
        _hx_o.topic = None
        _hx_o.messages = None
        _hx_o.creator = None
connect_models_Conversation._hx_class = connect_models_Conversation
_hx_classes["connect.models.Conversation"] = connect_models_Conversation


class connect_models_Country(connect_models_IdModel):
    _hx_class_name = "connect.models.Country"
    __slots__ = ("name", "icon", "zone")
    _hx_fields = ["name", "icon", "zone"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_IdModel


    def __init__(self):
        self.zone = None
        self.icon = None
        self.name = None
        super().__init__()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.name = None
        _hx_o.icon = None
        _hx_o.zone = None
connect_models_Country._hx_class = connect_models_Country
_hx_classes["connect.models.Country"] = connect_models_Country


class connect_models_CustomerUiSettings(connect_models_Model):
    _hx_class_name = "connect.models.CustomerUiSettings"
    __slots__ = ("description", "gettingStarted", "downloadLinks", "documents")
    _hx_fields = ["description", "gettingStarted", "downloadLinks", "documents"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_Model


    def __init__(self):
        self.documents = None
        self.downloadLinks = None
        self.gettingStarted = None
        self.description = None
        super().__init__()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.description = None
        _hx_o.gettingStarted = None
        _hx_o.downloadLinks = None
        _hx_o.documents = None
connect_models_CustomerUiSettings._hx_class = connect_models_CustomerUiSettings
_hx_classes["connect.models.CustomerUiSettings"] = connect_models_CustomerUiSettings


class connect_models_Document(connect_models_Model):
    _hx_class_name = "connect.models.Document"
    __slots__ = ("title", "url")
    _hx_fields = ["title", "url"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_Model


    def __init__(self):
        self.url = None
        self.title = None
        super().__init__()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.title = None
        _hx_o.url = None
connect_models_Document._hx_class = connect_models_Document
_hx_classes["connect.models.Document"] = connect_models_Document


class connect_models_DownloadLink(connect_models_Model):
    _hx_class_name = "connect.models.DownloadLink"
    __slots__ = ("title", "url", "visibleFor")
    _hx_fields = ["title", "url", "visibleFor"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_Model


    def __init__(self):
        self.visibleFor = None
        self.url = None
        self.title = None
        super().__init__()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.title = None
        _hx_o.url = None
        _hx_o.visibleFor = None
connect_models_DownloadLink._hx_class = connect_models_DownloadLink
_hx_classes["connect.models.DownloadLink"] = connect_models_DownloadLink


class connect_models_Event(connect_models_Model):
    _hx_class_name = "connect.models.Event"
    __slots__ = ("at", "by")
    _hx_fields = ["at", "by"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_Model


    def __init__(self):
        self.by = None
        self.at = None
        super().__init__()
        _g = haxe_ds_StringMap()
        _g.h["at"] = "DateTime"
        _g.h["by"] = "User"
        self._setFieldClassNames(_g)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.at = None
        _hx_o.by = None
connect_models_Event._hx_class = connect_models_Event
_hx_classes["connect.models.Event"] = connect_models_Event


class connect_models_Events(connect_models_Model):
    _hx_class_name = "connect.models.Events"
    __slots__ = ("created", "inquired", "pended", "validated", "updated", "approved", "uploaded", "submitted", "accepted", "rejected", "closed")
    _hx_fields = ["created", "inquired", "pended", "validated", "updated", "approved", "uploaded", "submitted", "accepted", "rejected", "closed"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_Model


    def __init__(self):
        self.closed = None
        self.rejected = None
        self.accepted = None
        self.submitted = None
        self.uploaded = None
        self.approved = None
        self.updated = None
        self.validated = None
        self.pended = None
        self.inquired = None
        self.created = None
        super().__init__()
        _g = haxe_ds_StringMap()
        _g.h["created"] = "Event"
        _g.h["inquired"] = "Event"
        _g.h["pended"] = "Event"
        _g.h["validated"] = "Event"
        _g.h["updated"] = "Event"
        _g.h["approved"] = "Event"
        _g.h["uploaded"] = "Event"
        _g.h["submitted"] = "Event"
        _g.h["accepted"] = "Event"
        _g.h["rejected"] = "Event"
        _g.h["closed"] = "Event"
        self._setFieldClassNames(_g)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.created = None
        _hx_o.inquired = None
        _hx_o.pended = None
        _hx_o.validated = None
        _hx_o.updated = None
        _hx_o.approved = None
        _hx_o.uploaded = None
        _hx_o.submitted = None
        _hx_o.accepted = None
        _hx_o.rejected = None
        _hx_o.closed = None
connect_models_Events._hx_class = connect_models_Events
_hx_classes["connect.models.Events"] = connect_models_Events


class connect_models_ExtIdHub(connect_models_Model):
    _hx_class_name = "connect.models.ExtIdHub"
    __slots__ = ("hub", "externalId")
    _hx_fields = ["hub", "externalId"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_Model


    def __init__(self):
        self.externalId = None
        self.hub = None
        super().__init__()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.hub = None
        _hx_o.externalId = None
connect_models_ExtIdHub._hx_class = connect_models_ExtIdHub
_hx_classes["connect.models.ExtIdHub"] = connect_models_ExtIdHub


class connect_models_Family(connect_models_IdModel):
    _hx_class_name = "connect.models.Family"
    __slots__ = ("name",)
    _hx_fields = ["name"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_IdModel


    def __init__(self):
        self.name = None
        super().__init__()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.name = None
connect_models_Family._hx_class = connect_models_Family
_hx_classes["connect.models.Family"] = connect_models_Family


class connect_models_Hub(connect_models_IdModel):
    _hx_class_name = "connect.models.Hub"
    __slots__ = ("name", "company", "description", "instance", "events", "stats")
    _hx_fields = ["name", "company", "description", "instance", "events", "stats"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_IdModel


    def __init__(self):
        self.stats = None
        self.events = None
        self.instance = None
        self.description = None
        self.company = None
        self.name = None
        super().__init__()
        _g = haxe_ds_StringMap()
        _g.h["company"] = "Account"
        _g.h["stats"] = "HubStats"
        self._setFieldClassNames(_g)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.name = None
        _hx_o.company = None
        _hx_o.description = None
        _hx_o.instance = None
        _hx_o.events = None
        _hx_o.stats = None
connect_models_Hub._hx_class = connect_models_Hub
_hx_classes["connect.models.Hub"] = connect_models_Hub


class connect_models_HubStats(connect_models_Model):
    _hx_class_name = "connect.models.HubStats"
    __slots__ = ("connections", "marketplaces")
    _hx_fields = ["connections", "marketplaces"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_Model


    def __init__(self):
        self.marketplaces = None
        self.connections = None
        super().__init__()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.connections = None
        _hx_o.marketplaces = None
connect_models_HubStats._hx_class = connect_models_HubStats
_hx_classes["connect.models.HubStats"] = connect_models_HubStats


class connect_models_Instance(connect_models_IdModel):
    _hx_class_name = "connect.models.Instance"
    __slots__ = ("type",)
    _hx_fields = ["type"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_IdModel


    def __init__(self):
        self.type = None
        super().__init__()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.type = None
connect_models_Instance._hx_class = connect_models_Instance
_hx_classes["connect.models.Instance"] = connect_models_Instance


class connect_models_Item(connect_models_IdModel):
    _hx_class_name = "connect.models.Item"
    __slots__ = ("mpn", "quantity", "oldQuantity", "renewal", "params", "status", "displayName", "globalId", "itemType", "period", "type", "name", "description", "billing")
    _hx_fields = ["mpn", "quantity", "oldQuantity", "renewal", "params", "status", "displayName", "globalId", "itemType", "period", "type", "name", "description", "billing"]
    _hx_methods = ["getParamById"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_IdModel


    def __init__(self):
        self.billing = None
        self.description = None
        self.name = None
        self.type = None
        self.period = None
        self.itemType = None
        self.globalId = None
        self.displayName = None
        self.status = None
        self.params = None
        self.renewal = None
        self.oldQuantity = None
        self.quantity = None
        self.mpn = None
        super().__init__()
        _g = haxe_ds_StringMap()
        _g.h["billing"] = "ItemBilling"
        self._setFieldClassNames(_g)

    def getParamById(self,paramId):
        def _hx_local_0(param):
            return (param.id == paramId)
        params = list(filter(_hx_local_0,self.params.toArray()))
        if (len(params) > 0):
            return (params[0] if 0 < len(params) else None)
        else:
            return None

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.mpn = None
        _hx_o.quantity = None
        _hx_o.oldQuantity = None
        _hx_o.renewal = None
        _hx_o.params = None
        _hx_o.status = None
        _hx_o.displayName = None
        _hx_o.globalId = None
        _hx_o.itemType = None
        _hx_o.period = None
        _hx_o.type = None
        _hx_o.name = None
        _hx_o.description = None
        _hx_o.billing = None
connect_models_Item._hx_class = connect_models_Item
_hx_classes["connect.models.Item"] = connect_models_Item


class connect_models_ItemBilling(connect_models_Model):
    _hx_class_name = "connect.models.ItemBilling"
    __slots__ = ("cycleNumber",)
    _hx_fields = ["cycleNumber"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_Model


    def __init__(self):
        self.cycleNumber = None
        super().__init__()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.cycleNumber = None
connect_models_ItemBilling._hx_class = connect_models_ItemBilling
_hx_classes["connect.models.ItemBilling"] = connect_models_ItemBilling


class connect_models_Listing(connect_models_IdModel):
    _hx_class_name = "connect.models.Listing"
    __slots__ = ("status", "contract", "product", "created", "vendor", "provider", "sourcing", "pendingRequest")
    _hx_fields = ["status", "contract", "product", "created", "vendor", "provider", "sourcing", "pendingRequest"]
    _hx_methods = ["put"]
    _hx_statics = ["list", "get"]
    _hx_interfaces = []
    _hx_super = connect_models_IdModel


    def __init__(self):
        self.pendingRequest = None
        self.sourcing = None
        self.provider = None
        self.vendor = None
        self.created = None
        self.product = None
        self.contract = None
        self.status = None
        super().__init__()
        _g = haxe_ds_StringMap()
        _g.h["created"] = "DateTime"
        _g.h["vendor"] = "Account"
        _g.h["provider"] = "Account"
        _g.h["sourcing"] = "ListingSourcing"
        _g.h["pendingRequest"] = "ListingRequest"
        self._setFieldClassNames(_g)

    def put(self):
        diff = self._toDiff()
        hasModifiedFields = (len(python_Boot.fields(diff)) > 1)
        if hasModifiedFields:
            listing = connect_Env.getMarketplaceApi().putListing(self.id,haxe_format_JsonPrinter.print(diff,None,None))
            return connect_models_Model.parse(connect_models_Listing,listing)
        else:
            return self

    @staticmethod
    def list(filters):
        listings = connect_Env.getMarketplaceApi().listListings(filters)
        return connect_models_Model.parseArray(connect_models_Listing,listings)

    @staticmethod
    def get(id):
        try:
            listing = connect_Env.getMarketplaceApi().getListing(id)
            return connect_models_Model.parse(connect_models_Listing,listing)
        except BaseException as _g:
            None
            return None

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.status = None
        _hx_o.contract = None
        _hx_o.product = None
        _hx_o.created = None
        _hx_o.vendor = None
        _hx_o.provider = None
        _hx_o.sourcing = None
        _hx_o.pendingRequest = None
connect_models_Listing._hx_class = connect_models_Listing
_hx_classes["connect.models.Listing"] = connect_models_Listing


class connect_models_ListingRequest(connect_models_IdModel):
    _hx_class_name = "connect.models.ListingRequest"
    __slots__ = ("type", "product", "state", "listing", "created", "updated")
    _hx_fields = ["type", "product", "state", "listing", "created", "updated"]
    _hx_methods = ["register", "assign", "unassign", "changeToDraft", "changeToDeploying", "changeToCompleted", "changeToCanceled", "changeToReviewing"]
    _hx_statics = ["list", "get"]
    _hx_interfaces = []
    _hx_super = connect_models_IdModel


    def __init__(self):
        self.updated = None
        self.created = None
        self.listing = None
        self.state = None
        self.product = None
        self.type = None
        super().__init__()
        _g = haxe_ds_StringMap()
        _g.h["created"] = "DateTime"
        _g.h["updated"] = "DateTime"
        self._setFieldClassNames(_g)

    def register(self):
        try:
            request = connect_Env.getMarketplaceApi().createListingRequest(self.toString())
            return connect_models_Model.parse(connect_models_ListingRequest,request)
        except BaseException as _g:
            None
            return None

    def assign(self):
        try:
            connect_Env.getMarketplaceApi().assignListingRequest(self.id)
            return True
        except BaseException as _g:
            None
            return False

    def unassign(self):
        try:
            connect_Env.getMarketplaceApi().unassignListingRequest(self.id)
            return True
        except BaseException as _g:
            None
            return False

    def changeToDraft(self):
        try:
            connect_Env.getMarketplaceApi().changeListingRequestToDraft(self.id)
            return True
        except BaseException as _g:
            None
            return False

    def changeToDeploying(self):
        try:
            connect_Env.getMarketplaceApi().changeListingRequestToDeploying(self.id)
            return True
        except BaseException as _g:
            None
            return False

    def changeToCompleted(self):
        try:
            connect_Env.getMarketplaceApi().changeListingRequestToCompleted(self.id)
            return True
        except BaseException as _g:
            None
            return False

    def changeToCanceled(self):
        try:
            connect_Env.getMarketplaceApi().changeListingRequestToCanceled(self.id)
            return True
        except BaseException as _g:
            None
            return False

    def changeToReviewing(self):
        try:
            connect_Env.getMarketplaceApi().changeListingRequestToReviewing(self.id)
            return True
        except BaseException as _g:
            None
            return False

    @staticmethod
    def list(filters):
        requests = connect_Env.getMarketplaceApi().listListingRequests(filters)
        return connect_models_Model.parseArray(connect_models_ListingRequest,requests)

    @staticmethod
    def get(id):
        try:
            request = connect_Env.getMarketplaceApi().getListingRequest(id)
            return connect_models_Model.parse(connect_models_ListingRequest,request)
        except BaseException as _g:
            None
            return None

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.type = None
        _hx_o.product = None
        _hx_o.state = None
        _hx_o.listing = None
        _hx_o.created = None
        _hx_o.updated = None
connect_models_ListingRequest._hx_class = connect_models_ListingRequest
_hx_classes["connect.models.ListingRequest"] = connect_models_ListingRequest


class connect_models_ListingSourcing(connect_models_Model):
    _hx_class_name = "connect.models.ListingSourcing"
    __slots__ = ("agreement", "published")
    _hx_fields = ["agreement", "published"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_Model


    def __init__(self):
        self.published = None
        self.agreement = None
        super().__init__()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.agreement = None
        _hx_o.published = None
connect_models_ListingSourcing._hx_class = connect_models_ListingSourcing
_hx_classes["connect.models.ListingSourcing"] = connect_models_ListingSourcing


class connect_models_Marketplace(connect_models_IdModel):
    _hx_class_name = "connect.models.Marketplace"
    __slots__ = ("name", "description", "activeContracts", "icon", "owner", "hubs", "zone", "countries", "sourcing", "currency")
    _hx_fields = ["name", "description", "activeContracts", "icon", "owner", "hubs", "zone", "countries", "sourcing", "currency"]
    _hx_methods = ["register", "update", "setIcon", "remove"]
    _hx_statics = ["list", "get"]
    _hx_interfaces = []
    _hx_super = connect_models_IdModel


    def __init__(self):
        self.currency = None
        self.sourcing = None
        self.countries = None
        self.zone = None
        self.hubs = None
        self.owner = None
        self.icon = None
        self.activeContracts = None
        self.description = None
        self.name = None
        super().__init__()
        _g = haxe_ds_StringMap()
        _g.h["owner"] = "Account"
        _g.h["hubs"] = "ExtIdHub"
        _g.h["countries"] = "Country"
        self._setFieldClassNames(_g)

    def register(self):
        try:
            request = connect_Env.getMarketplaceApi().createMarketplace(self.toString())
            return connect_models_Model.parse(connect_models_Marketplace,request)
        except BaseException as _g:
            None
            return None

    def update(self):
        try:
            diff = self._toDiff()
            hasModifiedFields = (len(python_Boot.fields(diff)) > 1)
            if hasModifiedFields:
                marketplace = connect_Env.getMarketplaceApi().updateMarketplace(self.id,haxe_format_JsonPrinter.print(diff,None,None))
                return connect_models_Model.parse(connect_models_Marketplace,marketplace)
            else:
                return self
        except BaseException as _g:
            None
            return None

    def setIcon(self,icon):
        try:
            connect_Env.getMarketplaceApi().setMarketplaceIcon(self.id,icon)
            return True
        except BaseException as _g:
            None
            return False

    def remove(self):
        try:
            connect_Env.getMarketplaceApi().deleteMarketplace(self.id)
            return True
        except BaseException as _g:
            None
            return False

    @staticmethod
    def list(filters):
        marketplaces = connect_Env.getMarketplaceApi().listMarketplaces(filters)
        return connect_models_Model.parseArray(connect_models_Marketplace,marketplaces)

    @staticmethod
    def get(id):
        try:
            marketplace = connect_Env.getMarketplaceApi().getMarketplace(id)
            return connect_models_Model.parse(connect_models_Marketplace,marketplace)
        except BaseException as _g:
            None
            return None

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.name = None
        _hx_o.description = None
        _hx_o.activeContracts = None
        _hx_o.icon = None
        _hx_o.owner = None
        _hx_o.hubs = None
        _hx_o.zone = None
        _hx_o.countries = None
        _hx_o.sourcing = None
        _hx_o.currency = None
connect_models_Marketplace._hx_class = connect_models_Marketplace
_hx_classes["connect.models.Marketplace"] = connect_models_Marketplace


class connect_models_Media(connect_models_IdModel):
    _hx_class_name = "connect.models.Media"
    __slots__ = ("position", "type", "thumbnail", "url")
    _hx_fields = ["position", "type", "thumbnail", "url"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_IdModel


    def __init__(self):
        self.url = None
        self.thumbnail = None
        self.type = None
        self.position = None
        super().__init__()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.position = None
        _hx_o.type = None
        _hx_o.thumbnail = None
        _hx_o.url = None
connect_models_Media._hx_class = connect_models_Media
_hx_classes["connect.models.Media"] = connect_models_Media


class connect_models_Message(connect_models_IdModel):
    _hx_class_name = "connect.models.Message"
    __slots__ = ("conversation", "created", "creator", "text")
    _hx_fields = ["conversation", "created", "creator", "text"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_IdModel


    def __init__(self):
        self.text = None
        self.creator = None
        self.created = None
        self.conversation = None
        super().__init__()
        _g = haxe_ds_StringMap()
        _g.h["created"] = "DateTime"
        _g.h["creator"] = "User"
        self._setFieldClassNames(_g)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.conversation = None
        _hx_o.created = None
        _hx_o.creator = None
        _hx_o.text = None
connect_models_Message._hx_class = connect_models_Message
_hx_classes["connect.models.Message"] = connect_models_Message


class connect_models_Param(connect_models_IdModel):
    _hx_class_name = "connect.models.Param"
    __slots__ = ("name", "title", "description", "type", "hint", "placeholder", "value", "valueError", "valueChoice", "constraints", "shared", "valueChoices", "events", "structuredValue", "scope", "phase", "marketplace")
    _hx_fields = ["name", "title", "description", "type", "hint", "placeholder", "value", "valueError", "valueChoice", "constraints", "shared", "valueChoices", "events", "structuredValue", "scope", "phase", "marketplace"]
    _hx_methods = ["isCheckboxChecked"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_IdModel


    def __init__(self):
        self.marketplace = None
        self.phase = None
        self.scope = None
        self.structuredValue = None
        self.events = None
        self.valueChoices = None
        self.shared = None
        self.constraints = None
        self.valueChoice = None
        self.valueError = None
        self.value = None
        self.placeholder = None
        self.hint = None
        self.type = None
        self.description = None
        self.title = None
        self.name = None
        super().__init__()
        _g = haxe_ds_StringMap()
        _g.h["valueChoice"] = "String"
        _g.h["valueChoices"] = "Choice"
        _g.h["structuredValue"] = "Dictionary"
        self._setFieldClassNames(_g)

    def isCheckboxChecked(self,fieldName):
        if ((self.type == "checkbox") and ((self.structuredValue is not None))):
            return self.structuredValue.getBool(fieldName)
        else:
            return False

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.name = None
        _hx_o.title = None
        _hx_o.description = None
        _hx_o.type = None
        _hx_o.hint = None
        _hx_o.placeholder = None
        _hx_o.value = None
        _hx_o.valueError = None
        _hx_o.valueChoice = None
        _hx_o.constraints = None
        _hx_o.shared = None
        _hx_o.valueChoices = None
        _hx_o.events = None
        _hx_o.structuredValue = None
        _hx_o.scope = None
        _hx_o.phase = None
        _hx_o.marketplace = None
connect_models_Param._hx_class = connect_models_Param
_hx_classes["connect.models.Param"] = connect_models_Param


class connect_models_Period(connect_models_Model):
    _hx_class_name = "connect.models.Period"
    __slots__ = ("_hx_from", "to", "delta", "uom")
    _hx_fields = ["from", "to", "delta", "uom"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_Model


    def __init__(self):
        self.uom = None
        self.delta = None
        self.to = None
        self._hx_from = None
        super().__init__()
        _g = haxe_ds_StringMap()
        _g.h["from"] = "DateTime"
        _g.h["to"] = "DateTime"
        self._setFieldClassNames(_g)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o._hx_from = None
        _hx_o.to = None
        _hx_o.delta = None
        _hx_o.uom = None
connect_models_Period._hx_class = connect_models_Period
_hx_classes["connect.models.Period"] = connect_models_Period


class connect_models_PhoneNumber(connect_models_Model):
    _hx_class_name = "connect.models.PhoneNumber"
    __slots__ = ("countryCode", "areaCode", "phoneNumber", "extension")
    _hx_fields = ["countryCode", "areaCode", "phoneNumber", "extension"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_Model


    def __init__(self):
        self.extension = None
        self.phoneNumber = None
        self.areaCode = None
        self.countryCode = None
        super().__init__()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.countryCode = None
        _hx_o.areaCode = None
        _hx_o.phoneNumber = None
        _hx_o.extension = None
connect_models_PhoneNumber._hx_class = connect_models_PhoneNumber
_hx_classes["connect.models.PhoneNumber"] = connect_models_PhoneNumber


class connect_models_Product(connect_models_IdModel):
    _hx_class_name = "connect.models.Product"
    __slots__ = ("name", "icon", "shortDescription", "detailedDescription", "version", "publishedAt", "configurations", "customerUiSettings", "category", "owner", "latest", "stats", "status")
    _hx_fields = ["name", "icon", "shortDescription", "detailedDescription", "version", "publishedAt", "configurations", "customerUiSettings", "category", "owner", "latest", "stats", "status"]
    _hx_methods = ["listActions", "getAction", "getActionLink", "getConnections", "listItems", "getItems", "listParameters", "getParameter", "createParameter", "updateParameter", "deleteParameter", "getTemplates", "getVersions", "getVersion", "getVersionActions", "getVersionAction", "getVersionActionLink", "getVersionItems", "getVersionParameters", "getVersionTemplates", "listConfigurations", "setConfigurationParam", "listAgreements", "listMedia", "createMedia", "getMedia", "updateMedia", "deleteMedia"]
    _hx_statics = ["list", "get"]
    _hx_interfaces = []
    _hx_super = connect_models_IdModel


    def __init__(self):
        self.status = None
        self.stats = None
        self.latest = None
        self.owner = None
        self.category = None
        self.customerUiSettings = None
        self.configurations = None
        self.publishedAt = None
        self.version = None
        self.detailedDescription = None
        self.shortDescription = None
        self.icon = None
        self.name = None
        super().__init__()
        _g = haxe_ds_StringMap()
        _g.h["publishedAt"] = "DateTime"
        _g.h["owner"] = "Account"
        _g.h["stats"] = "ProductStats"
        self._setFieldClassNames(_g)

    def listActions(self,filters):
        try:
            actions = connect_Env.getGeneralApi().listProductActions(self.id,filters)
            return connect_models_Model.parseArray(connect_models_Action,actions)
        except BaseException as _g:
            None
            return connect_util_Collection()

    def getAction(self,actionId):
        try:
            action = connect_Env.getGeneralApi().getProductAction(self.id,actionId)
            return connect_models_Model.parse(connect_models_Action,action)
        except BaseException as _g:
            None
            return None

    def getActionLink(self,actionId):
        try:
            return connect_Env.getGeneralApi().getProductActionLink(self.id,actionId)
        except BaseException as _g:
            None
            return ""

    def getConnections(self):
        try:
            connections = connect_Env.getGeneralApi().getProductConnections(self.id)
            return connect_models_Model.parseArray(connect_models_Connection,connections)
        except BaseException as _g:
            None
            return connect_util_Collection()

    def listItems(self,filters):
        try:
            items = connect_Env.getGeneralApi().listProductItems(self.id,filters)
            return connect_models_Model.parseArray(connect_models_Item,items)
        except BaseException as _g:
            None
            return connect_util_Collection()

    def getItems(self):
        return self.listItems(None)

    def listParameters(self,filters):
        try:
            params = connect_Env.getGeneralApi().listProductParameters(self.id,filters)
            return connect_models_Model.parseArray(connect_models_Param,params)
        except BaseException as _g:
            None
            return connect_util_Collection()

    def getParameter(self,paramId):
        try:
            param = connect_Env.getGeneralApi().getProductParameter(self.id,paramId)
            return connect_models_Model.parse(connect_models_Param,param)
        except BaseException as _g:
            None
            return None

    def createParameter(self,param):
        try:
            param1 = connect_Env.getGeneralApi().createProductParameter(self.id,param.toString())
            return connect_models_Model.parse(connect_models_Param,param1)
        except BaseException as _g:
            None
            return None

    def updateParameter(self,param):
        try:
            param1 = connect_Env.getGeneralApi().updateProductParameter(self.id,param.id,param.toString())
            return connect_models_Model.parse(connect_models_Param,param1)
        except BaseException as _g:
            None
            return None

    def deleteParameter(self,paramId):
        try:
            connect_Env.getGeneralApi().deleteProductParameter(self.id,paramId)
            return True
        except BaseException as _g:
            None
            return False

    def getTemplates(self):
        try:
            templates = connect_Env.getGeneralApi().getProductTemplates(self.id)
            return connect_models_Model.parseArray(connect_models_Template,templates)
        except BaseException as _g:
            None
            return connect_util_Collection()

    def getVersions(self):
        try:
            versions = connect_Env.getGeneralApi().getProductVersions(self.id)
            return connect_models_Model.parseArray(connect_models_Product,versions)
        except BaseException as _g:
            None
            return connect_util_Collection()

    def getVersion(self,version):
        try:
            version1 = connect_Env.getGeneralApi().getProductVersion(self.id,version)
            return connect_models_Model.parse(connect_models_Product,version1)
        except BaseException as _g:
            None
            return None

    def getVersionActions(self,version):
        try:
            actions = connect_Env.getGeneralApi().getProductVersionActions(self.id,version)
            return connect_models_Model.parseArray(connect_models_Action,actions)
        except BaseException as _g:
            None
            return connect_util_Collection()

    def getVersionAction(self,version,actionId):
        try:
            action = connect_Env.getGeneralApi().getProductVersionAction(self.id,version,actionId)
            return connect_models_Model.parse(connect_models_Action,action)
        except BaseException as _g:
            None
            return None

    def getVersionActionLink(self,version,actionId):
        try:
            return connect_Env.getGeneralApi().getProductVersionActionLink(self.id,version,actionId)
        except BaseException as _g:
            None
            return ""

    def getVersionItems(self,version):
        try:
            items = connect_Env.getGeneralApi().getProductVersionItems(self.id,version)
            return connect_models_Model.parseArray(connect_models_Item,items)
        except BaseException as _g:
            None
            return connect_util_Collection()

    def getVersionParameters(self,version):
        try:
            params = connect_Env.getGeneralApi().getProductVersionParameters(self.id,version)
            return connect_models_Model.parseArray(connect_models_Param,params)
        except BaseException as _g:
            None
            return connect_util_Collection()

    def getVersionTemplates(self,version):
        try:
            templates = connect_Env.getGeneralApi().getProductVersionTemplates(self.id,version)
            return connect_models_Model.parseArray(connect_models_Template,templates)
        except BaseException as _g:
            None
            return connect_util_Collection()

    def listConfigurations(self,filters):
        try:
            templates = connect_Env.getGeneralApi().listProductConfigurations(self.id,filters)
            return connect_models_Model.parseArray(connect_models_ProductConfigurationParam,templates)
        except BaseException as _g:
            None
            return connect_util_Collection()

    def setConfigurationParam(self,param):
        try:
            param1 = connect_Env.getGeneralApi().setProductConfigurationParam(self.id,param.toString())
            return connect_models_Model.parse(connect_models_ProductConfigurationParam,param1)
        except BaseException as _g:
            None
            return None

    def listAgreements(self,filters):
        try:
            agreements = connect_Env.getGeneralApi().listProductAgreements(self.id,filters)
            return connect_models_Model.parseArray(connect_models_Agreement,agreements)
        except BaseException as _g:
            None
            return connect_util_Collection()

    def listMedia(self,filters):
        try:
            media = connect_Env.getGeneralApi().listProductMedia(self.id,filters)
            return connect_models_Model.parseArray(connect_models_Media,media)
        except BaseException as _g:
            None
            return connect_util_Collection()

    def createMedia(self):
        try:
            media = connect_Env.getGeneralApi().createProductMedia(self.id)
            return connect_models_Model.parse(connect_models_Media,media)
        except BaseException as _g:
            None
            return None

    def getMedia(self,mediaId):
        try:
            media = connect_Env.getGeneralApi().getProductMedia(self.id,mediaId)
            return connect_models_Model.parse(connect_models_Media,media)
        except BaseException as _g:
            None
            return None

    def updateMedia(self,media):
        try:
            updated = connect_Env.getGeneralApi().updateProductMedia(self.id,media.id,media.toString())
            return connect_models_Model.parse(connect_models_Media,updated)
        except BaseException as _g:
            None
            return None

    def deleteMedia(self,mediaId):
        try:
            media = connect_Env.getGeneralApi().deleteProductMedia(self.id,mediaId)
            return connect_models_Model.parse(connect_models_Media,media)
        except BaseException as _g:
            None
            return None

    @staticmethod
    def list(filters):
        products = connect_Env.getGeneralApi().listProducts(filters)
        return connect_models_Model.parseArray(connect_models_Product,products)

    @staticmethod
    def get(id):
        try:
            product = connect_Env.getGeneralApi().getProduct(id)
            return connect_models_Model.parse(connect_models_Product,product)
        except BaseException as _g:
            None
            return None

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.name = None
        _hx_o.icon = None
        _hx_o.shortDescription = None
        _hx_o.detailedDescription = None
        _hx_o.version = None
        _hx_o.publishedAt = None
        _hx_o.configurations = None
        _hx_o.customerUiSettings = None
        _hx_o.category = None
        _hx_o.owner = None
        _hx_o.latest = None
        _hx_o.stats = None
        _hx_o.status = None
connect_models_Product._hx_class = connect_models_Product
_hx_classes["connect.models.Product"] = connect_models_Product


class connect_models_ProductConfigurationParam(connect_models_Model):
    _hx_class_name = "connect.models.ProductConfigurationParam"
    __slots__ = ("value", "parameter", "marketplace", "item", "events", "constraints")
    _hx_fields = ["value", "parameter", "marketplace", "item", "events", "constraints"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_Model


    def __init__(self):
        self.constraints = None
        self.events = None
        self.item = None
        self.marketplace = None
        self.parameter = None
        self.value = None
        super().__init__()
        _g = haxe_ds_StringMap()
        _g.h["parameter"] = "Param"
        self._setFieldClassNames(_g)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.value = None
        _hx_o.parameter = None
        _hx_o.marketplace = None
        _hx_o.item = None
        _hx_o.events = None
        _hx_o.constraints = None
connect_models_ProductConfigurationParam._hx_class = connect_models_ProductConfigurationParam
_hx_classes["connect.models.ProductConfigurationParam"] = connect_models_ProductConfigurationParam


class connect_models_ProductStats(connect_models_Model):
    _hx_class_name = "connect.models.ProductStats"
    __slots__ = ("listings", "agreements", "contracts")
    _hx_fields = ["listings", "agreements", "contracts"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_Model


    def __init__(self):
        self.contracts = None
        self.agreements = None
        self.listings = None
        super().__init__()
        _g = haxe_ds_StringMap()
        _g.h["agreements"] = "ProductStatsInfo"
        _g.h["contracts"] = "ProductStatsInfo"
        self._setFieldClassNames(_g)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.listings = None
        _hx_o.agreements = None
        _hx_o.contracts = None
connect_models_ProductStats._hx_class = connect_models_ProductStats
_hx_classes["connect.models.ProductStats"] = connect_models_ProductStats


class connect_models_ProductStatsInfo(connect_models_Model):
    _hx_class_name = "connect.models.ProductStatsInfo"
    __slots__ = ("distribution", "sourcing")
    _hx_fields = ["distribution", "sourcing"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_Model


    def __init__(self):
        self.sourcing = None
        self.distribution = None
        super().__init__()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.distribution = None
        _hx_o.sourcing = None
connect_models_ProductStatsInfo._hx_class = connect_models_ProductStatsInfo
_hx_classes["connect.models.ProductStatsInfo"] = connect_models_ProductStatsInfo


class connect_models_Renewal(connect_models_Model):
    _hx_class_name = "connect.models.Renewal"
    __slots__ = ("_hx_from", "to", "periodDelta", "periodUom")
    _hx_fields = ["from", "to", "periodDelta", "periodUom"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_Model


    def __init__(self):
        self.periodUom = None
        self.periodDelta = None
        self.to = None
        self._hx_from = None
        super().__init__()
        _g = haxe_ds_StringMap()
        _g.h["from"] = "DateTime"
        _g.h["to"] = "DateTime"
        self._setFieldClassNames(_g)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o._hx_from = None
        _hx_o.to = None
        _hx_o.periodDelta = None
        _hx_o.periodUom = None
connect_models_Renewal._hx_class = connect_models_Renewal
_hx_classes["connect.models.Renewal"] = connect_models_Renewal


class connect_models_Subscription(connect_models_IdModel):
    _hx_class_name = "connect.models.Subscription"
    __slots__ = ("status", "events", "externalId", "externalUid", "product", "connection", "params", "tiers", "marketplace", "contract", "items", "billing")
    _hx_fields = ["status", "events", "externalId", "externalUid", "product", "connection", "params", "tiers", "marketplace", "contract", "items", "billing"]
    _hx_methods = []
    _hx_statics = ["list", "get"]
    _hx_interfaces = []
    _hx_super = connect_models_IdModel


    def __init__(self):
        self.billing = None
        self.items = None
        self.contract = None
        self.marketplace = None
        self.tiers = None
        self.params = None
        self.connection = None
        self.product = None
        self.externalUid = None
        self.externalId = None
        self.events = None
        self.status = None
        super().__init__()
        _g = haxe_ds_StringMap()
        _g.h["billing"] = "BillingInfo"
        self._setFieldClassNames(_g)

    @staticmethod
    def list(filters):
        subscriptions = connect_Env.getSubscriptionsApi().listRecurringAssets(filters)
        return connect_models_Model.parseArray(connect_models_Subscription,subscriptions)

    @staticmethod
    def get(id):
        try:
            subscription = connect_Env.getSubscriptionsApi().getRecurringAsset(id)
            return connect_models_Model.parse(connect_models_Subscription,subscription)
        except BaseException as _g:
            None
            return None

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.status = None
        _hx_o.events = None
        _hx_o.externalId = None
        _hx_o.externalUid = None
        _hx_o.product = None
        _hx_o.connection = None
        _hx_o.params = None
        _hx_o.tiers = None
        _hx_o.marketplace = None
        _hx_o.contract = None
        _hx_o.items = None
        _hx_o.billing = None
connect_models_Subscription._hx_class = connect_models_Subscription
_hx_classes["connect.models.Subscription"] = connect_models_Subscription


class connect_models_SubscriptionRequest(connect_models_IdModel):
    _hx_class_name = "connect.models.SubscriptionRequest"
    __slots__ = ("type", "events", "asset", "items", "attributes", "period")
    _hx_fields = ["type", "events", "asset", "items", "attributes", "period"]
    _hx_methods = ["register", "updateAttributes"]
    _hx_statics = ["list", "get"]
    _hx_interfaces = []
    _hx_super = connect_models_IdModel


    def __init__(self):
        self.period = None
        self.attributes = None
        self.items = None
        self.asset = None
        self.events = None
        self.type = None
        super().__init__()
        _g = haxe_ds_StringMap()
        _g.h["asset"] = "Subscription"
        _g.h["attributes"] = "SubscriptionRequestAttributes"
        self._setFieldClassNames(_g)

    def register(self):
        try:
            request = connect_Env.getSubscriptionsApi().createBillingRequest(self.toString(),self)
            return connect_models_Model.parse(connect_models_SubscriptionRequest,request)
        except BaseException as _g:
            None
            return None

    def updateAttributes(self):
        try:
            data = ((("{\"provider\": " + HxOverrides.stringOrNull(self.attributes.provider.toString())) + "}") if ((((self.type == "provider") and ((self.attributes is not None))) and ((self.attributes.provider is not None)))) else ((("{\"vendor\": " + HxOverrides.stringOrNull(self.attributes.vendor.toString())) + "}") if ((((self.type == "vendor") and ((self.attributes is not None))) and ((self.attributes.vendor is not None)))) else None))
            attr = (connect_Env.getSubscriptionsApi().updateBillingRequestAttributes(self.id,data) if ((data is not None)) else None)
            if (attr is not None):
                self.attributes = connect_models_Model.parse(connect_models_SubscriptionRequestAttributes,attr)
                return True
            else:
                return False
        except BaseException as _g:
            None
            return False

    @staticmethod
    def list(filters):
        requests = connect_Env.getSubscriptionsApi().listBillingRequests(filters)
        return connect_models_Model.parseArray(connect_models_SubscriptionRequest,requests)

    @staticmethod
    def get(id):
        try:
            request = connect_Env.getSubscriptionsApi().getBillingRequest(id)
            return connect_models_Model.parse(connect_models_SubscriptionRequest,request)
        except BaseException as _g:
            None
            return None

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.type = None
        _hx_o.events = None
        _hx_o.asset = None
        _hx_o.items = None
        _hx_o.attributes = None
        _hx_o.period = None
connect_models_SubscriptionRequest._hx_class = connect_models_SubscriptionRequest
_hx_classes["connect.models.SubscriptionRequest"] = connect_models_SubscriptionRequest


class connect_models_SubscriptionRequestAttributes(connect_models_Model):
    _hx_class_name = "connect.models.SubscriptionRequestAttributes"
    __slots__ = ("vendor", "provider")
    _hx_fields = ["vendor", "provider"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_Model


    def __init__(self):
        self.provider = None
        self.vendor = None
        super().__init__()
        _g = haxe_ds_StringMap()
        _g.h["vendor"] = "Dictionary"
        _g.h["provider"] = "Dictionary"
        self._setFieldClassNames(_g)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.vendor = None
        _hx_o.provider = None
connect_models_SubscriptionRequestAttributes._hx_class = connect_models_SubscriptionRequestAttributes
_hx_classes["connect.models.SubscriptionRequestAttributes"] = connect_models_SubscriptionRequestAttributes


class connect_models_Template(connect_models_IdModel):
    _hx_class_name = "connect.models.Template"
    __slots__ = ("title", "body")
    _hx_fields = ["title", "body"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_IdModel


    def __init__(self):
        self.body = None
        self.title = None
        super().__init__()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.title = None
        _hx_o.body = None
connect_models_Template._hx_class = connect_models_Template
_hx_classes["connect.models.Template"] = connect_models_Template


class connect_models_TierAccount(connect_models_IdModel):
    _hx_class_name = "connect.models.TierAccount"
    __slots__ = ("externalId", "name", "environment", "scopes", "contactInfo", "marketplace", "hub", "externalUid", "taxId")
    _hx_fields = ["externalId", "name", "environment", "scopes", "contactInfo", "marketplace", "hub", "externalUid", "taxId"]
    _hx_methods = ["getTierConfig"]
    _hx_statics = ["list", "get"]
    _hx_interfaces = []
    _hx_super = connect_models_IdModel


    def __init__(self):
        self.taxId = None
        self.externalUid = None
        self.hub = None
        self.marketplace = None
        self.contactInfo = None
        self.scopes = None
        self.environment = None
        self.name = None
        self.externalId = None
        super().__init__()

    def getTierConfig(self,productId,tierLevel):
        configs = connect_models_TierConfig.list(connect_api_Query().equal("account.id",self.id).equal("product.id",productId).equal("tier_level",Std.string(tierLevel)))
        if (configs.length() > 0):
            return configs.get(0)
        else:
            return None

    @staticmethod
    def list(filters):
        accounts = connect_Env.getTierApi().listTierAccounts(filters)
        return connect_models_Model.parseArray(connect_models_TierAccount,accounts)

    @staticmethod
    def get(id):
        try:
            account = connect_Env.getTierApi().getTierAccount(id)
            return connect_models_Model.parse(connect_models_TierAccount,account)
        except BaseException as _g:
            None
            return None

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.externalId = None
        _hx_o.name = None
        _hx_o.environment = None
        _hx_o.scopes = None
        _hx_o.contactInfo = None
        _hx_o.marketplace = None
        _hx_o.hub = None
        _hx_o.externalUid = None
        _hx_o.taxId = None
connect_models_TierAccount._hx_class = connect_models_TierAccount
_hx_classes["connect.models.TierAccount"] = connect_models_TierAccount


class connect_models_TierConfig(connect_models_IdModel):
    _hx_class_name = "connect.models.TierConfig"
    __slots__ = ("name", "account", "product", "tierLevel", "params", "connection", "openRequest", "template", "contract", "marketplace", "configuration", "events", "tiers", "status")
    _hx_fields = ["name", "account", "product", "tierLevel", "params", "connection", "openRequest", "template", "contract", "marketplace", "configuration", "events", "tiers", "status"]
    _hx_methods = ["getParamById"]
    _hx_statics = ["list", "get"]
    _hx_interfaces = []
    _hx_super = connect_models_IdModel


    def __init__(self):
        self.status = None
        self.tiers = None
        self.events = None
        self.configuration = None
        self.marketplace = None
        self.contract = None
        self.template = None
        self.openRequest = None
        self.connection = None
        self.params = None
        self.tierLevel = None
        self.product = None
        self.account = None
        self.name = None
        super().__init__()
        _g = haxe_ds_StringMap()
        _g.h["account"] = "TierAccount"
        _g.h["openRequest"] = "TierConfigRequest"
        self._setFieldClassNames(_g)

    def getParamById(self,paramId):
        def _hx_local_0(param):
            return (param.id == paramId)
        params = list(filter(_hx_local_0,self.params.toArray()))
        if (len(params) > 0):
            return (params[0] if 0 < len(params) else None)
        else:
            return None

    @staticmethod
    def list(filters):
        configs = connect_Env.getTierApi().listTierConfigs(filters)
        return connect_models_Model.parseArray(connect_models_TierConfig,configs)

    @staticmethod
    def get(id):
        try:
            account = connect_Env.getTierApi().getTierConfig(id)
            return connect_models_Model.parse(connect_models_TierConfig,account)
        except BaseException as _g:
            None
            return None

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.name = None
        _hx_o.account = None
        _hx_o.product = None
        _hx_o.tierLevel = None
        _hx_o.params = None
        _hx_o.connection = None
        _hx_o.openRequest = None
        _hx_o.template = None
        _hx_o.contract = None
        _hx_o.marketplace = None
        _hx_o.configuration = None
        _hx_o.events = None
        _hx_o.tiers = None
        _hx_o.status = None
connect_models_TierConfig._hx_class = connect_models_TierConfig
_hx_classes["connect.models.TierConfig"] = connect_models_TierConfig


class connect_models_TierConfigRequest(connect_models_IdModel):
    _hx_class_name = "connect.models.TierConfigRequest"
    __slots__ = ("type", "status", "configuration", "parentConfiguration", "account", "product", "tierLevel", "params", "environment", "assignee", "template", "reason", "activation", "notes", "events", "tiers", "marketplace", "contract")
    _hx_fields = ["type", "status", "configuration", "parentConfiguration", "account", "product", "tierLevel", "params", "environment", "assignee", "template", "reason", "activation", "notes", "events", "tiers", "marketplace", "contract"]
    _hx_methods = ["register", "update", "getModifiedTcrParams", "prepareUpdateBody", "approveByTemplate", "fail", "inquire", "pend", "assign", "unassign", "getParamById"]
    _hx_statics = ["list", "get", "isParamInList"]
    _hx_interfaces = []
    _hx_super = connect_models_IdModel


    def __init__(self):
        self.contract = None
        self.marketplace = None
        self.tiers = None
        self.events = None
        self.notes = None
        self.activation = None
        self.reason = None
        self.template = None
        self.assignee = None
        self.environment = None
        self.params = None
        self.tierLevel = None
        self.product = None
        self.account = None
        self.parentConfiguration = None
        self.configuration = None
        self.status = None
        self.type = None
        super().__init__()
        _g = haxe_ds_StringMap()
        _g.h["configuration"] = "TierConfig"
        _g.h["parentConfiguration"] = "TierConfig"
        _g.h["account"] = "TierAccount"
        _g.h["assignee"] = "User"
        self._setFieldClassNames(_g)

    def register(self):
        try:
            request = connect_Env.getTierApi().createTierConfigRequest(self.toString())
            return connect_models_Model.parse(connect_models_TierConfigRequest,request)
        except BaseException as _g:
            None
            return None

    def update(self,params):
        try:
            if (params is None):
                modifiedParams = self.getModifiedTcrParams()
                if (modifiedParams is not None):
                    return self.update(modifiedParams)
                else:
                    diff = self._toDiff()
                    hasModifiedFields = (len(python_Boot.fields(diff)) > 1)
                    if hasModifiedFields:
                        request = connect_Env.getTierApi().updateTierConfigRequest(self.id,self.prepareUpdateBody(diff))
                        return connect_models_Model.parse(connect_models_TierConfigRequest,request)
                    else:
                        return self
            else:
                if (params.length() > 0):
                    connect_Env.getTierApi().updateTierConfigRequest(self.id,(("{\"params\":" + HxOverrides.stringOrNull(params.toString())) + "}"))
                return self
        except BaseException as _g:
            None
            return None

    def getModifiedTcrParams(self):
        oldTcr = connect_models_Model.parse(connect_models_TierConfigRequest,self._footprint)
        if ((oldTcr.params is not None) and ((self.params.length() != oldTcr.params.length()))):
            def _hx_local_0(p):
                return p.toString()
            oldParamsAsString = list(map(_hx_local_0,oldTcr.params.toArray()))
            result = connect_util_Collection()
            _g = 0
            _g1 = self.params.toArray()
            while (_g < len(_g1)):
                param = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                _g = (_g + 1)
                if (python_internal_ArrayImpl.indexOf(oldParamsAsString,param.toString(),None) == -1):
                    result.push(param)
            return result
        else:
            return None

    def prepareUpdateBody(self,diff):
        _gthis = self
        hasConfiguration = python_Boot.hasField(diff,"configuration")
        hasTcrParams = python_Boot.hasField(diff,"params")
        hasTcParams = (hasConfiguration and python_Boot.hasField(Reflect.field(diff,"configuration"),"params"))
        hasConfigParams = ((hasConfiguration and python_Boot.hasField(Reflect.field(diff,"configuration"),"configuration")) and python_Boot.hasField(Reflect.field(Reflect.field(diff,"configuration"),"configuration"),"params"))
        if (((hasTcParams or hasConfigParams)) and (not hasTcrParams)):
            Reflect.setField(diff,"params",[])
        if hasTcParams:
            def _hx_local_0(p):
                return (not connect_models_TierConfigRequest.isParamInList(p,Reflect.field(diff,"params")))
            tcParams = Lambda.filter(Reflect.field(Reflect.field(diff,"configuration"),"params"),_hx_local_0)
            Reflect.setField(diff,"params",Reflect.field(Reflect.field(diff,"params"),"concat")(tcParams))
        if hasConfigParams:
            def _hx_local_1(p):
                return (not connect_models_TierConfigRequest.isParamInList(p,Reflect.field(diff,"params")))
            configParams = Lambda.filter(Reflect.field(Reflect.field(Reflect.field(diff,"configuration"),"configuration"),"params"),_hx_local_1)
            Reflect.setField(diff,"params",Reflect.field(Reflect.field(diff,"params"),"concat")(configParams))
        if hasConfiguration:
            Reflect.deleteField(diff,"configuration")
        if ((hasTcrParams or hasTcParams) or hasConfigParams):
            def _hx_local_2(p):
                if (not python_Boot.hasField(p,"value")):
                    id = Reflect.field(p,"id")
                    tcrValue = (_gthis.getParamById(id).value if ((hasTcrParams and ((_gthis.getParamById(id) is not None)))) else None)
                    tcValue = (_gthis.configuration.getParamById(id).value if ((((tcrValue is None) and hasTcParams) and ((_gthis.configuration.getParamById(id) is not None)))) else tcrValue)
                    value = (_gthis.configuration.configuration.getParamById(id).value if ((((tcValue is None) and hasConfigParams) and ((_gthis.configuration.configuration.getParamById(id) is not None)))) else tcValue)
                    setattr(p,(("_hx_" + "value") if (("value" in python_Boot.keywords)) else (("_hx_" + "value") if (((((len("value") > 2) and ((ord("value"[0]) == 95))) and ((ord("value"[1]) == 95))) and ((ord("value"[(len("value") - 1)]) != 95)))) else "value")),value)
            Lambda.iter(Reflect.field(diff,"params"),_hx_local_2)
        return haxe_format_JsonPrinter.print(diff,None,None)

    def approveByTemplate(self,id):
        try:
            connect_Env.getTierApi().approveTierConfigRequest(self.id,haxe_format_JsonPrinter.print(_hx_AnonObject({'template': _hx_AnonObject({'id': id})}),None,None))
            return True
        except BaseException as _g:
            None
            return False

    def fail(self,reason):
        try:
            connect_Env.getTierApi().failTierConfigRequest(self.id,haxe_format_JsonPrinter.print(_hx_AnonObject({'reason': reason}),None,None))
            return True
        except BaseException as _g:
            None
            return False

    def inquire(self):
        try:
            connect_Env.getTierApi().inquireTierConfigRequest(self.id)
            return True
        except BaseException as _g:
            None
            return False

    def pend(self):
        try:
            connect_Env.getTierApi().pendTierConfigRequest(self.id)
            return True
        except BaseException as _g:
            None
            return False

    def assign(self):
        try:
            connect_Env.getTierApi().assignTierConfigRequest(self.id)
            return True
        except BaseException as _g:
            None
            return False

    def unassign(self):
        try:
            connect_Env.getTierApi().unassignTierConfigRequest(self.id)
            return True
        except BaseException as _g:
            None
            return False

    def getParamById(self,paramId):
        def _hx_local_0(param):
            return (param.id == paramId)
        params = list(filter(_hx_local_0,self.params.toArray()))
        if (len(params) > 0):
            return (params[0] if 0 < len(params) else None)
        else:
            return None

    @staticmethod
    def list(filters):
        requests = connect_Env.getTierApi().listTierConfigRequests(filters)
        return connect_models_Model.parseArray(connect_models_TierConfigRequest,requests)

    @staticmethod
    def get(id):
        try:
            request = connect_Env.getTierApi().getTierConfigRequest(id)
            return connect_models_Model.parse(connect_models_TierConfigRequest,request)
        except BaseException as _g:
            None
            return None

    @staticmethod
    def isParamInList(param,_hx_list):
        _g = 0
        while (_g < len(_hx_list)):
            p = (_hx_list[_g] if _g >= 0 and _g < len(_hx_list) else None)
            _g = (_g + 1)
            if HxOverrides.eq(Reflect.field(p,"id"),Reflect.field(param,"id")):
                return True
        return False

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.type = None
        _hx_o.status = None
        _hx_o.configuration = None
        _hx_o.parentConfiguration = None
        _hx_o.account = None
        _hx_o.product = None
        _hx_o.tierLevel = None
        _hx_o.params = None
        _hx_o.environment = None
        _hx_o.assignee = None
        _hx_o.template = None
        _hx_o.reason = None
        _hx_o.activation = None
        _hx_o.notes = None
        _hx_o.events = None
        _hx_o.tiers = None
        _hx_o.marketplace = None
        _hx_o.contract = None
connect_models_TierConfigRequest._hx_class = connect_models_TierConfigRequest
_hx_classes["connect.models.TierConfigRequest"] = connect_models_TierConfigRequest


class connect_models_Tiers(connect_models_Model):
    _hx_class_name = "connect.models.Tiers"
    __slots__ = ("customer", "tier1", "tier2")
    _hx_fields = ["customer", "tier1", "tier2"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_Model


    def __init__(self):
        self.tier2 = None
        self.tier1 = None
        self.customer = None
        super().__init__()
        _g = haxe_ds_StringMap()
        _g.h["customer"] = "TierAccount"
        _g.h["tier1"] = "TierAccount"
        _g.h["tier2"] = "TierAccount"
        self._setFieldClassNames(_g)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.customer = None
        _hx_o.tier1 = None
        _hx_o.tier2 = None
connect_models_Tiers._hx_class = connect_models_Tiers
_hx_classes["connect.models.Tiers"] = connect_models_Tiers


class connect_models_UsageCategory(connect_models_IdModel):
    _hx_class_name = "connect.models.UsageCategory"
    __slots__ = ("name", "description")
    _hx_fields = ["name", "description"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_IdModel


    def __init__(self):
        self.description = None
        self.name = None
        super().__init__()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.name = None
        _hx_o.description = None
connect_models_UsageCategory._hx_class = connect_models_UsageCategory
_hx_classes["connect.models.UsageCategory"] = connect_models_UsageCategory


class connect_models_UsageFile(connect_models_IdModel):
    _hx_class_name = "connect.models.UsageFile"
    __slots__ = ("name", "description", "note", "status", "period", "currency", "schema", "usageFileUri", "processedFileUri", "product", "contract", "marketplace", "vendor", "provider", "acceptanceNote", "rejectionNote", "errorDetail", "stats", "events", "externalId", "environment")
    _hx_fields = ["name", "description", "note", "status", "period", "currency", "schema", "usageFileUri", "processedFileUri", "product", "contract", "marketplace", "vendor", "provider", "acceptanceNote", "rejectionNote", "errorDetail", "stats", "events", "externalId", "environment"]
    _hx_methods = ["register", "update", "delete", "uploadRecords", "uploadRecordsAndCategories", "upload", "submit", "accept", "reject", "close", "getTemplate", "getTemplateLink", "uploadReconciliation", "reprocess"]
    _hx_statics = ["list", "get", "createSpreadsheet", "getRecordParamNames", "getRecordParamValue"]
    _hx_interfaces = []
    _hx_super = connect_models_IdModel


    def __init__(self):
        self.environment = None
        self.externalId = None
        self.events = None
        self.stats = None
        self.errorDetail = None
        self.rejectionNote = None
        self.acceptanceNote = None
        self.provider = None
        self.vendor = None
        self.marketplace = None
        self.contract = None
        self.product = None
        self.processedFileUri = None
        self.usageFileUri = None
        self.schema = None
        self.currency = None
        self.period = None
        self.status = None
        self.note = None
        self.description = None
        self.name = None
        super().__init__()
        _g = haxe_ds_StringMap()
        _g.h["vendor"] = "Account"
        _g.h["provider"] = "Account"
        _g.h["stats"] = "UsageStats"
        self._setFieldClassNames(_g)

    def register(self):
        try:
            newUsageFile = connect_Env.getUsageApi().createUsageFile(self.toString())
            return connect_models_Model.parse(connect_models_UsageFile,newUsageFile)
        except BaseException as _g:
            None
            return None

    def update(self):
        try:
            diff = self._toDiff()
            hasModifiedFields = (len(python_Boot.fields(diff)) > 1)
            if hasModifiedFields:
                usageFile = connect_Env.getUsageApi().updateUsageFile(self.id,haxe_format_JsonPrinter.print(diff,None,None))
                return connect_models_Model.parse(connect_models_UsageFile,usageFile)
            else:
                return self
        except BaseException as _g:
            None
            return None

    def delete(self):
        try:
            connect_Env.getUsageApi().deleteUsageFile(self.id)
            return True
        except BaseException as _g:
            None
            return False

    def uploadRecords(self,records):
        sheet = connect_models_UsageFile.createSpreadsheet(self.id,records.toArray(),None)
        data = connect_util_Blob._fromBytes(sheet)
        return self.upload(data)

    def uploadRecordsAndCategories(self,records,categories):
        sheet = connect_models_UsageFile.createSpreadsheet(self.id,records.toArray(),categories.toArray())
        data = connect_util_Blob._fromBytes(sheet)
        return self.upload(data)

    def upload(self,content):
        usageFile = connect_Env.getUsageApi().uploadUsageFile(self.id,content)
        return connect_models_Model.parse(connect_models_UsageFile,usageFile)

    def submit(self):
        usageFile = connect_Env.getUsageApi().submitUsageFileAction(self.id)
        return connect_models_Model.parse(connect_models_UsageFile,usageFile)

    def accept(self,note):
        usageFile = connect_Env.getUsageApi().acceptUsageFileAction(self.id,note)
        return connect_models_Model.parse(connect_models_UsageFile,usageFile)

    def reject(self,note):
        usageFile = connect_Env.getUsageApi().rejectUsageFileAction(self.id,note)
        return connect_models_Model.parse(connect_models_UsageFile,usageFile)

    def close(self):
        usageFile = connect_Env.getUsageApi().closeUsageFileAction(self.id)
        return connect_models_Model.parse(connect_models_UsageFile,usageFile)

    def getTemplate(self):
        try:
            link = self.getTemplateLink()
            response = connect_Env.getApiClient().syncRequest("GET",link,None,None,None,None,None,None)
            return response.data
        except BaseException as _g:
            None
            return None

    def getTemplateLink(self):
        link = python_lib_Json.loads(connect_Env.getUsageApi().getProductSpecificUsageFileTemplate(self.id),**python__KwArgs_KwArgs_Impl_.fromT(_hx_AnonObject({'object_hook': python_Lib.dictToAnon})))
        return link.template_link

    def uploadReconciliation(self,content):
        usageFile = connect_Env.getUsageApi().uploadReconciliationFileFromProvider(self.id,content)
        return connect_models_Model.parse(connect_models_UsageFile,usageFile)

    def reprocess(self):
        usageFile = connect_Env.getUsageApi().reprocessProcessedFile(self.id)
        return connect_models_Model.parse(connect_models_UsageFile,usageFile)

    @staticmethod
    def list(filters):
        usageFiles = connect_Env.getUsageApi().listUsageFiles(filters)
        return connect_models_Model.parseArray(connect_models_UsageFile,usageFiles)

    @staticmethod
    def get(id):
        try:
            usageFile = connect_Env.getUsageApi().getUsageFile(id)
            return connect_models_Model.parse(connect_models_UsageFile,usageFile)
        except BaseException as _g:
            None
            return None

    @staticmethod
    def createSpreadsheet(fileId,records,categories):
        paramNames = connect_models_UsageFile.getRecordParamNames(records)
        def _hx_local_0(n):
            return ("s:" + ("null" if n is None else n))
        usageColumns = (["s:record_id", "s:record_note", "s:item_search_criteria", "s:item_search_value", "s:amount", "s:quantity", "s:start_time_utc", "s:end_time_utc", "s:asset_search_criteria", "s:asset_search_value", "s:item_name", "s:item_mpn", "s:item_precision", "s:item_unit", "s:category_id", "s:asset_recon_id", "s:tier"] + list(map(_hx_local_0,paramNames)))
        usageSheet = [usageColumns]
        _g = 0
        _g1 = len(records)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            record = [(records[i] if i >= 0 and i < len(records) else None)]
            _this = ((record[0] if 0 < len(record) else None).recordId if (((record[0] if 0 < len(record) else None).recordId is not None)) else ((("" + ("null" if fileId is None else fileId)) + "_record_") + Std.string(i)))
            _this1 = ((record[0] if 0 < len(record) else None).recordNote if (((record[0] if 0 < len(record) else None).recordNote is not None)) else "")
            _this2 = ((record[0] if 0 < len(record) else None).itemSearchCriteria if (((record[0] if 0 < len(record) else None).itemSearchCriteria is not None)) else "")
            _this3 = ((record[0] if 0 < len(record) else None).itemSearchValue if (((record[0] if 0 < len(record) else None).itemSearchValue is not None)) else "")
            _this4 = (Std.string((record[0] if 0 < len(record) else None).amount) if (((record[0] if 0 < len(record) else None).amount is not None)) else "0")
            _this5 = (Std.string((record[0] if 0 < len(record) else None).quantity) if (((record[0] if 0 < len(record) else None).quantity is not None)) else "0")
            _this6 = None
            if ((record[0] if 0 < len(record) else None).startTimeUtc is not None):
                _this7 = StringTools.replace((record[0] if 0 < len(record) else None).startTimeUtc.toString(),"T"," ")
                _this6 = python_internal_ArrayImpl._get(_this7.split("+"), 0)
            else:
                _this6 = ""
            _this8 = None
            if ((record[0] if 0 < len(record) else None).endTimeUtc is not None):
                _this9 = StringTools.replace((record[0] if 0 < len(record) else None).endTimeUtc.toString(),"T"," ")
                _this8 = python_internal_ArrayImpl._get(_this9.split("+"), 0)
            else:
                _this8 = ""
            def _hx_local_2(record):
                def _hx_local_1(n):
                    return ("s:" + HxOverrides.stringOrNull(connect_models_UsageFile.getRecordParamValue((record[0] if 0 < len(record) else None),n)))
                return _hx_local_1
            x = ([("s:" + ("null" if _this is None else _this)), ("s:" + ("null" if _this1 is None else _this1)), ("s:" + ("null" if _this2 is None else _this2)), ("s:" + ("null" if _this3 is None else _this3)), ("n:" + ("null" if _this4 is None else _this4)), ("n:" + ("null" if _this5 is None else _this5)), ("s:" + ("null" if _this6 is None else _this6)), ("s:" + ("null" if _this8 is None else _this8)), ("s:" + HxOverrides.stringOrNull((((record[0] if 0 < len(record) else None).assetSearchCriteria if (((record[0] if 0 < len(record) else None).assetSearchCriteria is not None)) else "")))), ("s:" + HxOverrides.stringOrNull((((record[0] if 0 < len(record) else None).assetSearchValue if (((record[0] if 0 < len(record) else None).assetSearchValue is not None)) else "")))), ("s:" + HxOverrides.stringOrNull((((record[0] if 0 < len(record) else None).itemName if (((record[0] if 0 < len(record) else None).itemName is not None)) else "")))), ("s:" + HxOverrides.stringOrNull((((record[0] if 0 < len(record) else None).itemMpn if (((record[0] if 0 < len(record) else None).itemMpn is not None)) else "")))), ("s:" + HxOverrides.stringOrNull((((record[0] if 0 < len(record) else None).itemPrecision if (((record[0] if 0 < len(record) else None).itemPrecision is not None)) else "")))), ("s:" + HxOverrides.stringOrNull((((record[0] if 0 < len(record) else None).itemUnit if (((record[0] if 0 < len(record) else None).itemUnit is not None)) else "")))), ("s:" + HxOverrides.stringOrNull((((record[0] if 0 < len(record) else None).categoryId if (((record[0] if 0 < len(record) else None).categoryId is not None)) else "generic_category")))), ("s:" + HxOverrides.stringOrNull((((record[0] if 0 < len(record) else None).assetReconId if (((record[0] if 0 < len(record) else None).assetReconId is not None)) else "")))), (Std.string((record[0] if 0 < len(record) else None).tier) if ((("s:" + Std.string((record[0] if 0 < len(record) else None).tier)) is not None)) else "")] + list(map(_hx_local_2(record),paramNames)))
            usageSheet.append(x)
        categoriesSheet = []
        categoriesSheet.append(["s:category_id", "s:category_name", "s:category_description"])
        if (categories is not None):
            _g = 0
            while (_g < len(categories)):
                category = (categories[_g] if _g >= 0 and _g < len(categories) else None)
                _g = (_g + 1)
                x = [("s:" + HxOverrides.stringOrNull(category.id)), ("s:" + HxOverrides.stringOrNull(category.name)), ("s:" + HxOverrides.stringOrNull(category.description))]
                categoriesSheet.append(x)
        else:
            categoriesSheet.append(["s:generic_category", "s:Generic Category", "s:Generic autogenerated category"])
        return connect_util_ExcelWriter().addSheet("categories",categoriesSheet).addSheet("usage_records",usageSheet).compress()

    @staticmethod
    def getRecordParamNames(records):
        names = []
        _g = 0
        while (_g < len(records)):
            record = (records[_g] if _g >= 0 and _g < len(records) else None)
            _g = (_g + 1)
            if (record.params is not None):
                param = record.params.iterator()
                while param.hasNext():
                    param1 = param.next()
                    if (python_internal_ArrayImpl.indexOf(names,param1.parameterName,None) == -1):
                        x = param1.parameterName
                        names.append(x)
        return names

    @staticmethod
    def getRecordParamValue(record,name):
        if (record.params is not None):
            def _hx_local_0(p):
                return (p.parameterName == name)
            param = Lambda.find(record.params,_hx_local_0)
            if (param is not None):
                return param.parameterValue
            else:
                return ""
        else:
            return ""

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.name = None
        _hx_o.description = None
        _hx_o.note = None
        _hx_o.status = None
        _hx_o.period = None
        _hx_o.currency = None
        _hx_o.schema = None
        _hx_o.usageFileUri = None
        _hx_o.processedFileUri = None
        _hx_o.product = None
        _hx_o.contract = None
        _hx_o.marketplace = None
        _hx_o.vendor = None
        _hx_o.provider = None
        _hx_o.acceptanceNote = None
        _hx_o.rejectionNote = None
        _hx_o.errorDetail = None
        _hx_o.stats = None
        _hx_o.events = None
        _hx_o.externalId = None
        _hx_o.environment = None
connect_models_UsageFile._hx_class = connect_models_UsageFile
_hx_classes["connect.models.UsageFile"] = connect_models_UsageFile


class connect_models_UsageParam(connect_models_Model):
    _hx_class_name = "connect.models.UsageParam"
    __slots__ = ("parameterName", "parameterValue")
    _hx_fields = ["parameterName", "parameterValue"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_Model


    def __init__(self):
        self.parameterValue = None
        self.parameterName = None
        super().__init__()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.parameterName = None
        _hx_o.parameterValue = None
connect_models_UsageParam._hx_class = connect_models_UsageParam
_hx_classes["connect.models.UsageParam"] = connect_models_UsageParam


class connect_models_UsageRecord(connect_models_Model):
    _hx_class_name = "connect.models.UsageRecord"
    __slots__ = ("recordId", "recordNote", "itemSearchCriteria", "itemSearchValue", "amount", "quantity", "startTimeUtc", "endTimeUtc", "assetSearchCriteria", "assetSearchValue", "itemName", "itemMpn", "itemUnit", "itemPrecision", "categoryId", "assetReconId", "tier", "params")
    _hx_fields = ["recordId", "recordNote", "itemSearchCriteria", "itemSearchValue", "amount", "quantity", "startTimeUtc", "endTimeUtc", "assetSearchCriteria", "assetSearchValue", "itemName", "itemMpn", "itemUnit", "itemPrecision", "categoryId", "assetReconId", "tier", "params"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_Model


    def __init__(self):
        self.params = None
        self.tier = None
        self.assetReconId = None
        self.categoryId = None
        self.itemPrecision = None
        self.itemUnit = None
        self.itemMpn = None
        self.itemName = None
        self.assetSearchValue = None
        self.assetSearchCriteria = None
        self.endTimeUtc = None
        self.startTimeUtc = None
        self.quantity = None
        self.amount = None
        self.itemSearchValue = None
        self.itemSearchCriteria = None
        self.recordNote = None
        self.recordId = None
        super().__init__()
        _g = haxe_ds_StringMap()
        _g.h["startTimeUtc"] = "DateTime"
        _g.h["endTimeUtc"] = "DateTime"
        _g.h["params"] = "UsageParam"
        self._setFieldClassNames(_g)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.recordId = None
        _hx_o.recordNote = None
        _hx_o.itemSearchCriteria = None
        _hx_o.itemSearchValue = None
        _hx_o.amount = None
        _hx_o.quantity = None
        _hx_o.startTimeUtc = None
        _hx_o.endTimeUtc = None
        _hx_o.assetSearchCriteria = None
        _hx_o.assetSearchValue = None
        _hx_o.itemName = None
        _hx_o.itemMpn = None
        _hx_o.itemUnit = None
        _hx_o.itemPrecision = None
        _hx_o.categoryId = None
        _hx_o.assetReconId = None
        _hx_o.tier = None
        _hx_o.params = None
connect_models_UsageRecord._hx_class = connect_models_UsageRecord
_hx_classes["connect.models.UsageRecord"] = connect_models_UsageRecord


class connect_models_UsageStats(connect_models_Model):
    _hx_class_name = "connect.models.UsageStats"
    __slots__ = ("uploaded", "validated", "pending", "accepted", "closed")
    _hx_fields = ["uploaded", "validated", "pending", "accepted", "closed"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_Model


    def __init__(self):
        self.closed = None
        self.accepted = None
        self.pending = None
        self.validated = None
        self.uploaded = None
        super().__init__()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.uploaded = None
        _hx_o.validated = None
        _hx_o.pending = None
        _hx_o.accepted = None
        _hx_o.closed = None
connect_models_UsageStats._hx_class = connect_models_UsageStats
_hx_classes["connect.models.UsageStats"] = connect_models_UsageStats


class connect_models_User(connect_models_IdModel):
    _hx_class_name = "connect.models.User"
    __slots__ = ("name", "email")
    _hx_fields = ["name", "email"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = connect_models_IdModel


    def __init__(self):
        self.email = None
        self.name = None
        super().__init__()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.name = None
        _hx_o.email = None
connect_models_User._hx_class = connect_models_User
_hx_classes["connect.models.User"] = connect_models_User


class connect_native_PythonRequest:
    _hx_class_name = "connect.native.PythonRequest"
    __slots__ = ()
    _hx_statics = ["request"]

    @staticmethod
    def request(method,url,headers,body,fileArg,fileName,fileContent,timeout,certificate):
        import requests
        parsedHeaders = dict()
        if (headers is not None):
            key = headers.keys()
            while key.hasNext():
                key1 = key.next()
                parsedHeaders[key1] = headers.get(key1)
        pythonBytes = (bytes(fileContent._toArray()) if ((((fileArg is not None) and ((fileName is not None))) and ((fileContent is not None)))) else None)
        files = (dict() if ((fileContent is not None)) else None)
        if (files is not None):
            files[fileArg] = (fileName, pythonBytes)
        resp = (requests.request(method, url, headers=parsedHeaders, data=body.encode() if body else None, timeout=timeout,cert=certificate) if ((files is None)) else requests.request(method, url, headers=parsedHeaders, files=files, timeout=timeout,cert=certificate))
        contentBytes = haxe_io_Bytes.ofData(resp.content)
        return connect_api_Response(resp.status_code,resp.text,connect_util_Blob._fromBytes(contentBytes))
connect_native_PythonRequest._hx_class = connect_native_PythonRequest
_hx_classes["connect.native.PythonRequest"] = connect_native_PythonRequest


class connect_native_PythonZlib:
    _hx_class_name = "connect.native.PythonZlib"
    __slots__ = ()
    _hx_statics = ["compress", "decompress"]

    @staticmethod
    def compress(data,level):
        import zlib
        pythonBytes = bytes(connect_util_Blob._bytesToArray(data))
        result = zlib.compress(pythonBytes, level)
        return haxe_io_Bytes.ofData(result)

    @staticmethod
    def decompress(data):
        import zlib
        pythonBytes = bytes(connect_util_Blob._bytesToArray(data))
        result = zlib.decompress(pythonBytes)
        return haxe_io_Bytes.ofData(result)
connect_native_PythonZlib._hx_class = connect_native_PythonZlib
_hx_classes["connect.native.PythonZlib"] = connect_native_PythonZlib


class connect_util_Blob(connect_Base):
    _hx_class_name = "connect.util.Blob"
    __slots__ = ("bytes",)
    _hx_fields = ["bytes"]
    _hx_methods = ["save", "length", "toString", "_getBytes", "_toArray"]
    _hx_statics = ["load", "_fromBytes", "_bytesToArray"]
    _hx_interfaces = []
    _hx_super = connect_Base


    def __init__(self,_hx_bytes):
        self.bytes = _hx_bytes

    def save(self,path):
        sys_io_File.saveBytes(path,self.bytes)

    def length(self):
        if (self.bytes is not None):
            return self.bytes.length
        else:
            return -1

    def toString(self):
        if (self.bytes is not None):
            return self.bytes.toString()
        else:
            return ""

    def _getBytes(self):
        return self.bytes

    def _toArray(self):
        return connect_util_Blob._bytesToArray(self._getBytes())

    @staticmethod
    def load(path):
        try:
            return connect_util_Blob(sys_io_File.getBytes(path))
        except BaseException as _g:
            None
            return connect_util_Blob(None)

    @staticmethod
    def _fromBytes(_hx_bytes):
        return connect_util_Blob(_hx_bytes)

    @staticmethod
    def _bytesToArray(_hx_bytes):
        if (_hx_bytes is not None):
            _g = []
            _g1 = 0
            _g2 = haxe_io__UInt8Array_UInt8Array_Impl_.fromBytes(_hx_bytes)
            while (_g1 < _g2.byteLength):
                b = _g2.bytes.b[(_g1 + _g2.byteOffset)]
                _g1 = (_g1 + 1)
                _g.append(b)
            return _g
        else:
            return None

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.bytes = None
connect_util_Blob._hx_class = connect_util_Blob
_hx_classes["connect.util.Blob"] = connect_util_Blob


class connect_util_Collection(connect_Base):
    _hx_class_name = "connect.util.Collection"
    __slots__ = ("_array",)
    _hx_fields = ["_array"]
    _hx_methods = ["length", "get", "set", "toArray", "concat", "copy", "indexOf", "insert", "iterator", "__iter__", "join", "lastIndexOf", "pop", "push", "remove", "reverse", "shift", "slice", "splice", "toString", "unshift"]
    _hx_statics = ["_fromArray"]
    _hx_interfaces = []
    _hx_super = connect_Base


    def __init__(self):
        self._array = list()

    def length(self):
        return len(self._array)

    def get(self,index):
        return (self._array[index] if index >= 0 and index < len(self._array) else None)

    def set(self,index,x):
        python_internal_ArrayImpl._set(self._array, index, x)
        return self

    def toArray(self):
        return list(self._array)

    def concat(self,c):
        return connect_util_Collection._fromArray((self._array + c._array))

    def copy(self):
        return connect_util_Collection._fromArray(list(self._array))

    def indexOf(self,x,fromIndex = None):
        return python_internal_ArrayImpl.indexOf(self._array,x,fromIndex)

    def insert(self,pos,x):
        self._array.insert(pos, x)

    def iterator(self):
        return haxe_iterators_ArrayIterator(self._array)

    def __iter__(self):
        _hx_list = self._array
        return Reflect.field(_hx_list,"__iter__")()

    def join(self,sep):
        _this = self._array
        return sep.join([python_Boot.toString1(x1,'') for x1 in _this])

    def lastIndexOf(self,x,fromIndex = None):
        return python_internal_ArrayImpl.lastIndexOf(self._array,x,fromIndex)

    def pop(self):
        _this = self._array
        return (None if ((len(_this) == 0)) else _this.pop())

    def push(self,x):
        _this = self._array
        _this.append(x)
        return self

    def remove(self,x):
        return python_internal_ArrayImpl.remove(self._array,x)

    def reverse(self):
        self._array.reverse()

    def shift(self):
        _this = self._array
        return (None if ((len(_this) == 0)) else _this.pop(0))

    def slice(self,pos,end = None):
        return connect_util_Collection._fromArray(self._array[pos:end])

    def splice(self,pos,_hx_len):
        _this = self._array
        pos1 = pos
        if (pos1 < 0):
            pos1 = (len(_this) + pos1)
        if (pos1 < 0):
            pos1 = 0
        res = _this[pos1:(pos1 + _hx_len)]
        del _this[pos1:(pos1 + _hx_len)]
        return connect_util_Collection._fromArray(res)

    def toString(self):
        if ((self.length() > 0) and Std.isOfType(self.get(0),connect_models_Model)):
            def _hx_local_0(el):
                return Std.string(el)
            _this = list(map(_hx_local_0,self._array))
            return (("[" + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in _this]))) + "]")
        else:
            return haxe_format_JsonPrinter.print(self._array,None,None)

    def unshift(self,x):
        self._array.insert(0, x)
        return self

    @staticmethod
    def _fromArray(array):
        col = connect_util_Collection()
        col._array = list(array)
        return col

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o._array = None
connect_util_Collection._hx_class = connect_util_Collection
_hx_classes["connect.util.Collection"] = connect_util_Collection


class connect_util_DateTime:
    _hx_class_name = "connect.util.DateTime"
    __slots__ = ("year", "month", "day", "hours", "minutes", "seconds")
    _hx_fields = ["year", "month", "day", "hours", "minutes", "seconds"]
    _hx_methods = ["getYear", "getMonth", "getDay", "getHours", "getMinutes", "getSeconds", "getTimestamp", "toString", "compare", "equals", "isBetweenDates"]
    _hx_statics = ["now", "fromString"]

    def __init__(self,year,month,day,hour,_hx_min,sec):
        self.year = year
        self.month = month
        self.day = day
        self.hours = hour
        self.minutes = _hx_min
        self.seconds = sec

    def getYear(self):
        return self.year

    def getMonth(self):
        return self.month

    def getDay(self):
        return self.day

    def getHours(self):
        return self.hours

    def getMinutes(self):
        return self.minutes

    def getSeconds(self):
        return self.seconds

    def getTimestamp(self):
        thisDate = Date(self.year,self.month,self.day,self.hours,self.minutes,self.seconds)
        otherDate = Date(1970,0,1,0,0,0)
        return (((thisDate.date.timestamp() * 1000) / 1000) - (((otherDate.date.timestamp() * 1000) / 1000)))

    def toString(self):
        year = StringTools.lpad(Std.string(self.year),"0",4)
        month = StringTools.lpad(Std.string((self.month + 1)),"0",2)
        day = StringTools.lpad(Std.string(self.day),"0",2)
        hour = StringTools.lpad(Std.string(self.hours),"0",2)
        minute = StringTools.lpad(Std.string(self.minutes),"0",2)
        second = StringTools.lpad(Std.string(self.seconds),"0",2)
        return (((((((((((("" + ("null" if year is None else year)) + "-") + ("null" if month is None else month)) + "-") + ("null" if day is None else day)) + "T") + ("null" if hour is None else hour)) + ":") + ("null" if minute is None else minute)) + ":") + ("null" if second is None else second)) + "+00:00")

    def compare(self,other):
        thisDate = Date(self.year,self.month,self.day,self.hours,self.minutes,self.seconds)
        otherDate = Date(other.year,other.month,other.day,other.hours,other.minutes,other.seconds)
        x = ((thisDate.date.timestamp() * 1000) / 1000)
        tmp = None
        try:
            tmp = int(x)
        except BaseException as _g:
            None
            tmp = None
        x = ((otherDate.date.timestamp() * 1000) / 1000)
        tmp1 = None
        try:
            tmp1 = int(x)
        except BaseException as _g:
            None
            tmp1 = None
        return (tmp - tmp1)

    def equals(self,other):
        return (self.compare(other) == 0)

    def isBetweenDates(self,first,last):
        if (last.compare(first) < 0):
            temp = first
            first = last
            last = temp
        length = last.compare(first)
        offset = self.compare(first)
        if (offset >= 0):
            return (offset <= length)
        else:
            return False

    @staticmethod
    def now():
        date = Date.now()
        return connect_util_DateTime(date.dateUTC.year,(date.dateUTC.month - 1),date.dateUTC.day,date.dateUTC.hour,date.dateUTC.minute,date.dateUTC.second)

    @staticmethod
    def fromString(s):
        startIndex = None
        plusIndex = None
        if (startIndex is None):
            plusIndex = s.rfind("+", 0, len(s))
        else:
            i = s.rfind("+", 0, (startIndex + 1))
            startLeft = (max(0,((startIndex + 1) - len("+"))) if ((i == -1)) else (i + 1))
            check = s.find("+", startLeft, len(s))
            plusIndex = (check if (((check > i) and ((check <= startIndex)))) else i)
        strippedOffset = (HxString.substring(s,0,plusIndex) if ((plusIndex != -1)) else s)
        dateTimeSplit = strippedOffset.split("T")
        _this = (dateTimeSplit[0] if 0 < len(dateTimeSplit) else None)
        dateSplit = _this.split("-")
        timeSplit = None
        if (len(dateTimeSplit) > 1):
            _this = (dateTimeSplit[1] if 1 < len(dateTimeSplit) else None)
            timeSplit = _this.split(":")
        else:
            timeSplit = "00:00:00".split(":")
        try:
            year = Std.parseInt((dateSplit[0] if 0 < len(dateSplit) else None))
            if (year is None):
                return None
            month = ((Std.parseInt((dateSplit[1] if 1 < len(dateSplit) else None)) - 1) if ((len(dateSplit) > 1)) else 0)
            day = (Std.parseInt((dateSplit[2] if 2 < len(dateSplit) else None)) if ((len(dateSplit) > 2)) else 1)
            hour = Std.parseInt((timeSplit[0] if 0 < len(timeSplit) else None))
            minute = (Std.parseInt((timeSplit[1] if 1 < len(timeSplit) else None)) if ((len(timeSplit) > 1)) else 0)
            second = (Std.parseInt((timeSplit[2] if 2 < len(timeSplit) else None)) if ((len(timeSplit) > 2)) else 0)
            return connect_util_DateTime(year,month,day,hour,minute,second)
        except BaseException as _g:
            None
            return None

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.year = None
        _hx_o.month = None
        _hx_o.day = None
        _hx_o.hours = None
        _hx_o.minutes = None
        _hx_o.seconds = None
connect_util_DateTime._hx_class = connect_util_DateTime
_hx_classes["connect.util.DateTime"] = connect_util_DateTime


class connect_util_Diff:
    _hx_class_name = "connect.util.Diff"
    __slots__ = ("a", "d", "c")
    _hx_fields = ["a", "d", "c"]
    _hx_methods = ["apply", "swap", "toString", "toObject"]
    _hx_statics = ["isStruct", "isArray", "checkStructs", "areEqual", "compareArrays", "applyArray", "swapArray", "mapToObject", "changeArrayToObject"]

    def __init__(self,first,second):
        self.c = None
        self.d = None
        self.a = None
        _gthis = self
        connect_util_Diff.checkStructs(first,second)
        firstFields = python_Boot.fields(first)
        secondFields = python_Boot.fields(second)
        _g = []
        _g1 = 0
        while (_g1 < len(secondFields)):
            f = (secondFields[_g1] if _g1 >= 0 and _g1 < len(secondFields) else None)
            _g1 = (_g1 + 1)
            if (not python_Boot.hasField(first,f)):
                _g.append(f)
        addedFields = _g
        _g = []
        _g1 = 0
        while (_g1 < len(firstFields)):
            f = (firstFields[_g1] if _g1 >= 0 and _g1 < len(firstFields) else None)
            _g1 = (_g1 + 1)
            if (not python_Boot.hasField(second,f)):
                _g.append(f)
        deletedFields = _g
        _g = []
        _g1 = 0
        while (_g1 < len(firstFields)):
            f = (firstFields[_g1] if _g1 >= 0 and _g1 < len(firstFields) else None)
            _g1 = (_g1 + 1)
            if python_Boot.hasField(second,f):
                _g.append(f)
        commonFields = _g
        def _hx_local_3(f):
            return (not connect_util_Diff.areEqual(Reflect.field(first,f),Reflect.field(second,f)))
        changedFields = list(filter(_hx_local_3,commonFields))
        self.a = haxe_ds_StringMap()
        def _hx_local_4(f):
            _this = _gthis.a
            value = Reflect.field(second,f)
            _this.h[f] = value
        Lambda.iter(addedFields,_hx_local_4)
        self.d = haxe_ds_StringMap()
        def _hx_local_5(f):
            _this = _gthis.d
            value = Reflect.field(first,f)
            _this.h[f] = value
        Lambda.iter(deletedFields,_hx_local_5)
        self.c = haxe_ds_StringMap()
        def _hx_local_6(f):
            a = Reflect.field(first,f)
            b = Reflect.field(second,f)
            if (connect_util_Diff.isStruct(a) and connect_util_Diff.isStruct(b)):
                _this = _gthis.c
                value = connect_util_Diff(a,b)
                _this.h[f] = value
            elif (connect_util_Diff.isArray(a) and connect_util_Diff.isArray(b)):
                _this = _gthis.c
                value = connect_util_Diff.compareArrays(a,b)
                _this.h[f] = value
            else:
                _gthis.c.h[f] = [a, b]
        Lambda.iter(changedFields,_hx_local_6)

    def apply(self,obj):
        _gthis = self
        out = Reflect.copy(obj)
        _g = []
        k = self.a.keys()
        while k.hasNext():
            k1 = k.next()
            _g.append(k1)
        addedKeys = _g
        def _hx_local_0(k):
            value = _gthis.a.h.get(k,None)
            setattr(out,(("_hx_" + k) if ((k in python_Boot.keywords)) else (("_hx_" + k) if (((((len(k) > 2) and ((ord(k[0]) == 95))) and ((ord(k[1]) == 95))) and ((ord(k[(len(k) - 1)]) != 95)))) else k)),value)
        Lambda.iter(addedKeys,_hx_local_0)
        _g = []
        k = self.d.keys()
        while k.hasNext():
            k1 = k.next()
            _g.append(k1)
        deletedKeys = _g
        def _hx_local_1(k):
            Reflect.deleteField(out,k)
        Lambda.iter(deletedKeys,_hx_local_1)
        _g = []
        k = self.c.keys()
        while k.hasNext():
            k1 = k.next()
            _g.append(k1)
        changedKeys = _g
        def _hx_local_4(k):
            change = _gthis.c.h.get(k,None)
            if Std.isOfType(change,list):
                if (Reflect.field(change,"length") == 2):
                    def _hx_local_3():
                        _hx_local_2 = change
                        if (Std.isOfType(_hx_local_2,list) or ((_hx_local_2 is None))):
                            _hx_local_2
                        else:
                            raise "Class cast error"
                        return _hx_local_2
                    value = python_internal_ArrayImpl._get((_hx_local_3()), 1)
                    setattr(out,(("_hx_" + k) if ((k in python_Boot.keywords)) else (("_hx_" + k) if (((((len(k) > 2) and ((ord(k[0]) == 95))) and ((ord(k[1]) == 95))) and ((ord(k[(len(k) - 1)]) != 95)))) else k)),value)
                else:
                    field = Reflect.field(out,k)
                    original = (field if ((field is not None)) else [])
                    value = connect_util_Diff.applyArray(original,change)
                    setattr(out,(("_hx_" + k) if ((k in python_Boot.keywords)) else (("_hx_" + k) if (((((len(k) > 2) and ((ord(k[0]) == 95))) and ((ord(k[1]) == 95))) and ((ord(k[(len(k) - 1)]) != 95)))) else k)),value)
            else:
                field = Reflect.field(out,k)
                original = (field if ((field is not None)) else _hx_AnonObject({}))
                value = Reflect.field(change,"apply")(original)
                setattr(out,(("_hx_" + k) if ((k in python_Boot.keywords)) else (("_hx_" + k) if (((((len(k) > 2) and ((ord(k[0]) == 95))) and ((ord(k[1]) == 95))) and ((ord(k[(len(k) - 1)]) != 95)))) else k)),value)
        Lambda.iter(changedKeys,_hx_local_4)
        return out

    def swap(self):
        _gthis = self
        additions = self.d
        deletions = self.a
        changes = haxe_ds_StringMap()
        _g = []
        k = self.c.keys()
        while k.hasNext():
            k1 = k.next()
            _g.append(k1)
        changedKeys = _g
        def _hx_local_4(k):
            change = _gthis.c.h.get(k,None)
            if Std.isOfType(change,list):
                if (Reflect.field(change,"length") == 2):
                    def _hx_local_1():
                        _hx_local_0 = change
                        if (Std.isOfType(_hx_local_0,list) or ((_hx_local_0 is None))):
                            _hx_local_0
                        else:
                            raise "Class cast error"
                        return _hx_local_0
                    def _hx_local_3():
                        _hx_local_2 = change
                        if (Std.isOfType(_hx_local_2,list) or ((_hx_local_2 is None))):
                            _hx_local_2
                        else:
                            raise "Class cast error"
                        return _hx_local_2
                    changes.h[k] = [python_internal_ArrayImpl._get((_hx_local_1()), 1), python_internal_ArrayImpl._get((_hx_local_3()), 0)]
                else:
                    value = connect_util_Diff.swapArray(change)
                    changes.h[k] = value
            else:
                value = Reflect.field(change,"swap")()
                changes.h[k] = value
        Lambda.iter(changedKeys,_hx_local_4)
        diff = Type.createEmptyInstance(connect_util_Diff)
        setattr(diff,(("_hx_" + "a") if (("a" in python_Boot.keywords)) else (("_hx_" + "a") if (((((len("a") > 2) and ((ord("a"[0]) == 95))) and ((ord("a"[1]) == 95))) and ((ord("a"[(len("a") - 1)]) != 95)))) else "a")),additions)
        setattr(diff,(("_hx_" + "d") if (("d" in python_Boot.keywords)) else (("_hx_" + "d") if (((((len("d") > 2) and ((ord("d"[0]) == 95))) and ((ord("d"[1]) == 95))) and ((ord("d"[(len("d") - 1)]) != 95)))) else "d")),deletions)
        setattr(diff,(("_hx_" + "c") if (("c" in python_Boot.keywords)) else (("_hx_" + "c") if (((((len("c") > 2) and ((ord("c"[0]) == 95))) and ((ord("c"[1]) == 95))) and ((ord("c"[(len("c") - 1)]) != 95)))) else "c")),changes)
        return diff

    def toString(self):
        return haxe_format_JsonPrinter.print(self.toObject(),None,None)

    def toObject(self):
        _gthis = self
        obj = _hx_AnonObject({'a': connect_util_Diff.mapToObject(self.a), 'd': connect_util_Diff.mapToObject(self.d), 'c': _hx_AnonObject({})})
        _g = []
        k = self.c.keys()
        while k.hasNext():
            k1 = k.next()
            _g.append(k1)
        changedKeys = _g
        def _hx_local_0(key):
            value = _gthis.c.h.get(key,None)
            if Std.isOfType(value,connect_util_Diff):
                o = obj.c
                value1 = Reflect.field(value,"toObject")()
                setattr(o,(("_hx_" + key) if ((key in python_Boot.keywords)) else (("_hx_" + key) if (((((len(key) > 2) and ((ord(key[0]) == 95))) and ((ord(key[1]) == 95))) and ((ord(key[(len(key) - 1)]) != 95)))) else key)),value1)
            elif (connect_util_Diff.isArray(value) and ((Reflect.field(value,"length") == 3))):
                o = obj.c
                value1 = connect_util_Diff.changeArrayToObject(value)
                setattr(o,(("_hx_" + key) if ((key in python_Boot.keywords)) else (("_hx_" + key) if (((((len(key) > 2) and ((ord(key[0]) == 95))) and ((ord(key[1]) == 95))) and ((ord(key[(len(key) - 1)]) != 95)))) else key)),value1)
            else:
                setattr(obj.c,(("_hx_" + key) if ((key in python_Boot.keywords)) else (("_hx_" + key) if (((((len(key) > 2) and ((ord(key[0]) == 95))) and ((ord(key[1]) == 95))) and ((ord(key[(len(key) - 1)]) != 95)))) else key)),value)
        Lambda.iter(changedKeys,_hx_local_0)
        return obj

    @staticmethod
    def isStruct(value):
        return (Type.typeof(value) == ValueType.TObject)

    @staticmethod
    def isArray(value):
        return Std.isOfType(value,list)

    @staticmethod
    def checkStructs(first,second):
        if ((not connect_util_Diff.isStruct(first)) or (not connect_util_Diff.isStruct(second))):
            raise haxe_Exception.thrown(("Unsupported types in Diff. Values must be structs. " + (((("Got: " + Std.string(Type.typeof(first))) + ", ") + Std.string(Type.typeof(second))))))

    @staticmethod
    def areEqual(first,second):
        if (Std.string(Type.typeof(first)) == Std.string(Type.typeof(second))):
            return (Std.string(first) == Std.string(second))
        else:
            return False

    @staticmethod
    def compareArrays(first,second):
        fixedFirst = (first if ((len(first) <= len(second))) else first[0:len(second)])
        i = 0
        _g = []
        _g_current = 0
        _g_array = fixedFirst
        while (_g_current < len(_g_array)):
            x = _g_current
            _g_current = (_g_current + 1)
            x1 = (_g_array[x] if x >= 0 and x < len(_g_array) else None)
            i1 = i
            i = (i + 1)
            a = x1
            b = (second[i1] if i1 >= 0 and i1 < len(second) else None)
            x2 = (None if (connect_util_Diff.areEqual(a,b)) else ([i1, connect_util_Diff(a,b)] if ((connect_util_Diff.isStruct(a) and connect_util_Diff.isStruct(b))) else ([i1, connect_util_Diff.compareArrays(a,b)] if ((connect_util_Diff.isArray(a) and connect_util_Diff.isArray(b))) else [i1, a, b])))
            _g.append(x2)
        changeList = _g
        _g = []
        _g1 = 0
        while (_g1 < len(changeList)):
            el = (changeList[_g1] if _g1 >= 0 and _g1 < len(changeList) else None)
            _g1 = (_g1 + 1)
            _g.append(el)
        def _hx_local_1(el):
            return (el is not None)
        changes = list(filter(_hx_local_1,_g))
        return [second[len(first):None], first[len(second):None], changes]

    @staticmethod
    def applyArray(obj,arr):
        slice = obj[0:(len(obj) - len((arr[1] if 1 < len(arr) else None)))]
        deleted = (slice if ((slice is not None)) else [])
        added = (deleted + (arr[0] if 0 < len(arr) else None))
        out = added
        def _hx_local_0(change):
            i = (change[0] if 0 < len(change) else None)
            originalArray = ((out[i] if i >= 0 and i < len(out) else None) if ((len(out) > i)) else [])
            originalObject = ((out[i] if i >= 0 and i < len(out) else None) if ((len(out) > i)) else _hx_AnonObject({}))
            python_internal_ArrayImpl._set(out, i, ((change[2] if 2 < len(change) else None) if ((len(change) == 3)) else (connect_util_Diff.applyArray(originalArray,(change[1] if 1 < len(change) else None)) if (Std.isOfType((change[1] if 1 < len(change) else None),list)) else Reflect.field((change[1] if 1 < len(change) else None),"apply")(originalObject))))
        Lambda.iter((arr[2] if 2 < len(arr) else None),_hx_local_0)
        return out

    @staticmethod
    def swapArray(arr):
        additions = (arr[1] if 1 < len(arr) else None)
        deletions = (arr[0] if 0 < len(arr) else None)
        changes = (arr[2] if 2 < len(arr) else None)
        def _hx_local_0(change):
            i = (change[0] if 0 < len(change) else None)
            first = (change[1] if 1 < len(change) else None)
            second = (change[2] if 2 < len(change) else None)
            swappedChange = ([i, second, first] if ((len(change) == 3)) else ([i, connect_util_Diff.swapArray(first)] if (Std.isOfType(first,list)) else [i, Reflect.field(first,"swap")()]))
            return swappedChange
        swappedChanges = list(map(_hx_local_0,changes))
        return [additions, deletions, swappedChanges]

    @staticmethod
    def mapToObject(_hx_map):
        _g = []
        k = _hx_map.keys()
        while k.hasNext():
            k1 = k.next()
            _g.append(k1)
        keys = _g
        obj = _hx_AnonObject({})
        def _hx_local_0(key):
            value = _hx_map.h.get(key,None)
            setattr(obj,(("_hx_" + key) if ((key in python_Boot.keywords)) else (("_hx_" + key) if (((((len(key) > 2) and ((ord(key[0]) == 95))) and ((ord(key[1]) == 95))) and ((ord(key[(len(key) - 1)]) != 95)))) else key)),value)
        Lambda.iter(keys,_hx_local_0)
        return obj

    @staticmethod
    def changeArrayToObject(arr):
        _g = []
        _g_current = 0
        _g_array = (arr[2] if 2 < len(arr) else None)
        while (_g_current < len(_g_array)):
            x = _g_current
            _g_current = (_g_current + 1)
            x1 = (_g_array[x] if x >= 0 and x < len(_g_array) else None)
            x2 = ([(x1[0] if 0 < len(x1) else None), Reflect.field((x1[1] if 1 < len(x1) else None),"toObject")()] if (Std.isOfType((x1[1] if 1 < len(x1) else None),connect_util_Diff)) else ([(x1[0] if 0 < len(x1) else None), connect_util_Diff.changeArrayToObject((x1[1] if 1 < len(x1) else None))] if (connect_util_Diff.isArray((x1[1] if 1 < len(x1) else None))) else x1))
            _g.append(x2)
        changesList = _g
        _g = []
        _g1 = 0
        while (_g1 < len(changesList)):
            change = (changesList[_g1] if _g1 >= 0 and _g1 < len(changesList) else None)
            _g1 = (_g1 + 1)
            _g.append(change)
        changes = _g
        arr1 = [(arr[0] if 0 < len(arr) else None), (arr[1] if 1 < len(arr) else None), changes]
        return arr1

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.a = None
        _hx_o.d = None
        _hx_o.c = None
connect_util_Diff._hx_class = connect_util_Diff
_hx_classes["connect.util.Diff"] = connect_util_Diff


class connect_util_ExcelWriter:
    _hx_class_name = "connect.util.ExcelWriter"
    __slots__ = ("sheets",)
    _hx_fields = ["sheets"]
    _hx_methods = ["addSheet", "sheetExists", "compress", "getStrings", "getSheetNames", "parseSheetsStrings", "getWorkbook", "getRels2", "getContentTypes"]
    _hx_statics = ["APP", "CORE", "RELS1", "THEME", "STYLES", "zipEntry", "parseSheet", "getRowNames"]

    def __init__(self):
        self.sheets = haxe_ds_StringMap()

    def addSheet(self,name,sheet):
        if (not self.sheetExists(name)):
            self.sheets.h[name] = sheet
        return self

    def sheetExists(self,name):
        return (name in self.sheets.h)

    def compress(self):
        strings = self.getStrings()
        sheetNames = self.getSheetNames()
        entries = haxe_ds_List()
        entries.add(connect_util_ExcelWriter.zipEntry("_rels/.rels",connect_util_ExcelWriter.RELS1))
        entries.add(connect_util_ExcelWriter.zipEntry("docProps/app.xml",connect_util_ExcelWriter.APP))
        entries.add(connect_util_ExcelWriter.zipEntry("docProps/core.xml",StringTools.replace(connect_util_ExcelWriter.CORE,"%DATE%",connect_util_DateTime.now().toString())))
        entries.add(connect_util_ExcelWriter.zipEntry("xl/theme/theme1.xml",connect_util_ExcelWriter.THEME))
        entries.add(connect_util_ExcelWriter.zipEntry("xl/sharedStrings.xml",self.parseSheetsStrings()))
        entries.add(connect_util_ExcelWriter.zipEntry("xl/styles.xml",connect_util_ExcelWriter.STYLES))
        entries.add(connect_util_ExcelWriter.zipEntry("xl/workbook.xml",self.getWorkbook()))
        _g = 0
        _g1 = len(sheetNames)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            entries.add(connect_util_ExcelWriter.zipEntry((("xl/worksheets/sheet" + Std.string(((i + 1)))) + ".xml"),connect_util_ExcelWriter.parseSheet(self.sheets.h.get((sheetNames[i] if i >= 0 and i < len(sheetNames) else None),None),strings)))
        entries.add(connect_util_ExcelWriter.zipEntry("xl/_rels/workbook.xml.rels",self.getRels2()))
        entries.add(connect_util_ExcelWriter.zipEntry("[Content_Types].xml",self.getContentTypes()))
        output = haxe_io_BytesOutput()
        haxe_zip_Writer(output).write(entries)
        return output.getBytes()

    def getStrings(self):
        _g = []
        sheet = self.sheets.iterator()
        while sheet.hasNext():
            sheet1 = sheet.next()
            _g1 = 0
            while (_g1 < len(sheet1)):
                row = (sheet1[_g1] if _g1 >= 0 and _g1 < len(sheet1) else None)
                _g1 = (_g1 + 1)
                _g2 = 0
                while (_g2 < len(row)):
                    col = (row[_g2] if _g2 >= 0 and _g2 < len(row) else None)
                    _g2 = (_g2 + 1)
                    if (HxOverrides.arrayGet(col.split(":"), 0) == "s"):
                        _this = col.split(":")[1:None]
                        x = ":".join([python_Boot.toString1(x1,'') for x1 in _this])
                        _g.append(x)
        stringsIncludingDuplicates = _g
        fixedStrings = []
        def _hx_local_2(s):
            if (python_internal_ArrayImpl.indexOf(fixedStrings,s,None) == -1):
                fixedStrings.append(s)
        Lambda.iter(stringsIncludingDuplicates,_hx_local_2)
        return fixedStrings

    def getSheetNames(self):
        _g = []
        k = self.sheets.keys()
        while k.hasNext():
            k1 = k.next()
            _g.append(k1)
        names = _g
        def _hx_local_0(a,b):
            return (connect_util_Util.boolToInt((a > b)) - connect_util_Util.boolToInt((b > a)))
        haxe_ds_ArraySort.sort(names,_hx_local_0)
        return names

    def parseSheetsStrings(self):
        strings = self.getStrings()
        buf_b = python_lib_io_StringIO()
        buf_b.write(Std.string((("<sst uniqueCount=\"" + Std.string(len(strings))) + "\" xmlns=\"http://schemas.openxmlformats.org/spreadsheetml/2006/main\">")))
        _g = 0
        while (_g < len(strings)):
            string = (strings[_g] if _g >= 0 and _g < len(strings) else None)
            _g = (_g + 1)
            buf_b.write(Std.string((("<si><t>" + ("null" if string is None else string)) + "</t></si>")))
        buf_b.write("</sst>")
        return buf_b.getvalue()

    def getWorkbook(self):
        sheet = "<sheet name=\"%NAME%\" sheetId=\"%ID%\" state=\"visible\" r:id=\"rId%ID%\" />"
        sheetNames = self.getSheetNames()
        buffer_b = python_lib_io_StringIO()
        buffer_b.write("<workbook xmlns:r=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships\" xmlns=\"http://schemas.openxmlformats.org/spreadsheetml/2006/main\">")
        buffer_b.write("<workbookPr />")
        buffer_b.write("<workbookProtection />")
        buffer_b.write("<bookViews><workbookView activeTab=\"0\" autoFilterDateGrouping=\"1\" firstSheet=\"0\" minimized=\"0\" showHorizontalScroll=\"1\" showSheetTabs=\"1\" showVerticalScroll=\"1\" tabRatio=\"600\" visibility=\"visible\" /></bookViews>")
        buffer_b.write("<sheets>")
        _g = 0
        _g1 = len(sheetNames)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            replacedId = StringTools.replace(sheet,"%ID%",Std.string((i + 1)))
            replacedName = StringTools.replace(replacedId,"%NAME%",(sheetNames[i] if i >= 0 and i < len(sheetNames) else None))
            buffer_b.write(Std.string(replacedName))
        buffer_b.write("</sheets>")
        buffer_b.write("<definedNames />")
        buffer_b.write("<calcPr calcId=\"124519\" fullCalcOnLoad=\"1\" />")
        buffer_b.write("</workbook>")
        return buffer_b.getvalue()

    def getRels2(self):
        sheetRel = "<Relationship Id=\"rId%ID%\" Target=\"/xl/worksheets/sheet%ID%.xml\" Type=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet\" />"
        stringsRel = "<Relationship Id=\"rId%ID%\" Target=\"sharedStrings.xml\" Type=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships/sharedStrings\" />"
        stylesRel = "<Relationship Id=\"rId%ID%\" Target=\"styles.xml\" Type=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles\" />"
        themeRel = "<Relationship Id=\"rId%ID%\" Target=\"theme/theme1.xml\" Type=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme\" />"
        def _hx_local_0(_,n):
            return (n + 1)
        numSheets = Lambda.fold(self.sheets,_hx_local_0,0)
        buffer_b = python_lib_io_StringIO()
        buffer_b.write("<Relationships xmlns=\"http://schemas.openxmlformats.org/package/2006/relationships\">")
        _g = 0
        _g1 = numSheets
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            buffer_b.write(Std.string(StringTools.replace(sheetRel,"%ID%",Std.string((i + 1)))))
        buffer_b.write(Std.string(StringTools.replace(stringsRel,"%ID%",Std.string((numSheets + 1)))))
        buffer_b.write(Std.string(StringTools.replace(stylesRel,"%ID%",Std.string((numSheets + 2)))))
        buffer_b.write(Std.string(StringTools.replace(themeRel,"%ID%",Std.string((numSheets + 3)))))
        buffer_b.write("</Relationships>")
        return buffer_b.getvalue()

    def getContentTypes(self):
        sheet = "<Override ContentType=\"application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml\" PartName=\"/xl/worksheets/sheet%ID%.xml\" />"
        def _hx_local_0(_,n):
            return (n + 1)
        numSheets = Lambda.fold(self.sheets,_hx_local_0,0)
        buffer_b = python_lib_io_StringIO()
        buffer_b.write("<Types xmlns=\"http://schemas.openxmlformats.org/package/2006/content-types\">")
        buffer_b.write("<Default ContentType=\"application/vnd.openxmlformats-package.relationships+xml\" Extension=\"rels\" />")
        buffer_b.write("<Default ContentType=\"application/xml\" Extension=\"xml\" />")
        buffer_b.write("<Override ContentType=\"application/vnd.openxmlformats-officedocument.spreadsheetml.sharedStrings+xml\" PartName=\"/xl/sharedStrings.xml\" />")
        buffer_b.write("<Override ContentType=\"application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml\" PartName=\"/xl/styles.xml\" />")
        buffer_b.write("<Override ContentType=\"application/vnd.openxmlformats-officedocument.theme+xml\" PartName=\"/xl/theme/theme1.xml\" />")
        buffer_b.write("<Override ContentType=\"application/vnd.openxmlformats-package.core-properties+xml\" PartName=\"/docProps/core.xml\" />")
        buffer_b.write("<Override ContentType=\"application/vnd.openxmlformats-officedocument.extended-properties+xml\" PartName=\"/docProps/app.xml\" />")
        _g = 0
        _g1 = numSheets
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            buffer_b.write(Std.string(StringTools.replace(sheet,"%ID%",Std.string((i + 1)))))
        buffer_b.write("<Override ContentType=\"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml\" PartName=\"/xl/workbook.xml\" />")
        buffer_b.write("</Types>")
        return buffer_b.getvalue()

    @staticmethod
    def zipEntry(name,content):
        _hx_bytes = haxe_io_Bytes.ofString(content)
        entry = _hx_AnonObject({'compressed': False, 'crc32': haxe_crypto_Crc32.make(_hx_bytes), 'data': _hx_bytes, 'dataSize': 0, 'fileName': name, 'fileSize': _hx_bytes.length, 'fileTime': Date.now()})
        compressed = connect_native_PythonZlib.compress(_hx_bytes,9)
        entry.compressed = True
        entry.data = compressed.sub(2,(compressed.length - 6))
        entry.dataSize = entry.data.length
        return entry

    @staticmethod
    def parseSheet(sheet,strings):
        firstRowNames = connect_util_ExcelWriter.getRowNames((sheet[0] if 0 < len(sheet) else None),1)
        lastRowNames = connect_util_ExcelWriter.getRowNames(python_internal_ArrayImpl._get(sheet, (len(sheet) - 1)),len(sheet))
        buf_b = python_lib_io_StringIO()
        buf_b.write("<worksheet xmlns=\"http://schemas.openxmlformats.org/spreadsheetml/2006/main\">")
        buf_b.write("<sheetPr><outlinePr summaryBelow=\"1\" summaryRight=\"1\" /><pageSetUpPr /></sheetPr>")
        buf_b.write(Std.string((((("<dimension ref=\"" + HxOverrides.stringOrNull((firstRowNames[0] if 0 < len(firstRowNames) else None))) + ":") + HxOverrides.stringOrNull(python_internal_ArrayImpl._get(lastRowNames, (len(lastRowNames) - 1)))) + "\" />")))
        buf_b.write("<sheetViews><sheetView workbookViewId=\"0\"><selection activeCell=\"A1\" sqref=\"A1\" /></sheetView></sheetViews>")
        buf_b.write("<sheetFormatPr baseColWidth=\"8\" defaultRowHeight=\"15\" />")
        buf_b.write("<sheetData>")
        _g = 0
        _g1 = len(sheet)
        while (_g < _g1):
            r = _g
            _g = (_g + 1)
            rowNames = connect_util_ExcelWriter.getRowNames((sheet[r] if r >= 0 and r < len(sheet) else None),(r + 1))
            buf_b.write(Std.string((((("<row r=\"" + Std.string(((r + 1)))) + "\" spans=\"1:") + Std.string(len((sheet[r] if r >= 0 and r < len(sheet) else None)))) + "\">")))
            _g2 = 0
            _g3 = len(rowNames)
            while (_g2 < _g3):
                c = _g2
                _g2 = (_g2 + 1)
                elem = python_internal_ArrayImpl._get((sheet[r] if r >= 0 and r < len(sheet) else None), c)
                if (elem is not None):
                    split = elem.split(":")
                    _hx_type = (split[0] if 0 < len(split) else None)
                    _this = split[1:None]
                    value = ":".join([python_Boot.toString1(x1,'') for x1 in _this])
                    fixedValue = Std.string((python_internal_ArrayImpl.indexOf(strings,value,None) if ((_hx_type == "s")) else value))
                    buf_b.write(Std.string((((("<c r=\"" + HxOverrides.stringOrNull((rowNames[c] if c >= 0 and c < len(rowNames) else None))) + "\" t=\"") + ("null" if _hx_type is None else _hx_type)) + "\">")))
                    buf_b.write(Std.string((("<v>" + ("null" if fixedValue is None else fixedValue)) + "</v>")))
                    buf_b.write("</c>")
            buf_b.write("</row>")
        buf_b.write("</sheetData>")
        buf_b.write("<pageMargins bottom=\"1\" footer=\"0.5\" header=\"0.5\" left=\"0.75\" right=\"0.75\" top=\"1\" />")
        buf_b.write("</worksheet>")
        return buf_b.getvalue()

    @staticmethod
    def getRowNames(row,rowNumber):
        _g = []
        _g1 = 0
        _g2 = len(row)
        while (_g1 < _g2):
            c = _g1
            _g1 = (_g1 + 1)
            x = (("" + HxOverrides.stringOrNull("".join(map(chr,[(65 + c)])))) + Std.string(rowNumber))
            _g.append(x)
        return _g

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.sheets = None
connect_util_ExcelWriter._hx_class = connect_util_ExcelWriter
_hx_classes["connect.util.ExcelWriter"] = connect_util_ExcelWriter


class connect_util_Masker:
    _hx_class_name = "connect.util.Masker"
    __slots__ = ()
    _hx_statics = ["maskString", "maskObject", "maskFields", "maskParams", "maskParamsInObject", "maskParamsArray", "maskConfigParam", "replaceStrSensitiveData"]

    @staticmethod
    def maskString(text):
        try:
            return connect_util_Masker.maskObject(python_lib_Json.loads(text,**python__KwArgs_KwArgs_Impl_.fromT(_hx_AnonObject({'object_hook': python_Lib.dictToAnon}))))
        except BaseException as _g:
            None
            return connect_util_Masker.replaceStrSensitiveData(text,connect_Env.getLogger()._getRegExMaskingList())

    @staticmethod
    def maskObject(obj):
        return haxe_format_JsonPrinter.print(connect_util_Masker.maskParams(connect_util_Masker.maskFields(obj)),None,None)

    @staticmethod
    def maskFields(obj):
        if (Type.typeof(obj) == ValueType.TObject):
            maskedFields = connect_Env.getLogger().getMaskedFields()
            _g = 0
            _g1 = python_Boot.fields(obj)
            while (_g < len(_g1)):
                fieldName = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                _g = (_g + 1)
                value = Reflect.field(obj,fieldName)
                if (maskedFields.indexOf(fieldName) != -1):
                    if (Type.typeof(value) == ValueType.TObject):
                        if python_Boot.hasField(value,"id"):
                            value1 = value.id
                            setattr(obj,(("_hx_" + fieldName) if ((fieldName in python_Boot.keywords)) else (("_hx_" + fieldName) if (((((len(fieldName) > 2) and ((ord(fieldName[0]) == 95))) and ((ord(fieldName[1]) == 95))) and ((ord(fieldName[(len(fieldName) - 1)]) != 95)))) else fieldName)),value1)
                        else:
                            setattr(obj,(("_hx_" + fieldName) if ((fieldName in python_Boot.keywords)) else (("_hx_" + fieldName) if (((((len(fieldName) > 2) and ((ord(fieldName[0]) == 95))) and ((ord(fieldName[1]) == 95))) and ((ord(fieldName[(len(fieldName) - 1)]) != 95)))) else fieldName)),"{object}")
                    else:
                        value2 = StringTools.lpad("","*",HxOverrides.length(value))
                        setattr(obj,(("_hx_" + fieldName) if ((fieldName in python_Boot.keywords)) else (("_hx_" + fieldName) if (((((len(fieldName) > 2) and ((ord(fieldName[0]) == 95))) and ((ord(fieldName[1]) == 95))) and ((ord(fieldName[(len(fieldName) - 1)]) != 95)))) else fieldName)),value2)
                elif (((Type.typeof(value) == ValueType.TObject) or Std.isOfType(value,connect_util_Collection)) or Std.isOfType(value,list)):
                    value3 = connect_util_Masker.maskFields(value)
                    setattr(obj,(("_hx_" + fieldName) if ((fieldName in python_Boot.keywords)) else (("_hx_" + fieldName) if (((((len(fieldName) > 2) and ((ord(fieldName[0]) == 95))) and ((ord(fieldName[1]) == 95))) and ((ord(fieldName[(len(fieldName) - 1)]) != 95)))) else fieldName)),value3)
            return obj
        elif Std.isOfType(obj,list):
            arr = obj
            def _hx_local_2():
                def _hx_local_1(el):
                    return connect_util_Masker.maskFields(el)
                return list(map(_hx_local_1,arr))
            return _hx_local_2()
        return obj

    @staticmethod
    def maskParams(obj):
        if (Type.typeof(obj) == ValueType.TObject):
            connect_util_Masker.maskParamsInObject(obj)
        elif Std.isOfType(obj,list):
            def _hx_local_3():
                def _hx_local_0(el):
                    return connect_util_Masker.maskParams(el)
                def _hx_local_2():
                    _hx_local_1 = obj
                    if (Std.isOfType(_hx_local_1,list) or ((_hx_local_1 is None))):
                        _hx_local_1
                    else:
                        raise "Class cast error"
                    return _hx_local_1
                return list(map(_hx_local_0,_hx_local_2()))
            return _hx_local_3()
        return obj

    @staticmethod
    def maskParamsInObject(obj):
        maskedParams = connect_Env.getLogger().getMaskedParams()
        if (maskedParams.length() > 0):
            hasParameterField = python_Boot.hasField(obj,"parameter")
            _g = 0
            _g1 = python_Boot.fields(obj)
            while (_g < len(_g1)):
                fieldName = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                _g = (_g + 1)
                value = Reflect.field(obj,fieldName)
                if ((fieldName == "params") and Std.isOfType(value,list)):
                    connect_util_Masker.maskParamsArray(value,maskedParams)
                elif ((fieldName == "value") and hasParameterField):
                    connect_util_Masker.maskConfigParam(obj,Reflect.field(obj,"parameter"),maskedParams)
                elif (((Type.typeof(value) == ValueType.TObject) or Std.isOfType(value,connect_util_Collection)) or Std.isOfType(value,list)):
                    value1 = connect_util_Masker.maskParams(value)
                    setattr(obj,(("_hx_" + fieldName) if ((fieldName in python_Boot.keywords)) else (("_hx_" + fieldName) if (((((len(fieldName) > 2) and ((ord(fieldName[0]) == 95))) and ((ord(fieldName[1]) == 95))) and ((ord(fieldName[(len(fieldName) - 1)]) != 95)))) else fieldName)),value1)

    @staticmethod
    def maskParamsArray(arr,maskedParams):
        _g = 0
        while (_g < len(arr)):
            param = (arr[_g] if _g >= 0 and _g < len(arr) else None)
            _g = (_g + 1)
            if (((Type.typeof(param) == ValueType.TObject) and python_Boot.hasField(param,"id")) and python_Boot.hasField(param,"value")):
                isPassword = (python_Boot.hasField(param,"type") and ((Reflect.field(param,"type") == "password")))
                if ((maskedParams.indexOf(Std.string(Reflect.field(param,"id"))) != -1) or isPassword):
                    paramValue = Std.string(Reflect.field(param,"value"))
                    value = StringTools.lpad("","*",len(paramValue))
                    setattr(param,(("_hx_" + "value") if (("value" in python_Boot.keywords)) else (("_hx_" + "value") if (((((len("value") > 2) and ((ord("value"[0]) == 95))) and ((ord("value"[1]) == 95))) and ((ord("value"[(len("value") - 1)]) != 95)))) else "value")),value)

    @staticmethod
    def maskConfigParam(obj,configParam,maskedParams):
        if ((Type.typeof(configParam) == ValueType.TObject) and python_Boot.hasField(configParam,"id")):
            isPassword = (python_Boot.hasField(configParam,"type") and ((Reflect.field(configParam,"type") == "password")))
            if ((maskedParams.indexOf(Std.string(Reflect.field(configParam,"id"))) != -1) or isPassword):
                paramValue = Std.string(Reflect.field(obj,"value"))
                value = StringTools.lpad("","*",len(paramValue))
                setattr(obj,(("_hx_" + "value") if (("value" in python_Boot.keywords)) else (("_hx_" + "value") if (((((len("value") > 2) and ((ord("value"[0]) == 95))) and ((ord("value"[1]) == 95))) and ((ord("value"[(len("value") - 1)]) != 95)))) else "value")),value)
                if python_Boot.hasField(configParam,"value"):
                    paramValue = Std.string(Reflect.field(configParam,"value"))
                    value = StringTools.lpad("","*",len(paramValue))
                    setattr(configParam,(("_hx_" + "value") if (("value" in python_Boot.keywords)) else (("_hx_" + "value") if (((((len("value") > 2) and ((ord("value"[0]) == 95))) and ((ord("value"[1]) == 95))) and ((ord("value"[(len("value") - 1)]) != 95)))) else "value")),value)

    @staticmethod
    def replaceStrSensitiveData(text,regExData):
        regEx = regExData.iterator()
        while regEx.hasNext():
            regEx1 = regEx.next()
            while True:
                regEx1.matchObj = python_lib_Re.search(regEx1.pattern,text)
                if (not ((regEx1.matchObj is not None))):
                    break
                text = StringTools.replace(text,regEx1.matchObj.group(1),StringTools.lpad("","*",9))
        return text
connect_util_Masker._hx_class = connect_util_Masker
_hx_classes["connect.util.Masker"] = connect_util_Masker


class connect_util_Util:
    _hx_class_name = "connect.util.Util"
    __slots__ = ()
    _hx_statics = ["isJson", "isJsonObject", "isJsonArray", "isArray", "isStruct", "createObjectDiff", "addIdsToObject", "compactArray", "getLines", "boolToInt", "toRegEx"]

    @staticmethod
    def isJson(text):
        if (not connect_util_Util.isJsonObject(text)):
            return connect_util_Util.isJsonArray(text)
        else:
            return True

    @staticmethod
    def isJsonObject(text):
        _this = StringTools.trim(text)
        return ((("" if ((0 >= len(_this))) else _this[0])) == "{")

    @staticmethod
    def isJsonArray(text):
        _this = StringTools.trim(text)
        return ((("" if ((0 >= len(_this))) else _this[0])) == "[")

    @staticmethod
    def isArray(value):
        return Std.isOfType(value,list)

    @staticmethod
    def isStruct(value):
        return (Type.typeof(value) == ValueType.TObject)

    @staticmethod
    def createObjectDiff(object,previous):
        return connect_util_Util.addIdsToObject(connect_util_Diff(previous,object).apply(_hx_AnonObject({'id': Reflect.field(object,"id")})),previous)

    @staticmethod
    def addIdsToObject(object,original):
        out = _hx_AnonObject({})
        id = "id"
        if ((not python_Boot.hasField(object,id)) and python_Boot.hasField(original,id)):
            value = Reflect.field(original,id)
            setattr(out,(("_hx_" + id) if ((id in python_Boot.keywords)) else (("_hx_" + id) if (((((len(id) > 2) and ((ord(id[0]) == 95))) and ((ord(id[1]) == 95))) and ((ord(id[(len(id) - 1)]) != 95)))) else id)),value)
        _g = 0
        _g1 = python_Boot.fields(object)
        while (_g < len(_g1)):
            field = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            value = Reflect.field(object,field)
            if python_Boot.hasField(original,field):
                originalValue = Reflect.field(original,field)
                if (connect_util_Util.isStruct(value) and connect_util_Util.isStruct(originalValue)):
                    value1 = connect_util_Util.addIdsToObject(value,originalValue)
                    setattr(out,(("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field)),value1)
                elif (connect_util_Util.isArray(value) and connect_util_Util.isArray(originalValue)):
                    def _hx_local_2():
                        _hx_local_1 = value
                        if (Std.isOfType(_hx_local_1,list) or ((_hx_local_1 is None))):
                            _hx_local_1
                        else:
                            raise "Class cast error"
                        return _hx_local_1
                    valueArr = _hx_local_2()
                    def _hx_local_4():
                        _hx_local_3 = originalValue
                        if (Std.isOfType(_hx_local_3,list) or ((_hx_local_3 is None))):
                            _hx_local_3
                        else:
                            raise "Class cast error"
                        return _hx_local_3
                    originalValueArr = _hx_local_4()
                    value2 = connect_util_Util.compactArray(valueArr,originalValueArr)
                    setattr(out,(("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field)),value2)
                else:
                    setattr(out,(("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field)),value)
            else:
                setattr(out,(("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field)),value)
        return out

    @staticmethod
    def compactArray(array,second):
        out = []
        _g = 0
        _g1 = len(array)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            value = (array[i] if i >= 0 and i < len(array) else None)
            secondValue = (second[i] if i >= 0 and i < len(second) else None)
            if (connect_util_Util.isStruct(value) and connect_util_Util.isStruct(secondValue)):
                x = connect_util_Util.addIdsToObject(value,secondValue)
                out.append(x)
            elif (connect_util_Util.isArray(value) and connect_util_Util.isArray(secondValue)):
                def _hx_local_1():
                    _hx_local_0 = value
                    if (Std.isOfType(_hx_local_0,list) or ((_hx_local_0 is None))):
                        _hx_local_0
                    else:
                        raise "Class cast error"
                    return _hx_local_0
                valueArr = _hx_local_1()
                def _hx_local_3():
                    _hx_local_2 = secondValue
                    if (Std.isOfType(_hx_local_2,list) or ((_hx_local_2 is None))):
                        _hx_local_2
                    else:
                        raise "Class cast error"
                    return _hx_local_2
                secondValueArr = _hx_local_3()
                x1 = connect_util_Util.compactArray(valueArr,secondValueArr)
                out.append(x1)
            elif (value is not None):
                out.append(value)
        return out

    @staticmethod
    def getLines(text):
        windowsReplaced = StringTools.replace(Std.string(text),"\r\n","\n")
        macosReplaced = StringTools.replace(windowsReplaced,"\r","\n")
        return macosReplaced.split("\n")

    @staticmethod
    def boolToInt(b):
        if b:
            return 1
        else:
            return 0

    @staticmethod
    def toRegEx(expression):
        if (not expression.startswith("(")):
            expression = ("(" + ("null" if expression is None else expression))
        if (not expression.endswith(")")):
            expression = (("null" if expression is None else expression) + ")")
        return EReg(expression,"g")
connect_util_Util._hx_class = connect_util_Util
_hx_classes["connect.util.Util"] = connect_util_Util

class haxe_StackItem(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.StackItem"
    _hx_constructs = ["CFunction", "Module", "FilePos", "Method", "LocalFunction"]

    @staticmethod
    def Module(m):
        return haxe_StackItem("Module", 1, (m,))

    @staticmethod
    def FilePos(s,file,line,column = None):
        return haxe_StackItem("FilePos", 2, (s,file,line,column))

    @staticmethod
    def Method(classname,method):
        return haxe_StackItem("Method", 3, (classname,method))

    @staticmethod
    def LocalFunction(v = None):
        return haxe_StackItem("LocalFunction", 4, (v,))
haxe_StackItem.CFunction = haxe_StackItem("CFunction", 0, ())
haxe_StackItem._hx_class = haxe_StackItem
_hx_classes["haxe.StackItem"] = haxe_StackItem


class haxe__CallStack_CallStack_Impl_:
    _hx_class_name = "haxe._CallStack.CallStack_Impl_"
    __slots__ = ()
    _hx_statics = ["get_length", "callStack", "exceptionStack", "toString", "subtract", "copy", "get", "asArray", "equalItems", "exceptionToString", "itemToString"]
    length = None

    @staticmethod
    def get_length(this1):
        return len(this1)

    @staticmethod
    def callStack():
        infos = python_lib_Traceback.extract_stack()
        if (len(infos) != 0):
            infos.pop()
        infos.reverse()
        return haxe_NativeStackTrace.toHaxe(infos)

    @staticmethod
    def exceptionStack(fullStack = None):
        if (fullStack is None):
            fullStack = False
        eStack = haxe_NativeStackTrace.toHaxe(haxe_NativeStackTrace.exceptionStack())
        return (eStack if fullStack else haxe__CallStack_CallStack_Impl_.subtract(eStack,haxe__CallStack_CallStack_Impl_.callStack()))

    @staticmethod
    def toString(stack):
        b = StringBuf()
        _g = 0
        _g1 = stack
        while (_g < len(_g1)):
            s = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            b.b.write("\nCalled from ")
            haxe__CallStack_CallStack_Impl_.itemToString(b,s)
        return b.b.getvalue()

    @staticmethod
    def subtract(this1,stack):
        startIndex = -1
        i = -1
        while True:
            i = (i + 1)
            tmp = i
            if (not ((tmp < len(this1)))):
                break
            _g = 0
            _g1 = len(stack)
            while (_g < _g1):
                j = _g
                _g = (_g + 1)
                if haxe__CallStack_CallStack_Impl_.equalItems((this1[i] if i >= 0 and i < len(this1) else None),python_internal_ArrayImpl._get(stack, j)):
                    if (startIndex < 0):
                        startIndex = i
                    i = (i + 1)
                    if (i >= len(this1)):
                        break
                else:
                    startIndex = -1
            if (startIndex >= 0):
                break
        if (startIndex >= 0):
            return this1[0:startIndex]
        else:
            return this1

    @staticmethod
    def copy(this1):
        return list(this1)

    @staticmethod
    def get(this1,index):
        return (this1[index] if index >= 0 and index < len(this1) else None)

    @staticmethod
    def asArray(this1):
        return this1

    @staticmethod
    def equalItems(item1,item2):
        if (item1 is None):
            if (item2 is None):
                return True
            else:
                return False
        else:
            tmp = item1.index
            if (tmp == 0):
                if (item2 is None):
                    return False
                elif (item2.index == 0):
                    return True
                else:
                    return False
            elif (tmp == 1):
                if (item2 is None):
                    return False
                elif (item2.index == 1):
                    m2 = item2.params[0]
                    m1 = item1.params[0]
                    return (m1 == m2)
                else:
                    return False
            elif (tmp == 2):
                if (item2 is None):
                    return False
                elif (item2.index == 2):
                    item21 = item2.params[0]
                    file2 = item2.params[1]
                    line2 = item2.params[2]
                    col2 = item2.params[3]
                    col1 = item1.params[3]
                    line1 = item1.params[2]
                    file1 = item1.params[1]
                    item11 = item1.params[0]
                    if (((file1 == file2) and ((line1 == line2))) and ((col1 == col2))):
                        return haxe__CallStack_CallStack_Impl_.equalItems(item11,item21)
                    else:
                        return False
                else:
                    return False
            elif (tmp == 3):
                if (item2 is None):
                    return False
                elif (item2.index == 3):
                    class2 = item2.params[0]
                    method2 = item2.params[1]
                    method1 = item1.params[1]
                    class1 = item1.params[0]
                    if (class1 == class2):
                        return (method1 == method2)
                    else:
                        return False
                else:
                    return False
            elif (tmp == 4):
                if (item2 is None):
                    return False
                elif (item2.index == 4):
                    v2 = item2.params[0]
                    v1 = item1.params[0]
                    return (v1 == v2)
                else:
                    return False
            else:
                pass

    @staticmethod
    def exceptionToString(e):
        if (e.get_previous() is None):
            tmp = ("Exception: " + HxOverrides.stringOrNull(e.toString()))
            tmp1 = e.get_stack()
            return (("null" if tmp is None else tmp) + HxOverrides.stringOrNull((("null" if ((tmp1 is None)) else haxe__CallStack_CallStack_Impl_.toString(tmp1)))))
        result = ""
        e1 = e
        prev = None
        while (e1 is not None):
            if (prev is None):
                result1 = ("Exception: " + HxOverrides.stringOrNull(e1.get_message()))
                tmp = e1.get_stack()
                result = ((("null" if result1 is None else result1) + HxOverrides.stringOrNull((("null" if ((tmp is None)) else haxe__CallStack_CallStack_Impl_.toString(tmp))))) + ("null" if result is None else result))
            else:
                prevStack = haxe__CallStack_CallStack_Impl_.subtract(e1.get_stack(),prev.get_stack())
                result = (((("Exception: " + HxOverrides.stringOrNull(e1.get_message())) + HxOverrides.stringOrNull((("null" if ((prevStack is None)) else haxe__CallStack_CallStack_Impl_.toString(prevStack))))) + "\n\nNext ") + ("null" if result is None else result))
            prev = e1
            e1 = e1.get_previous()
        return result

    @staticmethod
    def itemToString(b,s):
        tmp = s.index
        if (tmp == 0):
            b.b.write("a C function")
        elif (tmp == 1):
            m = s.params[0]
            b.b.write("module ")
            s1 = Std.string(m)
            b.b.write(s1)
        elif (tmp == 2):
            s1 = s.params[0]
            file = s.params[1]
            line = s.params[2]
            col = s.params[3]
            if (s1 is not None):
                haxe__CallStack_CallStack_Impl_.itemToString(b,s1)
                b.b.write(" (")
            s2 = Std.string(file)
            b.b.write(s2)
            b.b.write(" line ")
            s2 = Std.string(line)
            b.b.write(s2)
            if (col is not None):
                b.b.write(" column ")
                s2 = Std.string(col)
                b.b.write(s2)
            if (s1 is not None):
                b.b.write(")")
        elif (tmp == 3):
            cname = s.params[0]
            meth = s.params[1]
            s1 = Std.string(("<unknown>" if ((cname is None)) else cname))
            b.b.write(s1)
            b.b.write(".")
            s1 = Std.string(meth)
            b.b.write(s1)
        elif (tmp == 4):
            n = s.params[0]
            b.b.write("local function #")
            s = Std.string(n)
            b.b.write(s)
        else:
            pass
haxe__CallStack_CallStack_Impl_._hx_class = haxe__CallStack_CallStack_Impl_
_hx_classes["haxe._CallStack.CallStack_Impl_"] = haxe__CallStack_CallStack_Impl_


class haxe_Exception(Exception):
    _hx_class_name = "haxe.Exception"
    __slots__ = ("_hx___exceptionStack", "_hx___nativeStack", "_hx___skipStack", "_hx___nativeException", "_hx___previousException")
    _hx_fields = ["__exceptionStack", "__nativeStack", "__skipStack", "__nativeException", "__previousException"]
    _hx_methods = ["unwrap", "toString", "details", "__shiftStack", "get_message", "get_previous", "get_native", "get_stack"]
    _hx_statics = ["caught", "thrown"]
    _hx_interfaces = []
    _hx_super = Exception


    def __init__(self,message,previous = None,native = None):
        self._hx___previousException = None
        self._hx___nativeException = None
        self._hx___nativeStack = None
        self._hx___exceptionStack = None
        self._hx___skipStack = 0
        super().__init__(message)
        self._hx___previousException = previous
        if ((native is not None) and Std.isOfType(native,BaseException)):
            self._hx___nativeException = native
            self._hx___nativeStack = haxe_NativeStackTrace.exceptionStack()
        else:
            self._hx___nativeException = self
            infos = python_lib_Traceback.extract_stack()
            if (len(infos) != 0):
                infos.pop()
            infos.reverse()
            self._hx___nativeStack = infos

    def unwrap(self):
        return self._hx___nativeException

    def toString(self):
        return self.get_message()

    def details(self):
        if (self.get_previous() is None):
            tmp = ("Exception: " + HxOverrides.stringOrNull(self.toString()))
            tmp1 = self.get_stack()
            return (("null" if tmp is None else tmp) + HxOverrides.stringOrNull((("null" if ((tmp1 is None)) else haxe__CallStack_CallStack_Impl_.toString(tmp1)))))
        else:
            result = ""
            e = self
            prev = None
            while (e is not None):
                if (prev is None):
                    result1 = ("Exception: " + HxOverrides.stringOrNull(e.get_message()))
                    tmp = e.get_stack()
                    result = ((("null" if result1 is None else result1) + HxOverrides.stringOrNull((("null" if ((tmp is None)) else haxe__CallStack_CallStack_Impl_.toString(tmp))))) + ("null" if result is None else result))
                else:
                    prevStack = haxe__CallStack_CallStack_Impl_.subtract(e.get_stack(),prev.get_stack())
                    result = (((("Exception: " + HxOverrides.stringOrNull(e.get_message())) + HxOverrides.stringOrNull((("null" if ((prevStack is None)) else haxe__CallStack_CallStack_Impl_.toString(prevStack))))) + "\n\nNext ") + ("null" if result is None else result))
                prev = e
                e = e.get_previous()
            return result

    def _hx___shiftStack(self):
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0._hx___skipStack
        _hx_local_0._hx___skipStack = (_hx_local_1 + 1)
        _hx_local_1

    def get_message(self):
        return str(self)

    def get_previous(self):
        return self._hx___previousException

    def get_native(self):
        return self._hx___nativeException

    def get_stack(self):
        _g = self._hx___exceptionStack
        if (_g is None):
            def _hx_local_1():
                def _hx_local_0():
                    self._hx___exceptionStack = haxe_NativeStackTrace.toHaxe(self._hx___nativeStack,self._hx___skipStack)
                    return self._hx___exceptionStack
                return _hx_local_0()
            return _hx_local_1()
        else:
            s = _g
            return s

    @staticmethod
    def caught(value):
        if Std.isOfType(value,haxe_Exception):
            return value
        elif Std.isOfType(value,BaseException):
            return haxe_Exception(str(value),None,value)
        else:
            return haxe_ValueException(value,None,value)

    @staticmethod
    def thrown(value):
        if Std.isOfType(value,haxe_Exception):
            return value.get_native()
        elif Std.isOfType(value,BaseException):
            return value
        else:
            e = haxe_ValueException(value)
            e._hx___skipStack = (e._hx___skipStack + 1)
            return e

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o._hx___exceptionStack = None
        _hx_o._hx___nativeStack = None
        _hx_o._hx___skipStack = None
        _hx_o._hx___nativeException = None
        _hx_o._hx___previousException = None
haxe_Exception._hx_class = haxe_Exception
_hx_classes["haxe.Exception"] = haxe_Exception


class haxe__Int32_Int32_Impl_:
    _hx_class_name = "haxe._Int32.Int32_Impl_"
    __slots__ = ()
    _hx_statics = ["negate", "preIncrement", "postIncrement", "preDecrement", "postDecrement", "add", "addInt", "sub", "subInt", "intSub", "mul", "mulInt", "complement", "or", "orInt", "xor", "xorInt", "shr", "shrInt", "intShr", "shl", "shlInt", "intShl", "toFloat", "ucompare", "clamp"]

    @staticmethod
    def negate(this1):
        return (((~this1 + 1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def preIncrement(this1):
        this1 = (this1 + 1)
        x = this1
        this1 = ((x + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        return this1

    @staticmethod
    def postIncrement(this1):
        ret = this1
        this1 = (this1 + 1)
        this1 = ((this1 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        return ret

    @staticmethod
    def preDecrement(this1):
        this1 = (this1 - 1)
        x = this1
        this1 = ((x + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        return this1

    @staticmethod
    def postDecrement(this1):
        ret = this1
        this1 = (this1 - 1)
        this1 = ((this1 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        return ret

    @staticmethod
    def add(a,b):
        return (((a + b) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def addInt(a,b):
        return (((a + b) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def sub(a,b):
        return (((a - b) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def subInt(a,b):
        return (((a - b) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def intSub(a,b):
        return (((a - b) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def mul(a,b):
        return ((((a * ((b & 65535))) + ((((((a * (HxOverrides.rshift(b, 16))) << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def mulInt(a,b):
        return haxe__Int32_Int32_Impl_.mul(a,b)

    @staticmethod
    def complement(a):
        return ((~a + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def _hx_or(a,b):
        return ((((a | b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def orInt(a,b):
        return ((((a | b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def xor(a,b):
        return ((((a ^ b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def xorInt(a,b):
        return ((((a ^ b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def shr(a,b):
        return ((((a >> b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def shrInt(a,b):
        return ((((a >> b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def intShr(a,b):
        return ((((a >> b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def shl(a,b):
        return ((((a << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def shlInt(a,b):
        return ((((a << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def intShl(a,b):
        return ((((a << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def toFloat(this1):
        return this1

    @staticmethod
    def ucompare(a,b):
        if (a < 0):
            if (b < 0):
                return (((((~b + (2 ** 31)) % (2 ** 32) - (2 ** 31)) - (((~a + (2 ** 31)) % (2 ** 32) - (2 ** 31)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            else:
                return 1
        if (b < 0):
            return -1
        else:
            return (((a - b) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def clamp(x):
        return ((x + (2 ** 31)) % (2 ** 32) - (2 ** 31))
haxe__Int32_Int32_Impl_._hx_class = haxe__Int32_Int32_Impl_
_hx_classes["haxe._Int32.Int32_Impl_"] = haxe__Int32_Int32_Impl_


class haxe__Int64_Int64_Impl_:
    _hx_class_name = "haxe._Int64.Int64_Impl_"
    __slots__ = ()
    _hx_statics = ["_new", "copy", "make", "ofInt", "toInt", "is", "isInt64", "getHigh", "getLow", "isNeg", "isZero", "compare", "ucompare", "toStr", "toString", "parseString", "fromFloat", "divMod", "neg", "preIncrement", "postIncrement", "preDecrement", "postDecrement", "add", "addInt", "sub", "subInt", "intSub", "mul", "mulInt", "div", "divInt", "intDiv", "mod", "modInt", "intMod", "eq", "eqInt", "neq", "neqInt", "lt", "ltInt", "intLt", "lte", "lteInt", "intLte", "gt", "gtInt", "intGt", "gte", "gteInt", "intGte", "complement", "and", "or", "xor", "shl", "shr", "ushr", "get_high", "set_high", "get_low", "set_low"]
    high = None
    low = None

    @staticmethod
    def _new(x):
        this1 = x
        return this1

    @staticmethod
    def copy(this1):
        this2 = haxe__Int64____Int64(this1.high,this1.low)
        return this2

    @staticmethod
    def make(high,low):
        this1 = haxe__Int64____Int64(high,low)
        return this1

    @staticmethod
    def ofInt(x):
        this1 = haxe__Int64____Int64((x >> 31),x)
        return this1

    @staticmethod
    def toInt(x):
        if (x.high != ((((x.low >> 31)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))):
            raise haxe_Exception.thrown("Overflow")
        return x.low

    @staticmethod
    def _hx_is(val):
        return Std.isOfType(val,haxe__Int64____Int64)

    @staticmethod
    def isInt64(val):
        return Std.isOfType(val,haxe__Int64____Int64)

    @staticmethod
    def getHigh(x):
        return x.high

    @staticmethod
    def getLow(x):
        return x.low

    @staticmethod
    def isNeg(x):
        return (x.high < 0)

    @staticmethod
    def isZero(x):
        b_high = 0
        b_low = 0
        if (x.high == b_high):
            return (x.low == b_low)
        else:
            return False

    @staticmethod
    def compare(a,b):
        v = (((a.high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a.low,b.low)
        if (a.high < 0):
            if (b.high < 0):
                return v
            else:
                return -1
        elif (b.high >= 0):
            return v
        else:
            return 1

    @staticmethod
    def ucompare(a,b):
        v = haxe__Int32_Int32_Impl_.ucompare(a.high,b.high)
        if (v != 0):
            return v
        else:
            return haxe__Int32_Int32_Impl_.ucompare(a.low,b.low)

    @staticmethod
    def toStr(x):
        return haxe__Int64_Int64_Impl_.toString(x)

    @staticmethod
    def toString(this1):
        i = this1
        b_high = 0
        b_low = 0
        if ((i.high == b_high) and ((i.low == b_low))):
            return "0"
        _hx_str = ""
        neg = False
        if (i.high < 0):
            neg = True
        this1 = haxe__Int64____Int64(0,10)
        ten = this1
        while True:
            b_high = 0
            b_low = 0
            if (not (((i.high != b_high) or ((i.low != b_low))))):
                break
            r = haxe__Int64_Int64_Impl_.divMod(i,ten)
            if (r.modulus.high < 0):
                x = r.modulus
                high = ((~x.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                low = (((~x.low + 1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                if (low == 0):
                    ret = high
                    high = (high + 1)
                    high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                this_high = high
                this_low = low
                _hx_str = (Std.string(this_low) + ("null" if _hx_str is None else _hx_str))
                x1 = r.quotient
                high1 = ((~x1.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                low1 = (((~x1.low + 1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                if (low1 == 0):
                    ret1 = high1
                    high1 = (high1 + 1)
                    high1 = ((high1 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                this1 = haxe__Int64____Int64(high1,low1)
                i = this1
            else:
                _hx_str = (Std.string(r.modulus.low) + ("null" if _hx_str is None else _hx_str))
                i = r.quotient
        if neg:
            _hx_str = ("-" + ("null" if _hx_str is None else _hx_str))
        return _hx_str

    @staticmethod
    def parseString(sParam):
        return haxe_Int64Helper.parseString(sParam)

    @staticmethod
    def fromFloat(f):
        return haxe_Int64Helper.fromFloat(f)

    @staticmethod
    def divMod(dividend,divisor):
        if (divisor.high == 0):
            _g = divisor.low
            if (_g == 0):
                raise haxe_Exception.thrown("divide by zero")
            elif (_g == 1):
                this1 = haxe__Int64____Int64(dividend.high,dividend.low)
                this2 = haxe__Int64____Int64(0,0)
                return _hx_AnonObject({'quotient': this1, 'modulus': this2})
            else:
                pass
        divSign = ((dividend.high < 0) != ((divisor.high < 0)))
        modulus = None
        if (dividend.high < 0):
            high = ((~dividend.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            low = (((~dividend.low + 1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            if (low == 0):
                ret = high
                high = (high + 1)
                high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            this1 = haxe__Int64____Int64(high,low)
            modulus = this1
        else:
            this1 = haxe__Int64____Int64(dividend.high,dividend.low)
            modulus = this1
        if (divisor.high < 0):
            high = ((~divisor.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            low = (((~divisor.low + 1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            if (low == 0):
                ret = high
                high = (high + 1)
                high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            this1 = haxe__Int64____Int64(high,low)
            divisor = this1
        this1 = haxe__Int64____Int64(0,0)
        quotient = this1
        this1 = haxe__Int64____Int64(0,1)
        mask = this1
        while (not ((divisor.high < 0))):
            v = haxe__Int32_Int32_Impl_.ucompare(divisor.high,modulus.high)
            cmp = (v if ((v != 0)) else haxe__Int32_Int32_Impl_.ucompare(divisor.low,modulus.low))
            b = 1
            b = (b & 63)
            if (b == 0):
                this1 = haxe__Int64____Int64(divisor.high,divisor.low)
                divisor = this1
            elif (b < 32):
                this2 = haxe__Int64____Int64(((((((((divisor.high << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(divisor.low, ((32 - b))))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((((divisor.low << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
                divisor = this2
            else:
                this3 = haxe__Int64____Int64(((((divisor.low << ((b - 32)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),0)
                divisor = this3
            b1 = 1
            b1 = (b1 & 63)
            if (b1 == 0):
                this4 = haxe__Int64____Int64(mask.high,mask.low)
                mask = this4
            elif (b1 < 32):
                this5 = haxe__Int64____Int64(((((((((mask.high << b1)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(mask.low, ((32 - b1))))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((((mask.low << b1)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
                mask = this5
            else:
                this6 = haxe__Int64____Int64(((((mask.low << ((b1 - 32)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),0)
                mask = this6
            if (cmp >= 0):
                break
        while True:
            b_high = 0
            b_low = 0
            if (not (((mask.high != b_high) or ((mask.low != b_low))))):
                break
            v = haxe__Int32_Int32_Impl_.ucompare(modulus.high,divisor.high)
            if (((v if ((v != 0)) else haxe__Int32_Int32_Impl_.ucompare(modulus.low,divisor.low))) >= 0):
                this1 = haxe__Int64____Int64(((((quotient.high | mask.high)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((((quotient.low | mask.low)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
                quotient = this1
                high = (((modulus.high - divisor.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                low = (((modulus.low - divisor.low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                if (haxe__Int32_Int32_Impl_.ucompare(modulus.low,divisor.low) < 0):
                    ret = high
                    high = (high - 1)
                    high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                this2 = haxe__Int64____Int64(high,low)
                modulus = this2
            b = 1
            b = (b & 63)
            if (b == 0):
                this3 = haxe__Int64____Int64(mask.high,mask.low)
                mask = this3
            elif (b < 32):
                this4 = haxe__Int64____Int64(HxOverrides.rshift(mask.high, b),((((((((mask.high << ((32 - b)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(mask.low, b))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
                mask = this4
            else:
                this5 = haxe__Int64____Int64(0,HxOverrides.rshift(mask.high, ((b - 32))))
                mask = this5
            b1 = 1
            b1 = (b1 & 63)
            if (b1 == 0):
                this6 = haxe__Int64____Int64(divisor.high,divisor.low)
                divisor = this6
            elif (b1 < 32):
                this7 = haxe__Int64____Int64(HxOverrides.rshift(divisor.high, b1),((((((((divisor.high << ((32 - b1)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(divisor.low, b1))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
                divisor = this7
            else:
                this8 = haxe__Int64____Int64(0,HxOverrides.rshift(divisor.high, ((b1 - 32))))
                divisor = this8
        if divSign:
            high = ((~quotient.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            low = (((~quotient.low + 1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            if (low == 0):
                ret = high
                high = (high + 1)
                high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            this1 = haxe__Int64____Int64(high,low)
            quotient = this1
        if (dividend.high < 0):
            high = ((~modulus.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            low = (((~modulus.low + 1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            if (low == 0):
                ret = high
                high = (high + 1)
                high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            this1 = haxe__Int64____Int64(high,low)
            modulus = this1
        return _hx_AnonObject({'quotient': quotient, 'modulus': modulus})

    @staticmethod
    def neg(x):
        high = ((~x.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((~x.low + 1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (low == 0):
            ret = high
            high = (high + 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        this1 = haxe__Int64____Int64(high,low)
        return this1

    @staticmethod
    def preIncrement(this1):
        this2 = haxe__Int64____Int64(this1.high,this1.low)
        this1 = this2
        def _hx_local_1():
            _hx_local_0 = this1.low
            this1.low = (this1.low + 1)
            return _hx_local_0
        ret = _hx_local_1()
        this1.low = ((this1.low + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (this1.low == 0):
            def _hx_local_3():
                _hx_local_2 = this1.high
                this1.high = (this1.high + 1)
                return _hx_local_2
            ret = _hx_local_3()
            this1.high = ((this1.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        return this1

    @staticmethod
    def postIncrement(this1):
        ret = this1
        this2 = haxe__Int64____Int64(this1.high,this1.low)
        this1 = this2
        def _hx_local_2():
            _hx_local_0 = this1
            _hx_local_1 = _hx_local_0.low
            _hx_local_0.low = (_hx_local_1 + 1)
            return _hx_local_1
        ret1 = _hx_local_2()
        this1.low = ((this1.low + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (this1.low == 0):
            def _hx_local_5():
                _hx_local_3 = this1
                _hx_local_4 = _hx_local_3.high
                _hx_local_3.high = (_hx_local_4 + 1)
                return _hx_local_4
            ret1 = _hx_local_5()
            this1.high = ((this1.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        return ret

    @staticmethod
    def preDecrement(this1):
        this2 = haxe__Int64____Int64(this1.high,this1.low)
        this1 = this2
        if (this1.low == 0):
            def _hx_local_1():
                _hx_local_0 = this1.high
                this1.high = (this1.high - 1)
                return _hx_local_0
            ret = _hx_local_1()
            this1.high = ((this1.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        def _hx_local_3():
            _hx_local_2 = this1.low
            this1.low = (this1.low - 1)
            return _hx_local_2
        ret = _hx_local_3()
        this1.low = ((this1.low + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        return this1

    @staticmethod
    def postDecrement(this1):
        ret = this1
        this2 = haxe__Int64____Int64(this1.high,this1.low)
        this1 = this2
        if (this1.low == 0):
            def _hx_local_2():
                _hx_local_0 = this1
                _hx_local_1 = _hx_local_0.high
                _hx_local_0.high = (_hx_local_1 - 1)
                return _hx_local_1
            ret1 = _hx_local_2()
            this1.high = ((this1.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        def _hx_local_5():
            _hx_local_3 = this1
            _hx_local_4 = _hx_local_3.low
            _hx_local_3.low = (_hx_local_4 - 1)
            return _hx_local_4
        ret1 = _hx_local_5()
        this1.low = ((this1.low + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        return ret

    @staticmethod
    def add(a,b):
        high = (((a.high + b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((a.low + b.low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (haxe__Int32_Int32_Impl_.ucompare(low,a.low) < 0):
            ret = high
            high = (high + 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        this1 = haxe__Int64____Int64(high,low)
        return this1

    @staticmethod
    def addInt(a,b):
        b_high = (b >> 31)
        b_low = b
        high = (((a.high + b_high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((a.low + b_low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (haxe__Int32_Int32_Impl_.ucompare(low,a.low) < 0):
            ret = high
            high = (high + 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        this1 = haxe__Int64____Int64(high,low)
        return this1

    @staticmethod
    def sub(a,b):
        high = (((a.high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((a.low - b.low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (haxe__Int32_Int32_Impl_.ucompare(a.low,b.low) < 0):
            ret = high
            high = (high - 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        this1 = haxe__Int64____Int64(high,low)
        return this1

    @staticmethod
    def subInt(a,b):
        b_high = (b >> 31)
        b_low = b
        high = (((a.high - b_high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((a.low - b_low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (haxe__Int32_Int32_Impl_.ucompare(a.low,b_low) < 0):
            ret = high
            high = (high - 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        this1 = haxe__Int64____Int64(high,low)
        return this1

    @staticmethod
    def intSub(a,b):
        a_high = (a >> 31)
        a_low = a
        high = (((a_high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((a_low - b.low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (haxe__Int32_Int32_Impl_.ucompare(a_low,b.low) < 0):
            ret = high
            high = (high - 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        this1 = haxe__Int64____Int64(high,low)
        return this1

    @staticmethod
    def mul(a,b):
        mask = 65535
        al = (a.low & mask)
        ah = HxOverrides.rshift(a.low, 16)
        bl = (b.low & mask)
        bh = HxOverrides.rshift(b.low, 16)
        p00 = haxe__Int32_Int32_Impl_.mul(al,bl)
        p10 = haxe__Int32_Int32_Impl_.mul(ah,bl)
        p01 = haxe__Int32_Int32_Impl_.mul(al,bh)
        p11 = haxe__Int32_Int32_Impl_.mul(ah,bh)
        low = p00
        high = ((((((p11 + (HxOverrides.rshift(p01, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) + (HxOverrides.rshift(p10, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        p01 = ((((p01 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((low + p01) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (haxe__Int32_Int32_Impl_.ucompare(low,p01) < 0):
            ret = high
            high = (high + 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        p10 = ((((p10 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((low + p10) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (haxe__Int32_Int32_Impl_.ucompare(low,p10) < 0):
            ret = high
            high = (high + 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        high = (((high + ((((haxe__Int32_Int32_Impl_.mul(a.low,b.high) + haxe__Int32_Int32_Impl_.mul(a.high,b.low)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        this1 = haxe__Int64____Int64(high,low)
        return this1

    @staticmethod
    def mulInt(a,b):
        b_high = (b >> 31)
        b_low = b
        mask = 65535
        al = (a.low & mask)
        ah = HxOverrides.rshift(a.low, 16)
        bl = (b_low & mask)
        bh = HxOverrides.rshift(b_low, 16)
        p00 = haxe__Int32_Int32_Impl_.mul(al,bl)
        p10 = haxe__Int32_Int32_Impl_.mul(ah,bl)
        p01 = haxe__Int32_Int32_Impl_.mul(al,bh)
        p11 = haxe__Int32_Int32_Impl_.mul(ah,bh)
        low = p00
        high = ((((((p11 + (HxOverrides.rshift(p01, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) + (HxOverrides.rshift(p10, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        p01 = ((((p01 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((low + p01) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (haxe__Int32_Int32_Impl_.ucompare(low,p01) < 0):
            ret = high
            high = (high + 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        p10 = ((((p10 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((low + p10) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (haxe__Int32_Int32_Impl_.ucompare(low,p10) < 0):
            ret = high
            high = (high + 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        high = (((high + ((((haxe__Int32_Int32_Impl_.mul(a.low,b_high) + haxe__Int32_Int32_Impl_.mul(a.high,b_low)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        this1 = haxe__Int64____Int64(high,low)
        return this1

    @staticmethod
    def div(a,b):
        return haxe__Int64_Int64_Impl_.divMod(a,b).quotient

    @staticmethod
    def divInt(a,b):
        this1 = haxe__Int64____Int64((b >> 31),b)
        return haxe__Int64_Int64_Impl_.divMod(a,this1).quotient

    @staticmethod
    def intDiv(a,b):
        this1 = haxe__Int64____Int64((a >> 31),a)
        x = haxe__Int64_Int64_Impl_.divMod(this1,b).quotient
        if (x.high != ((((x.low >> 31)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))):
            raise haxe_Exception.thrown("Overflow")
        x1 = x.low
        this1 = haxe__Int64____Int64((x1 >> 31),x1)
        return this1

    @staticmethod
    def mod(a,b):
        return haxe__Int64_Int64_Impl_.divMod(a,b).modulus

    @staticmethod
    def modInt(a,b):
        this1 = haxe__Int64____Int64((b >> 31),b)
        x = haxe__Int64_Int64_Impl_.divMod(a,this1).modulus
        if (x.high != ((((x.low >> 31)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))):
            raise haxe_Exception.thrown("Overflow")
        x1 = x.low
        this1 = haxe__Int64____Int64((x1 >> 31),x1)
        return this1

    @staticmethod
    def intMod(a,b):
        this1 = haxe__Int64____Int64((a >> 31),a)
        x = haxe__Int64_Int64_Impl_.divMod(this1,b).modulus
        if (x.high != ((((x.low >> 31)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))):
            raise haxe_Exception.thrown("Overflow")
        x1 = x.low
        this1 = haxe__Int64____Int64((x1 >> 31),x1)
        return this1

    @staticmethod
    def eq(a,b):
        if (a.high == b.high):
            return (a.low == b.low)
        else:
            return False

    @staticmethod
    def eqInt(a,b):
        b_high = (b >> 31)
        b_low = b
        if (a.high == b_high):
            return (a.low == b_low)
        else:
            return False

    @staticmethod
    def neq(a,b):
        if (a.high == b.high):
            return (a.low != b.low)
        else:
            return True

    @staticmethod
    def neqInt(a,b):
        b_high = (b >> 31)
        b_low = b
        if (a.high == b_high):
            return (a.low != b_low)
        else:
            return True

    @staticmethod
    def lt(a,b):
        v = (((a.high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a.low,b.low)
        return ((((v if ((b.high < 0)) else -1) if ((a.high < 0)) else (v if ((b.high >= 0)) else 1))) < 0)

    @staticmethod
    def ltInt(a,b):
        b_high = (b >> 31)
        b_low = b
        v = (((a.high - b_high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a.low,b_low)
        return ((((v if ((b_high < 0)) else -1) if ((a.high < 0)) else (v if ((b_high >= 0)) else 1))) < 0)

    @staticmethod
    def intLt(a,b):
        a_high = (a >> 31)
        a_low = a
        v = (((a_high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a_low,b.low)
        return ((((v if ((b.high < 0)) else -1) if ((a_high < 0)) else (v if ((b.high >= 0)) else 1))) < 0)

    @staticmethod
    def lte(a,b):
        v = (((a.high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a.low,b.low)
        return ((((v if ((b.high < 0)) else -1) if ((a.high < 0)) else (v if ((b.high >= 0)) else 1))) <= 0)

    @staticmethod
    def lteInt(a,b):
        b_high = (b >> 31)
        b_low = b
        v = (((a.high - b_high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a.low,b_low)
        return ((((v if ((b_high < 0)) else -1) if ((a.high < 0)) else (v if ((b_high >= 0)) else 1))) <= 0)

    @staticmethod
    def intLte(a,b):
        a_high = (a >> 31)
        a_low = a
        v = (((a_high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a_low,b.low)
        return ((((v if ((b.high < 0)) else -1) if ((a_high < 0)) else (v if ((b.high >= 0)) else 1))) <= 0)

    @staticmethod
    def gt(a,b):
        v = (((a.high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a.low,b.low)
        return ((((v if ((b.high < 0)) else -1) if ((a.high < 0)) else (v if ((b.high >= 0)) else 1))) > 0)

    @staticmethod
    def gtInt(a,b):
        b_high = (b >> 31)
        b_low = b
        v = (((a.high - b_high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a.low,b_low)
        return ((((v if ((b_high < 0)) else -1) if ((a.high < 0)) else (v if ((b_high >= 0)) else 1))) > 0)

    @staticmethod
    def intGt(a,b):
        a_high = (a >> 31)
        a_low = a
        v = (((a_high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a_low,b.low)
        return ((((v if ((b.high < 0)) else -1) if ((a_high < 0)) else (v if ((b.high >= 0)) else 1))) > 0)

    @staticmethod
    def gte(a,b):
        v = (((a.high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a.low,b.low)
        return ((((v if ((b.high < 0)) else -1) if ((a.high < 0)) else (v if ((b.high >= 0)) else 1))) >= 0)

    @staticmethod
    def gteInt(a,b):
        b_high = (b >> 31)
        b_low = b
        v = (((a.high - b_high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a.low,b_low)
        return ((((v if ((b_high < 0)) else -1) if ((a.high < 0)) else (v if ((b_high >= 0)) else 1))) >= 0)

    @staticmethod
    def intGte(a,b):
        a_high = (a >> 31)
        a_low = a
        v = (((a_high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a_low,b.low)
        return ((((v if ((b.high < 0)) else -1) if ((a_high < 0)) else (v if ((b.high >= 0)) else 1))) >= 0)

    @staticmethod
    def complement(a):
        this1 = haxe__Int64____Int64(((~a.high + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((~a.low + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
        return this1

    @staticmethod
    def _hx_and(a,b):
        this1 = haxe__Int64____Int64((a.high & b.high),(a.low & b.low))
        return this1

    @staticmethod
    def _hx_or(a,b):
        this1 = haxe__Int64____Int64(((((a.high | b.high)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((((a.low | b.low)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
        return this1

    @staticmethod
    def xor(a,b):
        this1 = haxe__Int64____Int64(((((a.high ^ b.high)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((((a.low ^ b.low)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
        return this1

    @staticmethod
    def shl(a,b):
        b = (b & 63)
        if (b == 0):
            this1 = haxe__Int64____Int64(a.high,a.low)
            return this1
        elif (b < 32):
            this1 = haxe__Int64____Int64(((((((((a.high << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(a.low, ((32 - b))))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((((a.low << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
            return this1
        else:
            this1 = haxe__Int64____Int64(((((a.low << ((b - 32)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),0)
            return this1

    @staticmethod
    def shr(a,b):
        b = (b & 63)
        if (b == 0):
            this1 = haxe__Int64____Int64(a.high,a.low)
            return this1
        elif (b < 32):
            this1 = haxe__Int64____Int64(((((a.high >> b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((((((((a.high << ((32 - b)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(a.low, b))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
            return this1
        else:
            this1 = haxe__Int64____Int64(((((a.high >> 31)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((((a.high >> ((b - 32)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
            return this1

    @staticmethod
    def ushr(a,b):
        b = (b & 63)
        if (b == 0):
            this1 = haxe__Int64____Int64(a.high,a.low)
            return this1
        elif (b < 32):
            this1 = haxe__Int64____Int64(HxOverrides.rshift(a.high, b),((((((((a.high << ((32 - b)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(a.low, b))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
            return this1
        else:
            this1 = haxe__Int64____Int64(0,HxOverrides.rshift(a.high, ((b - 32))))
            return this1

    @staticmethod
    def get_high(this1):
        return this1.high

    @staticmethod
    def set_high(this1,x):
        def _hx_local_1():
            def _hx_local_0():
                this1.high = x
                return this1.high
            return _hx_local_0()
        return _hx_local_1()

    @staticmethod
    def get_low(this1):
        return this1.low

    @staticmethod
    def set_low(this1,x):
        def _hx_local_1():
            def _hx_local_0():
                this1.low = x
                return this1.low
            return _hx_local_0()
        return _hx_local_1()
haxe__Int64_Int64_Impl_._hx_class = haxe__Int64_Int64_Impl_
_hx_classes["haxe._Int64.Int64_Impl_"] = haxe__Int64_Int64_Impl_


class haxe__Int64____Int64:
    _hx_class_name = "haxe._Int64.___Int64"
    __slots__ = ("high", "low")
    _hx_fields = ["high", "low"]
    _hx_methods = ["toString"]

    def __init__(self,high,low):
        self.high = high
        self.low = low

    def toString(self):
        return haxe__Int64_Int64_Impl_.toString(self)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.high = None
        _hx_o.low = None
haxe__Int64____Int64._hx_class = haxe__Int64____Int64
_hx_classes["haxe._Int64.___Int64"] = haxe__Int64____Int64


class haxe_Int64Helper:
    _hx_class_name = "haxe.Int64Helper"
    __slots__ = ()
    _hx_statics = ["parseString", "fromFloat"]

    @staticmethod
    def parseString(sParam):
        base_high = 0
        base_low = 10
        this1 = haxe__Int64____Int64(0,0)
        current = this1
        this1 = haxe__Int64____Int64(0,1)
        multiplier = this1
        sIsNegative = False
        s = StringTools.trim(sParam)
        if ((("" if ((0 >= len(s))) else s[0])) == "-"):
            sIsNegative = True
            s = HxString.substring(s,1,len(s))
        _hx_len = len(s)
        _g = 0
        _g1 = _hx_len
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            digitInt = (HxString.charCodeAt(s,((_hx_len - 1) - i)) - 48)
            if ((digitInt < 0) or ((digitInt > 9))):
                raise haxe_Exception.thrown("NumberFormatError")
            if (digitInt != 0):
                digit_high = (digitInt >> 31)
                digit_low = digitInt
                if sIsNegative:
                    mask = 65535
                    al = (multiplier.low & mask)
                    ah = HxOverrides.rshift(multiplier.low, 16)
                    bl = (digit_low & mask)
                    bh = HxOverrides.rshift(digit_low, 16)
                    p00 = haxe__Int32_Int32_Impl_.mul(al,bl)
                    p10 = haxe__Int32_Int32_Impl_.mul(ah,bl)
                    p01 = haxe__Int32_Int32_Impl_.mul(al,bh)
                    p11 = haxe__Int32_Int32_Impl_.mul(ah,bh)
                    low = p00
                    high = ((((((p11 + (HxOverrides.rshift(p01, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) + (HxOverrides.rshift(p10, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    p01 = ((((p01 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    low = (((low + p01) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    if (haxe__Int32_Int32_Impl_.ucompare(low,p01) < 0):
                        ret = high
                        high = (high + 1)
                        high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    p10 = ((((p10 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    low = (((low + p10) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    if (haxe__Int32_Int32_Impl_.ucompare(low,p10) < 0):
                        ret1 = high
                        high = (high + 1)
                        high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    high = (((high + ((((haxe__Int32_Int32_Impl_.mul(multiplier.low,digit_high) + haxe__Int32_Int32_Impl_.mul(multiplier.high,digit_low)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    b_high = high
                    b_low = low
                    high1 = (((current.high - b_high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    low1 = (((current.low - b_low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    if (haxe__Int32_Int32_Impl_.ucompare(current.low,b_low) < 0):
                        ret2 = high1
                        high1 = (high1 - 1)
                        high1 = ((high1 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    this1 = haxe__Int64____Int64(high1,low1)
                    current = this1
                    if (not ((current.high < 0))):
                        raise haxe_Exception.thrown("NumberFormatError: Underflow")
                else:
                    mask1 = 65535
                    al1 = (multiplier.low & mask1)
                    ah1 = HxOverrides.rshift(multiplier.low, 16)
                    bl1 = (digit_low & mask1)
                    bh1 = HxOverrides.rshift(digit_low, 16)
                    p001 = haxe__Int32_Int32_Impl_.mul(al1,bl1)
                    p101 = haxe__Int32_Int32_Impl_.mul(ah1,bl1)
                    p011 = haxe__Int32_Int32_Impl_.mul(al1,bh1)
                    p111 = haxe__Int32_Int32_Impl_.mul(ah1,bh1)
                    low2 = p001
                    high2 = ((((((p111 + (HxOverrides.rshift(p011, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) + (HxOverrides.rshift(p101, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    p011 = ((((p011 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    low2 = (((low2 + p011) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    if (haxe__Int32_Int32_Impl_.ucompare(low2,p011) < 0):
                        ret3 = high2
                        high2 = (high2 + 1)
                        high2 = ((high2 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    p101 = ((((p101 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    low2 = (((low2 + p101) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    if (haxe__Int32_Int32_Impl_.ucompare(low2,p101) < 0):
                        ret4 = high2
                        high2 = (high2 + 1)
                        high2 = ((high2 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    high2 = (((high2 + ((((haxe__Int32_Int32_Impl_.mul(multiplier.low,digit_high) + haxe__Int32_Int32_Impl_.mul(multiplier.high,digit_low)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    b_high1 = high2
                    b_low1 = low2
                    high3 = (((current.high + b_high1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    low3 = (((current.low + b_low1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    if (haxe__Int32_Int32_Impl_.ucompare(low3,current.low) < 0):
                        ret5 = high3
                        high3 = (high3 + 1)
                        high3 = ((high3 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    this2 = haxe__Int64____Int64(high3,low3)
                    current = this2
                    if (current.high < 0):
                        raise haxe_Exception.thrown("NumberFormatError: Overflow")
            mask2 = 65535
            al2 = (multiplier.low & mask2)
            ah2 = HxOverrides.rshift(multiplier.low, 16)
            bl2 = (base_low & mask2)
            bh2 = HxOverrides.rshift(base_low, 16)
            p002 = haxe__Int32_Int32_Impl_.mul(al2,bl2)
            p102 = haxe__Int32_Int32_Impl_.mul(ah2,bl2)
            p012 = haxe__Int32_Int32_Impl_.mul(al2,bh2)
            p112 = haxe__Int32_Int32_Impl_.mul(ah2,bh2)
            low4 = p002
            high4 = ((((((p112 + (HxOverrides.rshift(p012, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) + (HxOverrides.rshift(p102, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            p012 = ((((p012 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            low4 = (((low4 + p012) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            if (haxe__Int32_Int32_Impl_.ucompare(low4,p012) < 0):
                ret6 = high4
                high4 = (high4 + 1)
                high4 = ((high4 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            p102 = ((((p102 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            low4 = (((low4 + p102) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            if (haxe__Int32_Int32_Impl_.ucompare(low4,p102) < 0):
                ret7 = high4
                high4 = (high4 + 1)
                high4 = ((high4 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            high4 = (((high4 + ((((haxe__Int32_Int32_Impl_.mul(multiplier.low,base_high) + haxe__Int32_Int32_Impl_.mul(multiplier.high,base_low)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            this3 = haxe__Int64____Int64(high4,low4)
            multiplier = this3
        return current

    @staticmethod
    def fromFloat(f):
        if (python_lib_Math.isnan(f) or (not ((((f != Math.POSITIVE_INFINITY) and ((f != Math.NEGATIVE_INFINITY))) and (not python_lib_Math.isnan(f)))))):
            raise haxe_Exception.thrown("Number is NaN or Infinite")
        noFractions = (f - (HxOverrides.modf(f, 1)))
        if (noFractions > 9007199254740991):
            raise haxe_Exception.thrown("Conversion overflow")
        if (noFractions < -9007199254740991):
            raise haxe_Exception.thrown("Conversion underflow")
        this1 = haxe__Int64____Int64(0,0)
        result = this1
        neg = (noFractions < 0)
        rest = (-noFractions if neg else noFractions)
        i = 0
        while (rest >= 1):
            curr = HxOverrides.modf(rest, 2)
            rest = (rest / 2)
            if (curr >= 1):
                a_high = 0
                a_low = 1
                b = i
                b = (b & 63)
                b1 = None
                if (b == 0):
                    this1 = haxe__Int64____Int64(a_high,a_low)
                    b1 = this1
                elif (b < 32):
                    this2 = haxe__Int64____Int64(((((((((a_high << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(a_low, ((32 - b))))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((((a_low << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
                    b1 = this2
                else:
                    this3 = haxe__Int64____Int64(((((a_low << ((b - 32)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),0)
                    b1 = this3
                high = (((result.high + b1.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                low = (((result.low + b1.low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                if (haxe__Int32_Int32_Impl_.ucompare(low,result.low) < 0):
                    ret = high
                    high = (high + 1)
                    high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                this4 = haxe__Int64____Int64(high,low)
                result = this4
            i = (i + 1)
        if neg:
            high = ((~result.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            low = (((~result.low + 1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            if (low == 0):
                ret = high
                high = (high + 1)
                high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            this1 = haxe__Int64____Int64(high,low)
            result = this1
        return result
haxe_Int64Helper._hx_class = haxe_Int64Helper
_hx_classes["haxe.Int64Helper"] = haxe_Int64Helper


class haxe_Json:
    _hx_class_name = "haxe.Json"
    __slots__ = ()
    _hx_statics = ["parse", "stringify"]

    @staticmethod
    def parse(text):
        return python_lib_Json.loads(text,**python__KwArgs_KwArgs_Impl_.fromT(_hx_AnonObject({'object_hook': python_Lib.dictToAnon})))

    @staticmethod
    def stringify(value,replacer = None,space = None):
        return haxe_format_JsonPrinter.print(value,replacer,space)
haxe_Json._hx_class = haxe_Json
_hx_classes["haxe.Json"] = haxe_Json


class haxe_NativeStackTrace:
    _hx_class_name = "haxe.NativeStackTrace"
    __slots__ = ()
    _hx_statics = ["saveStack", "callStack", "exceptionStack", "toHaxe"]

    @staticmethod
    def saveStack(exception):
        pass

    @staticmethod
    def callStack():
        infos = python_lib_Traceback.extract_stack()
        if (len(infos) != 0):
            infos.pop()
        infos.reverse()
        return infos

    @staticmethod
    def exceptionStack():
        exc = python_lib_Sys.exc_info()
        if (exc[2] is not None):
            infos = python_lib_Traceback.extract_tb(exc[2])
            infos.reverse()
            return infos
        else:
            return []

    @staticmethod
    def toHaxe(native,skip = None):
        if (skip is None):
            skip = 0
        stack = []
        _g = 0
        _g1 = len(native)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if (skip > i):
                continue
            elem = (native[i] if i >= 0 and i < len(native) else None)
            x = haxe_StackItem.FilePos(haxe_StackItem.Method(None,elem[2]),elem[0],elem[1])
            stack.append(x)
        return stack
haxe_NativeStackTrace._hx_class = haxe_NativeStackTrace
_hx_classes["haxe.NativeStackTrace"] = haxe_NativeStackTrace


class haxe__Rest_Rest_Impl_:
    _hx_class_name = "haxe._Rest.Rest_Impl_"
    __slots__ = ()
    _hx_statics = ["get_length", "of", "_new", "get", "toArray", "iterator", "keyValueIterator", "append", "prepend", "toString"]
    length = None

    @staticmethod
    def get_length(this1):
        return len(this1)

    @staticmethod
    def of(array):
        this1 = array
        return this1

    @staticmethod
    def _new(array):
        this1 = array
        return this1

    @staticmethod
    def get(this1,index):
        return (this1[index] if index >= 0 and index < len(this1) else None)

    @staticmethod
    def toArray(this1):
        return list(this1)

    @staticmethod
    def iterator(this1):
        return haxe_iterators_RestIterator(this1)

    @staticmethod
    def keyValueIterator(this1):
        return haxe_iterators_RestKeyValueIterator(this1)

    @staticmethod
    def append(this1,item):
        result = list(this1)
        result.append(item)
        this1 = result
        return this1

    @staticmethod
    def prepend(this1,item):
        result = list(this1)
        result.insert(0, item)
        this1 = result
        return this1

    @staticmethod
    def toString(this1):
        return (("[" + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in this1]))) + "]")
haxe__Rest_Rest_Impl_._hx_class = haxe__Rest_Rest_Impl_
_hx_classes["haxe._Rest.Rest_Impl_"] = haxe__Rest_Rest_Impl_


class haxe_ValueException(haxe_Exception):
    _hx_class_name = "haxe.ValueException"
    __slots__ = ("value",)
    _hx_fields = ["value"]
    _hx_methods = ["unwrap"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_Exception


    def __init__(self,value,previous = None,native = None):
        self.value = None
        super().__init__(Std.string(value),previous,native)
        self.value = value
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0._hx___skipStack
        _hx_local_0._hx___skipStack = (_hx_local_1 + 1)
        _hx_local_1

    def unwrap(self):
        return self.value

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.value = None
haxe_ValueException._hx_class = haxe_ValueException
_hx_classes["haxe.ValueException"] = haxe_ValueException


class haxe_crypto_Crc32:
    _hx_class_name = "haxe.crypto.Crc32"
    __slots__ = ("crc",)
    _hx_fields = ["crc"]
    _hx_methods = ["byte", "update", "get"]
    _hx_statics = ["make"]

    def __init__(self):
        self.crc = -1

    def byte(self,b):
        tmp = (((self.crc ^ b)) & 255)
        tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
        tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
        tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
        tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
        tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
        tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
        tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
        tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
        self.crc = (HxOverrides.rshift(self.crc, 8) ^ tmp)

    def update(self,b,pos,_hx_len):
        b1 = b.b
        _g = pos
        _g1 = (pos + _hx_len)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            tmp = (((self.crc ^ b1[i])) & 255)
            tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
            tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
            tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
            tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
            tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
            tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
            tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
            tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
            self.crc = (HxOverrides.rshift(self.crc, 8) ^ tmp)

    def get(self):
        return (self.crc ^ -1)

    @staticmethod
    def make(data):
        c_crc = -1
        b = data.b
        _g = 0
        _g1 = data.length
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            tmp = (((c_crc ^ b[i])) & 255)
            tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
            tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
            tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
            tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
            tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
            tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
            tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
            tmp = (HxOverrides.rshift(tmp, 1) ^ ((-((tmp & 1)) & -306674912)))
            c_crc = (HxOverrides.rshift(c_crc, 8) ^ tmp)
        return (c_crc ^ -1)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.crc = None
haxe_crypto_Crc32._hx_class = haxe_crypto_Crc32
_hx_classes["haxe.crypto.Crc32"] = haxe_crypto_Crc32


class haxe_ds_ArraySort:
    _hx_class_name = "haxe.ds.ArraySort"
    __slots__ = ()
    _hx_statics = ["sort", "rec", "doMerge", "rotate", "gcd", "upper", "lower", "swap", "compare"]

    @staticmethod
    def sort(a,cmp):
        haxe_ds_ArraySort.rec(a,cmp,0,len(a))

    @staticmethod
    def rec(a,cmp,_hx_from,to):
        middle = ((_hx_from + to) >> 1)
        if ((to - _hx_from) < 12):
            if (to <= _hx_from):
                return
            _g = (_hx_from + 1)
            _g1 = to
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                j = i
                while (j > _hx_from):
                    if (cmp((a[j] if j >= 0 and j < len(a) else None),python_internal_ArrayImpl._get(a, (j - 1))) < 0):
                        haxe_ds_ArraySort.swap(a,(j - 1),j)
                    else:
                        break
                    j = (j - 1)
            return
        haxe_ds_ArraySort.rec(a,cmp,_hx_from,middle)
        haxe_ds_ArraySort.rec(a,cmp,middle,to)
        haxe_ds_ArraySort.doMerge(a,cmp,_hx_from,middle,to,(middle - _hx_from),(to - middle))

    @staticmethod
    def doMerge(a,cmp,_hx_from,pivot,to,len1,len2):
        first_cut = None
        second_cut = None
        len11 = None
        len22 = None
        if ((len1 == 0) or ((len2 == 0))):
            return
        if ((len1 + len2) == 2):
            if (cmp((a[pivot] if pivot >= 0 and pivot < len(a) else None),(a[_hx_from] if _hx_from >= 0 and _hx_from < len(a) else None)) < 0):
                haxe_ds_ArraySort.swap(a,pivot,_hx_from)
            return
        if (len1 > len2):
            len11 = (len1 >> 1)
            first_cut = (_hx_from + len11)
            second_cut = haxe_ds_ArraySort.lower(a,cmp,pivot,to,first_cut)
            len22 = (second_cut - pivot)
        else:
            len22 = (len2 >> 1)
            second_cut = (pivot + len22)
            first_cut = haxe_ds_ArraySort.upper(a,cmp,_hx_from,pivot,second_cut)
            len11 = (first_cut - _hx_from)
        haxe_ds_ArraySort.rotate(a,cmp,first_cut,pivot,second_cut)
        new_mid = (first_cut + len22)
        haxe_ds_ArraySort.doMerge(a,cmp,_hx_from,first_cut,new_mid,len11,len22)
        haxe_ds_ArraySort.doMerge(a,cmp,new_mid,second_cut,to,(len1 - len11),(len2 - len22))

    @staticmethod
    def rotate(a,cmp,_hx_from,mid,to):
        if ((_hx_from == mid) or ((mid == to))):
            return
        n = haxe_ds_ArraySort.gcd((to - _hx_from),(mid - _hx_from))
        while True:
            tmp = n
            n = (n - 1)
            if (not ((tmp != 0))):
                break
            val = python_internal_ArrayImpl._get(a, (_hx_from + n))
            shift = (mid - _hx_from)
            p1 = (_hx_from + n)
            p2 = ((_hx_from + n) + shift)
            while (p2 != ((_hx_from + n))):
                python_internal_ArrayImpl._set(a, p1, (a[p2] if p2 >= 0 and p2 < len(a) else None))
                p1 = p2
                if ((to - p2) > shift):
                    p2 = (p2 + shift)
                else:
                    p2 = (_hx_from + ((shift - ((to - p2)))))
            python_internal_ArrayImpl._set(a, p1, val)

    @staticmethod
    def gcd(m,n):
        while (n != 0):
            t = HxOverrides.mod(m, n)
            m = n
            n = t
        return m

    @staticmethod
    def upper(a,cmp,_hx_from,to,val):
        _hx_len = (to - _hx_from)
        half = None
        mid = None
        while (_hx_len > 0):
            half = (_hx_len >> 1)
            mid = (_hx_from + half)
            if (cmp((a[val] if val >= 0 and val < len(a) else None),(a[mid] if mid >= 0 and mid < len(a) else None)) < 0):
                _hx_len = half
            else:
                _hx_from = (mid + 1)
                _hx_len = ((_hx_len - half) - 1)
        return _hx_from

    @staticmethod
    def lower(a,cmp,_hx_from,to,val):
        _hx_len = (to - _hx_from)
        half = None
        mid = None
        while (_hx_len > 0):
            half = (_hx_len >> 1)
            mid = (_hx_from + half)
            if (cmp((a[mid] if mid >= 0 and mid < len(a) else None),(a[val] if val >= 0 and val < len(a) else None)) < 0):
                _hx_from = (mid + 1)
                _hx_len = ((_hx_len - half) - 1)
            else:
                _hx_len = half
        return _hx_from

    @staticmethod
    def swap(a,i,j):
        tmp = (a[i] if i >= 0 and i < len(a) else None)
        python_internal_ArrayImpl._set(a, i, (a[j] if j >= 0 and j < len(a) else None))
        python_internal_ArrayImpl._set(a, j, tmp)

    @staticmethod
    def compare(a,cmp,i,j):
        return cmp((a[i] if i >= 0 and i < len(a) else None),(a[j] if j >= 0 and j < len(a) else None))
haxe_ds_ArraySort._hx_class = haxe_ds_ArraySort
_hx_classes["haxe.ds.ArraySort"] = haxe_ds_ArraySort


class haxe_ds_BalancedTree:
    _hx_class_name = "haxe.ds.BalancedTree"
    __slots__ = ("root",)
    _hx_fields = ["root"]
    _hx_methods = ["set", "get", "remove", "exists", "iterator", "keyValueIterator", "keys", "copy", "setLoop", "removeLoop", "keysLoop", "merge", "minBinding", "removeMinBinding", "balance", "compare", "toString", "clear"]
    _hx_statics = ["iteratorLoop"]
    _hx_interfaces = [haxe_IMap]

    def __init__(self):
        self.root = None

    def set(self,key,value):
        self.root = self.setLoop(key,value,self.root)

    def get(self,key):
        node = self.root
        while (node is not None):
            c = self.compare(key,node.key)
            if (c == 0):
                return node.value
            if (c < 0):
                node = node.left
            else:
                node = node.right
        return None

    def remove(self,key):
        try:
            self.root = self.removeLoop(key,self.root)
            return True
        except BaseException as _g:
            None
            if Std.isOfType(haxe_Exception.caught(_g).unwrap(),str):
                return False
            else:
                raise _g

    def exists(self,key):
        node = self.root
        while (node is not None):
            c = self.compare(key,node.key)
            if (c == 0):
                return True
            elif (c < 0):
                node = node.left
            else:
                node = node.right
        return False

    def iterator(self):
        ret = []
        haxe_ds_BalancedTree.iteratorLoop(self.root,ret)
        return haxe_iterators_ArrayIterator(ret)

    def keyValueIterator(self):
        return haxe_iterators_MapKeyValueIterator(self)

    def keys(self):
        ret = []
        self.keysLoop(self.root,ret)
        return haxe_iterators_ArrayIterator(ret)

    def copy(self):
        copied = haxe_ds_BalancedTree()
        copied.root = self.root
        return copied

    def setLoop(self,k,v,node):
        if (node is None):
            return haxe_ds_TreeNode(None,k,v,None)
        c = self.compare(k,node.key)
        if (c == 0):
            return haxe_ds_TreeNode(node.left,k,v,node.right,(0 if ((node is None)) else node._height))
        elif (c < 0):
            nl = self.setLoop(k,v,node.left)
            return self.balance(nl,node.key,node.value,node.right)
        else:
            nr = self.setLoop(k,v,node.right)
            return self.balance(node.left,node.key,node.value,nr)

    def removeLoop(self,k,node):
        if (node is None):
            raise haxe_Exception.thrown("Not_found")
        c = self.compare(k,node.key)
        if (c == 0):
            return self.merge(node.left,node.right)
        elif (c < 0):
            return self.balance(self.removeLoop(k,node.left),node.key,node.value,node.right)
        else:
            return self.balance(node.left,node.key,node.value,self.removeLoop(k,node.right))

    def keysLoop(self,node,acc):
        if (node is not None):
            self.keysLoop(node.left,acc)
            x = node.key
            acc.append(x)
            self.keysLoop(node.right,acc)

    def merge(self,t1,t2):
        if (t1 is None):
            return t2
        if (t2 is None):
            return t1
        t = self.minBinding(t2)
        return self.balance(t1,t.key,t.value,self.removeMinBinding(t2))

    def minBinding(self,t):
        if (t is None):
            raise haxe_Exception.thrown("Not_found")
        elif (t.left is None):
            return t
        else:
            return self.minBinding(t.left)

    def removeMinBinding(self,t):
        if (t.left is None):
            return t.right
        else:
            return self.balance(self.removeMinBinding(t.left),t.key,t.value,t.right)

    def balance(self,l,k,v,r):
        hl = (0 if ((l is None)) else l._height)
        hr = (0 if ((r is None)) else r._height)
        if (hl > ((hr + 2))):
            _this = l.left
            _this1 = l.right
            if (((0 if ((_this is None)) else _this._height)) >= ((0 if ((_this1 is None)) else _this1._height))):
                return haxe_ds_TreeNode(l.left,l.key,l.value,haxe_ds_TreeNode(l.right,k,v,r))
            else:
                return haxe_ds_TreeNode(haxe_ds_TreeNode(l.left,l.key,l.value,l.right.left),l.right.key,l.right.value,haxe_ds_TreeNode(l.right.right,k,v,r))
        elif (hr > ((hl + 2))):
            _this = r.right
            _this1 = r.left
            if (((0 if ((_this is None)) else _this._height)) > ((0 if ((_this1 is None)) else _this1._height))):
                return haxe_ds_TreeNode(haxe_ds_TreeNode(l,k,v,r.left),r.key,r.value,r.right)
            else:
                return haxe_ds_TreeNode(haxe_ds_TreeNode(l,k,v,r.left.left),r.left.key,r.left.value,haxe_ds_TreeNode(r.left.right,r.key,r.value,r.right))
        else:
            return haxe_ds_TreeNode(l,k,v,r,(((hl if ((hl > hr)) else hr)) + 1))

    def compare(self,k1,k2):
        return Reflect.compare(k1,k2)

    def toString(self):
        if (self.root is None):
            return "{}"
        else:
            return (("{" + HxOverrides.stringOrNull(self.root.toString())) + "}")

    def clear(self):
        self.root = None

    @staticmethod
    def iteratorLoop(node,acc):
        if (node is not None):
            haxe_ds_BalancedTree.iteratorLoop(node.left,acc)
            x = node.value
            acc.append(x)
            haxe_ds_BalancedTree.iteratorLoop(node.right,acc)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.root = None
haxe_ds_BalancedTree._hx_class = haxe_ds_BalancedTree
_hx_classes["haxe.ds.BalancedTree"] = haxe_ds_BalancedTree


class haxe_ds_TreeNode:
    _hx_class_name = "haxe.ds.TreeNode"
    __slots__ = ("left", "right", "key", "value", "_height")
    _hx_fields = ["left", "right", "key", "value", "_height"]
    _hx_methods = ["toString"]

    def __init__(self,l,k,v,r,h = None):
        if (h is None):
            h = -1
        self._height = None
        self.left = l
        self.key = k
        self.value = v
        self.right = r
        if (h == -1):
            tmp = None
            _this = self.left
            _this1 = self.right
            if (((0 if ((_this is None)) else _this._height)) > ((0 if ((_this1 is None)) else _this1._height))):
                _this = self.left
                tmp = (0 if ((_this is None)) else _this._height)
            else:
                _this = self.right
                tmp = (0 if ((_this is None)) else _this._height)
            self._height = (tmp + 1)
        else:
            self._height = h

    def toString(self):
        return ((HxOverrides.stringOrNull((("" if ((self.left is None)) else (HxOverrides.stringOrNull(self.left.toString()) + ", ")))) + (((("" + Std.string(self.key)) + "=") + Std.string(self.value)))) + HxOverrides.stringOrNull((("" if ((self.right is None)) else (", " + HxOverrides.stringOrNull(self.right.toString()))))))

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.left = None
        _hx_o.right = None
        _hx_o.key = None
        _hx_o.value = None
        _hx_o._height = None
haxe_ds_TreeNode._hx_class = haxe_ds_TreeNode
_hx_classes["haxe.ds.TreeNode"] = haxe_ds_TreeNode


class haxe_ds_EnumValueMap(haxe_ds_BalancedTree):
    _hx_class_name = "haxe.ds.EnumValueMap"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["compare", "compareArgs", "compareArg", "copy"]
    _hx_statics = []
    _hx_interfaces = [haxe_IMap]
    _hx_super = haxe_ds_BalancedTree


    def __init__(self):
        super().__init__()

    def compare(self,k1,k2):
        d = (k1.index - k2.index)
        if (d != 0):
            return d
        p1 = list(k1.params)
        p2 = list(k2.params)
        if ((len(p1) == 0) and ((len(p2) == 0))):
            return 0
        return self.compareArgs(p1,p2)

    def compareArgs(self,a1,a2):
        ld = (len(a1) - len(a2))
        if (ld != 0):
            return ld
        _g = 0
        _g1 = len(a1)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            d = self.compareArg((a1[i] if i >= 0 and i < len(a1) else None),(a2[i] if i >= 0 and i < len(a2) else None))
            if (d != 0):
                return d
        return 0

    def compareArg(self,v1,v2):
        if (Reflect.isEnumValue(v1) and Reflect.isEnumValue(v2)):
            return self.compare(v1,v2)
        elif (Std.isOfType(v1,list) and Std.isOfType(v2,list)):
            return self.compareArgs(v1,v2)
        else:
            return Reflect.compare(v1,v2)

    def copy(self):
        copied = haxe_ds_EnumValueMap()
        copied.root = self.root
        return copied

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
haxe_ds_EnumValueMap._hx_class = haxe_ds_EnumValueMap
_hx_classes["haxe.ds.EnumValueMap"] = haxe_ds_EnumValueMap


class haxe_ds__HashMap_HashMap_Impl_:
    _hx_class_name = "haxe.ds._HashMap.HashMap_Impl_"
    __slots__ = ()
    _hx_statics = ["_new", "set", "get", "exists", "remove", "keys", "copy", "iterator", "keyValueIterator", "clear"]

    @staticmethod
    def _new():
        this1 = haxe_ds__HashMap_HashMapData()
        return this1

    @staticmethod
    def set(this1,k,v):
        this1.keys.set(k.hashCode(),k)
        this1.values.set(k.hashCode(),v)

    @staticmethod
    def get(this1,k):
        _this = this1.values
        key = k.hashCode()
        return _this.h.get(key,None)

    @staticmethod
    def exists(this1,k):
        _this = this1.values
        return (k.hashCode() in _this.h)

    @staticmethod
    def remove(this1,k):
        this1.values.remove(k.hashCode())
        return this1.keys.remove(k.hashCode())

    @staticmethod
    def keys(this1):
        return this1.keys.iterator()

    @staticmethod
    def copy(this1):
        copied = haxe_ds__HashMap_HashMapData()
        copied.keys = this1.keys.copy()
        copied.values = this1.values.copy()
        return copied

    @staticmethod
    def iterator(this1):
        return this1.values.iterator()

    @staticmethod
    def keyValueIterator(this1):
        return haxe_iterators_HashMapKeyValueIterator(this1)

    @staticmethod
    def clear(this1):
        this1.keys.h.clear()
        this1.values.h.clear()
haxe_ds__HashMap_HashMap_Impl_._hx_class = haxe_ds__HashMap_HashMap_Impl_
_hx_classes["haxe.ds._HashMap.HashMap_Impl_"] = haxe_ds__HashMap_HashMap_Impl_


class haxe_ds__HashMap_HashMapData:
    _hx_class_name = "haxe.ds._HashMap.HashMapData"
    __slots__ = ("keys", "values")
    _hx_fields = ["keys", "values"]

    def __init__(self):
        self.keys = haxe_ds_IntMap()
        self.values = haxe_ds_IntMap()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.keys = None
        _hx_o.values = None
haxe_ds__HashMap_HashMapData._hx_class = haxe_ds__HashMap_HashMapData
_hx_classes["haxe.ds._HashMap.HashMapData"] = haxe_ds__HashMap_HashMapData


class haxe_ds_IntMap:
    _hx_class_name = "haxe.ds.IntMap"
    __slots__ = ("h",)
    _hx_fields = ["h"]
    _hx_methods = ["set", "get", "exists", "remove", "keys", "iterator", "keyValueIterator", "copy", "toString", "clear"]
    _hx_interfaces = [haxe_IMap]

    def __init__(self):
        self.h = dict()

    def set(self,key,value):
        self.h[key] = value

    def get(self,key):
        return self.h.get(key,None)

    def exists(self,key):
        return (key in self.h)

    def remove(self,key):
        if (not (key in self.h)):
            return False
        del self.h[key]
        return True

    def keys(self):
        return python_HaxeIterator(iter(self.h.keys()))

    def iterator(self):
        return python_HaxeIterator(iter(self.h.values()))

    def keyValueIterator(self):
        return haxe_iterators_MapKeyValueIterator(self)

    def copy(self):
        copied = haxe_ds_IntMap()
        key = self.keys()
        while key.hasNext():
            key1 = key.next()
            copied.set(key1,self.h.get(key1,None))
        return copied

    def toString(self):
        s_b = python_lib_io_StringIO()
        s_b.write("{")
        it = self.keys()
        i = it
        while i.hasNext():
            i1 = i.next()
            s_b.write(Std.string(i1))
            s_b.write(" => ")
            s_b.write(Std.string(Std.string(self.h.get(i1,None))))
            if it.hasNext():
                s_b.write(", ")
        s_b.write("}")
        return s_b.getvalue()

    def clear(self):
        self.h.clear()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.h = None
haxe_ds_IntMap._hx_class = haxe_ds_IntMap
_hx_classes["haxe.ds.IntMap"] = haxe_ds_IntMap


class haxe_ds_List:
    _hx_class_name = "haxe.ds.List"
    __slots__ = ("h", "q", "length")
    _hx_fields = ["h", "q", "length"]
    _hx_methods = ["add", "push", "first", "last", "pop", "isEmpty", "clear", "remove", "iterator", "keyValueIterator", "toString", "join", "filter", "map"]

    def __init__(self):
        self.q = None
        self.h = None
        self.length = 0

    def add(self,item):
        x = haxe_ds__List_ListNode(item,None)
        if (self.h is None):
            self.h = x
        else:
            self.q.next = x
        self.q = x
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0.length
        _hx_local_0.length = (_hx_local_1 + 1)
        _hx_local_1

    def push(self,item):
        x = haxe_ds__List_ListNode(item,self.h)
        self.h = x
        if (self.q is None):
            self.q = x
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0.length
        _hx_local_0.length = (_hx_local_1 + 1)
        _hx_local_1

    def first(self):
        if (self.h is None):
            return None
        else:
            return self.h.item

    def last(self):
        if (self.q is None):
            return None
        else:
            return self.q.item

    def pop(self):
        if (self.h is None):
            return None
        x = self.h.item
        self.h = self.h.next
        if (self.h is None):
            self.q = None
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0.length
        _hx_local_0.length = (_hx_local_1 - 1)
        _hx_local_1
        return x

    def isEmpty(self):
        return (self.h is None)

    def clear(self):
        self.h = None
        self.q = None
        self.length = 0

    def remove(self,v):
        prev = None
        l = self.h
        while (l is not None):
            if HxOverrides.eq(l.item,v):
                if (prev is None):
                    self.h = l.next
                else:
                    prev.next = l.next
                if (self.q == l):
                    self.q = prev
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.length
                _hx_local_0.length = (_hx_local_1 - 1)
                _hx_local_1
                return True
            prev = l
            l = l.next
        return False

    def iterator(self):
        return haxe_ds__List_ListIterator(self.h)

    def keyValueIterator(self):
        return haxe_ds__List_ListKeyValueIterator(self.h)

    def toString(self):
        s_b = python_lib_io_StringIO()
        first = True
        l = self.h
        s_b.write("{")
        while (l is not None):
            if first:
                first = False
            else:
                s_b.write(", ")
            s_b.write(Std.string(Std.string(l.item)))
            l = l.next
        s_b.write("}")
        return s_b.getvalue()

    def join(self,sep):
        s_b = python_lib_io_StringIO()
        first = True
        l = self.h
        while (l is not None):
            if first:
                first = False
            else:
                s_b.write(Std.string(sep))
            s_b.write(Std.string(l.item))
            l = l.next
        return s_b.getvalue()

    def filter(self,f):
        l2 = haxe_ds_List()
        l = self.h
        while (l is not None):
            v = l.item
            l = l.next
            if f(v):
                l2.add(v)
        return l2

    def map(self,f):
        b = haxe_ds_List()
        l = self.h
        while (l is not None):
            v = l.item
            l = l.next
            b.add(f(v))
        return b

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.h = None
        _hx_o.q = None
        _hx_o.length = None
haxe_ds_List._hx_class = haxe_ds_List
_hx_classes["haxe.ds.List"] = haxe_ds_List


class haxe_ds__List_ListNode:
    _hx_class_name = "haxe.ds._List.ListNode"
    __slots__ = ("item", "next")
    _hx_fields = ["item", "next"]

    def __init__(self,item,next):
        self.item = item
        self.next = next

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.item = None
        _hx_o.next = None
haxe_ds__List_ListNode._hx_class = haxe_ds__List_ListNode
_hx_classes["haxe.ds._List.ListNode"] = haxe_ds__List_ListNode


class haxe_ds__List_ListIterator:
    _hx_class_name = "haxe.ds._List.ListIterator"
    __slots__ = ("head",)
    _hx_fields = ["head"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,head):
        self.head = head

    def hasNext(self):
        return (self.head is not None)

    def next(self):
        val = self.head.item
        self.head = self.head.next
        return val

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.head = None
haxe_ds__List_ListIterator._hx_class = haxe_ds__List_ListIterator
_hx_classes["haxe.ds._List.ListIterator"] = haxe_ds__List_ListIterator


class haxe_ds__List_ListKeyValueIterator:
    _hx_class_name = "haxe.ds._List.ListKeyValueIterator"
    __slots__ = ("idx", "head")
    _hx_fields = ["idx", "head"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,head):
        self.head = head
        self.idx = 0

    def hasNext(self):
        return (self.head is not None)

    def next(self):
        val = self.head.item
        self.head = self.head.next
        def _hx_local_3():
            def _hx_local_2():
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.idx
                _hx_local_0.idx = (_hx_local_1 + 1)
                return _hx_local_1
            return _hx_AnonObject({'value': val, 'key': _hx_local_2()})
        return _hx_local_3()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.idx = None
        _hx_o.head = None
haxe_ds__List_ListKeyValueIterator._hx_class = haxe_ds__List_ListKeyValueIterator
_hx_classes["haxe.ds._List.ListKeyValueIterator"] = haxe_ds__List_ListKeyValueIterator


class haxe_ds_ObjectMap:
    _hx_class_name = "haxe.ds.ObjectMap"
    __slots__ = ("h",)
    _hx_fields = ["h"]
    _hx_methods = ["set", "get", "exists", "remove", "keys", "iterator", "keyValueIterator", "copy", "toString", "clear"]
    _hx_interfaces = [haxe_IMap]

    def __init__(self):
        self.h = dict()

    def set(self,key,value):
        self.h[key] = value

    def get(self,key):
        return self.h.get(key,None)

    def exists(self,key):
        return (key in self.h)

    def remove(self,key):
        r = (key in self.h)
        if r:
            del self.h[key]
        return r

    def keys(self):
        return python_HaxeIterator(iter(self.h.keys()))

    def iterator(self):
        return python_HaxeIterator(iter(self.h.values()))

    def keyValueIterator(self):
        return haxe_iterators_MapKeyValueIterator(self)

    def copy(self):
        copied = haxe_ds_ObjectMap()
        key = self.keys()
        while key.hasNext():
            key1 = key.next()
            copied.set(key1,self.h.get(key1,None))
        return copied

    def toString(self):
        s_b = python_lib_io_StringIO()
        s_b.write("{")
        it = self.keys()
        i = it
        while i.hasNext():
            i1 = i.next()
            s_b.write(Std.string(Std.string(i1)))
            s_b.write(" => ")
            s_b.write(Std.string(Std.string(self.h.get(i1,None))))
            if it.hasNext():
                s_b.write(", ")
        s_b.write("}")
        return s_b.getvalue()

    def clear(self):
        self.h.clear()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.h = None
haxe_ds_ObjectMap._hx_class = haxe_ds_ObjectMap
_hx_classes["haxe.ds.ObjectMap"] = haxe_ds_ObjectMap


class haxe_ds__ReadOnlyArray_ReadOnlyArray_Impl_:
    _hx_class_name = "haxe.ds._ReadOnlyArray.ReadOnlyArray_Impl_"
    __slots__ = ()
    _hx_statics = ["get_length", "get", "concat"]
    length = None

    @staticmethod
    def get_length(this1):
        return len(this1)

    @staticmethod
    def get(this1,i):
        return (this1[i] if i >= 0 and i < len(this1) else None)

    @staticmethod
    def concat(this1,a):
        return (this1 + a)
haxe_ds__ReadOnlyArray_ReadOnlyArray_Impl_._hx_class = haxe_ds__ReadOnlyArray_ReadOnlyArray_Impl_
_hx_classes["haxe.ds._ReadOnlyArray.ReadOnlyArray_Impl_"] = haxe_ds__ReadOnlyArray_ReadOnlyArray_Impl_


class haxe_ds_WeakMap:
    _hx_class_name = "haxe.ds.WeakMap"
    __slots__ = ()
    _hx_methods = ["set", "get", "exists", "remove", "keys", "iterator", "keyValueIterator", "copy", "toString", "clear"]
    _hx_interfaces = [haxe_IMap]

    def __init__(self):
        raise haxe_exceptions_NotImplementedException("Not implemented for this platform",None,_hx_AnonObject({'fileName': "haxe/ds/WeakMap.hx", 'lineNumber': 39, 'className': "haxe.ds.WeakMap", 'methodName': "new"}))

    def set(self,key,value):
        pass

    def get(self,key):
        return None

    def exists(self,key):
        return False

    def remove(self,key):
        return False

    def keys(self):
        return None

    def iterator(self):
        return None

    def keyValueIterator(self):
        return None

    def copy(self):
        return None

    def toString(self):
        return None

    def clear(self):
        pass

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
haxe_ds_WeakMap._hx_class = haxe_ds_WeakMap
_hx_classes["haxe.ds.WeakMap"] = haxe_ds_WeakMap


class haxe_exceptions_PosException(haxe_Exception):
    _hx_class_name = "haxe.exceptions.PosException"
    __slots__ = ("posInfos",)
    _hx_fields = ["posInfos"]
    _hx_methods = ["toString"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_Exception


    def __init__(self,message,previous = None,pos = None):
        self.posInfos = None
        super().__init__(message,previous)
        if (pos is None):
            self.posInfos = _hx_AnonObject({'fileName': "(unknown)", 'lineNumber': 0, 'className': "(unknown)", 'methodName': "(unknown)"})
        else:
            self.posInfos = pos
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0._hx___skipStack
        _hx_local_0._hx___skipStack = (_hx_local_1 + 1)
        _hx_local_1

    def toString(self):
        return ((((((((("" + HxOverrides.stringOrNull(super().toString())) + " in ") + HxOverrides.stringOrNull(self.posInfos.className)) + ".") + HxOverrides.stringOrNull(self.posInfos.methodName)) + " at ") + HxOverrides.stringOrNull(self.posInfos.fileName)) + ":") + Std.string(self.posInfos.lineNumber))

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.posInfos = None
haxe_exceptions_PosException._hx_class = haxe_exceptions_PosException
_hx_classes["haxe.exceptions.PosException"] = haxe_exceptions_PosException


class haxe_exceptions_NotImplementedException(haxe_exceptions_PosException):
    _hx_class_name = "haxe.exceptions.NotImplementedException"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_exceptions_PosException


    def __init__(self,message = None,previous = None,pos = None):
        if (message is None):
            message = "Not implemented"
        super().__init__(message,previous,pos)
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0._hx___skipStack
        _hx_local_0._hx___skipStack = (_hx_local_1 + 1)
        _hx_local_1
haxe_exceptions_NotImplementedException._hx_class = haxe_exceptions_NotImplementedException
_hx_classes["haxe.exceptions.NotImplementedException"] = haxe_exceptions_NotImplementedException


class haxe_format_JsonPrinter:
    _hx_class_name = "haxe.format.JsonPrinter"
    __slots__ = ("buf", "replacer", "indent", "pretty", "nind")
    _hx_fields = ["buf", "replacer", "indent", "pretty", "nind"]
    _hx_methods = ["ipad", "newl", "write", "classString", "objString", "fieldsString", "quote"]
    _hx_statics = ["print"]

    def __init__(self,replacer,space):
        self.replacer = replacer
        self.indent = space
        self.pretty = (space is not None)
        self.nind = 0
        self.buf = StringBuf()

    def ipad(self):
        if self.pretty:
            v = StringTools.lpad("",self.indent,(self.nind * len(self.indent)))
            _this = self.buf
            s = Std.string(v)
            _this.b.write(s)

    def newl(self):
        if self.pretty:
            _this = self.buf
            s = "".join(map(chr,[10]))
            _this.b.write(s)

    def write(self,k,v):
        if (self.replacer is not None):
            v = self.replacer(k,v)
        _g = Type.typeof(v)
        tmp = _g.index
        if (tmp == 0):
            self.buf.b.write("null")
        elif (tmp == 1):
            _this = self.buf
            s = Std.string(v)
            _this.b.write(s)
        elif (tmp == 2):
            f = v
            v1 = (Std.string(v) if ((((f != Math.POSITIVE_INFINITY) and ((f != Math.NEGATIVE_INFINITY))) and (not python_lib_Math.isnan(f)))) else "null")
            _this = self.buf
            s = Std.string(v1)
            _this.b.write(s)
        elif (tmp == 3):
            _this = self.buf
            s = Std.string(v)
            _this.b.write(s)
        elif (tmp == 4):
            self.fieldsString(v,python_Boot.fields(v))
        elif (tmp == 5):
            self.buf.b.write("\"<fun>\"")
        elif (tmp == 6):
            c = _g.params[0]
            if (c == str):
                self.quote(v)
            elif (c == list):
                v1 = v
                _this = self.buf
                s = "".join(map(chr,[91]))
                _this.b.write(s)
                _hx_len = len(v1)
                last = (_hx_len - 1)
                _g1 = 0
                _g2 = _hx_len
                while (_g1 < _g2):
                    i = _g1
                    _g1 = (_g1 + 1)
                    if (i > 0):
                        _this = self.buf
                        s = "".join(map(chr,[44]))
                        _this.b.write(s)
                    else:
                        _hx_local_0 = self
                        _hx_local_1 = _hx_local_0.nind
                        _hx_local_0.nind = (_hx_local_1 + 1)
                        _hx_local_1
                    if self.pretty:
                        _this1 = self.buf
                        s1 = "".join(map(chr,[10]))
                        _this1.b.write(s1)
                    if self.pretty:
                        v2 = StringTools.lpad("",self.indent,(self.nind * len(self.indent)))
                        _this2 = self.buf
                        s2 = Std.string(v2)
                        _this2.b.write(s2)
                    self.write(i,(v1[i] if i >= 0 and i < len(v1) else None))
                    if (i == last):
                        _hx_local_2 = self
                        _hx_local_3 = _hx_local_2.nind
                        _hx_local_2.nind = (_hx_local_3 - 1)
                        _hx_local_3
                        if self.pretty:
                            _this3 = self.buf
                            s3 = "".join(map(chr,[10]))
                            _this3.b.write(s3)
                        if self.pretty:
                            v3 = StringTools.lpad("",self.indent,(self.nind * len(self.indent)))
                            _this4 = self.buf
                            s4 = Std.string(v3)
                            _this4.b.write(s4)
                _this = self.buf
                s = "".join(map(chr,[93]))
                _this.b.write(s)
            elif (c == haxe_ds_StringMap):
                v1 = v
                o = _hx_AnonObject({})
                k = v1.keys()
                while k.hasNext():
                    k1 = k.next()
                    value = v1.h.get(k1,None)
                    setattr(o,(("_hx_" + k1) if ((k1 in python_Boot.keywords)) else (("_hx_" + k1) if (((((len(k1) > 2) and ((ord(k1[0]) == 95))) and ((ord(k1[1]) == 95))) and ((ord(k1[(len(k1) - 1)]) != 95)))) else k1)),value)
                v1 = o
                self.fieldsString(v1,python_Boot.fields(v1))
            elif (c == Date):
                v1 = v
                self.quote(v1.toString())
            else:
                self.classString(v)
        elif (tmp == 7):
            _g1 = _g.params[0]
            i = v.index
            _this = self.buf
            s = Std.string(i)
            _this.b.write(s)
        elif (tmp == 8):
            self.buf.b.write("\"???\"")
        else:
            pass

    def classString(self,v):
        self.fieldsString(v,python_Boot.getInstanceFields(Type.getClass(v)))

    def objString(self,v):
        self.fieldsString(v,python_Boot.fields(v))

    def fieldsString(self,v,fields):
        _this = self.buf
        s = "".join(map(chr,[123]))
        _this.b.write(s)
        _hx_len = len(fields)
        last = (_hx_len - 1)
        first = True
        _g = 0
        _g1 = _hx_len
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            f = (fields[i] if i >= 0 and i < len(fields) else None)
            value = Reflect.field(v,f)
            if Reflect.isFunction(value):
                continue
            if first:
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.nind
                _hx_local_0.nind = (_hx_local_1 + 1)
                _hx_local_1
                first = False
            else:
                _this = self.buf
                s = "".join(map(chr,[44]))
                _this.b.write(s)
            if self.pretty:
                _this1 = self.buf
                s1 = "".join(map(chr,[10]))
                _this1.b.write(s1)
            if self.pretty:
                v1 = StringTools.lpad("",self.indent,(self.nind * len(self.indent)))
                _this2 = self.buf
                s2 = Std.string(v1)
                _this2.b.write(s2)
            self.quote(f)
            _this3 = self.buf
            s3 = "".join(map(chr,[58]))
            _this3.b.write(s3)
            if self.pretty:
                _this4 = self.buf
                s4 = "".join(map(chr,[32]))
                _this4.b.write(s4)
            self.write(f,value)
            if (i == last):
                _hx_local_2 = self
                _hx_local_3 = _hx_local_2.nind
                _hx_local_2.nind = (_hx_local_3 - 1)
                _hx_local_3
                if self.pretty:
                    _this5 = self.buf
                    s5 = "".join(map(chr,[10]))
                    _this5.b.write(s5)
                if self.pretty:
                    v2 = StringTools.lpad("",self.indent,(self.nind * len(self.indent)))
                    _this6 = self.buf
                    s6 = Std.string(v2)
                    _this6.b.write(s6)
        _this = self.buf
        s = "".join(map(chr,[125]))
        _this.b.write(s)

    def quote(self,s):
        _this = self.buf
        s1 = "".join(map(chr,[34]))
        _this.b.write(s1)
        i = 0
        length = len(s)
        while (i < length):
            index = i
            i = (i + 1)
            c = ord(s[index])
            c1 = c
            if (c1 == 8):
                self.buf.b.write("\\b")
            elif (c1 == 9):
                self.buf.b.write("\\t")
            elif (c1 == 10):
                self.buf.b.write("\\n")
            elif (c1 == 12):
                self.buf.b.write("\\f")
            elif (c1 == 13):
                self.buf.b.write("\\r")
            elif (c1 == 34):
                self.buf.b.write("\\\"")
            elif (c1 == 92):
                self.buf.b.write("\\\\")
            else:
                _this = self.buf
                s1 = "".join(map(chr,[c]))
                _this.b.write(s1)
        _this = self.buf
        s = "".join(map(chr,[34]))
        _this.b.write(s)

    @staticmethod
    def print(o,replacer = None,space = None):
        printer = haxe_format_JsonPrinter(replacer,space)
        printer.write("",o)
        return printer.buf.b.getvalue()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.buf = None
        _hx_o.replacer = None
        _hx_o.indent = None
        _hx_o.pretty = None
        _hx_o.nind = None
haxe_format_JsonPrinter._hx_class = haxe_format_JsonPrinter
_hx_classes["haxe.format.JsonPrinter"] = haxe_format_JsonPrinter


class haxe_io_ArrayBufferViewImpl:
    _hx_class_name = "haxe.io.ArrayBufferViewImpl"
    __slots__ = ("bytes", "byteOffset", "byteLength")
    _hx_fields = ["bytes", "byteOffset", "byteLength"]
    _hx_methods = ["sub", "subarray"]

    def __init__(self,_hx_bytes,pos,length):
        self.bytes = _hx_bytes
        self.byteOffset = pos
        self.byteLength = length

    def sub(self,begin,length = None):
        if (length is None):
            length = (self.byteLength - begin)
        if (((begin < 0) or ((length < 0))) or (((begin + length) > self.byteLength))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        return haxe_io_ArrayBufferViewImpl(self.bytes,(self.byteOffset + begin),length)

    def subarray(self,begin = None,end = None):
        if (begin is None):
            begin = 0
        if (end is None):
            end = (self.byteLength - begin)
        return self.sub(begin,(end - begin))

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.bytes = None
        _hx_o.byteOffset = None
        _hx_o.byteLength = None
haxe_io_ArrayBufferViewImpl._hx_class = haxe_io_ArrayBufferViewImpl
_hx_classes["haxe.io.ArrayBufferViewImpl"] = haxe_io_ArrayBufferViewImpl


class haxe_io__ArrayBufferView_ArrayBufferView_Impl_:
    _hx_class_name = "haxe.io._ArrayBufferView.ArrayBufferView_Impl_"
    __slots__ = ()
    _hx_statics = ["_new", "get_byteOffset", "get_byteLength", "get_buffer", "sub", "subarray", "getData", "fromData", "fromBytes"]
    buffer = None
    byteOffset = None
    byteLength = None

    @staticmethod
    def _new(size):
        this1 = haxe_io_ArrayBufferViewImpl(haxe_io_Bytes.alloc(size),0,size)
        return this1

    @staticmethod
    def get_byteOffset(this1):
        return this1.byteOffset

    @staticmethod
    def get_byteLength(this1):
        return this1.byteLength

    @staticmethod
    def get_buffer(this1):
        return this1.bytes

    @staticmethod
    def sub(this1,begin,length = None):
        return this1.sub(begin,length)

    @staticmethod
    def subarray(this1,begin = None,end = None):
        return this1.subarray(begin,end)

    @staticmethod
    def getData(this1):
        return this1

    @staticmethod
    def fromData(a):
        return a

    @staticmethod
    def fromBytes(_hx_bytes,pos = None,length = None):
        if (pos is None):
            pos = 0
        if (length is None):
            length = (_hx_bytes.length - pos)
        if (((pos < 0) or ((length < 0))) or (((pos + length) > _hx_bytes.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        return haxe_io_ArrayBufferViewImpl(_hx_bytes,pos,length)
haxe_io__ArrayBufferView_ArrayBufferView_Impl_._hx_class = haxe_io__ArrayBufferView_ArrayBufferView_Impl_
_hx_classes["haxe.io._ArrayBufferView.ArrayBufferView_Impl_"] = haxe_io__ArrayBufferView_ArrayBufferView_Impl_


class haxe_io_Bytes:
    _hx_class_name = "haxe.io.Bytes"
    __slots__ = ("length", "b")
    _hx_fields = ["length", "b"]
    _hx_methods = ["get", "set", "blit", "fill", "sub", "compare", "getDouble", "getFloat", "setDouble", "setFloat", "getUInt16", "setUInt16", "getInt32", "getInt64", "setInt32", "setInt64", "getString", "readString", "toString", "toHex", "getData"]
    _hx_statics = ["alloc", "ofString", "ofData", "ofHex", "fastGet"]

    def __init__(self,length,b):
        self.length = length
        self.b = b

    def get(self,pos):
        return self.b[pos]

    def set(self,pos,v):
        self.b[pos] = (v & 255)

    def blit(self,pos,src,srcpos,_hx_len):
        if (((((pos < 0) or ((srcpos < 0))) or ((_hx_len < 0))) or (((pos + _hx_len) > self.length))) or (((srcpos + _hx_len) > src.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        self.b[pos:pos+_hx_len] = src.b[srcpos:srcpos+_hx_len]

    def fill(self,pos,_hx_len,value):
        _g = 0
        _g1 = _hx_len
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            pos1 = pos
            pos = (pos + 1)
            self.b[pos1] = (value & 255)

    def sub(self,pos,_hx_len):
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > self.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        return haxe_io_Bytes(_hx_len,self.b[pos:(pos + _hx_len)])

    def compare(self,other):
        b1 = self.b
        b2 = other.b
        _hx_len = (self.length if ((self.length < other.length)) else other.length)
        _g = 0
        _g1 = _hx_len
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if (b1[i] != b2[i]):
                return (b1[i] - b2[i])
        return (self.length - other.length)

    def getDouble(self,pos):
        v = (((self.b[pos] | ((self.b[(pos + 1)] << 8))) | ((self.b[(pos + 2)] << 16))) | ((self.b[(pos + 3)] << 24)))
        pos1 = (pos + 4)
        v1 = (((self.b[pos1] | ((self.b[(pos1 + 1)] << 8))) | ((self.b[(pos1 + 2)] << 16))) | ((self.b[(pos1 + 3)] << 24)))
        return haxe_io_FPHelper.i64ToDouble(((v | -2147483648) if ((((v & -2147483648)) != 0)) else v),((v1 | -2147483648) if ((((v1 & -2147483648)) != 0)) else v1))

    def getFloat(self,pos):
        v = (((self.b[pos] | ((self.b[(pos + 1)] << 8))) | ((self.b[(pos + 2)] << 16))) | ((self.b[(pos + 3)] << 24)))
        return haxe_io_FPHelper.i32ToFloat(((v | -2147483648) if ((((v & -2147483648)) != 0)) else v))

    def setDouble(self,pos,v):
        i = haxe_io_FPHelper.doubleToI64(v)
        v = i.low
        self.b[pos] = (v & 255)
        self.b[(pos + 1)] = ((v >> 8) & 255)
        self.b[(pos + 2)] = ((v >> 16) & 255)
        self.b[(pos + 3)] = (HxOverrides.rshift(v, 24) & 255)
        pos1 = (pos + 4)
        v = i.high
        self.b[pos1] = (v & 255)
        self.b[(pos1 + 1)] = ((v >> 8) & 255)
        self.b[(pos1 + 2)] = ((v >> 16) & 255)
        self.b[(pos1 + 3)] = (HxOverrides.rshift(v, 24) & 255)

    def setFloat(self,pos,v):
        v1 = haxe_io_FPHelper.floatToI32(v)
        self.b[pos] = (v1 & 255)
        self.b[(pos + 1)] = ((v1 >> 8) & 255)
        self.b[(pos + 2)] = ((v1 >> 16) & 255)
        self.b[(pos + 3)] = (HxOverrides.rshift(v1, 24) & 255)

    def getUInt16(self,pos):
        return (self.b[pos] | ((self.b[(pos + 1)] << 8)))

    def setUInt16(self,pos,v):
        self.b[pos] = (v & 255)
        self.b[(pos + 1)] = ((v >> 8) & 255)

    def getInt32(self,pos):
        v = (((self.b[pos] | ((self.b[(pos + 1)] << 8))) | ((self.b[(pos + 2)] << 16))) | ((self.b[(pos + 3)] << 24)))
        if (((v & -2147483648)) != 0):
            return (v | -2147483648)
        else:
            return v

    def getInt64(self,pos):
        pos1 = (pos + 4)
        v = (((self.b[pos1] | ((self.b[(pos1 + 1)] << 8))) | ((self.b[(pos1 + 2)] << 16))) | ((self.b[(pos1 + 3)] << 24)))
        v1 = (((self.b[pos] | ((self.b[(pos + 1)] << 8))) | ((self.b[(pos + 2)] << 16))) | ((self.b[(pos + 3)] << 24)))
        this1 = haxe__Int64____Int64(((v | -2147483648) if ((((v & -2147483648)) != 0)) else v),((v1 | -2147483648) if ((((v1 & -2147483648)) != 0)) else v1))
        return this1

    def setInt32(self,pos,v):
        self.b[pos] = (v & 255)
        self.b[(pos + 1)] = ((v >> 8) & 255)
        self.b[(pos + 2)] = ((v >> 16) & 255)
        self.b[(pos + 3)] = (HxOverrides.rshift(v, 24) & 255)

    def setInt64(self,pos,v):
        v1 = v.low
        self.b[pos] = (v1 & 255)
        self.b[(pos + 1)] = ((v1 >> 8) & 255)
        self.b[(pos + 2)] = ((v1 >> 16) & 255)
        self.b[(pos + 3)] = (HxOverrides.rshift(v1, 24) & 255)
        pos1 = (pos + 4)
        v1 = v.high
        self.b[pos1] = (v1 & 255)
        self.b[(pos1 + 1)] = ((v1 >> 8) & 255)
        self.b[(pos1 + 2)] = ((v1 >> 16) & 255)
        self.b[(pos1 + 3)] = (HxOverrides.rshift(v1, 24) & 255)

    def getString(self,pos,_hx_len,encoding = None):
        tmp = (encoding is None)
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > self.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        return self.b[pos:pos+_hx_len].decode('UTF-8','replace')

    def readString(self,pos,_hx_len):
        return self.getString(pos,_hx_len)

    def toString(self):
        return self.getString(0,self.length)

    def toHex(self):
        s_b = python_lib_io_StringIO()
        chars = []
        _hx_str = "0123456789abcdef"
        _g = 0
        _g1 = len(_hx_str)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            x = HxString.charCodeAt(_hx_str,i)
            chars.append(x)
        _g = 0
        _g1 = self.length
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            c = self.b[i]
            s_b.write("".join(map(chr,[python_internal_ArrayImpl._get(chars, (c >> 4))])))
            s_b.write("".join(map(chr,[python_internal_ArrayImpl._get(chars, (c & 15))])))
        return s_b.getvalue()

    def getData(self):
        return self.b

    @staticmethod
    def alloc(length):
        return haxe_io_Bytes(length,bytearray(length))

    @staticmethod
    def ofString(s,encoding = None):
        b = bytearray(s,"UTF-8")
        return haxe_io_Bytes(len(b),b)

    @staticmethod
    def ofData(b):
        return haxe_io_Bytes(len(b),b)

    @staticmethod
    def ofHex(s):
        _hx_len = len(s)
        if (((_hx_len & 1)) != 0):
            raise haxe_Exception.thrown("Not a hex string (odd number of digits)")
        ret = haxe_io_Bytes.alloc((_hx_len >> 1))
        _g = 0
        _g1 = ret.length
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            index = (i * 2)
            high = (-1 if ((index >= len(s))) else ord(s[index]))
            index1 = ((i * 2) + 1)
            low = (-1 if ((index1 >= len(s))) else ord(s[index1]))
            high = (((high & 15)) + ((((((high & 64)) >> 6)) * 9)))
            low = (((low & 15)) + ((((((low & 64)) >> 6)) * 9)))
            ret.b[i] = (((((high << 4) | low)) & 255) & 255)
        return ret

    @staticmethod
    def fastGet(b,pos):
        return b[pos]

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.length = None
        _hx_o.b = None
haxe_io_Bytes._hx_class = haxe_io_Bytes
_hx_classes["haxe.io.Bytes"] = haxe_io_Bytes


class haxe_io_BytesBuffer:
    _hx_class_name = "haxe.io.BytesBuffer"
    __slots__ = ("b",)
    _hx_fields = ["b"]
    _hx_methods = ["get_length", "addByte", "add", "addString", "addInt32", "addInt64", "addFloat", "addDouble", "addBytes", "getBytes"]

    def __init__(self):
        self.b = bytearray()

    def get_length(self):
        return len(self.b)

    def addByte(self,byte):
        self.b.append(byte)

    def add(self,src):
        self.b.extend(src.b)

    def addString(self,v,encoding = None):
        self.b.extend(bytearray(v,"UTF-8"))

    def addInt32(self,v):
        self.b.append((v & 255))
        self.b.append(((v >> 8) & 255))
        self.b.append(((v >> 16) & 255))
        self.b.append(HxOverrides.rshift(v, 24))

    def addInt64(self,v):
        self.addInt32(v.low)
        self.addInt32(v.high)

    def addFloat(self,v):
        self.addInt32(haxe_io_FPHelper.floatToI32(v))

    def addDouble(self,v):
        self.addInt64(haxe_io_FPHelper.doubleToI64(v))

    def addBytes(self,src,pos,_hx_len):
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > src.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        self.b.extend(src.b[pos:(pos + _hx_len)])

    def getBytes(self):
        _hx_bytes = haxe_io_Bytes(len(self.b),self.b)
        self.b = None
        return _hx_bytes

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.b = None
haxe_io_BytesBuffer._hx_class = haxe_io_BytesBuffer
_hx_classes["haxe.io.BytesBuffer"] = haxe_io_BytesBuffer


class haxe_io_Input:
    _hx_class_name = "haxe.io.Input"
    __slots__ = ("bigEndian",)
    _hx_fields = ["bigEndian"]
    _hx_methods = ["readByte", "readBytes", "close", "set_bigEndian", "readAll", "readFullBytes", "read", "readUntil", "readLine", "readFloat", "readDouble", "readInt8", "readInt16", "readUInt16", "readInt24", "readUInt24", "readInt32", "readString", "getDoubleSig"]

    def readByte(self):
        raise haxe_exceptions_NotImplementedException(None,None,_hx_AnonObject({'fileName': "haxe/io/Input.hx", 'lineNumber': 53, 'className': "haxe.io.Input", 'methodName': "readByte"}))

    def readBytes(self,s,pos,_hx_len):
        k = _hx_len
        b = s.b
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > s.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        try:
            while (k > 0):
                b[pos] = self.readByte()
                pos = (pos + 1)
                k = (k - 1)
        except BaseException as _g:
            None
            if (not Std.isOfType(haxe_Exception.caught(_g).unwrap(),haxe_io_Eof)):
                raise _g
        return (_hx_len - k)

    def close(self):
        pass

    def set_bigEndian(self,b):
        self.bigEndian = b
        return b

    def readAll(self,bufsize = None):
        if (bufsize is None):
            bufsize = 16384
        buf = haxe_io_Bytes.alloc(bufsize)
        total = haxe_io_BytesBuffer()
        try:
            while True:
                _hx_len = self.readBytes(buf,0,bufsize)
                if (_hx_len == 0):
                    raise haxe_Exception.thrown(haxe_io_Error.Blocked)
                if ((_hx_len < 0) or ((_hx_len > buf.length))):
                    raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
                total.b.extend(buf.b[0:_hx_len])
        except BaseException as _g:
            None
            if (not Std.isOfType(haxe_Exception.caught(_g).unwrap(),haxe_io_Eof)):
                raise _g
        return total.getBytes()

    def readFullBytes(self,s,pos,_hx_len):
        while (_hx_len > 0):
            k = self.readBytes(s,pos,_hx_len)
            if (k == 0):
                raise haxe_Exception.thrown(haxe_io_Error.Blocked)
            pos = (pos + k)
            _hx_len = (_hx_len - k)

    def read(self,nbytes):
        s = haxe_io_Bytes.alloc(nbytes)
        p = 0
        while (nbytes > 0):
            k = self.readBytes(s,p,nbytes)
            if (k == 0):
                raise haxe_Exception.thrown(haxe_io_Error.Blocked)
            p = (p + k)
            nbytes = (nbytes - k)
        return s

    def readUntil(self,end):
        buf = haxe_io_BytesBuffer()
        last = None
        while True:
            last = self.readByte()
            if (not ((last != end))):
                break
            buf.b.append(last)
        return buf.getBytes().toString()

    def readLine(self):
        buf = haxe_io_BytesBuffer()
        last = None
        s = None
        try:
            while True:
                last = self.readByte()
                if (not ((last != 10))):
                    break
                buf.b.append(last)
            s = buf.getBytes().toString()
            if (HxString.charCodeAt(s,(len(s) - 1)) == 13):
                s = HxString.substr(s,0,-1)
        except BaseException as _g:
            None
            _g1 = haxe_Exception.caught(_g).unwrap()
            if Std.isOfType(_g1,haxe_io_Eof):
                e = _g1
                s = buf.getBytes().toString()
                if (len(s) == 0):
                    raise haxe_Exception.thrown(e)
            else:
                raise _g
        return s

    def readFloat(self):
        return haxe_io_FPHelper.i32ToFloat(self.readInt32())

    def readDouble(self):
        i1 = self.readInt32()
        i2 = self.readInt32()
        if self.bigEndian:
            return haxe_io_FPHelper.i64ToDouble(i2,i1)
        else:
            return haxe_io_FPHelper.i64ToDouble(i1,i2)

    def readInt8(self):
        n = self.readByte()
        if (n >= 128):
            return (n - 256)
        return n

    def readInt16(self):
        ch1 = self.readByte()
        ch2 = self.readByte()
        n = ((ch2 | ((ch1 << 8))) if (self.bigEndian) else (ch1 | ((ch2 << 8))))
        if (((n & 32768)) != 0):
            return (n - 65536)
        return n

    def readUInt16(self):
        ch1 = self.readByte()
        ch2 = self.readByte()
        if self.bigEndian:
            return (ch2 | ((ch1 << 8)))
        else:
            return (ch1 | ((ch2 << 8)))

    def readInt24(self):
        ch1 = self.readByte()
        ch2 = self.readByte()
        ch3 = self.readByte()
        n = (((ch3 | ((ch2 << 8))) | ((ch1 << 16))) if (self.bigEndian) else ((ch1 | ((ch2 << 8))) | ((ch3 << 16))))
        if (((n & 8388608)) != 0):
            return (n - 16777216)
        return n

    def readUInt24(self):
        ch1 = self.readByte()
        ch2 = self.readByte()
        ch3 = self.readByte()
        if self.bigEndian:
            return ((ch3 | ((ch2 << 8))) | ((ch1 << 16)))
        else:
            return ((ch1 | ((ch2 << 8))) | ((ch3 << 16)))

    def readInt32(self):
        ch1 = self.readByte()
        ch2 = self.readByte()
        ch3 = self.readByte()
        ch4 = self.readByte()
        n = ((((ch4 | ((ch3 << 8))) | ((ch2 << 16))) | ((ch1 << 24))) if (self.bigEndian) else (((ch1 | ((ch2 << 8))) | ((ch3 << 16))) | ((ch4 << 24))))
        if (((n & -2147483648)) != 0):
            return (n | -2147483648)
        else:
            return n

    def readString(self,_hx_len,encoding = None):
        b = haxe_io_Bytes.alloc(_hx_len)
        self.readFullBytes(b,0,_hx_len)
        return b.getString(0,_hx_len,encoding)

    def getDoubleSig(self,_hx_bytes):
        return ((((((((((_hx_bytes[1] if 1 < len(_hx_bytes) else None) & 15)) << 16) | (((_hx_bytes[2] if 2 < len(_hx_bytes) else None) << 8))) | (_hx_bytes[3] if 3 < len(_hx_bytes) else None))) * 4294967296.) + (((((_hx_bytes[4] if 4 < len(_hx_bytes) else None) >> 7)) * 2147483648))) + ((((((((_hx_bytes[4] if 4 < len(_hx_bytes) else None) & 127)) << 24) | (((_hx_bytes[5] if 5 < len(_hx_bytes) else None) << 16))) | (((_hx_bytes[6] if 6 < len(_hx_bytes) else None) << 8))) | (_hx_bytes[7] if 7 < len(_hx_bytes) else None))))

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.bigEndian = None
haxe_io_Input._hx_class = haxe_io_Input
_hx_classes["haxe.io.Input"] = haxe_io_Input


class haxe_io_BytesInput(haxe_io_Input):
    _hx_class_name = "haxe.io.BytesInput"
    __slots__ = ("b", "pos", "len", "totlen")
    _hx_fields = ["b", "pos", "len", "totlen"]
    _hx_methods = ["get_position", "get_length", "set_position", "readByte", "readBytes"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_io_Input


    def __init__(self,b,pos = None,_hx_len = None):
        if (pos is None):
            pos = 0
        if (_hx_len is None):
            _hx_len = (b.length - pos)
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > b.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        self.b = b.b
        self.pos = pos
        self.len = _hx_len
        self.totlen = _hx_len
        self.set_bigEndian(False)

    def get_position(self):
        return self.pos

    def get_length(self):
        return self.totlen

    def set_position(self,p):
        if (p < 0):
            p = 0
        elif (p > self.totlen):
            p = self.totlen
        self.len = (self.totlen - p)
        def _hx_local_1():
            def _hx_local_0():
                self.pos = p
                return self.pos
            return _hx_local_0()
        return _hx_local_1()

    def readByte(self):
        if (self.len == 0):
            raise haxe_Exception.thrown(haxe_io_Eof())
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0.len
        _hx_local_0.len = (_hx_local_1 - 1)
        _hx_local_1
        b = self.b[self.pos]
        _hx_local_2 = self
        _hx_local_3 = _hx_local_2.pos
        _hx_local_2.pos = (_hx_local_3 + 1)
        _hx_local_3
        return b

    def readBytes(self,buf,pos,_hx_len):
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > buf.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        if ((self.len == 0) and ((_hx_len > 0))):
            raise haxe_Exception.thrown(haxe_io_Eof())
        if (self.len < _hx_len):
            _hx_len = self.len
        b1 = self.b
        b2 = buf.b
        _g = 0
        _g1 = _hx_len
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            b2[(pos + i)] = b1[(self.pos + i)]
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0.pos
        _hx_local_0.pos = (_hx_local_1 + _hx_len)
        _hx_local_0.pos
        _hx_local_2 = self
        _hx_local_3 = _hx_local_2.len
        _hx_local_2.len = (_hx_local_3 - _hx_len)
        _hx_local_2.len
        return _hx_len

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.b = None
        _hx_o.pos = None
        _hx_o.len = None
        _hx_o.totlen = None
haxe_io_BytesInput._hx_class = haxe_io_BytesInput
_hx_classes["haxe.io.BytesInput"] = haxe_io_BytesInput


class haxe_io_Output:
    _hx_class_name = "haxe.io.Output"
    __slots__ = ("bigEndian",)
    _hx_fields = ["bigEndian"]
    _hx_methods = ["writeByte", "writeBytes", "flush", "close", "set_bigEndian", "write", "writeFullBytes", "writeFloat", "writeDouble", "writeInt8", "writeInt16", "writeUInt16", "writeInt24", "writeUInt24", "writeInt32", "prepare", "writeInput", "writeString"]

    def writeByte(self,c):
        raise haxe_exceptions_NotImplementedException(None,None,_hx_AnonObject({'fileName': "haxe/io/Output.hx", 'lineNumber': 47, 'className': "haxe.io.Output", 'methodName': "writeByte"}))

    def writeBytes(self,s,pos,_hx_len):
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > s.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        b = s.b
        k = _hx_len
        while (k > 0):
            self.writeByte(b[pos])
            pos = (pos + 1)
            k = (k - 1)
        return _hx_len

    def flush(self):
        pass

    def close(self):
        pass

    def set_bigEndian(self,b):
        self.bigEndian = b
        return b

    def write(self,s):
        l = s.length
        p = 0
        while (l > 0):
            k = self.writeBytes(s,p,l)
            if (k == 0):
                raise haxe_Exception.thrown(haxe_io_Error.Blocked)
            p = (p + k)
            l = (l - k)

    def writeFullBytes(self,s,pos,_hx_len):
        while (_hx_len > 0):
            k = self.writeBytes(s,pos,_hx_len)
            pos = (pos + k)
            _hx_len = (_hx_len - k)

    def writeFloat(self,x):
        self.writeInt32(haxe_io_FPHelper.floatToI32(x))

    def writeDouble(self,x):
        i64 = haxe_io_FPHelper.doubleToI64(x)
        if self.bigEndian:
            self.writeInt32(i64.high)
            self.writeInt32(i64.low)
        else:
            self.writeInt32(i64.low)
            self.writeInt32(i64.high)

    def writeInt8(self,x):
        if ((x < -128) or ((x >= 128))):
            raise haxe_Exception.thrown(haxe_io_Error.Overflow)
        self.writeByte((x & 255))

    def writeInt16(self,x):
        if ((x < -32768) or ((x >= 32768))):
            raise haxe_Exception.thrown(haxe_io_Error.Overflow)
        self.writeUInt16((x & 65535))

    def writeUInt16(self,x):
        if ((x < 0) or ((x >= 65536))):
            raise haxe_Exception.thrown(haxe_io_Error.Overflow)
        if self.bigEndian:
            self.writeByte((x >> 8))
            self.writeByte((x & 255))
        else:
            self.writeByte((x & 255))
            self.writeByte((x >> 8))

    def writeInt24(self,x):
        if ((x < -8388608) or ((x >= 8388608))):
            raise haxe_Exception.thrown(haxe_io_Error.Overflow)
        self.writeUInt24((x & 16777215))

    def writeUInt24(self,x):
        if ((x < 0) or ((x >= 16777216))):
            raise haxe_Exception.thrown(haxe_io_Error.Overflow)
        if self.bigEndian:
            self.writeByte((x >> 16))
            self.writeByte(((x >> 8) & 255))
            self.writeByte((x & 255))
        else:
            self.writeByte((x & 255))
            self.writeByte(((x >> 8) & 255))
            self.writeByte((x >> 16))

    def writeInt32(self,x):
        if self.bigEndian:
            self.writeByte(HxOverrides.rshift(x, 24))
            self.writeByte(((x >> 16) & 255))
            self.writeByte(((x >> 8) & 255))
            self.writeByte((x & 255))
        else:
            self.writeByte((x & 255))
            self.writeByte(((x >> 8) & 255))
            self.writeByte(((x >> 16) & 255))
            self.writeByte(HxOverrides.rshift(x, 24))

    def prepare(self,nbytes):
        pass

    def writeInput(self,i,bufsize = None):
        if (bufsize is None):
            bufsize = 4096
        buf = haxe_io_Bytes.alloc(bufsize)
        try:
            while True:
                _hx_len = i.readBytes(buf,0,bufsize)
                if (_hx_len == 0):
                    raise haxe_Exception.thrown(haxe_io_Error.Blocked)
                p = 0
                while (_hx_len > 0):
                    k = self.writeBytes(buf,p,_hx_len)
                    if (k == 0):
                        raise haxe_Exception.thrown(haxe_io_Error.Blocked)
                    p = (p + k)
                    _hx_len = (_hx_len - k)
        except BaseException as _g:
            None
            if (not Std.isOfType(haxe_Exception.caught(_g).unwrap(),haxe_io_Eof)):
                raise _g

    def writeString(self,s,encoding = None):
        b = haxe_io_Bytes.ofString(s,encoding)
        self.writeFullBytes(b,0,b.length)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.bigEndian = None
haxe_io_Output._hx_class = haxe_io_Output
_hx_classes["haxe.io.Output"] = haxe_io_Output


class haxe_io_BytesOutput(haxe_io_Output):
    _hx_class_name = "haxe.io.BytesOutput"
    __slots__ = ("b",)
    _hx_fields = ["b"]
    _hx_methods = ["get_length", "writeByte", "writeBytes", "getBytes"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_io_Output


    def __init__(self):
        self.b = haxe_io_BytesBuffer()
        self.set_bigEndian(False)

    def get_length(self):
        return len(self.b.b)

    def writeByte(self,c):
        self.b.b.append(c)

    def writeBytes(self,buf,pos,_hx_len):
        _this = self.b
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > buf.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        _this.b.extend(buf.b[pos:(pos + _hx_len)])
        return _hx_len

    def getBytes(self):
        return self.b.getBytes()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.b = None
haxe_io_BytesOutput._hx_class = haxe_io_BytesOutput
_hx_classes["haxe.io.BytesOutput"] = haxe_io_BytesOutput

class haxe_io_Encoding(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.io.Encoding"
    _hx_constructs = ["UTF8", "RawNative"]
haxe_io_Encoding.UTF8 = haxe_io_Encoding("UTF8", 0, ())
haxe_io_Encoding.RawNative = haxe_io_Encoding("RawNative", 1, ())
haxe_io_Encoding._hx_class = haxe_io_Encoding
_hx_classes["haxe.io.Encoding"] = haxe_io_Encoding


class haxe_io_Eof:
    _hx_class_name = "haxe.io.Eof"
    __slots__ = ()
    _hx_methods = ["toString"]

    def __init__(self):
        pass

    def toString(self):
        return "Eof"

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
haxe_io_Eof._hx_class = haxe_io_Eof
_hx_classes["haxe.io.Eof"] = haxe_io_Eof

class haxe_io_Error(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.io.Error"
    _hx_constructs = ["Blocked", "Overflow", "OutsideBounds", "Custom"]

    @staticmethod
    def Custom(e):
        return haxe_io_Error("Custom", 3, (e,))
haxe_io_Error.Blocked = haxe_io_Error("Blocked", 0, ())
haxe_io_Error.Overflow = haxe_io_Error("Overflow", 1, ())
haxe_io_Error.OutsideBounds = haxe_io_Error("OutsideBounds", 2, ())
haxe_io_Error._hx_class = haxe_io_Error
_hx_classes["haxe.io.Error"] = haxe_io_Error


class haxe_io_FPHelper:
    _hx_class_name = "haxe.io.FPHelper"
    __slots__ = ()
    _hx_statics = ["i64tmp", "LN2", "_i32ToFloat", "_i64ToDouble", "_floatToI32", "_doubleToI64", "i32ToFloat", "floatToI32", "i64ToDouble", "doubleToI64"]

    @staticmethod
    def _i32ToFloat(i):
        sign = (1 - ((HxOverrides.rshift(i, 31) << 1)))
        e = ((i >> 23) & 255)
        if (e == 255):
            if (((i & 8388607)) == 0):
                if (sign > 0):
                    return Math.POSITIVE_INFINITY
                else:
                    return Math.NEGATIVE_INFINITY
            else:
                return Math.NaN
        m = ((((i & 8388607)) << 1) if ((e == 0)) else ((i & 8388607) | 8388608))
        return ((sign * m) * Math.pow(2,(e - 150)))

    @staticmethod
    def _i64ToDouble(lo,hi):
        sign = (1 - ((HxOverrides.rshift(hi, 31) << 1)))
        e = ((hi >> 20) & 2047)
        if (e == 2047):
            if ((lo == 0) and ((((hi & 1048575)) == 0))):
                if (sign > 0):
                    return Math.POSITIVE_INFINITY
                else:
                    return Math.NEGATIVE_INFINITY
            else:
                return Math.NaN
        m = (2.220446049250313e-16 * ((((((hi & 1048575)) * 4294967296.) + (((HxOverrides.rshift(lo, 31)) * 2147483648.))) + ((lo & 2147483647)))))
        if (e == 0):
            m = (m * 2.0)
        else:
            m = (m + 1.0)
        return ((sign * m) * Math.pow(2,(e - 1023)))

    @staticmethod
    def _floatToI32(f):
        if (f == 0):
            return 0
        af = (-f if ((f < 0)) else f)
        exp = Math.floor((((Math.NEGATIVE_INFINITY if ((af == 0.0)) else (Math.NaN if ((af < 0.0)) else python_lib_Math.log(af)))) / 0.6931471805599453))
        if (exp > 127):
            return 2139095040
        else:
            if (exp <= -127):
                exp = -127
                af = (af * 7.1362384635298e+44)
            else:
                af = ((((af / Math.pow(2,exp)) - 1.0)) * 8388608)
            return ((((-2147483648 if ((f < 0)) else 0)) | (((exp + 127) << 23))) | Math.floor((af + 0.5)))

    @staticmethod
    def _doubleToI64(v):
        i64 = haxe_io_FPHelper.i64tmp
        if (v == 0):
            i64.low = 0
            i64.high = 0
        elif (not ((((v != Math.POSITIVE_INFINITY) and ((v != Math.NEGATIVE_INFINITY))) and (not python_lib_Math.isnan(v))))):
            i64.low = 0
            i64.high = (2146435072 if ((v > 0)) else -1048576)
        else:
            av = (-v if ((v < 0)) else v)
            exp = Math.floor((((Math.NEGATIVE_INFINITY if ((av == 0.0)) else (Math.NaN if ((av < 0.0)) else python_lib_Math.log(av)))) / 0.6931471805599453))
            if (exp > 1023):
                i64.low = -1
                i64.high = 2146435071
            else:
                if (exp <= -1023):
                    exp = -1023
                    av = (av / 2.2250738585072014e-308)
                else:
                    av = ((av / Math.pow(2,exp)) - 1.0)
                v1 = (av * 4503599627370496.)
                sig = (v1 if (((v1 == Math.POSITIVE_INFINITY) or ((v1 == Math.NEGATIVE_INFINITY)))) else (Math.NaN if (python_lib_Math.isnan(v1)) else Math.floor((v1 + 0.5))))
                sig_l = None
                try:
                    sig_l = int(sig)
                except BaseException as _g:
                    None
                    sig_l = None
                sig_l1 = sig_l
                sig_h = None
                try:
                    sig_h = int((sig / 4294967296.0))
                except BaseException as _g:
                    None
                    sig_h = None
                sig_h1 = sig_h
                i64.low = sig_l1
                i64.high = ((((-2147483648 if ((v < 0)) else 0)) | (((exp + 1023) << 20))) | sig_h1)
        return i64

    @staticmethod
    def i32ToFloat(i):
        sign = (1 - ((HxOverrides.rshift(i, 31) << 1)))
        e = ((i >> 23) & 255)
        if (e == 255):
            if (((i & 8388607)) == 0):
                if (sign > 0):
                    return Math.POSITIVE_INFINITY
                else:
                    return Math.NEGATIVE_INFINITY
            else:
                return Math.NaN
        else:
            m = ((((i & 8388607)) << 1) if ((e == 0)) else ((i & 8388607) | 8388608))
            return ((sign * m) * Math.pow(2,(e - 150)))

    @staticmethod
    def floatToI32(f):
        if (f == 0):
            return 0
        else:
            af = (-f if ((f < 0)) else f)
            exp = Math.floor((((Math.NEGATIVE_INFINITY if ((af == 0.0)) else (Math.NaN if ((af < 0.0)) else python_lib_Math.log(af)))) / 0.6931471805599453))
            if (exp > 127):
                return 2139095040
            else:
                if (exp <= -127):
                    exp = -127
                    af = (af * 7.1362384635298e+44)
                else:
                    af = ((((af / Math.pow(2,exp)) - 1.0)) * 8388608)
                return ((((-2147483648 if ((f < 0)) else 0)) | (((exp + 127) << 23))) | Math.floor((af + 0.5)))

    @staticmethod
    def i64ToDouble(low,high):
        sign = (1 - ((HxOverrides.rshift(high, 31) << 1)))
        e = ((high >> 20) & 2047)
        if (e == 2047):
            if ((low == 0) and ((((high & 1048575)) == 0))):
                if (sign > 0):
                    return Math.POSITIVE_INFINITY
                else:
                    return Math.NEGATIVE_INFINITY
            else:
                return Math.NaN
        else:
            m = (2.220446049250313e-16 * ((((((high & 1048575)) * 4294967296.) + (((HxOverrides.rshift(low, 31)) * 2147483648.))) + ((low & 2147483647)))))
            if (e == 0):
                m = (m * 2.0)
            else:
                m = (m + 1.0)
            return ((sign * m) * Math.pow(2,(e - 1023)))

    @staticmethod
    def doubleToI64(v):
        i64 = haxe_io_FPHelper.i64tmp
        if (v == 0):
            i64.low = 0
            i64.high = 0
        elif (not ((((v != Math.POSITIVE_INFINITY) and ((v != Math.NEGATIVE_INFINITY))) and (not python_lib_Math.isnan(v))))):
            i64.low = 0
            i64.high = (2146435072 if ((v > 0)) else -1048576)
        else:
            av = (-v if ((v < 0)) else v)
            exp = Math.floor((((Math.NEGATIVE_INFINITY if ((av == 0.0)) else (Math.NaN if ((av < 0.0)) else python_lib_Math.log(av)))) / 0.6931471805599453))
            if (exp > 1023):
                i64.low = -1
                i64.high = 2146435071
            else:
                if (exp <= -1023):
                    exp = -1023
                    av = (av / 2.2250738585072014e-308)
                else:
                    av = ((av / Math.pow(2,exp)) - 1.0)
                v1 = (av * 4503599627370496.)
                sig = (v1 if (((v1 == Math.POSITIVE_INFINITY) or ((v1 == Math.NEGATIVE_INFINITY)))) else (Math.NaN if (python_lib_Math.isnan(v1)) else Math.floor((v1 + 0.5))))
                sig_l = None
                try:
                    sig_l = int(sig)
                except BaseException as _g:
                    None
                    sig_l = None
                sig_l1 = sig_l
                sig_h = None
                try:
                    sig_h = int((sig / 4294967296.0))
                except BaseException as _g:
                    None
                    sig_h = None
                sig_h1 = sig_h
                i64.low = sig_l1
                i64.high = ((((-2147483648 if ((v < 0)) else 0)) | (((exp + 1023) << 20))) | sig_h1)
        return i64
haxe_io_FPHelper._hx_class = haxe_io_FPHelper
_hx_classes["haxe.io.FPHelper"] = haxe_io_FPHelper


class haxe_io_Path:
    _hx_class_name = "haxe.io.Path"
    __slots__ = ("dir", "file", "ext", "backslash")
    _hx_fields = ["dir", "file", "ext", "backslash"]
    _hx_methods = ["toString"]
    _hx_statics = ["withoutExtension", "withoutDirectory", "directory", "extension", "withExtension", "join", "normalize", "addTrailingSlash", "removeTrailingSlashes", "isAbsolute", "unescape", "escape"]

    def __init__(self,path):
        self.backslash = None
        self.ext = None
        self.file = None
        self.dir = None
        path1 = path
        _hx_local_0 = len(path1)
        if (_hx_local_0 == 1):
            if (path1 == "."):
                self.dir = path
                self.file = ""
                return
        elif (_hx_local_0 == 2):
            if (path1 == ".."):
                self.dir = path
                self.file = ""
                return
        else:
            pass
        startIndex = None
        c1 = None
        if (startIndex is None):
            c1 = path.rfind("/", 0, len(path))
        else:
            i = path.rfind("/", 0, (startIndex + 1))
            startLeft = (max(0,((startIndex + 1) - len("/"))) if ((i == -1)) else (i + 1))
            check = path.find("/", startLeft, len(path))
            c1 = (check if (((check > i) and ((check <= startIndex)))) else i)
        startIndex = None
        c2 = None
        if (startIndex is None):
            c2 = path.rfind("\\", 0, len(path))
        else:
            i = path.rfind("\\", 0, (startIndex + 1))
            startLeft = (max(0,((startIndex + 1) - len("\\"))) if ((i == -1)) else (i + 1))
            check = path.find("\\", startLeft, len(path))
            c2 = (check if (((check > i) and ((check <= startIndex)))) else i)
        if (c1 < c2):
            self.dir = HxString.substr(path,0,c2)
            path = HxString.substr(path,(c2 + 1),None)
            self.backslash = True
        elif (c2 < c1):
            self.dir = HxString.substr(path,0,c1)
            path = HxString.substr(path,(c1 + 1),None)
        else:
            self.dir = None
        startIndex = None
        cp = None
        if (startIndex is None):
            cp = path.rfind(".", 0, len(path))
        else:
            i = path.rfind(".", 0, (startIndex + 1))
            startLeft = (max(0,((startIndex + 1) - len("."))) if ((i == -1)) else (i + 1))
            check = path.find(".", startLeft, len(path))
            cp = (check if (((check > i) and ((check <= startIndex)))) else i)
        if (cp != -1):
            self.ext = HxString.substr(path,(cp + 1),None)
            self.file = HxString.substr(path,0,cp)
        else:
            self.ext = None
            self.file = path

    def toString(self):
        return ((HxOverrides.stringOrNull((("" if ((self.dir is None)) else (HxOverrides.stringOrNull(self.dir) + HxOverrides.stringOrNull((("\\" if (self.backslash) else "/"))))))) + HxOverrides.stringOrNull(self.file)) + HxOverrides.stringOrNull((("" if ((self.ext is None)) else ("." + HxOverrides.stringOrNull(self.ext))))))

    @staticmethod
    def withoutExtension(path):
        s = haxe_io_Path(path)
        s.ext = None
        return s.toString()

    @staticmethod
    def withoutDirectory(path):
        s = haxe_io_Path(path)
        s.dir = None
        return s.toString()

    @staticmethod
    def directory(path):
        s = haxe_io_Path(path)
        if (s.dir is None):
            return ""
        return s.dir

    @staticmethod
    def extension(path):
        s = haxe_io_Path(path)
        if (s.ext is None):
            return ""
        return s.ext

    @staticmethod
    def withExtension(path,ext):
        s = haxe_io_Path(path)
        s.ext = ext
        return s.toString()

    @staticmethod
    def join(paths):
        def _hx_local_0(s):
            if (s is not None):
                return (s != "")
            else:
                return False
        paths1 = list(filter(_hx_local_0,paths))
        if (len(paths1) == 0):
            return ""
        path = (paths1[0] if 0 < len(paths1) else None)
        _g = 1
        _g1 = len(paths1)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            path = haxe_io_Path.addTrailingSlash(path)
            path = (("null" if path is None else path) + HxOverrides.stringOrNull((paths1[i] if i >= 0 and i < len(paths1) else None)))
        return haxe_io_Path.normalize(path)

    @staticmethod
    def normalize(path):
        slash = "/"
        _this = path.split("\\")
        path = slash.join([python_Boot.toString1(x1,'') for x1 in _this])
        if (path == slash):
            return slash
        target = []
        _g = 0
        _g1 = (list(path) if ((slash == "")) else path.split(slash))
        while (_g < len(_g1)):
            token = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            if (((token == "..") and ((len(target) > 0))) and ((python_internal_ArrayImpl._get(target, (len(target) - 1)) != ".."))):
                if (len(target) != 0):
                    target.pop()
            elif (token == ""):
                if ((len(target) > 0) or ((HxString.charCodeAt(path,0) == 47))):
                    target.append(token)
            elif (token != "."):
                target.append(token)
        tmp = slash.join([python_Boot.toString1(x1,'') for x1 in target])
        acc_b = python_lib_io_StringIO()
        colon = False
        slashes = False
        _g = 0
        _g1 = len(tmp)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            _g2 = (-1 if ((i >= len(tmp))) else ord(tmp[i]))
            _g3 = _g2
            if (_g3 == 47):
                if (not colon):
                    slashes = True
                else:
                    i1 = _g2
                    colon = False
                    if slashes:
                        acc_b.write("/")
                        slashes = False
                    acc_b.write("".join(map(chr,[i1])))
            elif (_g3 == 58):
                acc_b.write(":")
                colon = True
            else:
                i2 = _g2
                colon = False
                if slashes:
                    acc_b.write("/")
                    slashes = False
                acc_b.write("".join(map(chr,[i2])))
        return acc_b.getvalue()

    @staticmethod
    def addTrailingSlash(path):
        if (len(path) == 0):
            return "/"
        startIndex = None
        c1 = None
        if (startIndex is None):
            c1 = path.rfind("/", 0, len(path))
        else:
            i = path.rfind("/", 0, (startIndex + 1))
            startLeft = (max(0,((startIndex + 1) - len("/"))) if ((i == -1)) else (i + 1))
            check = path.find("/", startLeft, len(path))
            c1 = (check if (((check > i) and ((check <= startIndex)))) else i)
        startIndex = None
        c2 = None
        if (startIndex is None):
            c2 = path.rfind("\\", 0, len(path))
        else:
            i = path.rfind("\\", 0, (startIndex + 1))
            startLeft = (max(0,((startIndex + 1) - len("\\"))) if ((i == -1)) else (i + 1))
            check = path.find("\\", startLeft, len(path))
            c2 = (check if (((check > i) and ((check <= startIndex)))) else i)
        if (c1 < c2):
            if (c2 != ((len(path) - 1))):
                return (("null" if path is None else path) + "\\")
            else:
                return path
        elif (c1 != ((len(path) - 1))):
            return (("null" if path is None else path) + "/")
        else:
            return path

    @staticmethod
    def removeTrailingSlashes(path):
        while True:
            _g = HxString.charCodeAt(path,(len(path) - 1))
            if (_g is None):
                break
            else:
                _g1 = _g
                if ((_g1 == 92) or ((_g1 == 47))):
                    path = HxString.substr(path,0,-1)
                else:
                    break
        return path

    @staticmethod
    def isAbsolute(path):
        if path.startswith("/"):
            return True
        if ((("" if ((1 >= len(path))) else path[1])) == ":"):
            return True
        if path.startswith("\\\\"):
            return True
        return False

    @staticmethod
    def unescape(path):
        regex = EReg("-x([0-9][0-9])","g")
        def _hx_local_1():
            def _hx_local_0(regex):
                code = Std.parseInt(regex.matchObj.group(1))
                return "".join(map(chr,[code]))
            return regex.map(path,_hx_local_0)
        return _hx_local_1()

    @staticmethod
    def escape(path,allowSlashes = None):
        if (allowSlashes is None):
            allowSlashes = False
        regex = (EReg("[^A-Za-z0-9_/\\\\\\.]","g") if allowSlashes else EReg("[^A-Za-z0-9_\\.]","g"))
        def _hx_local_1():
            def _hx_local_0(v):
                return ("-x" + Std.string(HxString.charCodeAt(v.matchObj.group(0),0)))
            return regex.map(path,_hx_local_0)
        return _hx_local_1()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.dir = None
        _hx_o.file = None
        _hx_o.ext = None
        _hx_o.backslash = None
haxe_io_Path._hx_class = haxe_io_Path
_hx_classes["haxe.io.Path"] = haxe_io_Path


class haxe_io__UInt8Array_UInt8Array_Impl_:
    _hx_class_name = "haxe.io._UInt8Array.UInt8Array_Impl_"
    __slots__ = ()
    _hx_statics = ["BYTES_PER_ELEMENT", "_new", "get_length", "get_view", "get", "set", "sub", "subarray", "getData", "fromData", "fromArray", "fromBytes"]
    length = None
    view = None

    @staticmethod
    def _new(elements):
        this1 = haxe_io_ArrayBufferViewImpl(haxe_io_Bytes.alloc(elements),0,elements)
        this2 = this1
        return this2

    @staticmethod
    def get_length(this1):
        return this1.byteLength

    @staticmethod
    def get_view(this1):
        return this1

    @staticmethod
    def get(this1,index):
        return this1.bytes.b[(index + this1.byteOffset)]

    @staticmethod
    def set(this1,index,value):
        if ((index >= 0) and ((index < this1.byteLength))):
            this1.bytes.b[(index + this1.byteOffset)] = (value & 255)
            return value
        return 0

    @staticmethod
    def sub(this1,begin,length = None):
        return haxe_io__UInt8Array_UInt8Array_Impl_.fromData(this1.sub(begin,length))

    @staticmethod
    def subarray(this1,begin = None,end = None):
        return haxe_io__UInt8Array_UInt8Array_Impl_.fromData(this1.subarray(begin,end))

    @staticmethod
    def getData(this1):
        return this1

    @staticmethod
    def fromData(d):
        return d

    @staticmethod
    def fromArray(a,pos = None,length = None):
        if (pos is None):
            pos = 0
        if (length is None):
            length = (len(a) - pos)
        if (((pos < 0) or ((length < 0))) or (((pos + length) > len(a)))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        elements = len(a)
        this1 = haxe_io_ArrayBufferViewImpl(haxe_io_Bytes.alloc(elements),0,elements)
        this2 = this1
        i = this2
        _g = 0
        _g1 = length
        while (_g < _g1):
            idx = _g
            _g = (_g + 1)
            value = python_internal_ArrayImpl._get(a, (idx + pos))
            if ((idx >= 0) and ((idx < i.byteLength))):
                i.bytes.b[(idx + i.byteOffset)] = (value & 255)
        return i

    @staticmethod
    def fromBytes(_hx_bytes,bytePos = None,length = None):
        if (bytePos is None):
            bytePos = 0
        return haxe_io__UInt8Array_UInt8Array_Impl_.fromData(haxe_io__ArrayBufferView_ArrayBufferView_Impl_.fromBytes(_hx_bytes,bytePos,length))
haxe_io__UInt8Array_UInt8Array_Impl_._hx_class = haxe_io__UInt8Array_UInt8Array_Impl_
_hx_classes["haxe.io._UInt8Array.UInt8Array_Impl_"] = haxe_io__UInt8Array_UInt8Array_Impl_


class haxe_iterators_ArrayIterator:
    _hx_class_name = "haxe.iterators.ArrayIterator"
    __slots__ = ("array", "current")
    _hx_fields = ["array", "current"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,array):
        self.current = 0
        self.array = array

    def hasNext(self):
        return (self.current < len(self.array))

    def next(self):
        def _hx_local_3():
            def _hx_local_2():
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.current
                _hx_local_0.current = (_hx_local_1 + 1)
                return _hx_local_1
            return python_internal_ArrayImpl._get(self.array, _hx_local_2())
        return _hx_local_3()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.array = None
        _hx_o.current = None
haxe_iterators_ArrayIterator._hx_class = haxe_iterators_ArrayIterator
_hx_classes["haxe.iterators.ArrayIterator"] = haxe_iterators_ArrayIterator


class haxe_iterators_ArrayKeyValueIterator:
    _hx_class_name = "haxe.iterators.ArrayKeyValueIterator"
    __slots__ = ("current", "array")
    _hx_fields = ["current", "array"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,array):
        self.current = 0
        self.array = array

    def hasNext(self):
        return (self.current < len(self.array))

    def next(self):
        def _hx_local_3():
            def _hx_local_2():
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.current
                _hx_local_0.current = (_hx_local_1 + 1)
                return _hx_local_1
            return _hx_AnonObject({'value': python_internal_ArrayImpl._get(self.array, self.current), 'key': _hx_local_2()})
        return _hx_local_3()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.current = None
        _hx_o.array = None
haxe_iterators_ArrayKeyValueIterator._hx_class = haxe_iterators_ArrayKeyValueIterator
_hx_classes["haxe.iterators.ArrayKeyValueIterator"] = haxe_iterators_ArrayKeyValueIterator


class haxe_iterators_HashMapKeyValueIterator:
    _hx_class_name = "haxe.iterators.HashMapKeyValueIterator"
    __slots__ = ("map", "keys")
    _hx_fields = ["map", "keys"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,_hx_map):
        self.map = _hx_map
        self.keys = _hx_map.keys.iterator()

    def hasNext(self):
        return self.keys.hasNext()

    def next(self):
        key = self.keys.next()
        _this = self.map.values
        key1 = key.hashCode()
        return _hx_AnonObject({'value': _this.h.get(key1,None), 'key': key})

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.map = None
        _hx_o.keys = None
haxe_iterators_HashMapKeyValueIterator._hx_class = haxe_iterators_HashMapKeyValueIterator
_hx_classes["haxe.iterators.HashMapKeyValueIterator"] = haxe_iterators_HashMapKeyValueIterator


class haxe_iterators_MapKeyValueIterator:
    _hx_class_name = "haxe.iterators.MapKeyValueIterator"
    __slots__ = ("map", "keys")
    _hx_fields = ["map", "keys"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,_hx_map):
        self.map = _hx_map
        self.keys = _hx_map.keys()

    def hasNext(self):
        return self.keys.hasNext()

    def next(self):
        key = self.keys.next()
        return _hx_AnonObject({'value': self.map.get(key), 'key': key})

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.map = None
        _hx_o.keys = None
haxe_iterators_MapKeyValueIterator._hx_class = haxe_iterators_MapKeyValueIterator
_hx_classes["haxe.iterators.MapKeyValueIterator"] = haxe_iterators_MapKeyValueIterator


class haxe_iterators_RestIterator:
    _hx_class_name = "haxe.iterators.RestIterator"
    __slots__ = ("args", "current")
    _hx_fields = ["args", "current"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,args):
        self.current = 0
        self.args = args

    def hasNext(self):
        return (self.current < len(self.args))

    def next(self):
        index = self.current
        self.current = (self.current + 1)
        return python_internal_ArrayImpl._get(self.args, index)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.args = None
        _hx_o.current = None
haxe_iterators_RestIterator._hx_class = haxe_iterators_RestIterator
_hx_classes["haxe.iterators.RestIterator"] = haxe_iterators_RestIterator


class haxe_iterators_RestKeyValueIterator:
    _hx_class_name = "haxe.iterators.RestKeyValueIterator"
    __slots__ = ("args", "current")
    _hx_fields = ["args", "current"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,args):
        self.current = 0
        self.args = args

    def hasNext(self):
        return (self.current < len(self.args))

    def next(self):
        tmp = self.current
        index = self.current
        self.current = (self.current + 1)
        return _hx_AnonObject({'key': tmp, 'value': python_internal_ArrayImpl._get(self.args, index)})

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.args = None
        _hx_o.current = None
haxe_iterators_RestKeyValueIterator._hx_class = haxe_iterators_RestKeyValueIterator
_hx_classes["haxe.iterators.RestKeyValueIterator"] = haxe_iterators_RestKeyValueIterator


class haxe_iterators_StringIterator:
    _hx_class_name = "haxe.iterators.StringIterator"
    __slots__ = ("offset", "s")
    _hx_fields = ["offset", "s"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,s):
        self.offset = 0
        self.s = s

    def hasNext(self):
        return (self.offset < len(self.s))

    def next(self):
        index = self.offset
        self.offset = (self.offset + 1)
        return ord(self.s[index])

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.offset = None
        _hx_o.s = None
haxe_iterators_StringIterator._hx_class = haxe_iterators_StringIterator
_hx_classes["haxe.iterators.StringIterator"] = haxe_iterators_StringIterator


class haxe_iterators_StringIteratorUnicode:
    _hx_class_name = "haxe.iterators.StringIteratorUnicode"
    __slots__ = ("offset", "s")
    _hx_fields = ["offset", "s"]
    _hx_methods = ["hasNext", "next"]
    _hx_statics = ["unicodeIterator"]

    def __init__(self,s):
        self.offset = 0
        self.s = s

    def hasNext(self):
        return (self.offset < len(self.s))

    def next(self):
        index = self.offset
        self.offset = (self.offset + 1)
        return ord(self.s[index])

    @staticmethod
    def unicodeIterator(s):
        return haxe_iterators_StringIteratorUnicode(s)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.offset = None
        _hx_o.s = None
haxe_iterators_StringIteratorUnicode._hx_class = haxe_iterators_StringIteratorUnicode
_hx_classes["haxe.iterators.StringIteratorUnicode"] = haxe_iterators_StringIteratorUnicode


class haxe_iterators_StringKeyValueIterator:
    _hx_class_name = "haxe.iterators.StringKeyValueIterator"
    __slots__ = ("offset", "s")
    _hx_fields = ["offset", "s"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,s):
        self.offset = 0
        self.s = s

    def hasNext(self):
        return (self.offset < len(self.s))

    def next(self):
        tmp = self.offset
        s = self.s
        index = self.offset
        self.offset = (self.offset + 1)
        return _hx_AnonObject({'key': tmp, 'value': (-1 if ((index >= len(s))) else ord(s[index]))})

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.offset = None
        _hx_o.s = None
haxe_iterators_StringKeyValueIterator._hx_class = haxe_iterators_StringKeyValueIterator
_hx_classes["haxe.iterators.StringKeyValueIterator"] = haxe_iterators_StringKeyValueIterator


class haxe_macro_Compiler:
    _hx_class_name = "haxe.macro.Compiler"
    __slots__ = ()
haxe_macro_Compiler._hx_class = haxe_macro_Compiler
_hx_classes["haxe.macro.Compiler"] = haxe_macro_Compiler

class haxe_macro_StringLiteralKind(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.StringLiteralKind"
    _hx_constructs = ["DoubleQuotes", "SingleQuotes"]
haxe_macro_StringLiteralKind.DoubleQuotes = haxe_macro_StringLiteralKind("DoubleQuotes", 0, ())
haxe_macro_StringLiteralKind.SingleQuotes = haxe_macro_StringLiteralKind("SingleQuotes", 1, ())
haxe_macro_StringLiteralKind._hx_class = haxe_macro_StringLiteralKind
_hx_classes["haxe.macro.StringLiteralKind"] = haxe_macro_StringLiteralKind

class haxe_macro_Constant(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.Constant"
    _hx_constructs = ["CInt", "CFloat", "CString", "CIdent", "CRegexp"]

    @staticmethod
    def CInt(v):
        return haxe_macro_Constant("CInt", 0, (v,))

    @staticmethod
    def CFloat(f):
        return haxe_macro_Constant("CFloat", 1, (f,))

    @staticmethod
    def CString(s,kind = None):
        return haxe_macro_Constant("CString", 2, (s,kind))

    @staticmethod
    def CIdent(s):
        return haxe_macro_Constant("CIdent", 3, (s,))

    @staticmethod
    def CRegexp(r,opt):
        return haxe_macro_Constant("CRegexp", 4, (r,opt))
haxe_macro_Constant._hx_class = haxe_macro_Constant
_hx_classes["haxe.macro.Constant"] = haxe_macro_Constant

class haxe_macro_Binop(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.Binop"
    _hx_constructs = ["OpAdd", "OpMult", "OpDiv", "OpSub", "OpAssign", "OpEq", "OpNotEq", "OpGt", "OpGte", "OpLt", "OpLte", "OpAnd", "OpOr", "OpXor", "OpBoolAnd", "OpBoolOr", "OpShl", "OpShr", "OpUShr", "OpMod", "OpAssignOp", "OpInterval", "OpArrow", "OpIn"]

    @staticmethod
    def OpAssignOp(op):
        return haxe_macro_Binop("OpAssignOp", 20, (op,))
haxe_macro_Binop.OpAdd = haxe_macro_Binop("OpAdd", 0, ())
haxe_macro_Binop.OpMult = haxe_macro_Binop("OpMult", 1, ())
haxe_macro_Binop.OpDiv = haxe_macro_Binop("OpDiv", 2, ())
haxe_macro_Binop.OpSub = haxe_macro_Binop("OpSub", 3, ())
haxe_macro_Binop.OpAssign = haxe_macro_Binop("OpAssign", 4, ())
haxe_macro_Binop.OpEq = haxe_macro_Binop("OpEq", 5, ())
haxe_macro_Binop.OpNotEq = haxe_macro_Binop("OpNotEq", 6, ())
haxe_macro_Binop.OpGt = haxe_macro_Binop("OpGt", 7, ())
haxe_macro_Binop.OpGte = haxe_macro_Binop("OpGte", 8, ())
haxe_macro_Binop.OpLt = haxe_macro_Binop("OpLt", 9, ())
haxe_macro_Binop.OpLte = haxe_macro_Binop("OpLte", 10, ())
haxe_macro_Binop.OpAnd = haxe_macro_Binop("OpAnd", 11, ())
haxe_macro_Binop.OpOr = haxe_macro_Binop("OpOr", 12, ())
haxe_macro_Binop.OpXor = haxe_macro_Binop("OpXor", 13, ())
haxe_macro_Binop.OpBoolAnd = haxe_macro_Binop("OpBoolAnd", 14, ())
haxe_macro_Binop.OpBoolOr = haxe_macro_Binop("OpBoolOr", 15, ())
haxe_macro_Binop.OpShl = haxe_macro_Binop("OpShl", 16, ())
haxe_macro_Binop.OpShr = haxe_macro_Binop("OpShr", 17, ())
haxe_macro_Binop.OpUShr = haxe_macro_Binop("OpUShr", 18, ())
haxe_macro_Binop.OpMod = haxe_macro_Binop("OpMod", 19, ())
haxe_macro_Binop.OpInterval = haxe_macro_Binop("OpInterval", 21, ())
haxe_macro_Binop.OpArrow = haxe_macro_Binop("OpArrow", 22, ())
haxe_macro_Binop.OpIn = haxe_macro_Binop("OpIn", 23, ())
haxe_macro_Binop._hx_class = haxe_macro_Binop
_hx_classes["haxe.macro.Binop"] = haxe_macro_Binop

class haxe_macro_Unop(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.Unop"
    _hx_constructs = ["OpIncrement", "OpDecrement", "OpNot", "OpNeg", "OpNegBits", "OpSpread"]
haxe_macro_Unop.OpIncrement = haxe_macro_Unop("OpIncrement", 0, ())
haxe_macro_Unop.OpDecrement = haxe_macro_Unop("OpDecrement", 1, ())
haxe_macro_Unop.OpNot = haxe_macro_Unop("OpNot", 2, ())
haxe_macro_Unop.OpNeg = haxe_macro_Unop("OpNeg", 3, ())
haxe_macro_Unop.OpNegBits = haxe_macro_Unop("OpNegBits", 4, ())
haxe_macro_Unop.OpSpread = haxe_macro_Unop("OpSpread", 5, ())
haxe_macro_Unop._hx_class = haxe_macro_Unop
_hx_classes["haxe.macro.Unop"] = haxe_macro_Unop

class haxe_macro_QuoteStatus(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.QuoteStatus"
    _hx_constructs = ["Unquoted", "Quoted"]
haxe_macro_QuoteStatus.Unquoted = haxe_macro_QuoteStatus("Unquoted", 0, ())
haxe_macro_QuoteStatus.Quoted = haxe_macro_QuoteStatus("Quoted", 1, ())
haxe_macro_QuoteStatus._hx_class = haxe_macro_QuoteStatus
_hx_classes["haxe.macro.QuoteStatus"] = haxe_macro_QuoteStatus

class haxe_macro_FunctionKind(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.FunctionKind"
    _hx_constructs = ["FAnonymous", "FNamed", "FArrow"]

    @staticmethod
    def FNamed(name,inlined = None):
        return haxe_macro_FunctionKind("FNamed", 1, (name,inlined))
haxe_macro_FunctionKind.FAnonymous = haxe_macro_FunctionKind("FAnonymous", 0, ())
haxe_macro_FunctionKind.FArrow = haxe_macro_FunctionKind("FArrow", 2, ())
haxe_macro_FunctionKind._hx_class = haxe_macro_FunctionKind
_hx_classes["haxe.macro.FunctionKind"] = haxe_macro_FunctionKind

class haxe_macro_ExprDef(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.ExprDef"
    _hx_constructs = ["EConst", "EArray", "EBinop", "EField", "EParenthesis", "EObjectDecl", "EArrayDecl", "ECall", "ENew", "EUnop", "EVars", "EFunction", "EBlock", "EFor", "EIf", "EWhile", "ESwitch", "ETry", "EReturn", "EBreak", "EContinue", "EUntyped", "EThrow", "ECast", "EDisplay", "EDisplayNew", "ETernary", "ECheckType", "EMeta", "EIs"]

    @staticmethod
    def EConst(c):
        return haxe_macro_ExprDef("EConst", 0, (c,))

    @staticmethod
    def EArray(e1,e2):
        return haxe_macro_ExprDef("EArray", 1, (e1,e2))

    @staticmethod
    def EBinop(op,e1,e2):
        return haxe_macro_ExprDef("EBinop", 2, (op,e1,e2))

    @staticmethod
    def EField(e,field):
        return haxe_macro_ExprDef("EField", 3, (e,field))

    @staticmethod
    def EParenthesis(e):
        return haxe_macro_ExprDef("EParenthesis", 4, (e,))

    @staticmethod
    def EObjectDecl(fields):
        return haxe_macro_ExprDef("EObjectDecl", 5, (fields,))

    @staticmethod
    def EArrayDecl(values):
        return haxe_macro_ExprDef("EArrayDecl", 6, (values,))

    @staticmethod
    def ECall(e,params):
        return haxe_macro_ExprDef("ECall", 7, (e,params))

    @staticmethod
    def ENew(t,params):
        return haxe_macro_ExprDef("ENew", 8, (t,params))

    @staticmethod
    def EUnop(op,postFix,e):
        return haxe_macro_ExprDef("EUnop", 9, (op,postFix,e))

    @staticmethod
    def EVars(vars):
        return haxe_macro_ExprDef("EVars", 10, (vars,))

    @staticmethod
    def EFunction(kind,f):
        return haxe_macro_ExprDef("EFunction", 11, (kind,f))

    @staticmethod
    def EBlock(exprs):
        return haxe_macro_ExprDef("EBlock", 12, (exprs,))

    @staticmethod
    def EFor(it,expr):
        return haxe_macro_ExprDef("EFor", 13, (it,expr))

    @staticmethod
    def EIf(econd,eif,eelse):
        return haxe_macro_ExprDef("EIf", 14, (econd,eif,eelse))

    @staticmethod
    def EWhile(econd,e,normalWhile):
        return haxe_macro_ExprDef("EWhile", 15, (econd,e,normalWhile))

    @staticmethod
    def ESwitch(e,cases,edef):
        return haxe_macro_ExprDef("ESwitch", 16, (e,cases,edef))

    @staticmethod
    def ETry(e,catches):
        return haxe_macro_ExprDef("ETry", 17, (e,catches))

    @staticmethod
    def EReturn(e = None):
        return haxe_macro_ExprDef("EReturn", 18, (e,))

    @staticmethod
    def EUntyped(e):
        return haxe_macro_ExprDef("EUntyped", 21, (e,))

    @staticmethod
    def EThrow(e):
        return haxe_macro_ExprDef("EThrow", 22, (e,))

    @staticmethod
    def ECast(e,t):
        return haxe_macro_ExprDef("ECast", 23, (e,t))

    @staticmethod
    def EDisplay(e,displayKind):
        return haxe_macro_ExprDef("EDisplay", 24, (e,displayKind))

    @staticmethod
    def EDisplayNew(t):
        return haxe_macro_ExprDef("EDisplayNew", 25, (t,))

    @staticmethod
    def ETernary(econd,eif,eelse):
        return haxe_macro_ExprDef("ETernary", 26, (econd,eif,eelse))

    @staticmethod
    def ECheckType(e,t):
        return haxe_macro_ExprDef("ECheckType", 27, (e,t))

    @staticmethod
    def EMeta(s,e):
        return haxe_macro_ExprDef("EMeta", 28, (s,e))

    @staticmethod
    def EIs(e,t):
        return haxe_macro_ExprDef("EIs", 29, (e,t))
haxe_macro_ExprDef.EBreak = haxe_macro_ExprDef("EBreak", 19, ())
haxe_macro_ExprDef.EContinue = haxe_macro_ExprDef("EContinue", 20, ())
haxe_macro_ExprDef._hx_class = haxe_macro_ExprDef
_hx_classes["haxe.macro.ExprDef"] = haxe_macro_ExprDef

class haxe_macro_DisplayKind(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.DisplayKind"
    _hx_constructs = ["DKCall", "DKDot", "DKStructure", "DKMarked", "DKPattern"]

    @staticmethod
    def DKPattern(outermost):
        return haxe_macro_DisplayKind("DKPattern", 4, (outermost,))
haxe_macro_DisplayKind.DKCall = haxe_macro_DisplayKind("DKCall", 0, ())
haxe_macro_DisplayKind.DKDot = haxe_macro_DisplayKind("DKDot", 1, ())
haxe_macro_DisplayKind.DKStructure = haxe_macro_DisplayKind("DKStructure", 2, ())
haxe_macro_DisplayKind.DKMarked = haxe_macro_DisplayKind("DKMarked", 3, ())
haxe_macro_DisplayKind._hx_class = haxe_macro_DisplayKind
_hx_classes["haxe.macro.DisplayKind"] = haxe_macro_DisplayKind

class haxe_macro_ComplexType(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.ComplexType"
    _hx_constructs = ["TPath", "TFunction", "TAnonymous", "TParent", "TExtend", "TOptional", "TNamed", "TIntersection"]

    @staticmethod
    def TPath(p):
        return haxe_macro_ComplexType("TPath", 0, (p,))

    @staticmethod
    def TFunction(args,ret):
        return haxe_macro_ComplexType("TFunction", 1, (args,ret))

    @staticmethod
    def TAnonymous(fields):
        return haxe_macro_ComplexType("TAnonymous", 2, (fields,))

    @staticmethod
    def TParent(t):
        return haxe_macro_ComplexType("TParent", 3, (t,))

    @staticmethod
    def TExtend(p,fields):
        return haxe_macro_ComplexType("TExtend", 4, (p,fields))

    @staticmethod
    def TOptional(t):
        return haxe_macro_ComplexType("TOptional", 5, (t,))

    @staticmethod
    def TNamed(n,t):
        return haxe_macro_ComplexType("TNamed", 6, (n,t))

    @staticmethod
    def TIntersection(tl):
        return haxe_macro_ComplexType("TIntersection", 7, (tl,))
haxe_macro_ComplexType._hx_class = haxe_macro_ComplexType
_hx_classes["haxe.macro.ComplexType"] = haxe_macro_ComplexType

class haxe_macro_TypeParam(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.TypeParam"
    _hx_constructs = ["TPType", "TPExpr"]

    @staticmethod
    def TPType(t):
        return haxe_macro_TypeParam("TPType", 0, (t,))

    @staticmethod
    def TPExpr(e):
        return haxe_macro_TypeParam("TPExpr", 1, (e,))
haxe_macro_TypeParam._hx_class = haxe_macro_TypeParam
_hx_classes["haxe.macro.TypeParam"] = haxe_macro_TypeParam

class haxe_macro_Access(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.Access"
    _hx_constructs = ["APublic", "APrivate", "AStatic", "AOverride", "ADynamic", "AInline", "AMacro", "AFinal", "AExtern", "AAbstract", "AOverload"]
haxe_macro_Access.APublic = haxe_macro_Access("APublic", 0, ())
haxe_macro_Access.APrivate = haxe_macro_Access("APrivate", 1, ())
haxe_macro_Access.AStatic = haxe_macro_Access("AStatic", 2, ())
haxe_macro_Access.AOverride = haxe_macro_Access("AOverride", 3, ())
haxe_macro_Access.ADynamic = haxe_macro_Access("ADynamic", 4, ())
haxe_macro_Access.AInline = haxe_macro_Access("AInline", 5, ())
haxe_macro_Access.AMacro = haxe_macro_Access("AMacro", 6, ())
haxe_macro_Access.AFinal = haxe_macro_Access("AFinal", 7, ())
haxe_macro_Access.AExtern = haxe_macro_Access("AExtern", 8, ())
haxe_macro_Access.AAbstract = haxe_macro_Access("AAbstract", 9, ())
haxe_macro_Access.AOverload = haxe_macro_Access("AOverload", 10, ())
haxe_macro_Access._hx_class = haxe_macro_Access
_hx_classes["haxe.macro.Access"] = haxe_macro_Access

class haxe_macro_FieldType(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.FieldType"
    _hx_constructs = ["FVar", "FFun", "FProp"]

    @staticmethod
    def FVar(t,e = None):
        return haxe_macro_FieldType("FVar", 0, (t,e))

    @staticmethod
    def FFun(f):
        return haxe_macro_FieldType("FFun", 1, (f,))

    @staticmethod
    def FProp(get,set,t = None,e= None):
        return haxe_macro_FieldType("FProp", 2, (get,set,t,e))
haxe_macro_FieldType._hx_class = haxe_macro_FieldType
_hx_classes["haxe.macro.FieldType"] = haxe_macro_FieldType

class haxe_macro_TypeDefKind(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.TypeDefKind"
    _hx_constructs = ["TDEnum", "TDStructure", "TDClass", "TDAlias", "TDAbstract", "TDField"]

    @staticmethod
    def TDClass(superClass = None,interfaces= None,isInterface= None,isFinal= None,isAbstract= None):
        return haxe_macro_TypeDefKind("TDClass", 2, (superClass,interfaces,isInterface,isFinal,isAbstract))

    @staticmethod
    def TDAlias(t):
        return haxe_macro_TypeDefKind("TDAlias", 3, (t,))

    @staticmethod
    def TDAbstract(tthis,_hx_from = None,to= None):
        return haxe_macro_TypeDefKind("TDAbstract", 4, (tthis,_hx_from,to))

    @staticmethod
    def TDField(kind,access = None):
        return haxe_macro_TypeDefKind("TDField", 5, (kind,access))
haxe_macro_TypeDefKind.TDEnum = haxe_macro_TypeDefKind("TDEnum", 0, ())
haxe_macro_TypeDefKind.TDStructure = haxe_macro_TypeDefKind("TDStructure", 1, ())
haxe_macro_TypeDefKind._hx_class = haxe_macro_TypeDefKind
_hx_classes["haxe.macro.TypeDefKind"] = haxe_macro_TypeDefKind


class haxe_macro_Error(haxe_Exception):
    _hx_class_name = "haxe.macro.Error"
    __slots__ = ("pos",)
    _hx_fields = ["pos"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_Exception


    def __init__(self,message,pos,previous = None):
        self.pos = None
        super().__init__(message,previous)
        self.pos = pos
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0._hx___skipStack
        _hx_local_0._hx___skipStack = (_hx_local_1 + 1)
        _hx_local_1

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.pos = None
haxe_macro_Error._hx_class = haxe_macro_Error
_hx_classes["haxe.macro.Error"] = haxe_macro_Error

class haxe_macro_ImportMode(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.ImportMode"
    _hx_constructs = ["INormal", "IAsName", "IAll"]

    @staticmethod
    def IAsName(alias):
        return haxe_macro_ImportMode("IAsName", 1, (alias,))
haxe_macro_ImportMode.INormal = haxe_macro_ImportMode("INormal", 0, ())
haxe_macro_ImportMode.IAll = haxe_macro_ImportMode("IAll", 2, ())
haxe_macro_ImportMode._hx_class = haxe_macro_ImportMode
_hx_classes["haxe.macro.ImportMode"] = haxe_macro_ImportMode

class haxe_zip_ExtraField(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.zip.ExtraField"
    _hx_constructs = ["FUnknown", "FInfoZipUnicodePath", "FUtf8"]

    @staticmethod
    def FUnknown(tag,bytes):
        return haxe_zip_ExtraField("FUnknown", 0, (tag,bytes))

    @staticmethod
    def FInfoZipUnicodePath(name,crc):
        return haxe_zip_ExtraField("FInfoZipUnicodePath", 1, (name,crc))
haxe_zip_ExtraField.FUtf8 = haxe_zip_ExtraField("FUtf8", 2, ())
haxe_zip_ExtraField._hx_class = haxe_zip_ExtraField
_hx_classes["haxe.zip.ExtraField"] = haxe_zip_ExtraField


class haxe_zip_Writer:
    _hx_class_name = "haxe.zip.Writer"
    __slots__ = ("o", "files")
    _hx_fields = ["o", "files"]
    _hx_methods = ["writeZipDate", "writeEntryHeader", "write", "writeCDR"]
    _hx_statics = ["CENTRAL_DIRECTORY_RECORD_FIELDS_SIZE", "LOCAL_FILE_HEADER_FIELDS_SIZE"]

    def __init__(self,o):
        self.o = o
        self.files = haxe_ds_List()

    def writeZipDate(self,date):
        hour = date.date.hour
        _hx_min = date.date.minute
        sec = (date.date.second >> 1)
        self.o.writeUInt16((((hour << 11) | ((_hx_min << 5))) | sec))
        year = (date.date.year - 1980)
        month = ((date.date.month - 1) + 1)
        day = date.date.day
        self.o.writeUInt16((((year << 9) | ((month << 5))) | day))

    def writeEntryHeader(self,f):
        o = self.o
        flags = 0
        if (Reflect.field(f,"extraFields") is not None):
            _g_head = Reflect.field(f,"extraFields").h
            while (_g_head is not None):
                val = _g_head.item
                _g_head = _g_head.next
                e = val
                if (e.index == 2):
                    flags = (flags | 2048)
        o.writeInt32(67324752)
        o.writeUInt16(20)
        o.writeUInt16(flags)
        if (f.data is None):
            f.fileSize = 0
            f.dataSize = 0
            f.crc32 = 0
            f.compressed = False
            f.data = haxe_io_Bytes.alloc(0)
        else:
            if (f.crc32 is None):
                if f.compressed:
                    raise haxe_Exception.thrown("CRC32 must be processed before compression")
                f.crc32 = haxe_crypto_Crc32.make(f.data)
            if (not f.compressed):
                f.fileSize = f.data.length
            f.dataSize = f.data.length
        o.writeUInt16((8 if (f.compressed) else 0))
        self.writeZipDate(f.fileTime)
        o.writeInt32(f.crc32)
        o.writeInt32(f.dataSize)
        o.writeInt32(f.fileSize)
        o.writeUInt16(len(f.fileName))
        e = haxe_io_BytesOutput()
        if (Reflect.field(f,"extraFields") is not None):
            _g_head = Reflect.field(f,"extraFields").h
            while (_g_head is not None):
                val = _g_head.item
                _g_head = _g_head.next
                f1 = val
                tmp = f1.index
                if (tmp == 0):
                    tag = f1.params[0]
                    _hx_bytes = f1.params[1]
                    e.writeUInt16(tag)
                    e.writeUInt16(_hx_bytes.length)
                    e.write(_hx_bytes)
                elif (tmp == 1):
                    name = f1.params[0]
                    crc = f1.params[1]
                    namebytes = haxe_io_Bytes.ofString(name)
                    e.writeUInt16(28789)
                    e.writeUInt16((namebytes.length + 5))
                    e.writeByte(1)
                    e.writeInt32(crc)
                    e.write(namebytes)
                elif (tmp == 2):
                    pass
                else:
                    pass
        ebytes = e.getBytes()
        o.writeUInt16(ebytes.length)
        o.writeString(f.fileName)
        o.write(ebytes)
        self.files.add(_hx_AnonObject({'name': f.fileName, 'compressed': f.compressed, 'clen': f.data.length, 'size': f.fileSize, 'crc': f.crc32, 'date': f.fileTime, 'fields': ebytes}))

    def write(self,files):
        _g_head = files.h
        while (_g_head is not None):
            val = _g_head.item
            _g_head = _g_head.next
            f = val
            self.writeEntryHeader(f)
            self.o.writeFullBytes(f.data,0,f.data.length)
        self.writeCDR()

    def writeCDR(self):
        cdr_size = 0
        cdr_offset = 0
        _g_head = self.files.h
        while (_g_head is not None):
            val = _g_head.item
            _g_head = _g_head.next
            f = val
            namelen = len(f.name)
            extraFieldsLength = f.fields.length
            self.o.writeInt32(33639248)
            self.o.writeUInt16(20)
            self.o.writeUInt16(20)
            self.o.writeUInt16(0)
            self.o.writeUInt16((8 if (f.compressed) else 0))
            self.writeZipDate(f.date)
            self.o.writeInt32(f.crc)
            self.o.writeInt32(f.clen)
            self.o.writeInt32(f.size)
            self.o.writeUInt16(namelen)
            self.o.writeUInt16(extraFieldsLength)
            self.o.writeUInt16(0)
            self.o.writeUInt16(0)
            self.o.writeUInt16(0)
            self.o.writeInt32(0)
            self.o.writeInt32(cdr_offset)
            self.o.writeString(f.name)
            self.o.write(f.fields)
            cdr_size = (cdr_size + (((46 + namelen) + extraFieldsLength)))
            cdr_offset = (cdr_offset + ((((30 + namelen) + extraFieldsLength) + f.clen)))
        self.o.writeInt32(101010256)
        self.o.writeUInt16(0)
        self.o.writeUInt16(0)
        self.o.writeUInt16(self.files.length)
        self.o.writeUInt16(self.files.length)
        self.o.writeInt32(cdr_size)
        self.o.writeInt32(cdr_offset)
        self.o.writeUInt16(0)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.o = None
        _hx_o.files = None
haxe_zip_Writer._hx_class = haxe_zip_Writer
_hx_classes["haxe.zip.Writer"] = haxe_zip_Writer


class python_Boot:
    _hx_class_name = "python.Boot"
    __slots__ = ()
    _hx_statics = ["keywords", "arrayJoin", "safeJoin", "isPyBool", "isPyInt", "isPyFloat", "isClass", "isAnonObject", "_add_dynamic", "toString", "toString1", "isMetaType", "fields", "isString", "isArray", "simpleField", "createClosure", "hasField", "field", "getInstanceFields", "getSuperClass", "getClassFields", "unsafeFastCodeAt", "handleKeywords", "prefixLength", "unhandleKeywords", "implementsInterface"]

    @staticmethod
    def arrayJoin(x,sep):
        return sep.join([python_Boot.toString1(x1,'') for x1 in x])

    @staticmethod
    def safeJoin(x,sep):
        return sep.join([x1 for x1 in x])

    @staticmethod
    def isPyBool(o):
        return isinstance(o,bool)

    @staticmethod
    def isPyInt(o):
        if isinstance(o,int):
            return (not isinstance(o,bool))
        else:
            return False

    @staticmethod
    def isPyFloat(o):
        return isinstance(o,float)

    @staticmethod
    def isClass(o):
        if (o is not None):
            if not HxOverrides.eq(o,str):
                return python_lib_Inspect.isclass(o)
            else:
                return True
        else:
            return False

    @staticmethod
    def isAnonObject(o):
        return isinstance(o,_hx_AnonObject)

    @staticmethod
    def _add_dynamic(a,b):
        if (isinstance(a,str) and isinstance(b,str)):
            return (a + b)
        if (isinstance(a,str) or isinstance(b,str)):
            return (python_Boot.toString1(a,"") + python_Boot.toString1(b,""))
        return (a + b)

    @staticmethod
    def toString(o):
        return python_Boot.toString1(o,"")

    @staticmethod
    def toString1(o,s):
        if (o is None):
            return "null"
        if isinstance(o,str):
            return o
        if (s is None):
            s = ""
        if (len(s) >= 5):
            return "<...>"
        if isinstance(o,bool):
            if o:
                return "true"
            else:
                return "false"
        if (isinstance(o,int) and (not isinstance(o,bool))):
            return str(o)
        if isinstance(o,float):
            try:
                if (o == int(o)):
                    return str(Math.floor((o + 0.5)))
                else:
                    return str(o)
            except BaseException as _g:
                None
                return str(o)
        if isinstance(o,list):
            o1 = o
            l = len(o1)
            st = "["
            s = (("null" if s is None else s) + "\t")
            _g = 0
            _g1 = l
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                prefix = ""
                if (i > 0):
                    prefix = ","
                st = (("null" if st is None else st) + HxOverrides.stringOrNull(((("null" if prefix is None else prefix) + HxOverrides.stringOrNull(python_Boot.toString1((o1[i] if i >= 0 and i < len(o1) else None),s))))))
            st = (("null" if st is None else st) + "]")
            return st
        try:
            if hasattr(o,"toString"):
                return o.toString()
        except BaseException as _g:
            None
        if hasattr(o,"__class__"):
            if isinstance(o,_hx_AnonObject):
                toStr = None
                try:
                    fields = python_Boot.fields(o)
                    _g = []
                    _g1 = 0
                    while (_g1 < len(fields)):
                        f = (fields[_g1] if _g1 >= 0 and _g1 < len(fields) else None)
                        _g1 = (_g1 + 1)
                        x = ((("" + ("null" if f is None else f)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f),(("null" if s is None else s) + "\t"))))
                        _g.append(x)
                    fieldsStr = _g
                    toStr = (("{ " + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr]))) + " }")
                except BaseException as _g:
                    None
                    return "{ ... }"
                if (toStr is None):
                    return "{ ... }"
                else:
                    return toStr
            if isinstance(o,Enum):
                o1 = o
                l = len(o1.params)
                hasParams = (l > 0)
                if hasParams:
                    paramsStr = ""
                    _g = 0
                    _g1 = l
                    while (_g < _g1):
                        i = _g
                        _g = (_g + 1)
                        prefix = ""
                        if (i > 0):
                            prefix = ","
                        paramsStr = (("null" if paramsStr is None else paramsStr) + HxOverrides.stringOrNull(((("null" if prefix is None else prefix) + HxOverrides.stringOrNull(python_Boot.toString1(o1.params[i],s))))))
                    return (((HxOverrides.stringOrNull(o1.tag) + "(") + ("null" if paramsStr is None else paramsStr)) + ")")
                else:
                    return o1.tag
            if hasattr(o,"_hx_class_name"):
                if (o.__class__.__name__ != "type"):
                    fields = python_Boot.getInstanceFields(o)
                    _g = []
                    _g1 = 0
                    while (_g1 < len(fields)):
                        f = (fields[_g1] if _g1 >= 0 and _g1 < len(fields) else None)
                        _g1 = (_g1 + 1)
                        x = ((("" + ("null" if f is None else f)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f),(("null" if s is None else s) + "\t"))))
                        _g.append(x)
                    fieldsStr = _g
                    toStr = (((HxOverrides.stringOrNull(o._hx_class_name) + "( ") + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr]))) + " )")
                    return toStr
                else:
                    fields = python_Boot.getClassFields(o)
                    _g = []
                    _g1 = 0
                    while (_g1 < len(fields)):
                        f = (fields[_g1] if _g1 >= 0 and _g1 < len(fields) else None)
                        _g1 = (_g1 + 1)
                        x = ((("" + ("null" if f is None else f)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f),(("null" if s is None else s) + "\t"))))
                        _g.append(x)
                    fieldsStr = _g
                    toStr = (((("#" + HxOverrides.stringOrNull(o._hx_class_name)) + "( ") + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr]))) + " )")
                    return toStr
            if (o == str):
                return "#String"
            if (o == list):
                return "#Array"
            if callable(o):
                return "function"
            try:
                if hasattr(o,"__repr__"):
                    return o.__repr__()
            except BaseException as _g:
                None
            if hasattr(o,"__str__"):
                return o.__str__([])
            if hasattr(o,"__name__"):
                return o.__name__
            return "???"
        else:
            return str(o)

    @staticmethod
    def isMetaType(v,t):
        return (v == t)

    @staticmethod
    def fields(o):
        a = []
        if (o is not None):
            if hasattr(o,"_hx_fields"):
                fields = o._hx_fields
                if (fields is not None):
                    return list(fields)
            if isinstance(o,_hx_AnonObject):
                d = o.__dict__
                keys = d.keys()
                handler = python_Boot.unhandleKeywords
                for k in keys:
                    if (k != '_hx_disable_getattr'):
                        a.append(handler(k))
            elif hasattr(o,"__dict__"):
                d = o.__dict__
                keys1 = d.keys()
                for k in keys1:
                    a.append(k)
        return a

    @staticmethod
    def isString(o):
        return isinstance(o,str)

    @staticmethod
    def isArray(o):
        return isinstance(o,list)

    @staticmethod
    def simpleField(o,field):
        if (field is None):
            return None
        field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
        if hasattr(o,field1):
            return getattr(o,field1)
        else:
            return None

    @staticmethod
    def createClosure(obj,func):
        return python_internal_MethodClosure(obj,func)

    @staticmethod
    def hasField(o,field):
        if isinstance(o,_hx_AnonObject):
            return o._hx_hasattr(field)
        return hasattr(o,(("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field)))

    @staticmethod
    def field(o,field):
        if (field is None):
            return None
        if isinstance(o,str):
            field1 = field
            _hx_local_0 = len(field1)
            if (_hx_local_0 == 10):
                if (field1 == "charCodeAt"):
                    return python_internal_MethodClosure(o,HxString.charCodeAt)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_0 == 11):
                if (field1 == "lastIndexOf"):
                    return python_internal_MethodClosure(o,HxString.lastIndexOf)
                elif (field1 == "toLowerCase"):
                    return python_internal_MethodClosure(o,HxString.toLowerCase)
                elif (field1 == "toUpperCase"):
                    return python_internal_MethodClosure(o,HxString.toUpperCase)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_0 == 9):
                if (field1 == "substring"):
                    return python_internal_MethodClosure(o,HxString.substring)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_0 == 5):
                if (field1 == "split"):
                    return python_internal_MethodClosure(o,HxString.split)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_0 == 7):
                if (field1 == "indexOf"):
                    return python_internal_MethodClosure(o,HxString.indexOf)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_0 == 8):
                if (field1 == "toString"):
                    return python_internal_MethodClosure(o,HxString.toString)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_0 == 6):
                if (field1 == "charAt"):
                    return python_internal_MethodClosure(o,HxString.charAt)
                elif (field1 == "length"):
                    return len(o)
                elif (field1 == "substr"):
                    return python_internal_MethodClosure(o,HxString.substr)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            else:
                field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                if hasattr(o,field1):
                    return getattr(o,field1)
                else:
                    return None
        elif isinstance(o,list):
            field1 = field
            _hx_local_1 = len(field1)
            if (_hx_local_1 == 11):
                if (field1 == "lastIndexOf"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.lastIndexOf)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 4):
                if (field1 == "copy"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.copy)
                elif (field1 == "join"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.join)
                elif (field1 == "push"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.push)
                elif (field1 == "sort"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.sort)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 5):
                if (field1 == "shift"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.shift)
                elif (field1 == "slice"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.slice)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 7):
                if (field1 == "indexOf"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.indexOf)
                elif (field1 == "reverse"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.reverse)
                elif (field1 == "unshift"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.unshift)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 3):
                if (field1 == "map"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.map)
                elif (field1 == "pop"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.pop)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 8):
                if (field1 == "contains"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.contains)
                elif (field1 == "iterator"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.iterator)
                elif (field1 == "toString"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.toString)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 16):
                if (field1 == "keyValueIterator"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.keyValueIterator)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 6):
                if (field1 == "concat"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.concat)
                elif (field1 == "filter"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.filter)
                elif (field1 == "insert"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.insert)
                elif (field1 == "length"):
                    return len(o)
                elif (field1 == "remove"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.remove)
                elif (field1 == "splice"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.splice)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            else:
                field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                if hasattr(o,field1):
                    return getattr(o,field1)
                else:
                    return None
        else:
            field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
            if hasattr(o,field1):
                return getattr(o,field1)
            else:
                return None

    @staticmethod
    def getInstanceFields(c):
        f = (list(c._hx_fields) if (hasattr(c,"_hx_fields")) else [])
        if hasattr(c,"_hx_methods"):
            f = (f + c._hx_methods)
        sc = python_Boot.getSuperClass(c)
        if (sc is None):
            return f
        else:
            scArr = python_Boot.getInstanceFields(sc)
            scMap = set(scArr)
            _g = 0
            while (_g < len(f)):
                f1 = (f[_g] if _g >= 0 and _g < len(f) else None)
                _g = (_g + 1)
                if (not (f1 in scMap)):
                    scArr.append(f1)
            return scArr

    @staticmethod
    def getSuperClass(c):
        if (c is None):
            return None
        try:
            if hasattr(c,"_hx_super"):
                return c._hx_super
            return None
        except BaseException as _g:
            None
        return None

    @staticmethod
    def getClassFields(c):
        if hasattr(c,"_hx_statics"):
            x = c._hx_statics
            return list(x)
        else:
            return []

    @staticmethod
    def unsafeFastCodeAt(s,index):
        return ord(s[index])

    @staticmethod
    def handleKeywords(name):
        if (name in python_Boot.keywords):
            return ("_hx_" + name)
        elif ((((len(name) > 2) and ((ord(name[0]) == 95))) and ((ord(name[1]) == 95))) and ((ord(name[(len(name) - 1)]) != 95))):
            return ("_hx_" + name)
        else:
            return name

    @staticmethod
    def unhandleKeywords(name):
        if (HxString.substr(name,0,python_Boot.prefixLength) == "_hx_"):
            real = HxString.substr(name,python_Boot.prefixLength,None)
            if (real in python_Boot.keywords):
                return real
        return name

    @staticmethod
    def implementsInterface(value,cls):
        loop = None
        def _hx_local_1(intf):
            f = (intf._hx_interfaces if (hasattr(intf,"_hx_interfaces")) else [])
            if (f is not None):
                _g = 0
                while (_g < len(f)):
                    i = (f[_g] if _g >= 0 and _g < len(f) else None)
                    _g = (_g + 1)
                    if (i == cls):
                        return True
                    else:
                        l = loop(i)
                        if l:
                            return True
                return False
            else:
                return False
        loop = _hx_local_1
        currentClass = value.__class__
        result = False
        while (currentClass is not None):
            if loop(currentClass):
                result = True
                break
            currentClass = python_Boot.getSuperClass(currentClass)
        return result
python_Boot._hx_class = python_Boot
_hx_classes["python.Boot"] = python_Boot


class python_HaxeIterable:
    _hx_class_name = "python.HaxeIterable"
    __slots__ = ("x",)
    _hx_fields = ["x"]
    _hx_methods = ["iterator"]

    def __init__(self,x):
        self.x = x

    def iterator(self):
        return python_HaxeIterator(self.x.__iter__())

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.x = None
python_HaxeIterable._hx_class = python_HaxeIterable
_hx_classes["python.HaxeIterable"] = python_HaxeIterable


class python_HaxeIterator:
    _hx_class_name = "python.HaxeIterator"
    __slots__ = ("it", "x", "has", "checked")
    _hx_fields = ["it", "x", "has", "checked"]
    _hx_methods = ["next", "hasNext"]

    def __init__(self,it):
        self.checked = False
        self.has = False
        self.x = None
        self.it = it

    def next(self):
        if (not self.checked):
            self.hasNext()
        self.checked = False
        return self.x

    def hasNext(self):
        if (not self.checked):
            try:
                self.x = self.it.__next__()
                self.has = True
            except BaseException as _g:
                None
                if Std.isOfType(haxe_Exception.caught(_g).unwrap(),StopIteration):
                    self.has = False
                    self.x = None
                else:
                    raise _g
            self.checked = True
        return self.has

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.it = None
        _hx_o.x = None
        _hx_o.has = None
        _hx_o.checked = None
python_HaxeIterator._hx_class = python_HaxeIterator
_hx_classes["python.HaxeIterator"] = python_HaxeIterator


class python__KwArgs_KwArgs_Impl_:
    _hx_class_name = "python._KwArgs.KwArgs_Impl_"
    __slots__ = ()
    _hx_statics = ["_new", "toDict", "toDictHelper", "fromDict", "fromT", "typed", "get"]

    @staticmethod
    def _new(d):
        this1 = d
        return this1

    @staticmethod
    def toDict(this1):
        return python__KwArgs_KwArgs_Impl_.toDictHelper(this1,None)

    @staticmethod
    def toDictHelper(this1,x):
        return this1

    @staticmethod
    def fromDict(d):
        this1 = d
        return this1

    @staticmethod
    def fromT(d):
        this1 = python_Lib.anonAsDict(d)
        return this1

    @staticmethod
    def typed(this1):
        return _hx_AnonObject(python__KwArgs_KwArgs_Impl_.toDictHelper(this1,None))

    @staticmethod
    def get(this1,key,_hx_def):
        return this1.get(key,_hx_def)
python__KwArgs_KwArgs_Impl_._hx_class = python__KwArgs_KwArgs_Impl_
_hx_classes["python._KwArgs.KwArgs_Impl_"] = python__KwArgs_KwArgs_Impl_


class python_Lib:
    _hx_class_name = "python.Lib"
    __slots__ = ()
    _hx_statics = ["lineEnd", "get___name__", "print", "printString", "println", "dictToAnon", "anonToDict", "anonAsDict", "dictAsAnon", "toPythonIterable", "toHaxeIterable", "toHaxeIterator"]
    __name__ = None

    @staticmethod
    def get___name__():
        return __name__

    @staticmethod
    def print(v):
        python_Lib.printString(Std.string(v))

    @staticmethod
    def printString(_hx_str):
        encoding = "utf-8"
        if (encoding is None):
            encoding = "utf-8"
        python_lib_Sys.stdout.buffer.write(_hx_str.encode(encoding, "strict"))
        python_lib_Sys.stdout.flush()

    @staticmethod
    def println(v):
        _hx_str = Std.string(v)
        python_Lib.printString((("" + ("null" if _hx_str is None else _hx_str)) + HxOverrides.stringOrNull(python_Lib.lineEnd)))

    @staticmethod
    def dictToAnon(v):
        return _hx_AnonObject(v.copy())

    @staticmethod
    def anonToDict(o):
        if isinstance(o,_hx_AnonObject):
            return o.__dict__.copy()
        else:
            return None

    @staticmethod
    def anonAsDict(o):
        if isinstance(o,_hx_AnonObject):
            return o.__dict__
        else:
            return None

    @staticmethod
    def dictAsAnon(d):
        return _hx_AnonObject(d)

    @staticmethod
    def toPythonIterable(it):
        def _hx_local_3():
            def _hx_local_2():
                it1 = HxOverrides.iterator(it)
                _hx_self = None
                def _hx_local_0():
                    if it1.hasNext():
                        return it1.next()
                    else:
                        raise haxe_Exception.thrown(StopIteration())
                def _hx_local_1():
                    return _hx_self
                this1 = _hx_AnonObject({'__next__': _hx_local_0, '__iter__': _hx_local_1})
                _hx_self = this1
                return _hx_self
            return _hx_AnonObject({'__iter__': _hx_local_2})
        return _hx_local_3()

    @staticmethod
    def toHaxeIterable(it):
        return python_HaxeIterable(it)

    @staticmethod
    def toHaxeIterator(it):
        return python_HaxeIterator(it)
python_Lib._hx_class = python_Lib
_hx_classes["python.Lib"] = python_Lib


class python__NativeIterable_NativeIterable_Impl_:
    _hx_class_name = "python._NativeIterable.NativeIterable_Impl_"
    __slots__ = ()
    _hx_statics = ["toHaxeIterable", "iterator"]

    @staticmethod
    def toHaxeIterable(this1):
        return python_HaxeIterable(this1)

    @staticmethod
    def iterator(this1):
        return python_HaxeIterator(this1.__iter__())
python__NativeIterable_NativeIterable_Impl_._hx_class = python__NativeIterable_NativeIterable_Impl_
_hx_classes["python._NativeIterable.NativeIterable_Impl_"] = python__NativeIterable_NativeIterable_Impl_


class python__NativeIterator_NativeIterator_Impl_:
    _hx_class_name = "python._NativeIterator.NativeIterator_Impl_"
    __slots__ = ()
    _hx_statics = ["_new", "toHaxeIterator"]

    @staticmethod
    def _new(p):
        this1 = p
        return this1

    @staticmethod
    def toHaxeIterator(this1):
        return python_HaxeIterator(this1)
python__NativeIterator_NativeIterator_Impl_._hx_class = python__NativeIterator_NativeIterator_Impl_
_hx_classes["python._NativeIterator.NativeIterator_Impl_"] = python__NativeIterator_NativeIterator_Impl_


class python_NativeStringTools:
    _hx_class_name = "python.NativeStringTools"
    __slots__ = ()
    _hx_statics = ["format", "encode", "contains", "strip", "rpartition", "startswith", "endswith"]

    @staticmethod
    def format(s,args):
        return s.format(*args)

    @staticmethod
    def encode(s,encoding = None,errors = None):
        if (encoding is None):
            encoding = "utf-8"
        if (errors is None):
            errors = "strict"
        return s.encode(encoding, errors)

    @staticmethod
    def contains(s,e):
        return (e in s)

    @staticmethod
    def strip(s,chars = None):
        return s.strip(chars)

    @staticmethod
    def rpartition(s,sep):
        return s.rpartition(sep)

    @staticmethod
    def startswith(s,prefix):
        return s.startswith(prefix)

    @staticmethod
    def endswith(s,suffix):
        return s.endswith(suffix)
python_NativeStringTools._hx_class = python_NativeStringTools
_hx_classes["python.NativeStringTools"] = python_NativeStringTools


class python__VarArgs_VarArgs_Impl_:
    _hx_class_name = "python._VarArgs.VarArgs_Impl_"
    __slots__ = ()
    _hx_statics = ["_new", "raw", "toArray", "fromArray"]

    @staticmethod
    def _new(d):
        this1 = d
        return this1

    @staticmethod
    def raw(this1):
        return this1

    @staticmethod
    def toArray(this1):
        if (not Std.isOfType(this1,list)):
            return list(this1)
        else:
            return this1

    @staticmethod
    def fromArray(d):
        this1 = d
        return this1
python__VarArgs_VarArgs_Impl_._hx_class = python__VarArgs_VarArgs_Impl_
_hx_classes["python._VarArgs.VarArgs_Impl_"] = python__VarArgs_VarArgs_Impl_


class python_internal_ArrayImpl:
    _hx_class_name = "python.internal.ArrayImpl"
    __slots__ = ()
    _hx_statics = ["get_length", "concat", "copy", "iterator", "keyValueIterator", "indexOf", "lastIndexOf", "join", "toString", "pop", "push", "unshift", "remove", "contains", "shift", "slice", "sort", "splice", "map", "filter", "insert", "reverse", "_get", "_set", "unsafeGet", "unsafeSet", "resize"]

    @staticmethod
    def get_length(x):
        return len(x)

    @staticmethod
    def concat(a1,a2):
        return (a1 + a2)

    @staticmethod
    def copy(x):
        return list(x)

    @staticmethod
    def iterator(x):
        return python_HaxeIterator(x.__iter__())

    @staticmethod
    def keyValueIterator(x):
        return haxe_iterators_ArrayKeyValueIterator(x)

    @staticmethod
    def indexOf(a,x,fromIndex = None):
        _hx_len = len(a)
        l = (0 if ((fromIndex is None)) else ((_hx_len + fromIndex) if ((fromIndex < 0)) else fromIndex))
        if (l < 0):
            l = 0
        _g = l
        _g1 = _hx_len
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if HxOverrides.eq(a[i],x):
                return i
        return -1

    @staticmethod
    def lastIndexOf(a,x,fromIndex = None):
        _hx_len = len(a)
        l = (_hx_len if ((fromIndex is None)) else (((_hx_len + fromIndex) + 1) if ((fromIndex < 0)) else (fromIndex + 1)))
        if (l > _hx_len):
            l = _hx_len
        while True:
            l = (l - 1)
            tmp = l
            if (not ((tmp > -1))):
                break
            if HxOverrides.eq(a[l],x):
                return l
        return -1

    @staticmethod
    def join(x,sep):
        return sep.join([python_Boot.toString1(x1,'') for x1 in x])

    @staticmethod
    def toString(x):
        return (("[" + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in x]))) + "]")

    @staticmethod
    def pop(x):
        if (len(x) == 0):
            return None
        else:
            return x.pop()

    @staticmethod
    def push(x,e):
        x.append(e)
        return len(x)

    @staticmethod
    def unshift(x,e):
        x.insert(0, e)

    @staticmethod
    def remove(x,e):
        try:
            x.remove(e)
            return True
        except BaseException as _g:
            None
            return False

    @staticmethod
    def contains(x,e):
        return (e in x)

    @staticmethod
    def shift(x):
        if (len(x) == 0):
            return None
        return x.pop(0)

    @staticmethod
    def slice(x,pos,end = None):
        return x[pos:end]

    @staticmethod
    def sort(x,f):
        x.sort(key= python_lib_Functools.cmp_to_key(f))

    @staticmethod
    def splice(x,pos,_hx_len):
        if (pos < 0):
            pos = (len(x) + pos)
        if (pos < 0):
            pos = 0
        res = x[pos:(pos + _hx_len)]
        del x[pos:(pos + _hx_len)]
        return res

    @staticmethod
    def map(x,f):
        return list(map(f,x))

    @staticmethod
    def filter(x,f):
        return list(filter(f,x))

    @staticmethod
    def insert(a,pos,x):
        a.insert(pos, x)

    @staticmethod
    def reverse(a):
        a.reverse()

    @staticmethod
    def _get(x,idx):
        if ((idx > -1) and ((idx < len(x)))):
            return x[idx]
        else:
            return None

    @staticmethod
    def _set(x,idx,v):
        l = len(x)
        while (l < idx):
            x.append(None)
            l = (l + 1)
        if (l == idx):
            x.append(v)
        else:
            x[idx] = v
        return v

    @staticmethod
    def unsafeGet(x,idx):
        return x[idx]

    @staticmethod
    def unsafeSet(x,idx,val):
        x[idx] = val
        return val

    @staticmethod
    def resize(x,_hx_len):
        l = len(x)
        if (l < _hx_len):
            idx = (_hx_len - 1)
            v = None
            l1 = len(x)
            while (l1 < idx):
                x.append(None)
                l1 = (l1 + 1)
            if (l1 == idx):
                x.append(v)
            else:
                x[idx] = v
        elif (l > _hx_len):
            pos = _hx_len
            len1 = (l - _hx_len)
            if (pos < 0):
                pos = (len(x) + pos)
            if (pos < 0):
                pos = 0
            res = x[pos:(pos + len1)]
            del x[pos:(pos + len1)]
python_internal_ArrayImpl._hx_class = python_internal_ArrayImpl
_hx_classes["python.internal.ArrayImpl"] = python_internal_ArrayImpl


class HxOverrides:
    _hx_class_name = "HxOverrides"
    __slots__ = ()
    _hx_statics = ["iterator", "keyValueIterator", "eq", "stringOrNull", "shift", "pop", "push", "join", "filter", "map", "toUpperCase", "toLowerCase", "split", "length", "rshift", "modf", "mod", "arrayGet", "arraySet", "mapKwArgs", "reverseMapKwArgs"]

    @staticmethod
    def iterator(x):
        if isinstance(x,list):
            return haxe_iterators_ArrayIterator(x)
        return x.iterator()

    @staticmethod
    def keyValueIterator(x):
        if isinstance(x,list):
            return haxe_iterators_ArrayKeyValueIterator(x)
        return x.keyValueIterator()

    @staticmethod
    def eq(a,b):
        if (isinstance(a,list) or isinstance(b,list)):
            return a is b
        return (a == b)

    @staticmethod
    def stringOrNull(s):
        if (s is None):
            return "null"
        else:
            return s

    @staticmethod
    def shift(x):
        if isinstance(x,list):
            _this = x
            return (None if ((len(_this) == 0)) else _this.pop(0))
        return x.shift()

    @staticmethod
    def pop(x):
        if isinstance(x,list):
            _this = x
            return (None if ((len(_this) == 0)) else _this.pop())
        return x.pop()

    @staticmethod
    def push(x,e):
        if isinstance(x,list):
            _this = x
            _this.append(e)
            return len(_this)
        return x.push(e)

    @staticmethod
    def join(x,sep):
        if isinstance(x,list):
            return sep.join([python_Boot.toString1(x1,'') for x1 in x])
        return x.join(sep)

    @staticmethod
    def filter(x,f):
        if isinstance(x,list):
            return list(filter(f,x))
        return x.filter(f)

    @staticmethod
    def map(x,f):
        if isinstance(x,list):
            return list(map(f,x))
        return x.map(f)

    @staticmethod
    def toUpperCase(x):
        if isinstance(x,str):
            return x.upper()
        return x.toUpperCase()

    @staticmethod
    def toLowerCase(x):
        if isinstance(x,str):
            return x.lower()
        return x.toLowerCase()

    @staticmethod
    def split(x,delimiter):
        if isinstance(x,str):
            _this = x
            if (delimiter == ""):
                return list(_this)
            else:
                return _this.split(delimiter)
        return x.split(delimiter)

    @staticmethod
    def length(x):
        if isinstance(x,str):
            return len(x)
        elif isinstance(x,list):
            return len(x)
        return x.length

    @staticmethod
    def rshift(val,n):
        return ((val % 0x100000000) >> n)

    @staticmethod
    def modf(a,b):
        if (b == 0.0):
            return float('nan')
        elif (a < 0):
            if (b < 0):
                return -(-a % (-b))
            else:
                return -(-a % b)
        elif (b < 0):
            return a % (-b)
        else:
            return a % b

    @staticmethod
    def mod(a,b):
        if (a < 0):
            if (b < 0):
                return -(-a % (-b))
            else:
                return -(-a % b)
        elif (b < 0):
            return a % (-b)
        else:
            return a % b

    @staticmethod
    def arrayGet(a,i):
        if isinstance(a,list):
            x = a
            if ((i > -1) and ((i < len(x)))):
                return x[i]
            else:
                return None
        else:
            return a[i]

    @staticmethod
    def arraySet(a,i,v):
        if isinstance(a,list):
            x = a
            v1 = v
            l = len(x)
            while (l < i):
                x.append(None)
                l = (l + 1)
            if (l == i):
                x.append(v1)
            else:
                x[i] = v1
            return v1
        else:
            a[i] = v
            return v

    @staticmethod
    def mapKwArgs(a,v):
        a1 = _hx_AnonObject(python_Lib.anonToDict(a))
        k = python_HaxeIterator(iter(v.keys()))
        while k.hasNext():
            k1 = k.next()
            val = v.get(k1)
            if a1._hx_hasattr(k1):
                x = getattr(a1,k1)
                setattr(a1,val,x)
                delattr(a1,k1)
        return a1

    @staticmethod
    def reverseMapKwArgs(a,v):
        a1 = a.copy()
        k = python_HaxeIterator(iter(v.keys()))
        while k.hasNext():
            k1 = k.next()
            val = v.get(k1)
            if (val in a1):
                x = a1.get(val,None)
                a1[k1] = x
                del a1[val]
        return a1
HxOverrides._hx_class = HxOverrides
_hx_classes["HxOverrides"] = HxOverrides


class python_internal_Internal:
    _hx_class_name = "python.internal.Internal"
    __slots__ = ()
python_internal_Internal._hx_class = python_internal_Internal
_hx_classes["python.internal.Internal"] = python_internal_Internal


class python_internal_MethodClosure:
    _hx_class_name = "python.internal.MethodClosure"
    __slots__ = ("obj", "func")
    _hx_fields = ["obj", "func"]
    _hx_methods = ["__call__"]

    def __init__(self,obj,func):
        self.obj = obj
        self.func = func

    def __call__(self,*args):
        return self.func(self.obj,*args)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.obj = None
        _hx_o.func = None
python_internal_MethodClosure._hx_class = python_internal_MethodClosure
_hx_classes["python.internal.MethodClosure"] = python_internal_MethodClosure


class HxString:
    _hx_class_name = "HxString"
    __slots__ = ()
    _hx_statics = ["split", "charCodeAt", "charAt", "lastIndexOf", "toUpperCase", "toLowerCase", "indexOf", "indexOfImpl", "toString", "get_length", "fromCharCode", "substring", "substr"]

    @staticmethod
    def split(s,d):
        if (d == ""):
            return list(s)
        else:
            return s.split(d)

    @staticmethod
    def charCodeAt(s,index):
        if ((((s is None) or ((len(s) == 0))) or ((index < 0))) or ((index >= len(s)))):
            return None
        else:
            return ord(s[index])

    @staticmethod
    def charAt(s,index):
        if ((index < 0) or ((index >= len(s)))):
            return ""
        else:
            return s[index]

    @staticmethod
    def lastIndexOf(s,_hx_str,startIndex = None):
        if (startIndex is None):
            return s.rfind(_hx_str, 0, len(s))
        elif (_hx_str == ""):
            length = len(s)
            if (startIndex < 0):
                startIndex = (length + startIndex)
                if (startIndex < 0):
                    startIndex = 0
            if (startIndex > length):
                return length
            else:
                return startIndex
        else:
            i = s.rfind(_hx_str, 0, (startIndex + 1))
            startLeft = (max(0,((startIndex + 1) - len(_hx_str))) if ((i == -1)) else (i + 1))
            check = s.find(_hx_str, startLeft, len(s))
            if ((check > i) and ((check <= startIndex))):
                return check
            else:
                return i

    @staticmethod
    def toUpperCase(s):
        return s.upper()

    @staticmethod
    def toLowerCase(s):
        return s.lower()

    @staticmethod
    def indexOf(s,_hx_str,startIndex = None):
        if (startIndex is None):
            return s.find(_hx_str)
        else:
            return HxString.indexOfImpl(s,_hx_str,startIndex)

    @staticmethod
    def indexOfImpl(s,_hx_str,startIndex):
        if (_hx_str == ""):
            length = len(s)
            if (startIndex < 0):
                startIndex = (length + startIndex)
                if (startIndex < 0):
                    startIndex = 0
            if (startIndex > length):
                return length
            else:
                return startIndex
        return s.find(_hx_str, startIndex)

    @staticmethod
    def toString(s):
        return s

    @staticmethod
    def get_length(s):
        return len(s)

    @staticmethod
    def fromCharCode(code):
        return "".join(map(chr,[code]))

    @staticmethod
    def substring(s,startIndex,endIndex = None):
        if (startIndex < 0):
            startIndex = 0
        if (endIndex is None):
            return s[startIndex:]
        else:
            if (endIndex < 0):
                endIndex = 0
            if (endIndex < startIndex):
                return s[endIndex:startIndex]
            else:
                return s[startIndex:endIndex]

    @staticmethod
    def substr(s,startIndex,_hx_len = None):
        if (_hx_len is None):
            return s[startIndex:]
        else:
            if (_hx_len == 0):
                return ""
            if (startIndex < 0):
                startIndex = (len(s) + startIndex)
                if (startIndex < 0):
                    startIndex = 0
            return s[startIndex:(startIndex + _hx_len)]
HxString._hx_class = HxString
_hx_classes["HxString"] = HxString


class python_io_NativeInput(haxe_io_Input):
    _hx_class_name = "python.io.NativeInput"
    __slots__ = ("stream", "wasEof")
    _hx_fields = ["stream", "wasEof"]
    _hx_methods = ["get_canSeek", "close", "tell", "throwEof", "eof", "readinto", "seek", "readBytes"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_io_Input


    def __init__(self,s):
        self.wasEof = None
        self.stream = s
        self.set_bigEndian(False)
        self.wasEof = False
        if (not self.stream.readable()):
            raise haxe_Exception.thrown("Write-only stream")

    def get_canSeek(self):
        return self.stream.seekable()

    def close(self):
        self.stream.close()

    def tell(self):
        return self.stream.tell()

    def throwEof(self):
        self.wasEof = True
        raise haxe_Exception.thrown(haxe_io_Eof())

    def eof(self):
        return self.wasEof

    def readinto(self,b):
        raise haxe_Exception.thrown("abstract method, should be overridden")

    def seek(self,p,mode):
        raise haxe_Exception.thrown("abstract method, should be overridden")

    def readBytes(self,s,pos,_hx_len):
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > s.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        ba = bytearray(_hx_len)
        ret = self.readinto(ba)
        if (ret == 0):
            self.throwEof()
        s.blit(pos,haxe_io_Bytes.ofData(ba),0,_hx_len)
        return ret

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.stream = None
        _hx_o.wasEof = None
python_io_NativeInput._hx_class = python_io_NativeInput
_hx_classes["python.io.NativeInput"] = python_io_NativeInput


class python_io_IInput:
    _hx_class_name = "python.io.IInput"
    __slots__ = ("bigEndian",)
    _hx_fields = ["bigEndian"]
    _hx_methods = ["set_bigEndian", "readByte", "readBytes", "close", "readAll", "readFullBytes", "read", "readUntil", "readLine", "readFloat", "readDouble", "readInt8", "readInt16", "readUInt16", "readInt24", "readUInt24", "readInt32", "readString"]
python_io_IInput._hx_class = python_io_IInput
_hx_classes["python.io.IInput"] = python_io_IInput


class python_io_NativeBytesInput(python_io_NativeInput):
    _hx_class_name = "python.io.NativeBytesInput"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["readByte", "seek", "readinto"]
    _hx_statics = []
    _hx_interfaces = [python_io_IInput]
    _hx_super = python_io_NativeInput


    def __init__(self,stream):
        super().__init__(stream)

    def readByte(self):
        ret = self.stream.read(1)
        if (len(ret) == 0):
            self.throwEof()
        return ret[0]

    def seek(self,p,pos):
        self.wasEof = False
        python_io_IoTools.seekInBinaryMode(self.stream,p,pos)

    def readinto(self,b):
        return self.stream.readinto(b)

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
python_io_NativeBytesInput._hx_class = python_io_NativeBytesInput
_hx_classes["python.io.NativeBytesInput"] = python_io_NativeBytesInput


class python_io_IFileInput:
    _hx_class_name = "python.io.IFileInput"
    __slots__ = ()
    _hx_methods = ["seek", "tell", "eof"]
    _hx_interfaces = [python_io_IInput]
python_io_IFileInput._hx_class = python_io_IFileInput
_hx_classes["python.io.IFileInput"] = python_io_IFileInput


class python_io_FileBytesInput(python_io_NativeBytesInput):
    _hx_class_name = "python.io.FileBytesInput"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = [python_io_IFileInput]
    _hx_super = python_io_NativeBytesInput


    def __init__(self,stream):
        super().__init__(stream)
python_io_FileBytesInput._hx_class = python_io_FileBytesInput
_hx_classes["python.io.FileBytesInput"] = python_io_FileBytesInput


class python_io_NativeOutput(haxe_io_Output):
    _hx_class_name = "python.io.NativeOutput"
    __slots__ = ("stream",)
    _hx_fields = ["stream"]
    _hx_methods = ["get_canSeek", "close", "prepare", "flush", "tell"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_io_Output


    def __init__(self,stream):
        self.stream = None
        self.set_bigEndian(False)
        self.stream = stream
        if (not stream.writable()):
            raise haxe_Exception.thrown("Read only stream")

    def get_canSeek(self):
        return self.stream.seekable()

    def close(self):
        self.stream.close()

    def prepare(self,nbytes):
        self.stream.truncate(nbytes)

    def flush(self):
        self.stream.flush()

    def tell(self):
        return self.stream.tell()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.stream = None
python_io_NativeOutput._hx_class = python_io_NativeOutput
_hx_classes["python.io.NativeOutput"] = python_io_NativeOutput


class python_io_NativeBytesOutput(python_io_NativeOutput):
    _hx_class_name = "python.io.NativeBytesOutput"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["seek", "prepare", "writeByte", "writeBytes"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = python_io_NativeOutput


    def __init__(self,stream):
        super().__init__(stream)

    def seek(self,p,pos):
        python_io_IoTools.seekInBinaryMode(self.stream,p,pos)

    def prepare(self,nbytes):
        self.stream.truncate(nbytes)

    def writeByte(self,c):
        self.stream.write(bytearray([c]))

    def writeBytes(self,s,pos,_hx_len):
        return self.stream.write(s.b[pos:(pos + _hx_len)])

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
python_io_NativeBytesOutput._hx_class = python_io_NativeBytesOutput
_hx_classes["python.io.NativeBytesOutput"] = python_io_NativeBytesOutput


class python_io_IOutput:
    _hx_class_name = "python.io.IOutput"
    __slots__ = ("bigEndian",)
    _hx_fields = ["bigEndian"]
    _hx_methods = ["set_bigEndian", "writeByte", "writeBytes", "flush", "close", "write", "writeFullBytes", "writeFloat", "writeDouble", "writeInt8", "writeInt16", "writeUInt16", "writeInt24", "writeUInt24", "writeInt32", "prepare", "writeInput", "writeString"]
python_io_IOutput._hx_class = python_io_IOutput
_hx_classes["python.io.IOutput"] = python_io_IOutput


class python_io_IFileOutput:
    _hx_class_name = "python.io.IFileOutput"
    __slots__ = ()
    _hx_methods = ["seek", "tell"]
    _hx_interfaces = [python_io_IOutput]
python_io_IFileOutput._hx_class = python_io_IFileOutput
_hx_classes["python.io.IFileOutput"] = python_io_IFileOutput


class python_io_FileBytesOutput(python_io_NativeBytesOutput):
    _hx_class_name = "python.io.FileBytesOutput"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = [python_io_IFileOutput]
    _hx_super = python_io_NativeBytesOutput


    def __init__(self,stream):
        super().__init__(stream)
python_io_FileBytesOutput._hx_class = python_io_FileBytesOutput
_hx_classes["python.io.FileBytesOutput"] = python_io_FileBytesOutput


class python_io_NativeTextInput(python_io_NativeInput):
    _hx_class_name = "python.io.NativeTextInput"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["readByte", "seek", "readinto"]
    _hx_statics = []
    _hx_interfaces = [python_io_IInput]
    _hx_super = python_io_NativeInput


    def __init__(self,stream):
        super().__init__(stream)

    def readByte(self):
        ret = self.stream.buffer.read(1)
        if (len(ret) == 0):
            self.throwEof()
        return ret[0]

    def seek(self,p,pos):
        self.wasEof = False
        python_io_IoTools.seekInTextMode(self.stream,self.tell,p,pos)

    def readinto(self,b):
        return self.stream.buffer.readinto(b)

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
python_io_NativeTextInput._hx_class = python_io_NativeTextInput
_hx_classes["python.io.NativeTextInput"] = python_io_NativeTextInput


class python_io_FileTextInput(python_io_NativeTextInput):
    _hx_class_name = "python.io.FileTextInput"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = [python_io_IFileInput]
    _hx_super = python_io_NativeTextInput


    def __init__(self,stream):
        super().__init__(stream)
python_io_FileTextInput._hx_class = python_io_FileTextInput
_hx_classes["python.io.FileTextInput"] = python_io_FileTextInput


class python_io_NativeTextOutput(python_io_NativeOutput):
    _hx_class_name = "python.io.NativeTextOutput"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["seek", "writeBytes", "writeByte"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = python_io_NativeOutput


    def __init__(self,stream):
        super().__init__(stream)
        if (not stream.writable()):
            raise haxe_Exception.thrown("Read only stream")

    def seek(self,p,pos):
        python_io_IoTools.seekInTextMode(self.stream,self.tell,p,pos)

    def writeBytes(self,s,pos,_hx_len):
        return self.stream.buffer.write(s.b[pos:(pos + _hx_len)])

    def writeByte(self,c):
        self.stream.write("".join(map(chr,[c])))

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
python_io_NativeTextOutput._hx_class = python_io_NativeTextOutput
_hx_classes["python.io.NativeTextOutput"] = python_io_NativeTextOutput


class python_io_FileTextOutput(python_io_NativeTextOutput):
    _hx_class_name = "python.io.FileTextOutput"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = [python_io_IFileOutput]
    _hx_super = python_io_NativeTextOutput


    def __init__(self,stream):
        super().__init__(stream)
python_io_FileTextOutput._hx_class = python_io_FileTextOutput
_hx_classes["python.io.FileTextOutput"] = python_io_FileTextOutput


class python_io_IoTools:
    _hx_class_name = "python.io.IoTools"
    __slots__ = ()
    _hx_statics = ["createFileInputFromText", "createFileInputFromBytes", "createFileOutputFromText", "createFileOutputFromBytes", "seekInTextMode", "seekInBinaryMode"]

    @staticmethod
    def createFileInputFromText(t):
        return sys_io_FileInput(python_io_FileTextInput(t))

    @staticmethod
    def createFileInputFromBytes(t):
        return sys_io_FileInput(python_io_FileBytesInput(t))

    @staticmethod
    def createFileOutputFromText(t):
        return sys_io_FileOutput(python_io_FileTextOutput(t))

    @staticmethod
    def createFileOutputFromBytes(t):
        return sys_io_FileOutput(python_io_FileBytesOutput(t))

    @staticmethod
    def seekInTextMode(stream,tell,p,pos):
        pos1 = None
        pos2 = pos.index
        if (pos2 == 0):
            pos1 = 0
        elif (pos2 == 1):
            p = (tell() + p)
            pos1 = 0
        elif (pos2 == 2):
            stream.seek(0,2)
            p = (tell() + p)
            pos1 = 0
        else:
            pass
        stream.seek(p,pos1)

    @staticmethod
    def seekInBinaryMode(stream,p,pos):
        pos1 = None
        pos2 = pos.index
        if (pos2 == 0):
            pos1 = 0
        elif (pos2 == 1):
            pos1 = 1
        elif (pos2 == 2):
            pos1 = 2
        else:
            pass
        stream.seek(p,pos1)
python_io_IoTools._hx_class = python_io_IoTools
_hx_classes["python.io.IoTools"] = python_io_IoTools


class python_lib__Re_Choice_Impl_:
    _hx_class_name = "python.lib._Re.Choice_Impl_"
    __slots__ = ()
    _hx_statics = ["fromA", "fromB"]

    @staticmethod
    def fromA(x):
        return x

    @staticmethod
    def fromB(x):
        return x
python_lib__Re_Choice_Impl_._hx_class = python_lib__Re_Choice_Impl_
_hx_classes["python.lib._Re.Choice_Impl_"] = python_lib__Re_Choice_Impl_


class python_lib__Re_RegexHelper:
    _hx_class_name = "python.lib._Re.RegexHelper"
    __slots__ = ()
    _hx_statics = ["findallDynamic"]

    @staticmethod
    def findallDynamic(r,string,pos = None,endpos = None):
        if (endpos is None):
            if (pos is None):
                return r.findall(string)
            else:
                return r.findall(string,pos)
        else:
            return r.findall(string,pos,endpos)
python_lib__Re_RegexHelper._hx_class = python_lib__Re_RegexHelper
_hx_classes["python.lib._Re.RegexHelper"] = python_lib__Re_RegexHelper


class sys_io_File:
    _hx_class_name = "sys.io.File"
    __slots__ = ()
    _hx_statics = ["getContent", "saveContent", "getBytes", "saveBytes", "read", "write", "append", "update", "copy"]

    @staticmethod
    def getContent(path):
        f = python_lib_Builtins.open(path,"r",-1,"utf-8",None,"")
        content = f.read(-1)
        f.close()
        return content

    @staticmethod
    def saveContent(path,content):
        f = python_lib_Builtins.open(path,"w",-1,"utf-8",None,"")
        f.write(content)
        f.close()

    @staticmethod
    def getBytes(path):
        f = python_lib_Builtins.open(path,"rb",-1)
        size = f.read(-1)
        b = haxe_io_Bytes.ofData(size)
        f.close()
        return b

    @staticmethod
    def saveBytes(path,_hx_bytes):
        f = python_lib_Builtins.open(path,"wb",-1)
        f.write(_hx_bytes.b)
        f.close()

    @staticmethod
    def read(path,binary = None):
        if (binary is None):
            binary = True
        mode = ("rb" if binary else "r")
        f = python_lib_Builtins.open(path,mode,-1,None,None,(None if binary else ""))
        if binary:
            return python_io_IoTools.createFileInputFromBytes(f)
        else:
            return python_io_IoTools.createFileInputFromText(f)

    @staticmethod
    def write(path,binary = None):
        if (binary is None):
            binary = True
        mode = ("wb" if binary else "w")
        f = python_lib_Builtins.open(path,mode,-1,None,None,(None if binary else ""))
        if binary:
            return python_io_IoTools.createFileOutputFromBytes(f)
        else:
            return python_io_IoTools.createFileOutputFromText(f)

    @staticmethod
    def append(path,binary = None):
        if (binary is None):
            binary = True
        mode = ("ab" if binary else "a")
        f = python_lib_Builtins.open(path,mode,-1,None,None,(None if binary else ""))
        if binary:
            return python_io_IoTools.createFileOutputFromBytes(f)
        else:
            return python_io_IoTools.createFileOutputFromText(f)

    @staticmethod
    def update(path,binary = None):
        if (binary is None):
            binary = True
        if (not sys_FileSystem.exists(path)):
            sys_io_File.write(path).close()
        mode = ("rb+" if binary else "r+")
        f = python_lib_Builtins.open(path,mode,-1,None,None,(None if binary else ""))
        if binary:
            return python_io_IoTools.createFileOutputFromBytes(f)
        else:
            return python_io_IoTools.createFileOutputFromText(f)

    @staticmethod
    def copy(srcPath,dstPath):
        python_lib_Shutil.copy(srcPath,dstPath)
sys_io_File._hx_class = sys_io_File
_hx_classes["sys.io.File"] = sys_io_File


class sys_io_FileInput(haxe_io_Input):
    _hx_class_name = "sys.io.FileInput"
    __slots__ = ("impl",)
    _hx_fields = ["impl"]
    _hx_methods = ["set_bigEndian", "seek", "tell", "eof", "readByte", "readBytes", "close", "readAll", "readFullBytes", "read", "readUntil", "readLine", "readFloat", "readDouble", "readInt8", "readInt16", "readUInt16", "readInt24", "readUInt24", "readInt32", "readString"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_io_Input


    def __init__(self,impl):
        self.impl = impl

    def set_bigEndian(self,b):
        return self.impl.set_bigEndian(b)

    def seek(self,p,pos):
        self.impl.seek(p,pos)

    def tell(self):
        return self.impl.tell()

    def eof(self):
        return self.impl.eof()

    def readByte(self):
        return self.impl.readByte()

    def readBytes(self,s,pos,_hx_len):
        return self.impl.readBytes(s,pos,_hx_len)

    def close(self):
        self.impl.close()

    def readAll(self,bufsize = None):
        return self.impl.readAll(bufsize)

    def readFullBytes(self,s,pos,_hx_len):
        self.impl.readFullBytes(s,pos,_hx_len)

    def read(self,nbytes):
        return self.impl.read(nbytes)

    def readUntil(self,end):
        return self.impl.readUntil(end)

    def readLine(self):
        return self.impl.readLine()

    def readFloat(self):
        return self.impl.readFloat()

    def readDouble(self):
        return self.impl.readDouble()

    def readInt8(self):
        return self.impl.readInt8()

    def readInt16(self):
        return self.impl.readInt16()

    def readUInt16(self):
        return self.impl.readUInt16()

    def readInt24(self):
        return self.impl.readInt24()

    def readUInt24(self):
        return self.impl.readUInt24()

    def readInt32(self):
        return self.impl.readInt32()

    def readString(self,_hx_len,encoding = None):
        return self.impl.readString(_hx_len)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.impl = None
sys_io_FileInput._hx_class = sys_io_FileInput
_hx_classes["sys.io.FileInput"] = sys_io_FileInput


class sys_io_FileOutput(haxe_io_Output):
    _hx_class_name = "sys.io.FileOutput"
    __slots__ = ("impl",)
    _hx_fields = ["impl"]
    _hx_methods = ["seek", "tell", "set_bigEndian", "writeByte", "writeBytes", "flush", "close", "write", "writeFullBytes", "writeFloat", "writeDouble", "writeInt8", "writeInt16", "writeUInt16", "writeInt24", "writeUInt24", "writeInt32", "prepare", "writeInput", "writeString"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_io_Output


    def __init__(self,impl):
        self.impl = impl

    def seek(self,p,pos):
        self.impl.seek(p,pos)

    def tell(self):
        return self.impl.tell()

    def set_bigEndian(self,b):
        return self.impl.set_bigEndian(b)

    def writeByte(self,c):
        self.impl.writeByte(c)

    def writeBytes(self,s,pos,_hx_len):
        return self.impl.writeBytes(s,pos,_hx_len)

    def flush(self):
        self.impl.flush()

    def close(self):
        self.impl.close()

    def write(self,s):
        self.impl.write(s)

    def writeFullBytes(self,s,pos,_hx_len):
        self.impl.writeFullBytes(s,pos,_hx_len)

    def writeFloat(self,x):
        self.impl.writeFloat(x)

    def writeDouble(self,x):
        self.impl.writeDouble(x)

    def writeInt8(self,x):
        self.impl.writeInt8(x)

    def writeInt16(self,x):
        self.impl.writeInt16(x)

    def writeUInt16(self,x):
        self.impl.writeUInt16(x)

    def writeInt24(self,x):
        self.impl.writeInt24(x)

    def writeUInt24(self,x):
        self.impl.writeUInt24(x)

    def writeInt32(self,x):
        self.impl.writeInt32(x)

    def prepare(self,nbytes):
        self.impl.prepare(nbytes)

    def writeInput(self,i,bufsize = None):
        self.impl.writeInput(i,bufsize)

    def writeString(self,s,encoding = None):
        self.impl.writeString(s)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.impl = None
sys_io_FileOutput._hx_class = sys_io_FileOutput
_hx_classes["sys.io.FileOutput"] = sys_io_FileOutput

class sys_io_FileSeek(Enum):
    __slots__ = ()
    _hx_class_name = "sys.io.FileSeek"
    _hx_constructs = ["SeekBegin", "SeekCur", "SeekEnd"]
sys_io_FileSeek.SeekBegin = sys_io_FileSeek("SeekBegin", 0, ())
sys_io_FileSeek.SeekCur = sys_io_FileSeek("SeekCur", 1, ())
sys_io_FileSeek.SeekEnd = sys_io_FileSeek("SeekEnd", 2, ())
sys_io_FileSeek._hx_class = sys_io_FileSeek
_hx_classes["sys.io.FileSeek"] = sys_io_FileSeek

Math.NEGATIVE_INFINITY = float("-inf")
Math.POSITIVE_INFINITY = float("inf")
Math.NaN = float("nan")
Math.PI = python_lib_Math.pi

haxe_SysTools.winMetaCharacters = [32, 40, 41, 37, 33, 94, 34, 60, 62, 38, 124, 10, 13, 44, 59]
StringTools.winMetaCharacters = haxe_SysTools.winMetaCharacters
Sys._programPath = sys_FileSystem.fullPath(python_lib_Inspect.getsourcefile(Sys))
connect_Env.loggers = connect_util_Dictionary()
connect_Env.ROOT_LOGGER = "root"
connect_Flow.SKIP_MSG = "Skipping request because an exception was thrown: "
connect_api_FulfillmentApi.REQUESTS_PATH = "requests"
connect_api_FulfillmentApi.TEMPLATES_PATH = "templates"
connect_api_FulfillmentApi.ASSETS_PATH = "assets"
connect_api_GeneralApi.ACCOUNTS_PATH = "accounts"
connect_api_GeneralApi.CONVERSATIONS_PATH = "conversations"
connect_api_GeneralApi.PRODUCTS_PATH = "products"
connect_api_GeneralApi.CATEGORIES_PATH = "categories"
connect_api_MarketplaceApi.AGREEMENTS_PATH = "agreements"
connect_api_MarketplaceApi.LISTINGS_PATH = "listings"
connect_api_MarketplaceApi.LISTINGREQUESTS_PATH = "listing-requests"
connect_api_MarketplaceApi.MARKETPLACES_PATH = "marketplaces"
connect_api_SubscriptionsApi.ASSETS_PATH = "subscriptions/assets"
connect_api_SubscriptionsApi.REQUESTS_PATH = "subscriptions/requests"
connect_api_TierApi.TCR_PATH = "tier/config-requests"
connect_api_TierApi.TA_PATH = "tier/accounts"
connect_api_TierApi.TC_PATH = "tier/configs"
connect_api_UsageApi.USAGE_FILES_PATH = "usage/files"
connect_api_UsageApi.USAGE_PRODUCTS_PATH = "usage/products"
connect_api_UsageApi.USAGE_RECORDS_PATH = "usage/records"
connect_logger_Logger.LEVEL_ERROR = 0
connect_logger_Logger.LEVEL_WARNING = 1
connect_logger_Logger.LEVEL_INFO = 2
connect_logger_Logger.LEVEL_DEBUG = 3
def _hx_init_connect_logger_LoggerConfig_levelTranslation():
    def _hx_local_0():
        _g = haxe_ds_StringMap()
        _g.h["ERROR"] = connect_logger_Logger.LEVEL_ERROR
        _g.h["WARNING"] = connect_logger_Logger.LEVEL_WARNING
        _g.h["INFO"] = connect_logger_Logger.LEVEL_INFO
        _g.h["DEBUG"] = connect_logger_Logger.LEVEL_DEBUG
        return _g
    return _hx_local_0()
connect_logger_LoggerConfig.levelTranslation = _hx_init_connect_logger_LoggerConfig_levelTranslation()
connect_logger_PlainLoggerFormatter.NO_REQUEST = "NO_REQUEST"
connect_util_ExcelWriter.APP = "<Properties xmlns=\"http://schemas.openxmlformats.org/officeDocument/2006/extended-properties\"><Application>Microsoft Excel</Application><AppVersion>2.5</AppVersion></Properties>"
connect_util_ExcelWriter.CORE = "<cp:coreProperties xmlns:cp=\"http://schemas.openxmlformats.org/package/2006/metadata/core-properties\" xmlns:dc=\"http://purl.org/dc/elements/1.1/\" xmlns:dcterms=\"http://purl.org/dc/terms/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"><dc:creator>connect</dc:creator><dcterms:created xsi:type=\"dcterms:W3CDTF\">%DATE%</dcterms:created><dcterms:modified xsi:type=\"dcterms:W3CDTF\">%DATE%</dcterms:modified></cp:coreProperties>"
connect_util_ExcelWriter.RELS1 = "<Relationships xmlns=\"http://schemas.openxmlformats.org/package/2006/relationships\"><Relationship Id=\"rId1\" Target=\"xl/workbook.xml\" Type=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument\" /><Relationship Id=\"rId2\" Target=\"docProps/core.xml\" Type=\"http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties\" /><Relationship Id=\"rId3\" Target=\"docProps/app.xml\" Type=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties\" /></Relationships>"
connect_util_ExcelWriter.THEME = "<?xml version=\"1.0\"?><a:theme xmlns:a=\"http://schemas.openxmlformats.org/drawingml/2006/main\" name=\"Office Theme\"><a:themeElements><a:clrScheme name=\"Office\"><a:dk1><a:sysClr val=\"windowText\" lastClr=\"000000\"/></a:dk1><a:lt1><a:sysClr val=\"window\" lastClr=\"FFFFFF\"/></a:lt1><a:dk2><a:srgbClr val=\"1F497D\"/></a:dk2><a:lt2><a:srgbClr val=\"EEECE1\"/></a:lt2><a:accent1><a:srgbClr val=\"4F81BD\"/></a:accent1><a:accent2><a:srgbClr val=\"C0504D\"/></a:accent2><a:accent3><a:srgbClr val=\"9BBB59\"/></a:accent3><a:accent4><a:srgbClr val=\"8064A2\"/></a:accent4><a:accent5><a:srgbClr val=\"4BACC6\"/></a:accent5><a:accent6><a:srgbClr val=\"F79646\"/></a:accent6><a:hlink><a:srgbClr val=\"0000FF\"/></a:hlink><a:folHlink><a:srgbClr val=\"800080\"/></a:folHlink></a:clrScheme><a:fontScheme name=\"Office\"><a:majorFont><a:latin typeface=\"Cambria\"/><a:ea typeface=\"\"/><a:cs typeface=\"\"/><a:font script=\"Jpan\" typeface=\"&#xFF2D;&#xFF33; &#xFF30;&#x30B4;&#x30B7;&#x30C3;&#x30AF;\"/><a:font script=\"Hang\" typeface=\"&#xB9D1;&#xC740; &#xACE0;&#xB515;\"/><a:font script=\"Hans\" typeface=\"&#x5B8B;&#x4F53;\"/><a:font script=\"Hant\" typeface=\"&#x65B0;&#x7D30;&#x660E;&#x9AD4;\"/><a:font script=\"Arab\" typeface=\"Times New Roman\"/><a:font script=\"Hebr\" typeface=\"Times New Roman\"/><a:font script=\"Thai\" typeface=\"Tahoma\"/><a:font script=\"Ethi\" typeface=\"Nyala\"/><a:font script=\"Beng\" typeface=\"Vrinda\"/><a:font script=\"Gujr\" typeface=\"Shruti\"/><a:font script=\"Khmr\" typeface=\"MoolBoran\"/><a:font script=\"Knda\" typeface=\"Tunga\"/><a:font script=\"Guru\" typeface=\"Raavi\"/><a:font script=\"Cans\" typeface=\"Euphemia\"/><a:font script=\"Cher\" typeface=\"Plantagenet Cherokee\"/><a:font script=\"Yiii\" typeface=\"Microsoft Yi Baiti\"/><a:font script=\"Tibt\" typeface=\"Microsoft Himalaya\"/><a:font script=\"Thaa\" typeface=\"MV Boli\"/><a:font script=\"Deva\" typeface=\"Mangal\"/><a:font script=\"Telu\" typeface=\"Gautami\"/><a:font script=\"Taml\" typeface=\"Latha\"/><a:font script=\"Syrc\" typeface=\"Estrangelo Edessa\"/><a:font script=\"Orya\" typeface=\"Kalinga\"/><a:font script=\"Mlym\" typeface=\"Kartika\"/><a:font script=\"Laoo\" typeface=\"DokChampa\"/><a:font script=\"Sinh\" typeface=\"Iskoola Pota\"/><a:font script=\"Mong\" typeface=\"Mongolian Baiti\"/><a:font script=\"Viet\" typeface=\"Times New Roman\"/><a:font script=\"Uigh\" typeface=\"Microsoft Uighur\"/></a:majorFont><a:minorFont><a:latin typeface=\"Calibri\"/><a:ea typeface=\"\"/><a:cs typeface=\"\"/><a:font script=\"Jpan\" typeface=\"&#xFF2D;&#xFF33; &#xFF30;&#x30B4;&#x30B7;&#x30C3;&#x30AF;\"/><a:font script=\"Hang\" typeface=\"&#xB9D1;&#xC740; &#xACE0;&#xB515;\"/><a:font script=\"Hans\" typeface=\"&#x5B8B;&#x4F53;\"/><a:font script=\"Hant\" typeface=\"&#x65B0;&#x7D30;&#x660E;&#x9AD4;\"/><a:font script=\"Arab\" typeface=\"Arial\"/><a:font script=\"Hebr\" typeface=\"Arial\"/><a:font script=\"Thai\" typeface=\"Tahoma\"/><a:font script=\"Ethi\" typeface=\"Nyala\"/><a:font script=\"Beng\" typeface=\"Vrinda\"/><a:font script=\"Gujr\" typeface=\"Shruti\"/><a:font script=\"Khmr\" typeface=\"DaunPenh\"/><a:font script=\"Knda\" typeface=\"Tunga\"/><a:font script=\"Guru\" typeface=\"Raavi\"/><a:font script=\"Cans\" typeface=\"Euphemia\"/><a:font script=\"Cher\" typeface=\"Plantagenet Cherokee\"/><a:font script=\"Yiii\" typeface=\"Microsoft Yi Baiti\"/><a:font script=\"Tibt\" typeface=\"Microsoft Himalaya\"/><a:font script=\"Thaa\" typeface=\"MV Boli\"/><a:font script=\"Deva\" typeface=\"Mangal\"/><a:font script=\"Telu\" typeface=\"Gautami\"/><a:font script=\"Taml\" typeface=\"Latha\"/><a:font script=\"Syrc\" typeface=\"Estrangelo Edessa\"/><a:font script=\"Orya\" typeface=\"Kalinga\"/><a:font script=\"Mlym\" typeface=\"Kartika\"/><a:font script=\"Laoo\" typeface=\"DokChampa\"/><a:font script=\"Sinh\" typeface=\"Iskoola Pota\"/><a:font script=\"Mong\" typeface=\"Mongolian Baiti\"/><a:font script=\"Viet\" typeface=\"Arial\"/><a:font script=\"Uigh\" typeface=\"Microsoft Uighur\"/></a:minorFont></a:fontScheme><a:fmtScheme name=\"Office\"><a:fillStyleLst><a:solidFill><a:schemeClr val=\"phClr\"/></a:solidFill><a:gradFill rotWithShape=\"1\"><a:gsLst><a:gs pos=\"0\"><a:schemeClr val=\"phClr\"><a:tint val=\"50000\"/><a:satMod val=\"300000\"/></a:schemeClr></a:gs><a:gs pos=\"35000\"><a:schemeClr val=\"phClr\"><a:tint val=\"37000\"/><a:satMod val=\"300000\"/></a:schemeClr></a:gs><a:gs pos=\"100000\"><a:schemeClr val=\"phClr\"><a:tint val=\"15000\"/><a:satMod val=\"350000\"/></a:schemeClr></a:gs></a:gsLst><a:lin ang=\"16200000\" scaled=\"1\"/></a:gradFill><a:gradFill rotWithShape=\"1\"><a:gsLst><a:gs pos=\"0\"><a:schemeClr val=\"phClr\"><a:shade val=\"51000\"/><a:satMod val=\"130000\"/></a:schemeClr></a:gs><a:gs pos=\"80000\"><a:schemeClr val=\"phClr\"><a:shade val=\"93000\"/><a:satMod val=\"130000\"/></a:schemeClr></a:gs><a:gs pos=\"100000\"><a:schemeClr val=\"phClr\"><a:shade val=\"94000\"/><a:satMod val=\"135000\"/></a:schemeClr></a:gs></a:gsLst><a:lin ang=\"16200000\" scaled=\"0\"/></a:gradFill></a:fillStyleLst><a:lnStyleLst><a:ln w=\"9525\" cap=\"flat\" cmpd=\"sng\" algn=\"ctr\"><a:solidFill><a:schemeClr val=\"phClr\"><a:shade val=\"95000\"/><a:satMod val=\"105000\"/></a:schemeClr></a:solidFill><a:prstDash val=\"solid\"/></a:ln><a:ln w=\"25400\" cap=\"flat\" cmpd=\"sng\" algn=\"ctr\"><a:solidFill><a:schemeClr val=\"phClr\"/></a:solidFill><a:prstDash val=\"solid\"/></a:ln><a:ln w=\"38100\" cap=\"flat\" cmpd=\"sng\" algn=\"ctr\"><a:solidFill><a:schemeClr val=\"phClr\"/></a:solidFill><a:prstDash val=\"solid\"/></a:ln></a:lnStyleLst><a:effectStyleLst><a:effectStyle><a:effectLst><a:outerShdw blurRad=\"40000\" dist=\"20000\" dir=\"5400000\" rotWithShape=\"0\"><a:srgbClr val=\"000000\"><a:alpha val=\"38000\"/></a:srgbClr></a:outerShdw></a:effectLst></a:effectStyle><a:effectStyle><a:effectLst><a:outerShdw blurRad=\"40000\" dist=\"23000\" dir=\"5400000\" rotWithShape=\"0\"><a:srgbClr val=\"000000\"><a:alpha val=\"35000\"/></a:srgbClr></a:outerShdw></a:effectLst></a:effectStyle><a:effectStyle><a:effectLst><a:outerShdw blurRad=\"40000\" dist=\"23000\" dir=\"5400000\" rotWithShape=\"0\"><a:srgbClr val=\"000000\"><a:alpha val=\"35000\"/></a:srgbClr></a:outerShdw></a:effectLst><a:scene3d><a:camera prst=\"orthographicFront\"><a:rot lat=\"0\" lon=\"0\" rev=\"0\"/></a:camera><a:lightRig rig=\"threePt\" dir=\"t\"><a:rot lat=\"0\" lon=\"0\" rev=\"1200000\"/></a:lightRig></a:scene3d><a:sp3d><a:bevelT w=\"63500\" h=\"25400\"/></a:sp3d></a:effectStyle></a:effectStyleLst><a:bgFillStyleLst><a:solidFill><a:schemeClr val=\"phClr\"/></a:solidFill><a:gradFill rotWithShape=\"1\"><a:gsLst><a:gs pos=\"0\"><a:schemeClr val=\"phClr\"><a:tint val=\"40000\"/><a:satMod val=\"350000\"/></a:schemeClr></a:gs><a:gs pos=\"40000\"><a:schemeClr val=\"phClr\"><a:tint val=\"45000\"/><a:shade val=\"99000\"/><a:satMod val=\"350000\"/></a:schemeClr></a:gs><a:gs pos=\"100000\"><a:schemeClr val=\"phClr\"><a:shade val=\"20000\"/><a:satMod val=\"255000\"/></a:schemeClr></a:gs></a:gsLst><a:path path=\"circle\"><a:fillToRect l=\"50000\" t=\"-80000\" r=\"50000\" b=\"180000\"/></a:path></a:gradFill><a:gradFill rotWithShape=\"1\"><a:gsLst><a:gs pos=\"0\"><a:schemeClr val=\"phClr\"><a:tint val=\"80000\"/><a:satMod val=\"300000\"/></a:schemeClr></a:gs><a:gs pos=\"100000\"><a:schemeClr val=\"phClr\"><a:shade val=\"30000\"/><a:satMod val=\"200000\"/></a:schemeClr></a:gs></a:gsLst><a:path path=\"circle\"><a:fillToRect l=\"50000\" t=\"50000\" r=\"50000\" b=\"50000\"/></a:path></a:gradFill></a:bgFillStyleLst></a:fmtScheme></a:themeElements><a:objectDefaults/><a:extraClrSchemeLst/></a:theme>"
connect_util_ExcelWriter.STYLES = "<styleSheet xmlns=\"http://schemas.openxmlformats.org/spreadsheetml/2006/main\"><numFmts count=\"0\" /><fonts count=\"1\"><font><name val=\"Calibri\" /><family val=\"2\" /><color theme=\"1\" /><sz val=\"11\" /><scheme val=\"minor\" /></font></fonts><fills count=\"2\"><fill><patternFill /></fill><fill><patternFill patternType=\"gray125\" /></fill></fills><borders count=\"1\"><border><left /><right /><top /><bottom /><diagonal /></border></borders><cellStyleXfs count=\"1\"><xf borderId=\"0\" fillId=\"0\" fontId=\"0\" numFmtId=\"0\" /></cellStyleXfs><cellXfs count=\"1\"><xf borderId=\"0\" fillId=\"0\" fontId=\"0\" numFmtId=\"0\" pivotButton=\"0\" quotePrefix=\"0\" xfId=\"0\" /></cellXfs><cellStyles count=\"1\"><cellStyle builtinId=\"0\" hidden=\"0\" name=\"Normal\" xfId=\"0\" /></cellStyles><tableStyles count=\"0\" defaultPivotStyle=\"PivotStyleLight16\" defaultTableStyle=\"TableStyleMedium9\" /></styleSheet>"
def _hx_init_haxe_io_FPHelper_i64tmp():
    def _hx_local_0():
        this1 = haxe__Int64____Int64(0,0)
        return this1
    return _hx_local_0()
haxe_io_FPHelper.i64tmp = _hx_init_haxe_io_FPHelper_i64tmp()
haxe_io_FPHelper.LN2 = 0.6931471805599453
haxe_io__UInt8Array_UInt8Array_Impl_.BYTES_PER_ELEMENT = 1
haxe_zip_Writer.CENTRAL_DIRECTORY_RECORD_FIELDS_SIZE = 46
haxe_zip_Writer.LOCAL_FILE_HEADER_FIELDS_SIZE = 30
python_Boot.keywords = set(["and", "del", "from", "not", "with", "as", "elif", "global", "or", "yield", "assert", "else", "if", "pass", "None", "break", "except", "import", "raise", "True", "class", "exec", "in", "return", "False", "continue", "finally", "is", "try", "def", "for", "lambda", "while"])
python_Boot.prefixLength = len("_hx_")
python_Lib.lineEnd = ("\r\n" if ((Sys.systemName() == "Windows")) else "\n")

Connect.main()
