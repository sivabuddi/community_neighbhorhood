from pascal_voc_writer import Writer
import math

# Writer(path, width, height)
import glob
import json
classes = ['house']

train_file = open('Dataset/VOC2007/ImageSets/Main/train.txt','w')
for filepath in glob.iglob('s_dataset/ann/*.json'):
    with open(filepath,'r') as supervisely_file:
        json_obj = json.load(supervisely_file)
        print(json_obj)
        file_name = filepath.split('\\')[1].split('.json')[0]
        print(file_name)
        writer = Writer('Dataset/VOC2007/JPEGImages/'+file_name, 640, 640)
        bounding_box_length = len(json_obj['objects'])
        if bounding_box_length>0:
            train_file.write(filepath.split('\\')[1].split('.jpg')[0] + '\n')

        for item in range(0, bounding_box_length):
            class_name = "house"
            bounding_box_coordinates = json_obj['objects'][item]['points']['exterior']
            writer.addObject(class_name, bounding_box_coordinates[0][0], bounding_box_coordinates[0][1], bounding_box_coordinates[1][0], bounding_box_coordinates[1][1])

            writer.save('Dataset/VOC2007/Annotations/'+ filepath.split('\\')[1].split('.jpg')[0] + '.xml')


