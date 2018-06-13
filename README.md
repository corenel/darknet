![Darknet Logo](http://pjreddie.com/media/files/darknet-black-small.png)

#Darknet#
Darknet is an open source neural network framework written in C and CUDA. It is fast, easy to install, and supports CPU and GPU computation.

For more information see the [Darknet project website](http://pjreddie.com/darknet).

For questions or issues please use the [Google Group](https://groups.google.com/forum/#!forum/darknet).

# Usage

```shell
# make darknet
make -j
# get pretrained weights
wget http://pjreddie.com/media/files/darknet.conv.weights
# start training
./darknet yolo train cfg/tiny-yolo-hum.cfg darknet.conv.weights
```

See [this post](https://www.yuthon.com/2016/11/12/Train-YOLO-on-our-own-dataset/) for traning YOLOv1

