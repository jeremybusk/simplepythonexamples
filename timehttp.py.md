# simplepythonexamples
Simple Python 3 Examples For doing certain things

```
useradd -r timehttp
```

/etc/systemd/system/timehttp.service
```
[Unit]
Description=Simple ntptime via HTTP Service to sync drifted hosts.
[Service]
User=timehttp
WorkingDirectory=/app/timehttp
ExecStart=/usr/bin/python3 /app/timehttp/timehttp.py
ExecReload=/bin/kill -SIGUSR1 \$MAINPID
[Install]
WantedBy=multi-user.target
```

```
systemctl enable timehttp.server
systemctl start timehttp.server
```
