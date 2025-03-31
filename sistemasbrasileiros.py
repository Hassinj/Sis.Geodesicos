import math


# para usuario colocar grau, minuto, segundo e fazer direto a conversao


def gmsdecimal(g, m, s):
    if g > 0:
        decimal = math.radians(g + (m / 60) + (s / 3600))

    if g < 0:
        decimal = math.radians(g - (m / 60) - (s / 3600))

    return decimal


g1 = int(input("insira o grau da latitude: "))
m1 = int(input("insira os minutos da latitude: "))
s1 = float(input("insira os segundos da latitude: "))

lat = gmsdecimal(g1, m1, s1)

g2 = int(input("insira o grau da longitude: "))
m2 = int(input("insira os minutos da longitude: "))
s2 = float(input("insira os segundos da longitude: "))

lon = gmsdecimal(g2, m2, s2)
h = float(input("insira a altura em metros: "))

X = Y = Z = X1 = Y1 = Z1 = X2 = Y2 = Z2 = 0.000000
lat1 = lon1 = h1 = 0.000000

sis = int(
    input("Qual o atual sistema da coordenada? OBS: SAD=1 WGS=2 SIRGAS=3 Corrego Alegre=4 \ninsira a sua escolha: "))

sis2 = int(input("Para Qual sistema? OBS: SAD=1 WGS=2 SIRGAS=3 Corrego Alegre=4 \ninsira a sua escolha: "))


# para cada sistema/elipsoide tem: Semi-eixo maior(a), Achatamento(f)


def SAD_69(lon, lat, h):
    a = 6378160.0
    f = 0.0033528918692372
    b = (a * (1 - f))
    c = math.sqrt((a ** 2) - (b ** 2))
    e = c / a
    el = c / b
    N = (a) / math.sqrt(1 - ((e ** 2) * ((math.sin(lat)) ** 2)))
    p = (h + N) * math.cos(lat)
    X = (p) * math.cos(lon)
    Y = (p) * math.sin(lon)
    Z = ((N * (1 - (e * e))) + h) * (math.sin(lat))
    print(" X: ", X, "\n Y: ", Y, "\n Z: ", Z)
    return (X, Y, Z)

def WGS84(lon, lat, h):
    a = 6378137.0
    f = 0.0033528106647475
    b = (a * (1 - f))
    c = math.sqrt((a ** 2) - (b ** 2))
    e = c / a
    el = c / b
    N = (a) / math.sqrt(1 - ((e ** 2) * ((math.sin(lat)) ** 2)))
    p = (h + N) * math.cos(lat)
    X = (p) * math.cos(lon)
    Y = (p) * math.sin(lon)
    Z = ((N * (1 - (e * e))) + h) * (math.sin(lat))
    print(" X: ", X, "\n Y: ", Y, "\n Z: ", Z)
    return (X, Y, Z)


def SIRGAS(lon, lat, h):
    a = 6378137.0
    f = 0.0033528106811823
    b = (a * (1 - f))
    c = math.sqrt((a ** 2) - (b ** 2))
    e = c / a
    el = c / b
    N = (a) / math.sqrt(1 - ((e ** 2) * ((math.sin(lat)) ** 2)))
    p = (h + N) * math.cos(lat)
    X = (p) * math.cos(lon)
    Y = (p) * math.sin(lon)
    Z = ((N * (1 - (e * e))) + h) * (math.sin(lat))
    print(" X: ", X, "\n Y: ", Y, "\n Z: ", Z)
    return(X, Y, Z)



def CORREGO(lon, lat, h):
    a = 6378388.0
    f = 0.0033670033670034
    b = (a * (1 - f))
    c = math.sqrt((a ** 2) - (b ** 2))
    e = c / a
    el = c / b
    N = (a) / math.sqrt(1 - ((e ** 2) * ((math.sin(lat)) ** 2)))
    p = (h + N) * math.cos(lat)
    X = (p) * math.cos(lon)
    Y = (p) * math.sin(lon)
    Z = ((N * (1 - (e * e))) + h) * (math.sin(lat))
    print(" X: ", X, "\n Y: ", Y, "\n Z: ", Z)
    return (X, Y, Z)


