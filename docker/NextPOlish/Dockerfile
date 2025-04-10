FROM ubuntu:24.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    libssl-dev \
    libffi-dev \
    libncurses5-dev \
    libncursesw5-dev \
    bzip2 \
    liblzma-dev \
    libbz2-dev \
    python3-setuptools \
    python3-venv \
    python3-wheel \
    wget \
    git \
    && apt-get clean

# Create a Python virtual environment
RUN python3 -m venv /opt/venv


# Activate the virtual environment and install Python dependencies
RUN /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install paralleltask

# Add the virtual environment to PATH
ENV PATH="/opt/venv/bin:$PATH"

RUN wget https://github.com/Nextomics/NextPolish/releases/latest/download/NextPolish.tgz && \
    pip install paralleltask && \
    tar -xvzf NextPolish.tgz && \
    git clone https://github.com/lh3/bwa.git && \
    cd bwa && \
    make && \
    cd .. && \
    rm -rf NextPolish/util/bwa && \
    mv bwa NextPolish/util/ && \
    cd NextPolish && \
    make && \
    cd .. && \
    rm NextPolish.tgz && \
    mv NextPolish /usr/local


WORKDIR /data


RUN mkdir -p /data/inital_assembly && \
    mkdir -p /data/short_reads && \
    mkdir -p data/output && \
    mkdir -p data/long_reads


ENV PATH="/usr/local/NextPolish/:$PATH"
