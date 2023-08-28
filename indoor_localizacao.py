class PontoAcessoWiFi:
    def __init__(self, nome, coordenadas, intensidade_referencia):
        self.nome = nome
        self.coordenadas = coordenadas
        self.intensidade_referencia = intensidade_referencia

    def calcular_distancia(self, intensidade_sinal):
        # Simulação de cálculo de distância baseada na intensidade do sinal
        distancia = 10 ** ((self.intensidade_referencia - intensidade_sinal) / 20)  # Fórmula simplificada
        return distancia


class Indoor_localizacao:
    def __init__(self):
        self.pontos_acesso = [
            PontoAcessoWiFi("AP1", (0, 0), -40),
            PontoAcessoWiFi("AP2", (0, 5), -55),
            PontoAcessoWiFi("AP3", (5, 0), -50),
        ]

    def estimar_posicao(self, intensidades_sinais):
        posicao_estimada = None

        if len(intensidades_sinais) != len(self.pontos_acesso):
            return posicao_estimada

        distancias = [ponto.calcular_distancia(intensidade) for ponto, intensidade in
                      zip(self.pontos_acesso, intensidades_sinais)]

        # Simulação de trilateração simples (método dos mínimos quadrados)
        x = sum(ponto.coordenadas[0] * d for ponto, d in zip(self.pontos_acesso, distancias)) / sum(distancias)
        y = sum(ponto.coordenadas[1] * d for ponto, d in zip(self.pontos_acesso, distancias)) / sum(distancias)

        posicao_estimada = (x, y)
        return posicao_estimada


# Criando uma instância do sistema de localização
sistema_localizacao = Indoor_localizacao()

# Simulação de intensidades de sinal recebidas pelo dispositivo
intensidades_sinais = [-45, -50, -53]

# Estimando a posição do dispositivo
posicao_estimada = sistema_localizacao.estimar_posicao(intensidades_sinais)
if posicao_estimada:
    print("Posição estimada:", posicao_estimada)
else:
    print("Não foi possível estimar a posição.")
