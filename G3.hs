--1
--a
f1 :: Integer -> Integer
f1 n | n == 1 = 8
     | n == 4 = 131
     | n == 16 = 16
--b
g1 :: Integer -> Integer
g1 n | n == 8 = 16
     | n == 16 = 4
     | n == 1 = 131
--c
h :: Integer -> Integer
h n = f1(g1 n)

k :: Integer -> Integer
k n = g1(f1 n)

--3
estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados a b = mod (-a) b == 0

--5
todosMenores :: (Integer, Integer, Integer) -> Bool
todosMenores (n1, n2, n3) = f2 n1 > g2 n1 && f2 n2 > g2 n2 && f2 n3 > g2 n3

f2 :: Integer -> Integer
f2 n | n <= 7 = n ^ 2
     | n > 7 = 2 * n - 1

g2 :: Integer -> Integer
g2 n | esPar n = div n 2
     | otherwise = 3 * n + 1

esPar :: Integer -> Bool
esPar n = mod n 2 == 0

--6
bisiesto :: Integer -> Bool
bisiesto a = not (not (esMultiplo a 4) || (esMultiplo a 100 && not (esMultiplo a 400)))

esMultiplo :: Integer -> Integer -> Bool
esMultiplo x y = mod x y == 0

--7
distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (p1, p2, p3) (q1, q2, q3) = abs(p1 - q1) + abs(p2 - q2) + abs(p3 - q3)

--8
comparar :: Integer -> Integer -> Integer
comparar a b | sumaUltimosDosDigitos a < sumaUltimosDosDigitos b = 1
             | sumaUltimosDosDigitos a > sumaUltimosDosDigitos b = -1
             | otherwise = 0

sumaUltimosDosDigitos :: Integer -> Integer
sumaUltimosDosDigitos x = mod x 10 + mod (div x 10) 10