import datetime
import csv
from face_recognition import recognize_face
from emotion_detection import detect_emotion
START_TIME=datetime.time(9,30)
END_TIME=datetime.time(10,0)  # Defining time limits for attendance
def is_within_time():
    current_time=datetime.datetime.now().time()
    return START_TIME<=current_time<=END_TIME
def log_attendance(student_name,emotion,confidence):
    with open('attendance.csv','a',newline='') as file:
        writer=csv.writer(file)
        writer.writerow([student_name,emotion,confidence,datetime.datetime.now()])
def mark_attendance(image_path):
    if is_within_time():
        student_id,confidence_face=recognize_face(image_path)
        emotion_id,confidence_emotion=detect_emotion(image_path)
        # Replace  this with real student names and emotions
        student_name=f'Student_{student_id}'
        emotion=f'Emotion_{emotion_id}'
        log_attendance(student_name,emotion,confidence_face)
if __name__=='__main__':
    image_path='give your image here as .jpg format'
    mark_attendance(image_path)