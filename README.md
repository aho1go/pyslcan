# pyslcan

## Requirement

PySerial

```
pip install pyserial
```

## Usage

```
python pyslcan.py <cmd> <device> [baudrate] [delay]
```

引数

- cmd は、slcan コマンドをカンマ(,)で区切って指定します。

- device は、/dev/ttyXXX などの USB シリアルデバイスを指定します。
- baudrate は、115200 などのボーレートを指定します。
- delay は、コマンド送信とコマンド送信の間に入れるウエイトを msec 単位で指定します。

cmd の末端に、'-'を入れると受信モードになって、デバイスからの受信を表示します。終了する際は、`Control+C`や、`Control+D`などで終了させてください。

/dev/ttyXXX のデバイスに対して、オープンコマンド(O)を送信し、CAN 速度を 1Mbps に設定(S8)し、CAN メッセージ ID:111 MSG:1122 を送信し、クローズコマンド(C)を送信する場合は、以下の様にします（1 メッセージ送信）。

```
python pyslcan.py O,S8,t11121122,C /dev/ttyXXX
```
