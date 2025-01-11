FROM quay.io/ceph/ceph:v18.2.2

RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-* && \
    sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-* && \
    rm -f /etc/yum.repos.d/_copr:copr.fedorainfracloud.org:tchaikov:python-scikit-learn.repo && \
    dnf install -y python3 python3-pip

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

COPY placementoptimizer.py /usr/local/bin/placementoptimizer
RUN chmod +x /usr/local/bin/placementoptimizer
