# Jellytorrent -- a BitTorrent Client & ...?

(I am making the client first. If I want, maybe I will also implement the server tracker)

## Supported features:
Planning to do http, https, udp 


## Development timeline status:<br>
| Time & Date | Description |
| --- | --- |
| 05/23/2023 | planning stage, using CPython 3.10.6 |
| 05/30/2023 | plan to at least have the .torrent parser done |


## Style guides
Yes, I added the prefix jelly for every Python module name. Please don't judge if you attemp to.<br> 

https://peps.python.org/pep-0008

## Concurrency? CPython?
As I started to learn Python, I did a bit research on concurrency and parallelism. It turns out Python's threading is not the same as pthread in C because there is a thing called Global Interpreter Lock. Since Python uses reference counting for memory management, GIL is there to protect memory from sometimes leaking, not releasing, or incorrectly releasing when dealing with multiple threads.<br>

CPU intensive(matrix calc, image processing, etc)--> use multiprocessing<br>
IO intensive(write to disk, network read write, etc)--> use threading or asyncio<br>

Uhm, so thread or asyncio? I might use asyncio.
