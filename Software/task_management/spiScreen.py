import time # Manejo de pausas
import datetime # Obtener tiempo
import board # Interfaz para uso nativo de la Omega2+
import busio # Uso de buses SPI e I2C
import digitalio # Uso de GPIO para driver SSD1306
import adafruit_ssd1306 # Driver SSD1306
from un_logo import un_matrix # Logo UN

# Bus para MCP3021
i2c = busio.I2C(board.SCL, board.SDA)

# Bus para SSD1306
spi = busio.SPI(board.SCK, MOSI=board.MOSI)
reset_pin = digitalio.DigitalInOut(board.D1)
cs_pin = digitalio.DigitalInOut(board.D6)
dc_pin = digitalio.DigitalInOut(board.D0)

# Inicializacion de SSD1306
oled = adafruit_ssd1306.SSD1306_SPI(128, 32, spi, dc_pin, reset_pin, cs_pin)
oled.fill(0)
oled.show()
oled.rotate(False)

# Dibujar logo UN en SSD1306
for y in range(0, len(un_matrix)):
	for x in range(0, len(un_matrix[y])):
		oled.pixel(un_matrix[y][x], y+13, 1)
oled.text("Campus", 62, 16, 1)

# Sensado de voltaje en MCP3021
rawBytes = bytearray(2)
i2c.readfrom_into(0x4d, rawBytes)
adcOutput = (rawBytes[0]<<6) | (rawBytes[1]>>2)
adcIn = adcOutput * 3.27 / 1024
batteryVoltage = adcIn / (220.0/288)
batteryPercentage = (100/0.7)*batteryVoltage-500

# Visualizacion info de la bateria en la SSD1306
oled.text("%.2f"%(batteryVoltage), 0, 0, 1)
oled.text("%d%%" %batteryPercentage, 110, 0, 1)

# Temporizador para operaciones periodicas
timer = 0

# Ciclo principal
while True:
	if timer >= 10:
		# Sensado de voltaje en MCP3021
		i2c.readfrom_into(0x4d, rawBytes)
		adcOutput = (rawBytes[0]<<6) | (rawBytes[1]>>2)
		adcIn = adcOutput * 3.27 / 1024
		batteryVoltage = adcIn / (220.0/288)
		batteryPercentage = (100/0.7)*batteryVoltage-500
		
		# Visualizacion info de la bateria en la SSD1306
		oled.fill_rect(0, 0, 127, 8, 0)
		oled.text("%.2f"%(batteryVoltage), 0, 0, 1)
		oled.text("%d%%" %batteryPercentage, 110, 0, 1)
		
		timer = 0 # Reinicio temporizador
	
	# Obtener tiempo
	now = datetime.datetime.now()
	timeString = now.strftime("%H:%M:%S")
	
	# Sobreescribir tiempo en SSD1306
	oled.fill_rect(42, 0, 48, 8, 0)
	oled.text(timeString, 43, 0, 1)
	oled.show()
	
	# Iteracion del ciclo
	timer += 1
	time.sleep(0.9)
