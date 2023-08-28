class ProcessamentoImagemTexto:
    def __init__(self):
         self.modelo_IA = ModeloIA()  # Substituir por uma implementação real de IA

    def processar_imagem(self, imagem):
        # Simulação de processamento de imagem pela IA
        objetos_identificados = self.modelo_IA.processar_imagem(imagem)
        return objetos_identificados

    def processar_texto(self, texto):
        # Simulação de processamento de texto pela IA
        informacoes_extratadas = self.modelo_IA.processar_texto(texto)
        return informacoes_extratadas


class Tutorial:
    def __init__(self):
        self.passo_atual = 1

    def proximo_passo(self):
        if self.passo_atual == 1:
            self.passo_atual += 1
            return "Bem-vindo ao sistema de Processamento de Imagem e Texto! Aqui você pode carregar imagens ou inserir textos para obter informações úteis."
        elif self.passo_atual == 2:
            self.passo_atual += 1
            return "Vamos começar com imagens. Carregue uma imagem e veja como nossa IA identifica objetos nela."
        elif self.passo_atual == 3:
            self.passo_atual += 1
            return "Ótimo! Agora vamos experimentar com texto. Insira um texto e nossa IA extrairá informações dele."
        else:
            return "Tutorial concluído. Você está pronto para usar todas as funcionalidades do sistema!"


# Criando instâncias das classes
processamento = ProcessamentoImagemTexto()
tutorial = Tutorial()

# Interação com o usuário
while True:
    print(tutorial.proximo_passo())
    opcao = input("Digite 'i' para processar imagem, 't' para processar texto, ou 's' para sair: ").lower()

    if opcao == 'i':
        imagem = input("Insira o caminho da imagem: ")
        objetos_identificados = processamento.processar_imagem(imagem)
        print("Objetos identificados na imagem:", objetos_identificados)
    elif opcao == 't':
        texto = input("Insira o texto: ")
        informacoes_extratadas = processamento.processar_texto(texto)
        print("Informações extraídas do texto:", informacoes_extratadas)
    elif opcao == 's':
        print("Saindo do sistema. Até logo!")
        break
    else:
        print("Opção inválida. Escolha 'i', 't' ou 's'.")
