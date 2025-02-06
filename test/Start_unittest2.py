import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestParte1(unittest.TestCase):
    def test_buscar_por_id(self):
        self.driver = webdriver.Edge()
        self.driver.get("http://www.clouditeducation.com/pruebas")
        
        elemento = self.driver.find_element(By.ID, "noImportante")
        self.assertIsNotNone(elemento)
        print("Prueba 1: Elemento por ID encontrado")
        self.driver.quit()

class TestParte2(unittest.TestCase):
    def test_buscar_por_nombre(self):
        self.driver = webdriver.Edge()
        self.driver.get("http://www.clouditeducation.com/pruebas")
        
        elemento = self.driver.find_element(By.NAME, "ultimo")
        self.assertIsNotNone(elemento)
        print("Prueba 2: Elemento por nombre encontrado")
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()