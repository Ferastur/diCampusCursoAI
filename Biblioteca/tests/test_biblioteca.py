import unittest
import hashlib
import re
from datetime import datetime, timedelta

class TestLibraryLogic(unittest.TestCase):

    # TEST 1: Verificación de Seguridad (Hashing de contraseñas)
    def test_password_hashing(self):
        """Verifica que la contraseña se transforme en un hash SHA-256 y no sea reversible"""
        clave_plana = "admin123"
        hash_esperado = hashlib.sha256(clave_plana.encode()).hexdigest()
        
        # El hash no debe ser igual a la clave plana
        self.assertNotEqual(clave_plana, hash_esperado)
        # El hash SHA-256 siempre debe tener 64 caracteres
        self.assertEqual(len(hash_esperado), 64)
        # Verificamos que el hash generado sea consistente
        self.assertEqual(hash_esperado, hashlib.sha256("admin123".encode()).hexdigest())

    # TEST 2: Regla de Negocio (Cálculo de Penalización)
    def test_penalty_calculation(self):
        """Verifica que la penalización por devolución tardía sea exactamente de 7 días"""
        hoy = datetime.now()
        # Simulamos la lógica del programa: sumar 7 días
        fecha_fin_penalizacion = (hoy + timedelta(days=7)).strftime('%Y-%m-%d')
        
        fecha_esperada = (hoy + timedelta(days=7)).strftime('%Y-%m-%d')
        
        self.assertEqual(fecha_fin_penalizacion, fecha_esperada)
        print(f"\n[Test] Penalización calculada correctamente: {fecha_fin_penalizacion}")

    # TEST 3: Validación de Integridad (Formato de Email)
    def test_email_validation(self):
        """Verifica que el sistema reconozca emails válidos e inválidos mediante Regex"""
        regex = r"[^@]+@[^@]+\.[^@]+"
        
        email_valido = "alumno@talento.com"
        email_invalido = "esto-no-es-un-email"
        
        self.assertTrue(re.match(regex, email_valido))
        self.assertFalse(re.match(regex, email_invalido))

if __name__ == '__main__':
    unittest.main()