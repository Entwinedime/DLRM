FROM oneflowinc/oneflow:nightly-cuda11.8

RUN pip3 install --upgrade pip
RUN pip3 install petastorm
RUN pip3 install pyarrow==10.0.1
RUN pip3 install torch torchvision tensorboard

RUN apt update && apt install -y \
    openjdk-11-jdk
