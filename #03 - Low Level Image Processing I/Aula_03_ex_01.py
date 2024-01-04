# Aula_02_ex_01.py
#
# Drawing of 2D primitives and user Interaction
#
# Paulo Dias 


# import
import numpy as np
import cv2

gray_image = None

def mouse_gray(event, x, y, flags, params):
	choice = int(params)
	if event == cv2.EVENT_LBUTTONDOWN:
		if choice == 49:
			cv2.line(gray_image, (x - 20, y - 20), (x + 20, y + 20), (255))
			cv2.imshow("GRAY", gray_image)
		if choice == 50:
			cv2.circle(gray_image, (x, y), 10, (255))
			cv2.imshow("GRAY", gray_image)
		if choice == 51:
			cv2.rectangle(gray_image, (x - 10, y - 10), (x + 10, y + 10), (255))
			cv2.imshow("GRAY", gray_image)

def mouse_rgb(event, x, y, flags, params):
	if event == cv2.EVENT_LBUTTONDOWN:
		if params == 49:
			cv2.line(rgb_image, (x - 20, y - 20), (x + 20, y + 20), (0, 0, 255))
			cv2.imshow("RGB", rgb_image)
		if params == 50:
			cv2.circle(rgb_image, (x, y), 10, (255, 0, 0))
			cv2.imshow("RGB", rgb_image)
		if params == 51:
			cv2.rectangle(rgb_image, (x - 10, y - 10), (x + 10, y + 10), (0, 255, 0))
			cv2.imshow("RGB", rgb_image)

# Create two black windows
gray_image = np.zeros((512, 256,1))
rgb_image = np.zeros((512, 256, 3))

# Windows
cv2.namedWindow("GRAY", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("RGB", cv2.WINDOW_AUTOSIZE)

# Show images and print characteristics
cv2.imshow("GRAY", gray_image)
print("Gray level image")
print("Number of lines : %d" % gray_image.shape[0])
print("Number of columns : %d" % gray_image.shape[1])
print("Number of channels : %d" % 1)
print("Number of elements : %d" % gray_image.size)

cv2.imshow("RGB", gray_image)
print("Rgb level image")
print("Number of lines : %d" % rgb_image.shape[0])
print("Number of columns : %d" % rgb_image.shape[1])
print("Number of channels : %d" % rgb_image.shape[2])
print("Number of elements : %d" % rgb_image.size)

choice = 49

cv2.setMouseCallback("GRAY", mouse_gray, choice)
cv2.setMouseCallback("RGB", mouse_rgb, choice)
#
#  Processo keyboard input
while True:
	print("\n")
	print("1 -- Segmento de Recta")
	print("2 -- Circulo")
	print("3 -- Quadrado")
	print("Q -- Terminar")

	choice = cv2.waitKey(0);
	print(choice)

	if choice == 81 or choice == 113:
		break;

	if choice == 49:
		print("SEGMENTO DE RECTA : ")
		print("Seleccione o ponto medio com o BOTAO ESQUERDO do rato")
		cv2.setMouseCallback("GRAY", mouse_gray, choice)
		cv2.setMouseCallback("RGB", mouse_rgb, choice)

	if choice == 50:
		print("CIRCULO : Seleccione o centro com o BOTAO ESQUERDO do rato")
		cv2.setMouseCallback("GRAY", mouse_gray, choice)
		cv2.setMouseCallback("RGB", mouse_rgb, choice)

	if choice == 51:
		print("QUADRADO : Seleccione o centro com o BOTAO ESQUERDO do rato")
		cv2.setMouseCallback("GRAY", mouse_gray, choice)
		cv2.setMouseCallback("RGB", mouse_rgb, choice)

cv2.destroyAllWindows();
