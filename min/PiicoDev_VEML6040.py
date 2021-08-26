_B=b'\x00'
_A=None
from PiicoDev_Unified import *
from utime import sleep_ms
_veml6040Address=16
_CONF=_B
_REG_RED=b'\x08'
_REG_GREEN=b'\t'
_REG_BLUE=b'\n'
_REG_WHITE=b'\x0b'
_DEFAULT_SETTINGS=_B
_SHUTDOWN=b'\x01'
_INTEGRATION_TIME=40
_G_SENSITIVITY=0.25168
class PiicoDev_VEML6040:
	def __init__(self,bus=_A,freq=_A,sda=_A,scl=_A,addr=_veml6040Address):
		try:
			if compat_ind>=1:0
			else:print(compat_str)
		except:print(compat_str)
		self.i2c=create_unified_i2c(bus=bus,freq=freq,sda=sda,scl=scl);self.addr=addr
		try:self.i2c.write8(self.addr,_CONF,_SHUTDOWN);self.i2c.write8(self.addr,_CONF,_DEFAULT_SETTINGS)
		except Exception:print('Device 0x{:02X} not found'.format(self.addr))
	def read(self):
		B='little';A='NaN'
		try:raw_data=self.i2c.read16(self.addr,_REG_RED);data_red_int=int.from_bytes(raw_data,B);raw_data=self.i2c.read16(self.addr,_REG_GREEN);data_green_int=int.from_bytes(raw_data,B);raw_data=self.i2c.read16(self.addr,_REG_BLUE);data_blue_int=int.from_bytes(raw_data,B);raw_data=self.i2c.read16(self.addr,_REG_WHITE);data_white_int=int.from_bytes(raw_data,B)
		except:print(i2c_err_str.format(self.addr));return float(A),float(A),float(A),float(A),float(A),float(A)
		colour_X=-0.023249*data_red_int+0.291014*data_green_int+-0.36488*data_blue_int;colour_Y=-0.042799*data_red_int+0.272148*data_green_int+-0.279591*data_blue_int;colour_Z=-0.155901*data_red_int+0.251534*data_green_int+-0.07624*data_blue_int;colour_total=colour_X+colour_Y+colour_Z
		if colour_total==0:return float(A),float(A),float(A),float(A),float(A),float(A)
		else:colour_x=colour_X/colour_total;colour_y=colour_Y/colour_total
		colour_n=(colour_x-0.332)/(0.1858-colour_y);colour_CCT=449.0*colour_n**3+3525.0*colour_n**2+6823.3*colour_n+5520.33;colour_ALS=data_green_int*_G_SENSITIVITY;return data_red_int,data_green_int,data_blue_int,data_white_int,colour_ALS,colour_CCT