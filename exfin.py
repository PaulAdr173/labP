#ex1
print(0.0000000000000000000001)

#ex2
print(2**3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

#ex 3
print((2 ** 4), (2 * 4.), (2 * 4))

#ex4
print((-2 / 4), (2 % 4), (2 // 4), (-2 // 4))

#ex5

print((2%-4), (2 % 4), (2**3**2))

#ex 6
a= 1
b =1
c = (a**2 + b ** 2)** 0.5
print(c)

#ex 7
#1 mila = 1.61km
km = 12.25
mile = 7.38
mile_to_km = (7.38 * 1.61)
km_to_mile = (12.25 /1.61)

print(mile, "mile=", round(mile_to_km, 2), "kilometri")
print(km, "kilometri=", round(km_to_mile, 2), "mile")

#ex8
x = 3
rez = ((3*x**3) - (2*x**2)+ (3*x) -1)
print(rez)

#ex9
var =2
var = 3
print(var)

#ex10
#varianta "m 101"

#ex11

a = '1'
b = "1"
print(a + b)

#ex12
a = 6
b = 3
a /= 2 * b #a = a / (2 * b)
print (a)

#ex13
x =  4
y = 1
a = x & y
b = x | y
c = ~x
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)