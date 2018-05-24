import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX='f9beb4d9'.decode('hex')
P2P_PORT=17511
ADDRESS_VERSION=65
RPC_PORT=17510
RPC_CHECK=lambda bitcoind: True
SUBSIDY_FUNC=lambda height: 150*100000000 >> (height + 1)//210000
POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('lyra2re2_TTC').getPoWHash(data))
BLOCK_PERIOD=150 # s
SYMBOL='TTC'
CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'TTC') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/TTC/') if platform.system() == 'Darwin' else os.path.expanduser('~/.TTC'), 'TTC.conf')
BLOCK_EXPLORER_URL_PREFIX='http://90.188.88.19:3001/block/'
ADDRESS_EXPLORER_URL_PREFIX='http://90.188.88.19:3001/address/'
TX_EXPLORER_URL_PREFIX='http://90.188.88.19:3001/tx/'
SANE_TARGET_RANGE=(2**256//1000000000000000000 - 1, 2**256//100000 - 1)
DUMB_SCRYPT_DIFF=16
DUST_THRESHOLD=0.03e8
