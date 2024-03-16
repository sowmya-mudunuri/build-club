import cv2
cam = cv2.VideoCapture(0)
width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cam.get(cv2.CAP_PROP_FPS)
output_file = r"C:\Users\Sowmya Mudunuri\OneDrive\Desktop\CV_Builder_Series\task_2\recording.MP4"
output = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'H264'), fps, (width, height))
while True:
    _ , frame = cam.read()
    cv2.imshow('Webcam', frame)
    output.write(frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()
output.release()
cv2.destroyAllWindows()