def paraSAD_69(X, Y, Z):
    a = 6378160.0
    f = 1 / 298.25
    b = (a * (1 - f))
    c = math.sqrt((a * a) - (b * b))
    e = c / a
    el = c / b
    p = math.sqrt((X ** 2) + (Y ** 2))
    theta = math.atan((Z / p) * (a / b))
    senotheta = math.sin(theta)
    cossenotheta = math.cos(theta)
    lat1 = math.degrees(math.atan((Z + ((el ** 2) * b * (senotheta ** 3))) / (p - ( (e ** 2) * a * (cossenotheta ** 3)))))
    lon1 = math.degrees(math.atan(Y / X))
    N = ((a) / math.sqrt(1 - ((e ** 2) * ((math.sin(math.radians(lat1)) ** 2)))))
    h1 = (p / (math.cos(math.radians(lat1)))) - N
    glat1 = int(lat1) # lat =40.123456, glat=40
    minlat1 = int((lat1 - (glat1)) * 60)  # (40.123456-40) * 60 = 0.123456 * 60 = 7.40736, minlat = 7
    seglat1 = ((((lat1 - glat1) * 60) - minlat1) * 60) # (((40.123456 - 40) * 60 ) - 7) * 60))  = 
    glon1 = int(lon1)
    minlon1 = int((lon1 - (glon1)) * 60)
    seglon1 = ((((lon1 - glon1) * 60) - minlon1) * 60)
    
    print("Latitude: ", glat1,"° ", abs(minlat1), "' ", abs(seglat1),"'' ",  " \nLongitude: ", glon1,"° ", abs(minlon1), "' ", abs(seglon1),"'' ", "\nAltura: ", h1)
    return (lat1, lon1, h1)
    
def paraWGS84(X, Y, Z):
    a = 6378137.0
    f = 0.00335281066
    b = (a * (1 - f))
    c = math.sqrt((a * a) - (b * b))
    e = c / a
    el = c / b
    p = math.sqrt((X ** 2) + (Y ** 2))
    theta = math.atan((Z / p) * (a / b))
    senotheta = math.sin(theta)
    cossenotheta = math.cos(theta)
    lat1 = math.degrees(math.atan((Z + ((el ** 2) * b * (senotheta ** 3))) / (p - ( (e ** 2) * a * (cossenotheta ** 3)))))
    lon1 = math.degrees(math.atan(Y / X))
    N = ((a) / math.sqrt(1 - ((e ** 2) * ((math.sin(math.radians(lat1)) ** 2)))))
    h1 = (p / (math.cos(math.radians(lat1)))) - N
    glat1 = int(lat1) # lat =40.123456, glat=40
    minlat1 = int((lat1 - (glat1)) * 60)  # (40.123456-40) * 60 = 0.123456 * 60 = 7.40736, minlat = 7
    seglat1 = ((((lat1 - glat1) * 60) - minlat1) * 60) # (((40.123456 - 40) * 60 ) - 7) * 60))  = 
    glon1 = int(lon1)
    minlon1 = int((lon1 - (glon1)) * 60)
    seglon1 = ((((lon1 - glon1) * 60) - minlon1) * 60)
    
    print("Latitude: ", glat1,"° ", abs(minlat1), "' ", abs(seglat1),"'' ",  " \nLongitude: ", glon1,"° ", abs(minlon1), "' ", abs(seglon1),"'' ", "\nAltura: ", h1)
    return (lat1, lon1, h1)


