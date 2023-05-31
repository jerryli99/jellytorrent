import typing
from enum import Enum

class CodeType(Enum):
    INT  = 0x69
    LIST = 0x6c
    DICT = 0x64
    END  = 0x65
    STR_DELIMITER = 0x3a


class TorrentFileOpen:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, 'rb')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()

#---------------------------------
# There are two versions of bittorrent files, v1 and v2. for now implement v1 decoding
def decode_dict(data: bytes):
    
    



if __name__ == "__main__":
    with TorrentFileOpen("/home/jellybt/jellytorrent/torrents/test.torrent") as torrent_file:
        data: bytes = torrent_file.read() # this will print out binary data
        print(data, len(data))
        