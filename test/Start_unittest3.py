import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class TestAcciones(unittest.TestCase):
    def setUp(self):
        service = Service(EdgeChromiumDriverManager().install())
        options = Options()
        self.driver = webdriver.Edge(service=service, options=options)
        self.driver.get("https://juanfranq.github.io/PaginaPruebas/")
        
    def test_interacciones_pagina(self):
        try:
            # Encontrar y hacer clic en algún enlace
            enlaces = self.driver.find_elements(By.TAG_NAME, "a")
            if enlaces:
                enlaces[0].click()
                print("Click realizado en el primer enlace")
            
            # Volver a la página anterior
            self.driver.back()
            print("Regreso a la página principal")
            
            # Encontrar todos los elementos input
            inputs = self.driver.find_elements(By.TAG_NAME, "input")
            if inputs:
                # Escribir en el primer input encontrado
                inputs[0].send_keys("Prueba de escritura automatizada")
                print("Texto ingresado en el campo de entrada")
            
            # Esperar un momento para ver los resultados
            self.driver.implicitly_wait(5)
            
        except Exception as e:
            print(f"Se produjo un error: {e}")
            
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()