FROM quay.io/ceph/ceph:v19.2.0

RUN dnf install -y python3 python3-pip

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

COPY placementoptimizer.py /usr/local/bin/placementoptimizer
RUN chmod +x /usr/local/bin/placementoptimizer
