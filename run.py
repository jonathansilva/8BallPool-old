import cv2
import numpy as np
#import pyscreenshot as ImageGrab

def nothing(x):
    pass

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

def drawCirclesHoles(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.blur(gray, (3, 3))

    holes = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 20, param1 = 25, param2 = 25, minRadius = 12, maxRadius = 16)

    if holes is not None:
        holes = np.uint16(np.around(holes))

        for pt in holes[0, :]:
            a, b, r = pt[0], pt[1], pt[2]

            cv2.circle(frame, (a, b), r, (0, 255, 0), 2)
            cv2.circle(frame, (a, b), 1, (0, 0, 255), 2)

def main():
    '''
        Resolução dos screenshots do smartphone: 1080 x 1920
    '''

    # Tira screenshots da tela
    #original_frame = ImageGrab.grab(bbox = ( ... ))

    original_frame = cv2.imread('./screenshots/1.jpg')

    width = original_frame.shape[1] # 1280
    height = original_frame.shape[0] # 720

    xA = int(height * 0.161000) # Margin Top
    xB = int(width * 0.557800) # Margin Bottom
    yA = int(height * 0.138000) # Margin Left
    yB = int(width * 0.921000) # Margin Right

    # Pega apenas a mesa
    board = original_frame[xA : xB, yA : yB]
    frame = board.copy()

    # Modifica a escala da mesa em 50%
    scale_percent = 50
    original_width = int(board.shape[1] * scale_percent / 100)
    original_height = int(board.shape[0] * scale_percent / 100)
    frame = cv2.resize(board, (original_width, original_height))

    # Paredes
    '''
    drawLineLeft(frame)
    drawLineRight(frame)
    drawLineTopLeft(frame)
    drawLineTopRight(frame)
    drawLineBottomLeft(frame)
    drawLineBottomRight(frame)
    '''

    # Caçapas
    drawCirclesHoles(frame)

    while True:
        # Criar circulo com a linha

        cv2.imshow('Resultado', frame)

        key = cv2.waitKey(1)

        if key == 27:
            break

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
