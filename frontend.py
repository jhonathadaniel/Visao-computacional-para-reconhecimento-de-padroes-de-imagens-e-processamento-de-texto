from tkinter import Button, Tk, Label
from tkinter import ttk

class Frontend:
    def _init_(self, root):
        self.root = root
        self.root.title("Sistema de Interação do Usuário")
        self.root.geometry("400x300")

        self.tabControl = ttk.Notebook(root)
        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        self.tab3 = ttk.Frame(self.tabControl)
        self.tab4 = ttk.Frame(self.tabControl)

        self.tabControl.add(self.tab1, text="Processamento de Imagem e Texto")
        self.tabControl.add(self.tab2, text="Localização Indoor com Wi-Fi")
        self.tabControl.add(self.tab3, text="Identificação de Imagens via Câmera")
        self.tabControl.add(self.tab4, text="Banco de Dados e Entrega")

        self.tabControl.pack(expand=1, fill="both")

        self.create_tab1_content()
        self.create_tab2_content()
        self.create_tab3_content()
        self.create_tab4_content()

    def create_tab1_content(self):
        label = Label(self.tab1, text="Processamento de Imagem e Texto", font=("Helvetica", 12))
        label.pack(pady=10)

        # Botão de processamento de imagem e texto
        process_button = Button(self.tab1, text="Processar", command=self.process_image_text)
        process_button.pack()

    def create_tab2_content(self):
        label = Label(self.tab2, text="Localização Indoor com Wi-Fi", font=("Helvetica", 12))
        label.pack(pady=10)

        # Botão de localização indoor com Wi-Fi
        locate_button = Button(self.tab2, text="Localizar", command=self.locate_wifi)
        locate_button.pack()

    def create_tab3_content(self):
        label = Label(self.tab3, text="Identificação de Imagens via Câmera", font=("Helvetica", 12))
        label.pack(pady=10)

        # Botão de identificação de imagens via câmera
        identify_button = Button(self.tab3, text="Identificar", command=self.identify_camera_image)
        identify_button.pack()

    def create_tab4_content(self):
        label = Label(self.tab4, text="Banco de Dados e Entrega", font=("Helvetica", 12))
        label.pack(pady=10)

        # Botão de acesso ao banco de dados e sistema de entrega
        database_button = Button(self.tab4, text="Acessar Banco de Dados", command=self.access_database)
        database_button.pack()

    # Funções associadas aos botões
    def process_image_text(self):
        print("Processamento de imagem e texto")

    def locate_wifi(self):
        print("Localização indoor com Wi-Fi")

    def identify_camera_image(self):
        print("Identificação de imagem via câmera")

    def access_database(self):
        print("Acesso ao banco de dados e sistema de entrega")

def main():
    root = Tk()
    app = Frontend()

    root.mainloop()

if _name_ == "_main_":
    main()