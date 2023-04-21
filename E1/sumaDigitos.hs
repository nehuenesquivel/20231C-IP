main :: IO()
main = do {
  x <- readLn ;
  print(sumaDigitos(x ::(Int)))
  }

sumaDigitos :: Int -> Int
sumaDigitos n | n < 10 = n
              | otherwise = sumaDigitos(div n 10) + mod n 10