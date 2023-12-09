import os
import unittest

def encontrarArquivoCsv(nome_arquivo, pasta):
    caminho_pasta = os.path.join(os.path.dirname(os.path.abspath(__file__)), pasta)

    arquivos = os.listdir(caminho_pasta)

    for arquivo in arquivos:
        if nome_arquivo in arquivo:
            return os.path.join(caminho_pasta, arquivo)

class TestEncontrarArquivoCsv(unittest.TestCase):
    def test_encontrar_arquivo_csv_raises_value_error_for_null_input(self):
        with self.assertRaises(ValueError) as context:
            encontrarArquivoCsv(None, "pasta_qualquer")

        self.assertIn("O nome do arquivo e a pasta não podem ser nulos.", str(context.exception))

def encontrarArquivoCsv(nome_arquivo, pasta):

    if nome_arquivo is None or pasta is None:
        raise ValueError("O nome do arquivo e a pasta não podem ser nulos.")

    caminho_pasta = os.path.join(os.path.dirname(os.path.abspath(__file__)), pasta)

    arquivos = os.listdir(caminho_pasta)

    for arquivo in arquivos:
        if nome_arquivo in arquivo:
            return os.path.join(caminho_pasta, arquivo)
        
class TestEncontrarArquivoCsv(unittest.TestCase):
    def setUp(self):
        self.pasta_teste = 'pasta_teste_temporaria'
        os.makedirs(self.pasta_teste)

    def tearDown(self):
        os.rmdir(self.pasta_teste)
    
    def test_encontrar_arquivo_csv_raises_value_error_para_entrada_nao_string(self):
        with self.assertRaises(ValueError) as context:
            encontrarArquivoCsv(123, self.pasta_teste)

        self.assertIn("O nome do arquivo e a pasta devem ser strings.", str(context.exception))

def encontrarArquivoCsv(nome_arquivo, pasta):

    if nome_arquivo is None or pasta is None:
        raise ValueError("O nome do arquivo e a pasta não podem ser nulos.")

    if not isinstance(nome_arquivo, str) or not isinstance(pasta, str):
        raise ValueError("O nome do arquivo e a pasta devem ser strings.")

    caminho_pasta = os.path.join(os.path.dirname(os.path.abspath(__file__)), pasta)

    arquivos = os.listdir(caminho_pasta)

    for arquivo in arquivos:
        if nome_arquivo in arquivo:
            return os.path.join(caminho_pasta, arquivo)

class TestEncontrarArquivoCsv(unittest.TestCase):
    def setUp(self):
        self.pasta_teste = 'pasta_teste_temporaria'
        os.makedirs(self.pasta_teste)

    def tearDown(self):
        os.rmdir(self.pasta_teste)

    def test_encontrar_arquivo_csv_folder_does_exist(self):
        with self.assertRaises(ValueError) as context:
            encontrarArquivoCsv('arquivo.csv', 'pasta_inexistente')

        self.assertIn("A pasta pasta_inexistente não foi encontrada.", str(context.exception))


def encontrarArquivoCsv(nome_arquivo, pasta):

    if nome_arquivo is None or pasta is None:
        raise ValueError("O nome do arquivo e a pasta não podem ser nulos.")

    if not isinstance(nome_arquivo, str) or not isinstance(pasta, str):
        raise ValueError("O nome do arquivo e a pasta devem ser strings.")

    caminho_pasta = os.path.join(os.path.dirname(os.path.abspath(__file__)), pasta)

    if not os.path.exists(caminho_pasta):
            raise ValueError(f"A pasta {pasta} não foi encontrada.")
    
    arquivos = os.listdir(caminho_pasta)

    for arquivo in arquivos:
        if nome_arquivo in arquivo:
            return os.path.join(caminho_pasta, arquivo)
        
class TestEncontrarArquivoCsv(unittest.TestCase):
    def setUp(self):
        self.pasta_teste = 'pasta_teste_temporaria'
        os.makedirs(self.pasta_teste)

    def tearDown(self):
        os.rmdir(self.pasta_teste)

    def test_encontrar_arquivo_not_found(self):
        resultado = encontrarArquivoCsv('arquivo_inexistente.csv', self.pasta_teste)

        mensagem_esperada = f'O arquivo arquivo_inexistente.csv não foi encontrado na pasta {self.pasta_teste}'
        self.assertEqual(resultado, mensagem_esperada)
        
def encontrarArquivoCsv(nome_arquivo, pasta):

    if nome_arquivo is None or pasta is None:
        raise ValueError("O nome do arquivo e a pasta não podem ser nulos.")

    if not isinstance(nome_arquivo, str) or not isinstance(pasta, str):
        raise ValueError("O nome do arquivo e a pasta devem ser strings.")

    caminho_pasta = os.path.join(os.path.dirname(os.path.abspath(__file__)), pasta)

    if not os.path.exists(caminho_pasta):
            raise ValueError(f"A pasta {pasta} não foi encontrada.")
    
    arquivos = os.listdir(caminho_pasta)

    for arquivo in arquivos:
        if nome_arquivo in arquivo:
            return os.path.join(caminho_pasta, arquivo)
        
    return f'O arquivo {nome_arquivo} não foi encontrado na pasta {pasta}'

