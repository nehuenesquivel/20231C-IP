main :: IO()
main = do {
  x <- readLn ;
  print(prod(x ::(Integer)))
  }

prod :: Integer -> Integer
prod n = aux (2 * n)

aux :: Integer -> Integer
aux 1 = 3
aux n = aux (n - 1) * (n ^ 2 + 2 * n)