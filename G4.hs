--1
fibonacci :: Integer -> Integer
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci(n - 1) + fibonacci(n - 2)

{-
fibonacci n | n == 0 = 0
            | n == 1 = 0
            | otherwise = fibonacci(n - 1) + fibonacci(n - 2)
-}

--2
parteEntera :: Float -> Integer
parteEntera x = floor(x)

--3
esDivisible :: Integer -> Integer -> Bool
esDivisible a b = a == b || (b < a && True)

--4
sumaImpares :: Integer -> Integer
sumaImpares 1 = 1
sumaImpares n = sumaImpares(n - 1) + n * 2 - 1

{-noname :: Integer -> Integer
noname n | n * 2 - 1 + (n)

impar :: Integer -> Integer
impar 1 = 1
impar n = sumaImpares(n - 1) + 2
encontré banda de relacioes entre números, fibonacci es ^2 y tal n x2 contiene n impares-}