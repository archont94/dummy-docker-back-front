FROM python:3
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY backend.py backend.py
CMD ["python", "-u", "backend.py" ]
