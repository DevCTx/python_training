"""
    Shows another exception during the first one
"""
import traceback

class E(Exception):
    msg = ''
    def __init__(self,msg):
        E.msg = msg
        raise

try:
    raise E("unk")
except E as e:
    print("never until here because another exception appears!")
except Exception:
    print("What the F...", E.msg, traceback.format_exc())
else:
    print("ok")