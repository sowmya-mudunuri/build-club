import cv2
path = r"C:\Users\Sowmya Mudunuri\OneDrive\Desktop\CV_Builder_Series\task_1\tom.jpg"
image = cv2.imread(path)
new_image = image[:10,:10]
B = new_image[:,:,0]
G = new_image[:,:,1]
R = new_image[:,:,2]
print('Blue Channel')
print(B)
print('Green Channel')
print(G)
print('Red Channel')
print(R)
#or 
b,g,r = cv2.split(new_image)
image_merged = cv2.merge((b,g,r)) 
image[:,:] = (0,0,0)
cv2.imshow("Output",image)
cv2.waitKey()
cv2.destroyAllWindows()