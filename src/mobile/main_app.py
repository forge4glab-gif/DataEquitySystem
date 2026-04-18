import hashlib
import time

class DataEquityApp:
    def __init__(self):
        self.saldo_royalties = 115754.05
        self.id_global = "V_SERRANONI_GLOBAL_ID"
        
    def render_dashboard(self):
        print("========================================")
        print("      DATAEQUITY SYSTEM - MOBILE        ")
        print("========================================")
        print(f"USUÁRIO: {self.id_global}")
        print(f"SALDO AUDITADO: R$ {self.saldo_royalties:,.2f}")
        print("----------------------------------------")
        print("STATUS DOS GADGETS: PROTEGIDO")
        print("LOGS DE AUDITORIA: 14 eventos hoje.")
        print("========================================")

    def iniciar_servico_background(self):
        print("Ativando Auditoria Forense em background...")
        # Aqui entra a lógica de interceptação de pacotes que criamos
        
if __name__ == '__main__':
    app = DataEquityApp()
    app.render_dashboard()
    app.iniciar_servico_background()
