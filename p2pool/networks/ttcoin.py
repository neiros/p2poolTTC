from p2pool.bitcoin import networks

PARENT=networks.nets['ttcoin']
SHARE_PERIOD=15 # seconds
CHAIN_LENGTH=24*60*60//10 # shares
REAL_CHAIN_LENGTH=24*60*60//10 # shares
TARGET_LOOKBEHIND=200 # shares
SPREAD=12 # blocks
IDENTIFIER='cab983a06a81c827'.decode('hex')
PREFIX='cdcf7847c3614a6b'.decode('hex')
P2P_PORT=19346
MIN_TARGET=4
MAX_TARGET=2**256//2**20 - 1
PERSIST=False
WORKER_PORT=19171
BOOTSTRAP_ADDRS='192.168.1.104'.split(' ')
ANNOUNCE_CHANNEL='#p2pool-ttc'
VERSION_CHECK=lambda v: True
#SOFTFORKS_REQUIRED = set(['nversionbips', 'csv', 'segwit'])
#SEGWIT_ACTIVATION_VERSION = 16
