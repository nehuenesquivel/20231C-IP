main :: IO()
main = do {
  x <- readLn ;
  print(sumaPrimerosNImpares(x ::(Integer)))
  }

sumaPrimerosNImpares :: Integer -> Integer
sumaPrimerosNImpares n = aux (2 * n - 1)

aux :: Integer -> Integer
aux 1 = 4
aux n | mod n 2 == 0 = aux (n - 1) + 0
      | otherwise = aux (n - 1) + 2 * n + 2