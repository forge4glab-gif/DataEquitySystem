import hashlib
import time

class DataEquityMobile:
    def __init__(self, imei, android_id):
        self.user_id = "V_SERRANONI_GLOBAL_ID"
        self.device_id = self._generate_id(imei, android_id)

    def _generate_id(self, imei, android_id):
        seed = f"{imei}{android_id}FORGE4G_SECRET"
        return hashlib.sha256(seed.encode()).hexdigest()

    def audit_background_traffic(self):
        print("--- DATAEQUITY MOBILE AUDIT ---")
        print(f"ID Global Detectado: {self.user_id}")
        print(f"Device ID (Hash): {self.device_id}")
        print("Status: Escaneando background de apps (TikTok/Insta)...")
        time.sleep(1)
        print("Evento Detectado: Captura de Clipboard por app externo.")
        print("Ação: Prova forense gerada e enviada para AWS/Alibaba.")

if __name__ == '__main__':
    # Simulando com os dados do terminal
    app = DataEquityMobile("3589...", "AID992...")
    app.audit_background_traffic()
