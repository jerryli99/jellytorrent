import asyncio
from bt_decode import tokenize

class TorrentFile:
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

if __name__ == "__main__":
    with TorrentFile("torrents/debian-11.6.0-amd64-netinst.iso.torrent") as torrent_file:
        print(torrent_file.read())
        #decode.tokenize(torrent_file.read())