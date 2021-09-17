_G='val'
_F='hue'
_E=b'\x00'
_D=None
_C='blue'
_B='green'
_A='red'
from PiicoDev_Unified import *
from math import sqrt
_veml6040Address=16
_CONF=_E
_REG_RED=b'\x08'
_REG_GREEN=b'\t'
_REG_BLUE=b'\n'
_REG_WHITE=b'\x0b'
_DEFAULT_SETTINGS=_E
_SHUTDOWN=b'\x01'
_INTEGRATION_TIME=40
_G_SENSITIVITY=0.25168
_NaN=float('NaN')
def rgb2hsv(r,g,b):
	r=float(r/65535);g=float(g/65535);b=float(b/65535);high=max(r,g,b);low=min(r,g,b);h,s,v=high,high,high;d=high-low;s=0 if high==0 else d/high
	if high==low:h=0.0
	else:h={r:(g-b)/d+(6 if g<b else 0),g:(b-r)/d+2,b:(r-g)/d+4}[high];h/=6
	return{_F:h*360,'sat':s,_G:v}
class PiicoDev_VEML6040:
	def __init__(self,bus=_D,freq=_D,sda=_D,scl=_D,addr=_veml6040Address):
		try:
			if compat_ind>=1:0
			else:print(compat_str)
		except:print(compat_str)
		self.i2c=create_unified_i2c(bus=bus,freq=freq,sda=sda,scl=scl);self.addr=addr
		try:self.i2c.write8(self.addr,_CONF,_SHUTDOWN);self.i2c.write8(self.addr,_CONF,_DEFAULT_SETTINGS)
		except Exception:print('Device 0x{:02X} not found'.format(self.addr))
	def classifyHue(self,hues={_A:0,'yellow':60,_B:120,'cyan':180,_C:240,'magenta':300},min_brightness=0):
		d=self.readHSV()
		if d[_G]>min_brightness:key,val=min(hues.items(),key=lambda x:abs(d[_F]-x[1]));return key
		else:return'None'
	def readRGB(self):
		D='cct';C='als';B='white';A='little'
		try:raw_data=self.i2c.read16(self.addr,_REG_RED);u16red=int.from_bytes(raw_data,A);raw_data=self.i2c.read16(self.addr,_REG_GREEN);u16grn=int.from_bytes(raw_data,A);raw_data=self.i2c.read16(self.addr,_REG_BLUE);u16blu=int.from_bytes(raw_data,A);raw_data=self.i2c.read16(self.addr,_REG_WHITE);data_white_int=int.from_bytes(raw_data,A)
		except:print(i2c_err_str.format(self.addr));return{_A:_NaN,_B:_NaN,_C:_NaN,B:_NaN,C:_NaN,D:_NaN}
		colour_X=-0.023249*u16red+0.291014*u16grn+-0.36488*u16blu;colour_Y=-0.042799*u16red+0.272148*u16grn+-0.279591*u16blu;colour_Z=-0.155901*u16red+0.251534*u16grn+-0.07624*u16blu;colour_total=colour_X+colour_Y+colour_Z
		if colour_total==0:return{_A:_NaN,_B:_NaN,_C:_NaN,B:_NaN,C:_NaN,D:_NaN}
		else:colour_x=colour_X/colour_total;colour_y=colour_Y/colour_total
		colour_n=(colour_x-0.332)/(0.1858-colour_y);colour_CCT=449.0*colour_n**3+3525.0*colour_n**2+6823.3*colour_n+5520.33;colour_ALS=u16grn*_G_SENSITIVITY;return{_A:u16red,_B:u16grn,_C:u16blu,B:data_white_int,C:colour_ALS,D:colour_CCT}
	def readHSV(self):d=self.readRGB();return rgb2hsv(d[_A],d[_B],d[_C])