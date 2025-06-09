import math

def SAD_69(lon, lat, h):
    a = 6378160.0
    f = 0.0033528918692372
    b = (a * (1 - f))
    c = math.sqrt((a ** 2) - (b ** 2))
    e = c / a
    el = c / b
    N = (a) / math.sqrt(1 - ((e ** 2) * ((math.sin(lat)) ** 2)))
    K0 = 0.9996
    pll= 206264.8062 #segundos(em GMS) 
    A = 1+((3/4)*(e**2)) +((45/64)*(e**4))+((175/256)*(e**6))+((11025/16384)*(e**8))+((43659/65536)*(e**10))
    B = ((3/4)*(e**2))+((15/16)*(e**4))+((525/512)*(e**6))+((2205/2048)*(e**8))+((72765/65536)*(e**10))
    C = ((15/64)*(e**4))+((105/256)*(e**6))+((2205/4096)*(e**8))+((10395/16384)*(e**10))
    D = ((35/512)*(e**6))+((315/2048)*(e**8))+((31185/131072)*(e**10))
    E = ((315/16384)*(e**8))+((3465/65536)*(e**10))
    F = ((639/131072)*(e**10))
    S = (a(1-(e**2)))*(((A*lat)-((B/2)* math.sin(2*lat))+((C/4)* math.sin(4*lat))-((D/6)* math.sin(6*lat))+((E/8)* math.sin(8*lat))-((F/10)* math.sin(10*lat))))
    I = K0*S
    II = ((N*math.sin(lat)*math.cos(lat)*K0(10**8))/(2*(pll**2)))
    III = ((N*math.sin(lat)*((math.cos(lat))**3))/(24*(pll**4)))*(5-(math.tan(lat)**2)+(9*(el**2)*(math.cos(lat)**2))+(4*(el**4)*(math.cos(lat)**4)))*(K0*(10**16))
    IV = ((N*math.cos(lat)*K0(10**4))/(pll))
    V = ((N*((math.cos(lat))**3))/(6*(pll**3)))*(1-(math.tan(lat)**2)+((e**2)*(math.cos(lat)**2)))*(K0*(10**12))
    p = 0.0001*delta_arco #delta arco em segundos(GMS)
    delta_longitude = lon - lon_meridiano
    A6 = ((N*math.sin(lat)*(math.cos(lat)**5))/(720*(pll**5)))*(61-(58*(math.tan(lat)**2))+(math.tan(lat)**4)+(270*(el**2)*(math.cos(lat)**2))-(330*(el**2)*(math.sin(lat)**2)))*(K0*(10**24))
    B5 = ((N*(math.cos(lat)**5))/(120*(pll**5)))*(5-(18*(math.tan(lat)**2))+(math.tan(lat)**4)+(14*(el**2)*(math.cos(lat)**2))-(58*(el**2)*(math.sin(lat)**2)))*(K0*(10**20))
    return (a, A, B, C, D, E, F, S, I ,II ,III , IV, V, p, delta_longitude, A6, B5)

def WGS84(lon, lat, h):
    a = 6378137.0
    f = 0.0033528106647475
    b = (a * (1 - f))
    c = math.sqrt((a ** 2) - (b ** 2))
    e = c / a
    el = c / b
    N = (a) / math.sqrt(1 - ((e ** 2) * ((math.sin(lat)) ** 2)))
    K0 = 0.9996
    pll= 206264.8062 #segundos(em GMS) 
    A = 1+((3/4)*(e**2)) +((45/64)*(e**4))+((175/256)*(e**6))+((11025/16384)*(e**8))+((43659/65536)*(e**10))
    B = ((3/4)*(e**2))+((15/16)*(e**4))+((525/512)*(e**6))+((2205/2048)*(e**8))+((72765/65536)*(e**10))
    C = ((15/64)*(e**4))+((105/256)*(e**6))+((2205/4096)*(e**8))+((10395/16384)*(e**10))
    D = ((35/512)*(e**6))+((315/2048)*(e**8))+((31185/131072)*(e**10))
    E = ((315/16384)*(e**8))+((3465/65536)*(e**10))
    F = ((639/131072)*(e**10))
    S = (a(1-(e**2)))*(((A*lat)-((B/2)* math.sin(2*lat))+((C/4)* math.sin(4*lat))-((D/6)* math.sin(6*lat))+((E/8)* math.sin(8*lat))-((F/10)* math.sin(10*lat))))
    I = K0*S
    II = ((N*math.sin(lat)*math.cos(lat)*K0(10**8))/(2*(pll**2)))
    III = ((N*math.sin(lat)*((math.cos(lat))**3))/(24*(pll**4)))*(5-(math.tan(lat)**2)+(9*(el**2)*(math.cos(lat)**2))+(4*(el**4)*(math.cos(lat)**4)))*(K0*(10**16))
    IV = ((N*math.cos(lat)*K0(10**4))/(pll))
    V = ((N*((math.cos(lat))**3))/(6*(pll**3)))*(1-(math.tan(lat)**2)+((e**2)*(math.cos(lat)**2)))*(K0*(10**12))
    p = 0.0001*delta_arco #delta arco em segundos(GMS)
    delta_longitude = lon - lon_meridiano
    A6 = ((N*math.sin(lat)*(math.cos(lat)**5))/(720*(pll**5)))*(61-(58*(math.tan(lat)**2))+(math.tan(lat)**4)+(270*(el**2)*(math.cos(lat)**2))-(330*(el**2)*(math.sin(lat)**2)))*(K0*(10**24))
    B5 = ((N*(math.cos(lat)**5))/(120*(pll**5)))*(5-(18*(math.tan(lat)**2))+(math.tan(lat)**4)+(14*(el**2)*(math.cos(lat)**2))-(58*(el**2)*(math.sin(lat)**2)))*(K0*(10**20))
    return (a, A, B, C, D, E, F, S, I ,II ,III , IV, V, p, delta_longitude, A6, B5)

