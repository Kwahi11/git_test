[Unit]
Description=Tracking Car Auto Start Script
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/pi/Desktop/tracking_test02.py
WorkingDirectory=/home/pi/Desktop
StandardOutput=inherit
StandardError=inherit
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
