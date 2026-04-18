[app]
# (str) Título do seu aplicativo
title = DataEquity Collector

# (str) Nome do pacote (sem espaços)
package.name = dataequity_collector

# (str) Domínio do pacote (inverso do seu site)
package.domain = io.github.forge4glab_gif

# (str) Arquivo principal
source.dir = src/mobile
source.include_exts = py,png,jpg,kv,atlas

# (str) Versão do App
version = 4.0.1

# (list) Requisitos/Dependências
requirements = python3,kivy,requests,hashlib

# (list) Permissões Críticas para Auditoria
# INTERNET: Enviar hashes para nuvem
# READ_LOGS: Capturar eventos de sistema dos outros apps
# WRITE_EXTERNAL_STORAGE: Salvar logs forenses localmente
android.permissions = INTERNET, READ_LOGS, WRITE_EXTERNAL_STORAGE, FOREGROUND_SERVICE

# (str) Orientação da tela
orientation = portrait

# (bool) Indicar se o app deve rodar em background (Fundamental para auditoria)
android.service = DataEquityAudit:collector_agent.py

# (int) Android API (33 é o padrão atual para Android 13+)
android.api = 33

[buildozer]
# (int) Nível de log (2 para ver erros detalhados)
log_level = 2
