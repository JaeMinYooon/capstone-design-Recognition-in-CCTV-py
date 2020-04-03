import cv2

capture = cv2.VideoCapture("airport.mp4")
print("프레임속도  : ", capture.get(cv2.CAP_PROP_FPS))
print("총 프레임   : ", capture.get(cv2.CAP_PROP_FRAME_COUNT))
print("프레임 시간 : ", capture.get(cv2.CAP_PROP_POS_MSEC))
print("프레임 현재 : ", capture.get(cv2.CAP_PROP_POS_FRAMES))
print("동영상 시간 : ", capture.get(cv2.CAP_PROP_FRAME_COUNT)/capture.get(cv2.CAP_PROP_FPS))



while True:
    if(capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):
        capture.open("airport.mp4")
    #if capture.get(cv2.CAP_PROP_POS_FRAMES)== 100:
    #    print( capture.get(cv2.CAP_PROP_POS_MSEC)/1000)
    #    break
    ret, frame = capture.read()
    if capture.get(cv2.CAP_PROP_POS_FRAMES) >300:
        cv2.imshow("VideoFrame", frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    if cv2.waitKey(33) > 0: break

capture.release()
cv2.destroyAllWindows()