def paraSIRGAS(X, Y, Z):
    a = 6378137.0
    f = 0.00335281068
    b = (a * (1 - f))
    c = math.sqrt((a * a) - (b * b))
    e = c / a
    el = c / b
    p = math.sqrt((X ** 2) + (Y ** 2))
    theta = math.atan((Z / p) * (a / b))
    senotheta = math.sin(theta)
    cossenotheta = math.cos(theta)
    lat1 = math.degrees(math.atan((Z + ((el ** 2) * b * (senotheta ** 3))) / (p - ( (e ** 2) * a * (cossenotheta ** 3)))))
    lon1 = math.degrees(math.atan(Y / X))
    N = ((a) / math.sqrt(1 - ((e ** 2) * ((math.sin(math.radians(lat1)) ** 2)))))
    h1 = (p / (math.cos(math.radians(lat1)))) - N
    glat1 = int(lat1) # lat =40.123456, glat=40
    minlat1 = int((lat1 - (glat1)) * 60)  # (40.123456-40) * 60 = 0.123456 * 60 = 7.40736, minlat = 7
    seglat1 = ((((lat1 - glat1) * 60) - minlat1) * 60) # (((40.123456 - 40) * 60 ) - 7) * 60))  = 
    glon1 = int(lon1)
    minlon1 = int((lon1 - (glon1)) * 60)
    seglon1 = ((((lon1 - glon1) * 60) - minlon1) * 60)
    
    print("Latitude: ", glat1,"° ", abs(minlat1), "' ", abs(seglat1),"'' ",  " \nLongitude: ", glon1,"° ", abs(minlon1), "' ", abs(seglon1),"'' ", "\nAltura: ", h1)
    return (lat1, lon1, h1)

def paraCORREGO(X, Y, Z):
    a = 6378388.0
    f = 0.00336700337
    b = (a * (1 - f))
    c = math.sqrt((a * a) - (b * b))
    e = c / a
    el = c / b
    p = math.sqrt((X ** 2) + (Y ** 2))
    theta = math.atan((Z / p) * (a / b))
    senotheta = math.sin(theta)
    cossenotheta = math.cos(theta)
    lat1 = math.degrees(math.atan((Z + ((el ** 2) * b * (senotheta ** 3))) / (p - ( (e ** 2) * a * (cossenotheta ** 3)))))
    lon1 = math.degrees(math.atan(Y / X))
    N = ((a) / math.sqrt(1 - ((e ** 2) * ((math.sin(math.radians(lat1)) ** 2)))))
    h1 = (p / (math.cos(math.radians(lat1)))) - N
    glat1 = int(lat1) # lat =40.123456, glat=40
    minlat1 = int((lat1 - (glat1)) * 60)  # (40.123456-40) * 60 = 0.123456 * 60 = 7.40736, minlat = 7
    seglat1 = ((((lat1 - glat1) * 60) - minlat1) * 60) # (((40.123456 - 40) * 60 ) - 7) * 60))  = 
    glon1 = int(lon1)
    minlon1 = int((lon1 - (glon1)) * 60)
    seglon1 = ((((lon1 - glon1) * 60) - minlon1) * 60)
    
    print("Latitude: ", glat1,"° ", abs(minlat1), "' ", abs(seglat1),"'' ",  " \nLongitude: ", glon1,"° ", abs(minlon1), "' ", abs(seglon1),"'' ", "\nAltura: ", h1)
    return (lat1, lon1, h1)

if sis == 1 and sis2 == 1:
    SAD_69(lon, lat, h)

if sis == 1 and sis2 == 2:
    result = SAD_69(lon, lat, h)
    X1 = result[0] - 66.87
    Y1 = result[1] + 4.37
    Z1 = result[2] - 38.52
    paraWGS84(X1, Y1, Z1)

if sis == 1 and sis2 == 3:
    result = SAD_69(lon, lat, h)
    X1 = result[0] - 67.35
    Y1 = result[1] + 3.88
    Z1 = result[2] - 38.22
    paraSIRGAS(X1, Y1, Z1)

if sis == 1 and sis2 == 4:
    result = SAD_69(lon, lat, h)
    X1 = result[0] + 138.70
    Y1 = result[1] - 164.40
    Z1 = result[2] - 34.40
    paraCORREGO(X1, Y1, Z1)

