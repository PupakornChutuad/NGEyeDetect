from __future__ import division
from PySide2.QtCore import QRunnable, QSignalTransition, Signal, QObject
import cv2
import  numpy as np
import  dlib
import time



class Eyedetec_msg:
    def __init__(self):
        self.Eyedetec_start = False
        self.eye_position = "Off"
        self.eye_right = 0
        self.eye_center = 0
        self.eye_left = 0




def midpoint(p1 ,p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)

font = cv2.FONT_HERSHEY_PLAIN

def get_gaze_ratio(eye_points, facial_landmarks,frame,gray):
    left_eye_region = np.array([(facial_landmarks.part(eye_points[0]).x, facial_landmarks.part((eye_points[0])).y),
                                (facial_landmarks.part((eye_points[1])).x, facial_landmarks.part((eye_points[1])).y),
                                (facial_landmarks.part((eye_points[2])).x, facial_landmarks.part((eye_points[2])).y),
                                (facial_landmarks.part((eye_points[3])).x, facial_landmarks.part((eye_points[3])).y),
                                (facial_landmarks.part((eye_points[4])).x, facial_landmarks.part((eye_points[4])).y),
                                (facial_landmarks.part((eye_points[5])).x, facial_landmarks.part((eye_points[5])).y)], np.int32)



    height, width, _ = frame.shape
    mask = np.zeros((height, width), np.uint8)
    cv2.polylines(mask, [left_eye_region], True, 255, 2)
    cv2.fillPoly(mask, [left_eye_region], 255)
    eye = cv2.bitwise_and(gray, gray, mask=mask)

    min_x = np.min(left_eye_region[:, 0])
    max_x = np.max(left_eye_region[:, 0])
    min_y = np.min(left_eye_region[:, 1])
    max_y = np.max(left_eye_region[:, 1])

    gray_eye = eye[min_y: max_y, min_x: max_x]
    _, threshold_eye = cv2.threshold(gray_eye, 70, 255, cv2.THRESH_BINARY)
    height, width = threshold_eye.shape
    left_side_threshold = threshold_eye[0: height, 0: int(width / 2)]
    left_side_white = cv2.countNonZero(left_side_threshold)

    right_side_threshold = threshold_eye[0: height, int(width / 2): width]
    right_side_white = cv2.countNonZero(right_side_threshold)

    if left_side_white == 0:
        gaze_ratio = 1
    elif right_side_white == 0:
        gaze_ratio = 5
    else:
        gaze_ratio = left_side_white / right_side_white
    return gaze_ratio

class EyedetecSignel(QObject) :
    finished = Signal(str)
    updateEyedetec = Signal(str)
    updateTotaleye = Signal(str)
    updateMissing = Signal(str)
    updateArrive = Signal(str)
class Eyedetec_Thread(QRunnable):

    def __init__(self,msg : Eyedetec_msg):
        super(Eyedetec_Thread, self).__init__()
        self.msg = msg
        self.signel = EyedetecSignel()

    def run(self):
        cap = cv2.VideoCapture(0)


        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
        totalright = 0
        totalcenter = 0
        totalleft = 0
        while self.msg.Eyedetec_start:
            time.sleep(1/10)
            _, frame = cap.read()
            new_frame = np.zeros((500, 500, 3), np.uint8)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = detector(gray)
            if len(faces) == 0 :
                self.signel.updateEyedetec.emit("MISSING")
                self.signel.updateMissing.emit("OK")
            else :
                self.signel.updateArrive.emit("OK")
                for face in faces:

                    landmarks = predictor(gray, face)

                    gaze_ratio_left_eye = get_gaze_ratio([36, 37, 38, 39, 40, 41], landmarks, frame, gray)
                    gaze_ratio_right_eye = get_gaze_ratio([42, 43, 44, 45, 46, 47], landmarks, frame, gray)
                    gaze_ratio = (gaze_ratio_right_eye + gaze_ratio_left_eye) / 2

                    # facepocition
                    if gaze_ratio < 0.5 and gaze_ratio > 0:
                        cv2.putText(frame, "RIGHT", (50, 100), font, 2, (0, 0, 255), 3)
                        self.signel.updateEyedetec.emit("RIGHT")
                        # totalright += 1
                        # print("Right" ,totalright)


                    elif 0.5 < gaze_ratio < 1.2:
                        cv2.putText(frame, "CENTER", (50, 100), font, 2, (0, 0, 255), 3)
                        self.signel.updateEyedetec.emit("CENTER")
                        # totalcenter += 1
                        # print("Center", totalcenter)

                    elif gaze_ratio > 1.2:
                        cv2.putText(frame, "LEFT", (50, 100), font, 2, (0, 0, 255), 3)
                        self.signel.updateEyedetec.emit("LEFT")
                        # totalleft += 1
                        # print("Left",totalleft)





                # key = cv2.waitKey(1)
                # if key == 27:
                #     break
        self.signel.finished.emit("stop")

        cap.release()
        cv2.destroyAllWindows()