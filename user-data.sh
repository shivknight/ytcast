#!/bin/bash
date +%Y-%m-%d-%H-%M > /root/date

yum -y update
yum -y group install "Development Tools"

wget http://msp.ucsd.edu/Software/pd-0.49-0.src.tar.gz
tar xvzf pd-0.49-0.src.tar.gz
cd pd-0.49-0/
./autogen.sh
./configure
make

pip3 install rfeed
