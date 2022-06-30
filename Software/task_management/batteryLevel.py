# Importar lib I2C
from OmegaExpansion import onionI2C

# Crear objeto I2C
i2c = onionI2C.OnionI2C()

# Leer palabra de 2 bytes
rawBytes = i2c.readBytes(0x4d, 0x00, 2)

# Estructura de la lectura para el MCP3021
# [0][0][0][0][D9][D8][D7][D6] [D5][D4][D3][D1][D0][x][x]

# Opcional: Imprimir los bytes
#D9to6 = format(rawBytes[0], '08b')
#D5to0 = format(rawBytes[1], '08b')
#print(D9to6 + " " + D5to0)

# Realizar desplazamiento de 6 bits a la izquierda
# para el primer byte y 2 bits a la derecha para
# el segundo, formando los 10 bits de lectura.
adcOutput = (rawBytes[0]<<6) | (rawBytes[1]>>2)

# Opcional: Imprimir lectura en binario
#print format(adcOutput, '010b')

# Opcional: Imprimir lectura en entero
#print int(adcOutput)

# Voltaje obtenido en el ADC
adcIn = adcOutput * 3.27 / 1024

batteryVoltage = adcIn / (220.0/288)
print('Voltaje de la bateria: %.2f'%(batteryVoltage))

batteryPercentage = (100/0.7)*batteryVoltage-500
print('Porcentaje estimado de carga: %d%%' %batteryPercentage)
