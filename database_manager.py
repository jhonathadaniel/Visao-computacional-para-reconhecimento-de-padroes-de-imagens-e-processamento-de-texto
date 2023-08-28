class Produto:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco


class Ambiente:
    def __init__(self, codigo, nome, tamanho):
        self.codigo = codigo
        self.nome = nome
        self.tamanho = tamanho


class Database:
    def __init__(self):
        self.produtos = {}
        self.ambientes = {}

    def adicionar_produto(self, produto):
        self.produtos[produto.codigo] = produto

    def adicionar_ambiente(self, ambiente):
        self.ambientes[ambiente.codigo] = ambiente

    def obter_produto(self, codigo):
        return self.produtos.get(codigo)

    def obter_ambiente(self, codigo):
        return self.ambientes.get(codigo)


class SistemaEntrega:
    def __init__(self, banco_dados):
        self.banco_dados = banco_dados

    def gerar_qr_code_produto(self, codigo_produto):
        produto = self.banco_dados.obter_produto(codigo_produto)
        if produto:
            qr_code = f"QR Code do Produto {produto.nome}"
            return qr_code
        return None

    def gerar_qr_code_ambiente(self, codigo_ambiente):
        ambiente = self.banco_dados.obter_ambiente(codigo_ambiente)
        if ambiente:
            qr_code = f"QR Code do Ambiente {ambiente.nome}"
            return qr_code
        return None

    def rastrear_entrega(self, pedido):
        # Simulação de rastreamento de entrega
        print(f"Rastreando o pedido {pedido}")
        print("Status: Em trânsito")
        print("Previsão de entrega: 25/09/2023")
        print("Localização atual: Centro de Distribuição")
        print("Recursos alocados: Veículo, Motorista")


# Criando uma instância do banco de dados
banco_dados = Database()

# Adicionando produtos ao banco de dados
produto1 = Produto("P001", "Camiseta", 29.99)
produto2 = Produto("P002", "Calça", 49.99)
banco_dados.adicionar_produto(produto1)
banco_dados.adicionar_produto(produto2)

# Adicionando ambientes ao banco de dados
ambiente1 = Ambiente("A001", "Sala de Estar", "20 m²")
ambiente2 = Ambiente("A002", "Quarto", "15 m²")
banco_dados.adicionar_ambiente(ambiente1)
banco_dados.adicionar_ambiente(ambiente2)

# Criando uma instância do sistema de entrega
sistema_entrega = SistemaEntrega(banco_dados)

# Simulação de geração de QR Code para um produto e um ambiente
qr_code_produto = sistema_entrega.gerar_qr_code_produto("P001")
qr_code_ambiente = sistema_entrega.gerar_qr_code_ambiente("A002")

if qr_code_produto:
    print("QR Code do Produto:", qr_code_produto)
else:
    print("Produto não encontrado.")

if qr_code_ambiente:
    print("QR Code do Ambiente:", qr_code_ambiente)
else:
    print("Ambiente não encontrado.")

# Simulação de rastreamento de entrega
pedido = "Pedido123"
sistema_entrega.rastrear_entrega(pedido)
