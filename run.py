import cv2
import numpy as np
import pyscreenshot as ImageGrab

def passFunction():
    pass

def main():
    # Tira screenshots da tela
    #img = ImageGrab.grab(bbox = (100, 10, 400, 400))

    # Pega a imagem original e modifica a escala
    original_frame = cv2.imread('./screenshots/1.jpg')

    frame = cv2.GaussianBlur(original_frame, (5, 5), 0)
    windowName = 'Original'
    cv2.namedWindow(windowName)

    threshold1 = 50
    threshold2 = 150
    cv2.createTrackbar('threshold 1', windowName, threshold1, 255, passFunction)
    cv2.createTrackbar('threshold 2', windowName, threshold2, 255, passFunction)

    scale_percent = 50
    original_width = int(original_frame.shape[1] * scale_percent / 100)
    original_height = int(original_frame.shape[0] * scale_percent / 100)
    frame = cv2.resize(original_frame, (original_width, original_height))

    # Bônus
    height = frame.shape[0]
    width = frame.shape[1]

    print('Height: ', height)
    print('Width: ', width)

    while True:
        _threshold1 = cv2.getTrackbarPos('threshold 1', windowName)
        _threshold2 = cv2.getTrackbarPos('threshold 2', windowName)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, _threshold1, _threshold2, apertureSize = 3)

        lines = cv2.HoughLines(edges, rho = 1, theta = np.pi / 180, threshold = 50)

        for rho, theta in lines[0]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))

            cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

        cv2.imshow(windowName, frame)
        #cv2.imshow("Edges", edges)

        key = cv2.waitKey(1)

        if key == 27:
            break

    original_frame.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
