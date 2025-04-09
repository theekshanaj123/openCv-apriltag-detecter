import cv2
import serial
import time
from pyapriltags import Detector

# Global config
SERIAL_PORT = "COM16"  # Change this to your Arduino COM port
BAUD_RATE = 9600
IMAGE_FILE = "captured_img.jpg"

# Supported AprilTag families
TAG_FAMILIES = [
    'tag36h11', 'tag25h9', 'tag16h5',
    'tagStandard41h12', 'tagStandard52h13',
    'tagCircle21h7', 'tagCircle49h12',
    'tagCustom48h12'
]

def init_serial(port, baud):
    ser = serial.Serial(port, baud, timeout=1)
    time.sleep(2)  # Wait for Arduino to reset
    return ser

def wait_for_trigger(ser, trigger_value="20"):
    print("Waiting for trigger...")
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode("utf-8").strip()
            print("Received:", data)
            if data == trigger_value:
                return

def capture_image(filename):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    if ret:
        cv2.imwrite(filename, frame)
        print(f"Image saved as {filename}")
        return filename
    else:
        print("Failed to capture image.")
        return None

def detect_apriltags(image_path, families):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    best_id = None
    best_margin = 0

    for family in families:
        detector = Detector(families=family)
        results = detector.detect(image)

        print(results)
        # if not results:
        #     break
        if results:
            print(f"\n Family: {family}")
            for det in results:
                print(f"Tag ID: {det.tag_id}, Margin: {det.decision_margin:.2f}")
                if det.decision_margin > best_margin:
                    best_margin = det.decision_margin
                    best_id = det.tag_id

            if best_id is not None:
                print(f"\nBest Tag ID: {best_id} (Margin: {best_margin:.2f})")
                break  # Stop after finding the best tag

    return best_id

def serial_out(best_tag):
    ser.write(f"{best_tag}\n".encode())

# ---- Main Logic ----
if __name__ == "__main__":
    # ser = init_serial(SERIAL_PORT, BAUD_RATE)
    # wait_for_trigger(ser)

    image_path = capture_image(IMAGE_FILE)
    if image_path:
        best_tag = detect_apriltags(image_path, TAG_FAMILIES)

    # serial_out(best_tag)

    cv2.destroyAllWindows()
    exit()