def SIRGAS(lon, lat, h):
    a = 6378137.0
    f = 0.0033528106811823
    b = (a * (1 - f))
    c = math.sqrt((a ** 2) - (b ** 2))
    e = c / a
    el = c / b
    N = (a) / math.sqrt(1 - ((e ** 2) * ((math.sin(lat)) ** 2)))
    K0 = 0.9996
    pll= 206264.8062 #segundos(em GMS) 
    A = 1+((3/4)*(e**2)) +((45/64)*(e**4))+((175/256)*(e**6))+((11025/16384)*(e**8))+((43659/65536)*(e**10))
    B = ((3/4)*(e**2))+((15/16)*(e**4))+((525/512)*(e**6))+((2205/2048)*(e**8))+((72765/65536)*(e**10))
    C = ((15/64)*(e**4))+((105/256)*(e**6))+((2205/4096)*(e**8))+((10395/16384)*(e**10))
    D = ((35/512)*(e**6))+((315/2048)*(e**8))+((31185/131072)*(e**10))
    E = ((315/16384)*(e**8))+((3465/65536)*(e**10))
    F = ((639/131072)*(e**10))
    S = (a(1-(e**2)))*(((A*lat)-((B/2)* math.sin(2*lat))+((C/4)* math.sin(4*lat))-((D/6)* math.sin(6*lat))+((E/8)* math.sin(8*lat))-((F/10)* math.sin(10*lat))))
    I = K0*S
    II = ((N*math.sin(lat)*math.cos(lat)*K0(10**8))/(2*(pll**2)))
    III = ((N*math.sin(lat)*((math.cos(lat))**3))/(24*(pll**4)))*(5-(math.tan(lat)**2)+(9*(el**2)*(math.cos(lat)**2))+(4*(el**4)*(math.cos(lat)**4)))*(K0*(10**16))
    IV = ((N*math.cos(lat)*K0(10**4))/(pll))
    V = ((N*((math.cos(lat))**3))/(6*(pll**3)))*(1-(math.tan(lat)**2)+((e**2)*(math.cos(lat)**2)))*(K0*(10**12))
    p = 0.0001*delta_arco #delta arco em segundos(GMS)
    delta_longitude = lon - lon_meridiano
    A6 = ((N*math.sin(lat)*(math.cos(lat)**5))/(720*(pll**5)))*(61-(58*(math.tan(lat)**2))+(math.tan(lat)**4)+(270*(el**2)*(math.cos(lat)**2))-(330*(el**2)*(math.sin(lat)**2)))*(K0*(10**24))
    B5 = ((N*(math.cos(lat)**5))/(120*(pll**5)))*(5-(18*(math.tan(lat)**2))+(math.tan(lat)**4)+(14*(el**2)*(math.cos(lat)**2))-(58*(el**2)*(math.sin(lat)**2)))*(K0*(10**20))
    return (a, A, B, C, D, E, F, S, I ,II ,III , IV, V, p, delta_longitude, A6, B5)

