#"C:\Users\Sowmya Mudunuri\OneDrive\Desktop\CV_Builder_Series\task_2\checkerboard.MP4"
import numpy as np
import cv2
rows, cols = 4, 4
square_size = 100
canvas = np.ones((rows * square_size, cols * square_size, 3), dtype=np.uint8) * 255
for row in range(rows):
    for col in range(cols):
        if (row + col) % 2 == 1:
            canvas[row * square_size : (row + 1) * square_size, col * square_size : (col + 1) * square_size] = 0
cv2.imshow('Checkerboard', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
