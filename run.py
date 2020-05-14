import cv2
import numpy as np
#import pyscreenshot as ImageGrab

def passFunction():
    pass

def drawRectangle(frame):
    return cv2.rectangle(frame, (76, 85), (563, 329), (0, 0, 0), thickness = 1)

def draw_lines(frame, lines):
    for rho, theta in lines[0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))

        cv2.line(frame, (x1, y1), (x2, y2), [0, 0, 255], thickness = 2)

def weighted_frame(hough_lines_image, frame):
    return cv2.addWeighted(frame, 0.8, hough_lines_image, 1, 0)

def main():
    # Tira screenshots da tela
    #original_frame = ImageGrab.grab(bbox = (100, 10, 400, 400))

    original_frame = cv2.imread('./screenshots/1.jpg')
    frame = original_frame.copy()
    windowName = 'Original'
    cv2.namedWindow(windowName)

    threshold1 = 255
    threshold2 = 255
    cv2.createTrackbar('threshold 1', windowName, threshold1, 255, passFunction)
    cv2.createTrackbar('threshold 2', windowName, threshold2, 255, passFunction)

    # Modifica a escala
    scale_percent = 50
    original_width = int(original_frame.shape[1] * scale_percent / 100)
    original_height = int(original_frame.shape[0] * scale_percent / 100)
    frame = cv2.resize(original_frame, (original_width, original_height))

    ''' Bônus
    height = frame.shape[0]
    width = frame.shape[1]

    print('Height: ', height) # 360
    print('Width: ', width) # 640
    '''
    drawRectangle(frame)

    while True:
        _threshold1 = cv2.getTrackbarPos('threshold 1', windowName)
        _threshold2 = cv2.getTrackbarPos('threshold 2', windowName)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, _threshold1, _threshold2, apertureSize = 3)

        lines = cv2.HoughLines(edges, rho = 1, theta = np.pi / 180, threshold = 155)

        hough_lines_image = np.zeros_like(frame)

        draw_lines(hough_lines_image, lines)

        original_image_with_hough_lines = weighted_frame(hough_lines_image, frame)

        cv2.imshow(windowName, original_image_with_hough_lines)
        #cv2.imshow('Edges', edges)

        key = cv2.waitKey(1)

        if key == 27:
            break

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
