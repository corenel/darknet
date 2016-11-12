from __future__ import print_function
import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

labels = ['ball', 'goal']
label_numbers = ['n04254680', 'n03820318']
label_dict = dict(zip(labels, label_numbers))
label_number_dict = dict(zip(label_numbers, labels))


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(label, label_dir, label_file, img_id):
    in_file = open('%s/%s' % (label_dir, label_file))
    out_file = open('labels/%s/%s.txt' % (label, img_id), 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if (cls not in labels and cls not in label_numbers) or int(difficult) == 1:
            continue
        if cls in labels:
            cls_id = labels.index(cls)
        if cls in label_numbers:
            cls_id = label_numbers.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text),
             float(xmlbox.find('xmax').text),
             float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


if __name__ == "__main__":
    pwd = getcwd()
    if not os.path.exists('labels/'):
        os.makedirs('labels/')
    list_file = open('train.txt', 'w')
    for label in labels:
        if not os.path.exists('labels/%s' % label):
            os.makedirs('labels/%s' % label)
        label_dir = 'annotations/%s' % label
        img_dir = 'images/%s' % label
        label_files = listdir(label_dir)
        img_files = listdir(img_dir)
        # Remove those not in Images
        label_files = [x for x in label_files
                       if x.split('.')[0] + '.JPEG' in img_files]

        for label_file in label_files:
            img_id = label_file.split('.')[0]
            img_path = '%s/%s/%s\n' % (pwd, img_dir, img_id + '.JPEG')
            list_file.write(img_path)
            convert_annotation(label, label_dir, label_file, img_id)
    list_file.close()
