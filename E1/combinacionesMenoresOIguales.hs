main :: IO()
main = do {
  x <- readLn ;
  print(combinacionesMenoresOiguales(x ::(Integer)))
  }

combinacionesMenoresOiguales :: Integer -> Integer
combinacionesMenoresOiguales n = auxi n n n

auxi :: Integer -> Integer -> Integer -> Integer
auxi _ 1 j = j
auxi n i j = auxj n i j + auxi n (i - 1) j

auxj :: Integer -> Integer -> Integer -> Integer
auxj _ _ 1 = 1
auxj n i j | i * j <= n = 1 + auxj n i (j - 1)
           | otherwise = auxj n i (j - 1)