FROM python:3
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY frontend.py frontend.py
CMD ["python", "-u", "frontend.py" ]
