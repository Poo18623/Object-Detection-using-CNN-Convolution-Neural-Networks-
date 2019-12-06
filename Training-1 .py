# importing required libraries
import pandas as pd
import cv2
import os

#C:/Users/Pujitha/Desktop/Summer/edited data/Merged 100 images (P)-val.csv/Merged 84 images(P)-train.csv
#C:/Users/Pujitha/Desktop/Summer/edited data/Pose-1 Validation images and folders/Merged csv of internet images of pose 1 right.csv
input = "train_images/"
train = pd.read_csv(input+'merge.csv')

i = 1
j = 1
k = 1
l = 1

for idx, photo in enumerate(sorted(os.listdir(input))):
    if not photo.lower().endswith('.jpg'):
        continue
    photo_name = os.path.join(input,photo)
    img1 = cv2.imread(photo_name)


##cv2.imshow("img1",img1)
##cv2.waitKey(0)


    # iterating over the image for different objects
    for _,row in train[train.filename == photo].iterrows():
        xmin = row.xmin
        ymin = row.ymin
        xmax = row.xmax
        ymax = row.ymax

        #print(row.class_name)

        if row.class_name == "palm close":
            print("palm close")
            image_new = img1[ymin:ymax,xmin:xmax]
            cv2.imwrite(input+"palm close/palm close_%d.jpg"%i,image_new)
            print("[INFO] Saved "+str(photo))
            i+=1
        elif row.class_name == "legs straight":
            print("legs straight")
            image_new = img1[ymin:ymax,xmin:xmax]
            cv2.imwrite(input+"legs straight/legs straight_%d.jpg"%j,image_new)
            print("[INFO] Saved "+str(photo))
            j+=1
        elif row.class_name =="namaskar right":
            print("namaskar right")
            image_new = img1[ymin:ymax,xmin:xmax]
            cv2.imwrite(input+"namaskar right/namaskar right_%d.jpg"%k,image_new)
            print("[INFO] Saved "+str(photo))
            k+=1
        elif row.class_name =="palm open":
            print("palm open")
            image_new = img1[ymin:ymax,xmin:xmax]
            cv2.imwrite(input+"palm open/palm open_%d.jpg"%l,image_new)
            print("[INFO] Saved "+str(photo))
            l+=1
        elif row.class_name =="namaskar wrong":
            print("namaskar wrong")
            image_new = img1[ymin:ymax,xmin:xmax]
            cv2.imwrite(input+"namaskar wrong/namaskar wrong_%d.jpg"%l,image_new)
            print("[INFO] Saved "+str(photo))
            l+=1
        elif row.class_name =="legs wrong":
            print("legs wrong")
            image_new = img1[ymin:ymax,xmin:xmax]
            #cv2.imshow("img",image_new)
            #cv2.waitKey(0)
            cv2.imwrite(input+"legs wrong/legs wrong_%d.jpg"%l,image_new)
            print("[INFO] Saved "+str(photo))
            l+=1
        elif row.class_name =="hands up":
            print("hands up")
            image_new = img1[ymin:ymax,xmin:xmax]
            #cv2.imshow("img",image_new)
            #cv2.waitKey(0)
            cv2.imwrite(input+"hands up/hands up_%d.jpg"%l,image_new)
            print("[INFO] Saved "+str(photo))
            l+=1
        elif row.class_name =="head down":
            print("head down")
            image_new = img1[ymin:ymax,xmin:xmax]
            #cv2.imshow("img",image_new)
            #cv2.waitKey(0)
            cv2.imwrite(input+"head down/head down_%d.jpg"%l,image_new)
            print("[INFO] Saved "+str(photo))
            l+=1
        elif row.class_name =="hands down":
            print("hands down")
            image_new = img1[ymin:ymax,xmin:xmax]
            #cv2.imshow("img",image_new)
            #cv2.waitKey(0)
            cv2.imwrite(input+"hands down/hands down_%d.jpg"%l,image_new)
            print("[INFO] Saved "+str(photo))
            l+=1
        elif row.class_name =="right leg":
            print("right leg")
            image_new = img1[ymin:ymax,xmin:xmax]
            #cv2.imshow("img",image_new)
            #cv2.waitKey(0)
            cv2.imwrite(input+"right leg/right leg_%d.jpg"%l,image_new)
            print("[INFO] Saved "+str(photo))
            l+=1
        elif row.class_name =="hands wrong":
            print("hands wrong")
            image_new = img1[ymin:ymax,xmin:xmax]
            #cv2.imshow("img",image_new)
            #cv2.waitKey(0)
            cv2.imwrite(input+"hands wrong/hands wrong_%d.jpg"%l,image_new)
            print("[INFO] Saved "+str(photo))
            l+=1
print("[INFO] Saved Successfully :-)")