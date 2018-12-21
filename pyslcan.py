# MIT License
#
# Copyright(c) 2018 aho1go
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files(the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import serial
import sys
import time


def main():
    args = sys.argv
    if len(args) < 2:
        return

    cmd = args[1]
    dev = args[2]
    bps = 115200
    delay = 10

    if len(args) >= 4:
        bps = int(args[3])
    if len(args) >= 5:
        delay = int(args[4])

    cmds = cmd.split(",")

    s = serial.Serial(dev, bps)
    for c in cmds:
        if c == "-":
            rcv = ""
            while True:
                if s.in_waiting:
                    r = s.read().decode("ascii")
                    if r == '\r':
                        print(rcv)
                        rcv = ""
                    else:
                        rcv = rcv + r

        c = bytes((c + "\r").encode("ascii"))
        s.write(c)
        s.flush()
        time.sleep(delay/1000.0)

    s.close()


if __name__ == "__main__":
    main()
