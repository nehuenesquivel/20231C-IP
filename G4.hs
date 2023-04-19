--1
fibonacci :: Integer -> Integer
fibonacci n | n < 2 = n
            | otherwise = fibonacci(n - 1) + fibonacci(n - 2)

{-
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci(n - 1) + fibonacci(n - 2)
-}

--2
parteEntera :: Float -> Integer
parteEntera x | x <= -1 = parteEntera(x + 1) - 1
              | x < 0 = -1
              | x >= 1 = parteEntera(x - 1) + 1
              | otherwise = 0

{-
esPositivo :: Float -> Integer
esPositivo x | x > 0 = esPositivo(x - 1) + 1
             | otherwise = (-1)

esNegativo :: Float -> Integer
esNegativo x | x < 0 = esNegativo(x + 1) - 1
             | otherwise = 1
-}

--3
esDivisible :: Integer -> Integer -> Bool
esDivisible a b | a > b = esDivisible (a - b) b
                | otherwise = a == b

--4
sumaImpares :: Integer -> Integer
sumaImpares 1 = 1
sumaImpares n = sumaImpares(n - 1) + n * 2 - 1

--5
-- medioFact :: Integer -> Integer
-- medioFact 1 = 1
-- medioFact n = (n - 2) * 

--6
-- sumaDigitos :: Integer -> Integer
-- sumaDigitos n = mod n 10

{-noname :: Integer -> Integer
noname n | n * 2 - 1 + (n)

impar :: Integer -> Integer
impar 1 = 1
impar n = sumaImpares(n - 1) + 2
encontré banda de relacioes entre números, fibonacci es ^2 y tal n x2 contiene n impares-}