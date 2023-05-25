## Concurrency? CPython?
As I started to learn Python, I did a bit research on concurrency and parallelism. It turns out Python's threading is not the same as pthread in C because there is a thing called Global Interpreter Lock. Since Python uses reference counting for memory management, GIL is there to protect memory from sometimes leaking, not releasing, or incorrectly releasing when dealing with multiple threads.<br>

CPU intensive(matrix calc, image processing, etc)--> use multiprocessing<br>
IO intensive(write to disk, network read write, etc)--> use threading or asyncio<br>

Uhm, so thread or asyncio? I am going to use asyncio.