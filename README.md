# stdin2sock
Send stdin data stream to socket. Experimentation.

## Use-case

`raspivid` can accept TCP or UDP connections and send the video data stream there. It however is restricted to IPv4 connections. As an alternative have it send the video stream data to its stdout and pipe it to this stdin2socket streamer accepting IPv4 and IPv6 connections.

Inspiration mostly taken from:

https://docs.python.org/3.8/library/socket.html#example
