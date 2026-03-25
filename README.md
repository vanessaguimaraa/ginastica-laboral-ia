Registro de Ginástica Laboral com IA 🧘‍♂️
Este projeto utiliza Inteligência Artificial e Reconhecimento Facial para automatizar o registro de presença dos colaboradores durante as sessões de ginástica laboral da empresa. O sistema identifica o colaborador através da webcam e registra automaticamente a data e o horário em um arquivo de controle.

🚀 Funcionalidades
Reconhecimento Facial em Tempo Real: Identifica colaboradores previamente cadastrados através de fotos.

Feedback Sonoro (Bip): Emite um sinal sonoro ao confirmar a identificação do rosto.

Registro Automático: Gera um arquivo registro_presenca.csv com Nome, Data e Hora do acesso.

Otimização de Performance: Processamento leve para evitar travamentos durante os exercícios (processamento a cada 10 frames).

🛠️ Tecnologias Utilizadas
Python 3.x

DeepFace: Para a lógica de reconhecimento facial.

OpenCV: Para captura e manipulação de vídeo da webcam.

Pandas: Para organização dos registros (opcional).

Logging: Registro de eventos no terminal.

📋 Pré-requisitos
Antes de começar, você vai precisar ter instalado:

Python

Git

🔧 Instalação e Uso
Clone o repositório:

Bash
git clone https://github.com/vanessaguimaraa/ginastica-laboral-ia.git
cd激-laboral-ia
Crie um ambiente virtual e instale as dependências:

Bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
Configure as fotos:

Crie uma pasta chamada fotos_conhecidas.

Coloque fotos dos colaboradores com o nome do arquivo sendo o nome da pessoa (ex: vanessa.jpg).

Execute o sistema:

Bash
python executar.py
⌨️ Comandos do Teclado
q: Fecha a janela da câmera e encerra o programa de forma segura.

📄 Licença
Este projeto está sob a licença MIT.
