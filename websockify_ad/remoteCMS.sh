#!/bin/bash
nohup /opt/websockify/websockify/run \
--web="/opt/adwebsockify/websockify_ad/noVNC" \
--token-plugin=AuthServer 6080

# no hang up, run the programmin background even if terminal windows is closed.

