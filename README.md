This project is a lightweight, self hosted system monitoring dashboard for Raspberry Pi.



It displays Live CPU, RAM, disk temperature, uptime and network stats, refreshed automatically every 5 seconds



This project was built with FastAPI, UVIcorn, psutil, and a simple HTML/JS frontend. 



Features:

&nbsp;	

&nbsp;	-Live Raspberry Pi metrics:



&nbsp;		-CPU usage



&nbsp;		-RAM usage



&nbsp;		-Disk usage



&nbsp;		-Temperature



&nbsp;		-Network I/O



&nbsp;		-System uptime



&nbsp;	-Auto-refreshing dashboard (every 5 seconds)



&nbsp;	-REST API (/api/metrics/latest)



&nbsp;	-Can be accessed from any device on your network



&nbsp;	-Clean, responsive UI



&nbsp;	-Easy to install and run



Project structure:

rpi-monitor-dashboard/

├── backend/

│   ├── app.py

│   ├── metrics.py

│   ├── requirements.txt

├── frontend/

│   ├── index.html

│   └── script.js

├── Example-dashboard.png      

└── README.md





Installation and Setup:



Update system packages

&nbsp;	sudo apt update

&nbsp;	

&nbsp;	sudo apt upgrade -y



Install required system packages

&nbsp;	sudo apt install python3 python3-pip python3-venv git -y



Clone the repository

&nbsp;	git clone https://github.com/fortunatah/rpi-monitor-dashboard.git

&nbsp;	cd rpi-monitor-dashboard



Create and activate the virtual environment

&nbsp;	python3 -m venv venv

&nbsp;	source venv/bin/activate



Install backend dependencies

&nbsp;	cd backend

&nbsp;	pip install -r requirements.txt



Run the API server

&nbsp;	uvicorn app:app --host 0.0.0.0 --port 8000



Access the API at

&nbsp;	http://<pi-ip>:8000/



See example dashboard on what dashboard should look like if program is ran properly.



&nbsp;	









