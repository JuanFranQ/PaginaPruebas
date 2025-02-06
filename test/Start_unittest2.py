import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class TestParte1(unittest.TestCase):
    def setUp(self):
        service = Service(EdgeChromiumDriverManager().install())
        options = Options()
        self.driver = webdriver.Edge(service=service, options=options)
        self.driver.get("https://juanfranq.github.io/PaginaPruebas/")

    def test_busqueda_por_clase(self):
        # Buscar un elemento por clase
        elemento = self.driver.find_element(By.CLASS_NAME, "container")
        self.assertIsNotNone(elemento)
        print("Elemento encontrado por clase")

    def tearDown(self):
        self.driver.quit()

class TestParte2(unittest.TestCase):
    def setUp(self):
        service = Service(EdgeChromiumDriverManager().install())
        options = Options()
        self.driver = webdriver.Edge(service=service, options=options)
        self.driver.get("https://juanfranq.github.io/PaginaPruebas/")

    def test_buscar_multiples_elementos(self):
        # Encontrar elementos por nombre
        elementos = self.driver.find_elements(By.TAG_NAME, "a")
        print(f"Número de enlaces encontrados: {len(elementos)}")

        # Encontrar elementos por clase
        elementos_div = self.driver.find_elements(By.TAG_NAME, "div")
        print(f"Número de divs encontrados: {len(elementos_div)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()