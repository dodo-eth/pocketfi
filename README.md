1) clone repo 
2) pip3 install -r requirements.txt
3) mv folder to /root/PocketFi/
4) mv PocketFi.service /etc/systemd/system/
5) sudo systemctl daemon-reload
6) systemctl start PocketFi.service && systemctl enable PocketFi.service