if sis == 2 and sis2 == 1:
    result = WGS84(lon, lat, h)
    X1 = result[0] + 66.87
    Y1 = result[1] - 4.37
    Z1 = result[2] + 38.52
    paraSAD_69(X1, Y1, Z1)

if sis == 2 and sis2 == 2:
    WGS84(lon, lat, h)

if sis == 2 and sis2 == 3:
    result = WGS84(lon, lat, h)
    X1 = result[0] + 66.87
    Y1 = result[1] - 4.37
    Z1 = result[2] + 38.52
    result2 = paraSAD_69(X1, Y1, Z1)
    result1 = SAD_69(result2[0], result2[1], result2[2])
    X2 = result1[0] - 67.35
    Y2 = result1[1] + 3.88
    Z2 = result1[2] - 38.22
    paraSIRGAS(X2, Y2, Z2)

if sis == 2 and sis2 == 4:
    result = WGS84(lon, lat, h)
    X1 = result[0] + 66.87
    Y1 = result[1] - 4.37
    Z1 = result[2] + 38.52
    result2 = paraSAD_69(X1, Y1, Z1)
    result1 = SAD_69(result2[0], result2[1], result2[2])
    X2 = result1[0] + 138.70
    Y2 = result1[1] - 164.40
    Z2 = result1[2] - 34.40
    paraCORREGO(X2, Y2, Z2)

if sis == 3 and sis2 == 1:
    result = SIRGAS(lon, lat, h)
    X1 = result[0] + 67.35
    Y1 = result[1] - 3.88
    Z1 = result[2] + 38.22
    paraSAD_69(X1, Y1, Z1)
	
if sis == 3 and sis2 == 2:
    SIRGAS(lon, lat, h)
    X1 = result[0] + 67.35
    Y1 = result[1] - 3.88
    Z1 = result[2] + 38.22
    result2 = paraSAD_69(X1, Y1, Z1)
    result1 = SAD_69(result2[0], result2[1], result2[2])
    X2 = result1[0] - 66.87
    Y2 = result1[1] + 4.37
    Z2 = result1[2] - 38.52
    paraWGS84(X2, Y2, Z2)

if sis == 3 and sis2 == 3:
    SIRGAS(lon, lat, h)

if sis == 3 and sis2 == 4:
    SIRGAS(lon, lat, h)
    X1 = result[0] + 67.35
    Y1 = result[1] - 3.88
    Z1 = result[2] + 38.22
    result2 = paraSAD_69(X1, Y1, Z1)
    result1 = SAD_69(result2[0], result2[1], result2[2])
    X2 = result1[0] + 138.70
    Y2 = result1[1] - 164.40
    Z2 = result1[2] - 34.40
    paraCORREGO(X2, Y2, Z2)

if sis == 4 and sis2 == 1:
    CORREGO(lon, lat, h)
    X1 = result[0] - 138.70
    Y1 = result[1] + 164.40
    Z1 = result[2] + 34.40
    paraSAD_69(X1, Y1, Z1)

if sis == 4 and sis2 == 2:
    CORREGO(lon, lat, h)
    X1 = result[0] - 138.70
    Y1 = result[1] + 164.40
    Z1 = result[2] + 34.40
    result2 = paraSAD_69(X1, Y1, Z1)
    result1 = SAD_69(result2[0], result2[1], result2[2])
    X2 = result1[0] - 66.87
    Y2 = result1[1] + 4.37
    Z2 = result1[2] - 38.52
    paraWGS84(X2, Y2, Z2)

if sis == 4 and sis2 == 3:
    CORREGO(lon, lat, h)
    X1 = result[0] - 138.70
    Y1 = result[1] + 164.40
    Z1 = result[2] + 34.40
    result2 = paraSAD_69(X1, Y1, Z1)
    result1 = SAD_69(result2[0], result2[1], result2[2])
    X2 = result1[0] - 67.35
    Y2 = result1[1] + 3.88
    Z2 = result1[2] - 38.22
    paraSIRGAS(X2, Y2, Z2)

if sis == 4 and sis2 == 4:
    CORREGO(lon, lat, h)
