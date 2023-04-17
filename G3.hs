{-
--1
--a
f :: Integer -> Integer
f n | n == 1 = 8
    | n == 4 = 131
    | n == 16 = 16
--b
g :: Integer -> Integer
g n | n == 8 = 16
    | n == 16 = 4
    | n == 1 = 131
--c
h :: Integer -> Integer
h n = f(g n)

k :: Integer -> Integer
k n = g(f n)

--3
estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados a b = mod (-a) b == 0

--5
todosMenores :: (Integer, Integer, Integer) -> Bool
todosMenores (n1, n2, n3) = f n1 > g n1 && f n2 > g n2 && f n3 > g n3

f :: Integer -> Integer
f n | n <= 7 = n ^ 2
    | n > 7 = 2 * n - 1

g :: Integer -> Integer
g n | esPar n = div n 2
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
-}
