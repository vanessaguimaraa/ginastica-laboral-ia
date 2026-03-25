import cv2
from deepface import DeepFace
import os
from datetime import datetime
import winsound  # Biblioteca para o BIP no Windows

# Configurações
pasta_fotos = os.path.abspath("fotos_conhecidas")
arquivo_log = "registro_presenca.csv"
cap = cv2.VideoCapture(1) # Logitech

# Resolução leve
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

contador_frames = 0
processar_a_cada = 10 
nome_exibir = "ANALISANDO..."
cor_exibir = (0, 0, 255)

print("--- SISTEMA COM BIP ATIVADO ---")

while True:
    ret, frame = cap.read()
    if not ret: break

    contador_frames += 1

    if contador_frames % processar_a_cada == 0:
        try:
            df = DeepFace.find(img_path=frame, 
                               db_path=pasta_fotos, 
                               enforce_detection=False,
                               model_name="Facenet", 
                               detector_backend="opencv",
                               silent=True)

            if len(df) > 0 and not df[0].empty:
                caminho_foto = df[0]['identity'][0]
                nome_exibir = os.path.basename(caminho_foto).split('.')[0].upper()
                cor_exibir = (0, 255, 0)
                
                # Toca o BIP (Frequência: 1000Hz, Duração: 200ms)
                winsound.Beep(1000, 200)
                
                # Grava no CSV
                agora = datetime.now()
                with open(arquivo_log, "a") as f:
                    f.write(f"{nome_exibir};{agora.strftime('%d/%m/%Y')};{agora.strftime('%H:%M:%S')}\n")
            else:
                nome_exibir = "PROCURANDO..."
                cor_exibir = (0, 0, 255)
        except:
            pass

    cv2.putText(frame, nome_exibir, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, cor_exibir, 2)
    cv2.imshow("Ginastica Laboral - BIP ATIVO", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()