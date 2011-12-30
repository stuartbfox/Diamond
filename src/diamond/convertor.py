# Copyright (C) 2011-2012 by Ivan Pouzyrevsky.
# Copyright (C) 2010-2011 by Brightcove Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from diamond import *

_RE_FIND_FIRST_CAP = re.compile('(.)([A-Z][a-z]+)')
_RE_SPAN_OF_CAPS = re.compile('([a-z0-9])([A-Z])')

def camelcase_to_underscore(name):
    return _RE_SPAN_OF_CAPS.sub(r'\1_\2',
        _RE_FIND_FIRST_CAP.sub(r'\1_\2', name)
    ).lower()

class binary:
    '''
    Store the value in bits so we can convert between things easily
    '''
    value = None

    def __init__(self, value = None, unit = None):
        self.get(value = value, unit = unit)

    @staticmethod
    def convert ( value = None, oldUnit = None, newUnit = None):
        convertor = binary(value = value, unit = oldUnit)
        return convertor.get(unit = newUnit)

    def set( self, value = None, unit = None):
        return self.get( value = value, unit = unit)

    def get( self, value = None, unit = None):
        if not unit:
            return self.bit(value = value)

        if unit in [ 'bit', 'b']:
            return self.bit(value = value)
        if unit in [ 'kilobit', 'kbit', 'Kibit']:
            return self.kilobit(value = value)
        if unit in [ 'megabit', 'Mbit', 'Mibit']:
            return self.megabit(value = value)
        if unit in [ 'gigabit', 'Gbit', 'Gibit']:
            return self.gigabit(value = value)
        if unit in [ 'terabit', 'Tbit', 'Tibit']:
            return self.terabit(value = value)
        if unit in [ 'petabit', 'Pbit', 'Pibit']:
            return self.petabit(value = value)
        if unit in [ 'exabit', 'Ebit', 'Eibit']:
            return self.exabit(value = value)
        if unit in [ 'zettabit', 'Zbit', 'Zibit']:
            return self.zettabit(value = value)
        if unit in [ 'yottabit', 'Ybit', 'Yibit']:
            return self.yottabit(value = value)

        if unit in [ 'Byte', 'B']:
            return self.byte(value = value)
        if unit in [ 'kilobyte', 'kB', 'KiB']:
            return self.kilobyte(value = value)
        if unit in [ 'megabyte', 'MB', 'MiB']:
            return self.megabyte(value = value)
        if unit in [ 'gigabyte', 'GB', 'GiB']:
            return self.gigabyte(value = value)
        if unit in [ 'terabyte', 'TB', 'TiB']:
            return self.terabyte(value = value)
        if unit in [ 'petabyte', 'PB', 'PiB']:
            return self.petabyte(value = value)
        if unit in [ 'exabyte', 'EB', 'EiB']:
            return self.exabyte(value = value)
        if unit in [ 'zettabyte', 'ZB', 'ZiB']:
            return self.zettabyte(value = value)
        if unit in [ 'yottabyte', 'YB', 'YiB']:
            return self.yottabyte(value = value)

        raise NotImplementedError()

    def bit(self, value = None):
        if value is None:
            return self.value
        else:
            self.value = float(value)

    def kilobit(self, value = None):
        if value is None:
            return self.bit() / 1024
        else:
            self.bit(value * 1024)

    def megabit(self, value = None):
        if value is None:
            return self.kilobit() / 1024
        else:
            self.kilobit(value * 1024)

    def gigabit(self, value = None):
        if value is None:
            return self.megabit() / 1024
        else:
            self.megabit(value * 1024)

    def terabit(self, value = None):
        if value is None:
            return self.gigabit() / 1024
        else:
            self.gigabit(value * 1024)

    def petabit(self, value = None):
        if value is None:
            return self.terabit() / 1024
        else:
            self.terabit(value * 1024)

    def exabit(self, value = None):
        if value is None:
            return self.petabit() / 1024
        else:
            self.petabit(value * 1024)

    def zettabit(self, value = None):
        if value is None:
            return self.exabit() / 1024
        else:
            self.exabit(value * 1024)

    def yottabit(self, value = None):
        if value is None:
            return self.zettabit() / 1024
        else:
            self.zettabit(value * 1024)

    def byte(self, value = None):
        if value is None:
            return self.value / 8
        else:
            self.value = value * 8

    def kilobyte(self, value = None):
        if value is None:
            return self.byte() / 1024
        else:
            self.byte(value * 1024)

    def megabyte(self, value = None):
        if value is None:
            return self.kilobyte() / 1024
        else:
            self.kilobyte(value * 1024)

    def gigabyte(self, value = None):
        if value is None:
            return self.megabyte() / 1024
        else:
            self.megabyte(value * 1024)

    def terabyte(self, value = None):
        if value is None:
            return self.gigabyte() / 1024
        else:
            self.gigabyte(value * 1024)

    def petabyte(self, value = None):
        if value is None:
            return self.terabyte() / 1024
        else:
            self.terabyte(value * 1024)

    def exabyte(self, value = None):
        if value is None:
            return self.petabyte() / 1024
        else:
            self.petabyte(value * 1024)

    def zettabyte(self, value = None):
        if value is None:
            return self.exabyte() / 1024
        else:
            self.exabyte(value * 1024)

    def yottabyte(self, value = None):
        if value is None:
            return self.zettabyte() / 1024
        else:
            self.zettabyte(value * 1024)
