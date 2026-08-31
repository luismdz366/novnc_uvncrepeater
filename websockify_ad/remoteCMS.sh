#!/bin/bash
nohup /usr/local/adpgcc/Version1.1/websockify-master/run \
--web="/usr/local/adpgcc/Version1.1/noVNC-master" \
--token-plugin=AuthServer 6080 >> /var/log/adremote.log &

# no hang up, run the programmin background even if terminal windows is closed.

