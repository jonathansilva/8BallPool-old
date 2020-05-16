import cv2
import numpy as np
#import pyscreenshot as ImageGrab

'''
    Requerimento de resolução dos screenshots: 1080 x 1920
'''

def passFunction():
    pass

# Remover este retângulo e criar linhas ( 6 ) que vão servir como paredes da mesa
def drawRectangle(frame):
    return cv2.rectangle(frame, (76, 85), (563, 329), (0, 0, 0), thickness = 1)

def drawLineLeft(frame):
    width = frame.shape[1] # 640
    height = frame.shape[0] # 360

    xA = int(width * 0.115625) # width 74
    yA = int(height * 0.288889) # height 104

    xB = int(width * 0.115625) # width 74
    yB = int(height * 0.855556) # height 308

    start_point = (xA, yA)
    end_point = (xB, yB)

    color = (0, 0, 0)
    thickness = 3
    image = cv2.line(frame, start_point, end_point, color, thickness)

def drawLineRight(frame):
    width = frame.shape[1] # 640
    height = frame.shape[0] # 360

    xA = int(width * 0.882813) # width 565
    yA = int(height * 0.288889) # height 104

    xB = int(width * 0.882813) # width 565
    yB = int(height * 0.855556) # height 308

    start_point = (xA, yA)
    end_point = (xB, yB)

    color = (0, 0, 0)
    thickness = 3
    image = cv2.line(frame, start_point, end_point, color, thickness)

def drawLineTopLeft(frame):
    width = frame.shape[1] # 640
    height = frame.shape[0] # 360

    xA = int(width * 0.148438) # width 95
    yA = int(height * 0.230556) # height 83

    xB = int(width * 0.475) # width 304
    yB = int(height * 0.230556) # height 83

    start_point = (xA, yA)
    end_point = (xB, yB)

    color = (0, 0, 0)
    thickness = 3
    image = cv2.line(frame, start_point, end_point, color, thickness)

def drawLineTopRight(frame):
    width = frame.shape[1] # 640
    height = frame.shape[0] # 360

    xA = int(width * 0.523438) # width 335
    yA = int(height * 0.230556) # height 83

    xB = int(width * 0.848438) # width 543
    yB = int(height * 0.230556) # height 83

    start_point = (xA, yA)
    end_point = (xB, yB)

    color = (0, 0, 0)
    thickness = 3
    image = cv2.line(frame, start_point, end_point, color, thickness)

def drawLineBottomLeft(frame):
    width = frame.shape[1] # 640
    height = frame.shape[0] # 360

    xA = int(width * 0.148438) # width 95
    yA = int(height * 0.919444) # height 331

    xB = int(width * 0.475) # width 304
    yB = int(height * 0.919444) # height 331

    start_point = (xA, yA)
    end_point = (xB, yB)

    color = (0, 0, 0)
    thickness = 3
    image = cv2.line(frame, start_point, end_point, color, thickness)

def drawLineBottomRight(frame):
    width = frame.shape[1] # 640
    height = frame.shape[0] # 360

    xA = int(width * 0.523438) # width 335
    yA = int(height * 0.919444) # height 331

    xB = int(width * 0.848438) # width 543
    yB = int(height * 0.919444) # height 331

    start_point = (xA, yA)
    end_point = (xB, yB)

    color = (0, 0, 0)
    thickness = 3
    image = cv2.line(frame, start_point, end_point, color, thickness)

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

    drawLineLeft(frame)
    drawLineRight(frame)
    drawLineTopLeft(frame)
    drawLineTopRight(frame)
    drawLineBottomLeft(frame)
    drawLineBottomRight(frame)

    #drawRectangle(frame)

    while True:
        _threshold1 = cv2.getTrackbarPos('threshold 1', windowName)
        _threshold2 = cv2.getTrackbarPos('threshold 2', windowName)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, _threshold1, _threshold2, apertureSize = 3)

        lines = cv2.HoughLines(edges, rho = 1, theta = np.pi / 180, threshold = 155)

        hough_lines_image = np.zeros_like(frame)

        draw_lines(hough_lines_image, lines)

        original_image_with_hough_lines = weighted_frame(hough_lines_image, frame)

        cv2.imshow(windowName, frame) # original_image_with_hough_lines
        #cv2.imshow('Edges', edges)

        key = cv2.waitKey(1)

        if key == 27:
            break

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