def CORREGO(lon, lat, h):
    a = 6378388.0
    f = 0.0033670033670034
    b = (a * (1 - f))
    c = math.sqrt((a ** 2) - (b ** 2))
    e = c / a
    el = c / b
    N = (a) / math.sqrt(1 - ((e ** 2) * ((math.sin(lat)) ** 2)))
    K0 = 0.9996
    pll= 206264.8062 #segundos(em GMS) 
    A = 1+((3/4)*(e**2)) +((45/64)*(e**4))+((175/256)*(e**6))+((11025/16384)*(e**8))+((43659/65536)*(e**10))
    B = ((3/4)*(e**2))+((15/16)*(e**4))+((525/512)*(e**6))+((2205/2048)*(e**8))+((72765/65536)*(e**10))
    C = ((15/64)*(e**4))+((105/256)*(e**6))+((2205/4096)*(e**8))+((10395/16384)*(e**10))
    D = ((35/512)*(e**6))+((315/2048)*(e**8))+((31185/131072)*(e**10))
    E = ((315/16384)*(e**8))+((3465/65536)*(e**10))
    F = ((639/131072)*(e**10))
    S = (a(1-(e**2)))*(((A*lat)-((B/2)* math.sin(2*lat))+((C/4)* math.sin(4*lat))-((D/6)* math.sin(6*lat))+((E/8)* math.sin(8*lat))-((F/10)* math.sin(10*lat))))
    I = K0*S
    II = ((N*math.sin(lat)*math.cos(lat)*K0(10**8))/(2*(pll**2)))
    III = ((N*math.sin(lat)*((math.cos(lat))**3))/(24*(pll**4)))*(5-(math.tan(lat)**2)+(9*(el**2)*(math.cos(lat)**2))+(4*(el**4)*(math.cos(lat)**4)))*(K0*(10**16))
    IV = ((N*math.cos(lat)*K0(10**4))/(pll))
    V = ((N*((math.cos(lat))**3))/(6*(pll**3)))*(1-(math.tan(lat)**2)+((e**2)*(math.cos(lat)**2)))*(K0*(10**12))
    p = 0.0001*delta_arco #delta arco em segundos(GMS)
    delta_longitude = lon - lon_meridiano
    A6 = ((N*math.sin(lat)*(math.cos(lat)**5))/(720*(pll**5)))*(61-(58*(math.tan(lat)**2))+(math.tan(lat)**4)+(270*(el**2)*(math.cos(lat)**2))-(330*(el**2)*(math.sin(lat)**2)))*(K0*(10**24))
    B5 = ((N*(math.cos(lat)**5))/(120*(pll**5)))*(5-(18*(math.tan(lat)**2))+(math.tan(lat)**4)+(14*(el**2)*(math.cos(lat)**2))-(58*(el**2)*(math.sin(lat)**2)))*(K0*(10**20))
    return (a, A, B, C, D, E, F, S, I ,II ,III , IV, V, p, delta_longitude, A6, B5)


#Geodesica para UTM
K0 = 0.9996
pll= 206264.8062 #segundos(em GMS) 
A = 1+((3/4)*(e**2)) +((45/64)*(e**4))+((175/256)*(e**6))+((11025/16384)*(e**8))+((43659/65536)*(e**10))
B = ((3/4)*(e**2))+((15/16)*(e**4))+((525/512)*(e**6))+((2205/2048)*(e**8))+((72765/65536)*(e**10))
C = ((15/64)*(e**4))+((105/256)*(e**6))+((2205/4096)*(e**8))+((10395/16384)*(e**10))
D = ((35/512)*(e**6))+((315/2048)*(e**8))+((31185/131072)*(e**10))
E = ((315/16384)*(e**8))+((3465/65536)*(e**10))
F = ((639/131072)*(e**10))
S = (a(1-(e**2)))*(((A*lat)-((B/2)* math.sin(2*lat))+((C/4)* math.sin(4*lat))-((D/6)* math.sin(6*lat))+((E/8)* math.sin(8*lat))-((F/10)* math.sin(10*lat))))
I = K0*S
II = ((N*math.sin(lat)*math.cos(lat)*K0(10**8))/(2*(pll**2)))
III = ((N*math.sin(lat)*((math.cos(lat))**3))/(24*(pll**4)))*(5-(math.tan(lat)**2)+(9*(el**2)*(math.cos(lat)**2))+(4*(el**4)*(math.cos(lat)**4)))*(K0*(10**16))
IV = ((N*math.cos(lat)*K0(10**4))/(pll))
V = ((N*((math.cos(lat))**3))/(6*(pll**3)))*(1-(math.tan(lat)**2)+((e**2)*(math.cos(lat)**2)))*(K0*(10**12))
p = 0.0001*delta_arco #delta arco em segundos(GMS)
delta_longitude = lon - lon_meridiano
A6 = ((N*math.sin(lat)*(math.cos(lat)**5))/(720*(pll**5)))*(61-(58*(math.tan(lat)**2))+(math.tan(lat)**4)+(270*(el**2)*(math.cos(lat)**2))-(330*(el**2)*(math.sin(lat)**2)))*(K0*(10**24))
B5 = ((N*(math.cos(lat)**5))/(120*(pll**5)))*(5-(18*(math.tan(lat)**2))+(math.tan(lat)**4)+(14*(el**2)*(math.cos(lat)**2))-(58*(el**2)*(math.sin(lat)**2)))*(K0*(10**20))

#UTM para Geodesica
Nl = I+(II*(p**2))+(III*(p**4))+(A6*(p**6))
p_graus = 57.295779513 #em graus decimais °
alpha = A*a*(1-(e**2))
lat_0 = (Nl*p_graus)/(alpha*K0)
lat_


