# Igualdad
self.assertEqual(a, b)          # a == b
self.assertNotEqual(a, b)       # a != b

# Comparaciones
self.assertTrue(x)              # bool(x) is True
self.assertFalse(x)             # bool(x) is False
self.assertIs(a, b)             # a is b
self.assertIsNone(x)            # x is None

# Numéricos
self.assertAlmostEqual(a, b)    # round(a-b, 7) == 0
self.assertGreater(a, b)        # a > b
self.assertLess(a, b)           # a < b

# Colecciones
self.assertIn(a, b)             # a in b
self.assertNotIn(a, b)          # a not in b

# Excepciones
with self.assertRaises(ValueError):
    funcion_que_genera_error()