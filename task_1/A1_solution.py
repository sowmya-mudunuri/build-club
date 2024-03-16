import cv2
tom_image_path = "tom.jpg"
rdj_image_path = "rdj.jpg"
tom_image = cv2.imread(tom_image_path)
rdj_image = cv2.imread(rdj_image_path)
combined_image = cv2.hconcat([tom_image, rdj_image])
combined_image_gray = cv2.cvtColor(combined_image, cv2.COLOR_BGR2GRAY)
combined_image_gray_new = cv2.cvtColor(combined_image_gray, cv2.COLOR_GRAY2BGR)
solution = cv2.vconcat([combined_image, combined_image_gray_new])
cv2.imwrite("A1_solution.jpg",solution)
cv2.imshow("Output",combined_image)
cv2.imshow("Output_gray",combined_image_gray)
cv2.imshow("Solution",solution)
cv2.waitKey()
cv2.destroyAllWindows()