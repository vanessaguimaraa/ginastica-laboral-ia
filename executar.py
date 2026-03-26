import cv2
from deepface import DeepFace
import os
from datetime import datetime
import winsound

# --- CONFIGURAÇÕES ---
pasta_fotos = os.path.abspath("fotos_conhecidas")
arquivo_log = "registro_presenca.csv"
cap = cv2.VideoCapture(1) # Sua Logitech

# Carrega o detector de faces padrão do OpenCV (super rápido e leve)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

print("--- SISTEMA INTELIGENTE INICIADO ---")

while True:
    ret, frame = cap.read()
    if not ret: break

    # 1. Converte para cinza (mais rápido para detectar rostos)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 2. Procura por faces na imagem
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    nome_exibir = "AGUARDANDO COLABORADOR..."
    cor_exibir = (255, 255, 255) # Branco

    # 3. Só tenta reconhecer se encontrar ao menos uma face
    for (x, y, w, h) in faces:
        # Desenha um quadrado ao redor do rosto detectado
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        try:
            # Chama o reconhecimento apenas para a área do rosto
            df = DeepFace.find(img_path=frame, 
                               db_path=pasta_fotos, 
                               enforce_detection=False,
                               model_name="Facenet",
                               detector_backend="opencv",
                               silent=True)

            if len(df) > 0 and not df[0].empty:
                caminho_foto = df[0]['identity'][0]
                nome_exibir = os.path.basename(caminho_foto).split('.')[0].upper()
                cor_exibir = (0, 255, 0) # Verde
                
                winsound.Beep(1000, 200)
                
                # Registro no CSV
                agora = datetime.now()
                with open(arquivo_log, "a") as f:
                    f.write(f"{nome_exibir};{agora.strftime('%d/%m/%Y')};{agora.strftime('%H:%M:%S')}\n")
            else:
                nome_exibir = "DESCONHECIDO"
                cor_exibir = (0, 0, 255) # Vermelho
        except:
            pass

    # Exibe as informações na tela
    cv2.putText(frame, nome_exibir, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, cor_exibir, 2)
    cv2.imshow("Ginastica Laboral - Busca Ativa", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()