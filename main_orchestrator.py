import time
import subprocess
import logging
import os
import sys
import re

# Setup logging global para o Cérebro
logging.basicConfig(level=logging.INFO, format='%(asctime)s - [CÉREBRO COORDENADOR] - %(levelname)s - %(message)s')
logger = logging.getLogger("Orquestrador Principal")

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

def run_agent(script_path, agent_name):
    logger.info(f"A invocar o agente '{agent_name}'...")
    abs_path = os.path.join(BASE_DIR, script_path)
    result = subprocess.run([sys.executable, abs_path], capture_output=True, text=True, cwd=BASE_DIR)
    
    if result.returncode != 0:
        logger.error(f"Falha catastrófica no '{agent_name}'. (Exit Code {result.returncode})")
        logger.error(f"Detalhes do STDERR: {result.stderr.strip() if result.stderr else result.stdout.strip()}")
        
        success = auto_heal_diagnose_and_repair(agent_name)
        if success:
            logger.info(f"O pipeline recuperou o '{agent_name}'. A reiniciar a Run do agente...")
            return run_agent(script_path, agent_name) 
        else:
            logger.critical(f"A Falha no '{agent_name}' não foi mitigável autonomamente. O Job foi abortado.")
            return False
            
    logger.info(f"Feedback Operacional: '{agent_name}' terminou com sucesso (SAUDÁVEL).")
    return True

def auto_heal_diagnose_and_repair(agent_name):
    logger.info("=== INITIAÇÃO DO MÓDULO DE AUTO-CURA (Simulação LLM de Patching) ===")
    
    if agent_name == "Extractor":
        error_log_path = os.path.join(DATA_DIR, 'error_extractor.log')
        if os.path.exists(error_log_path):
            with open(error_log_path, 'r', encoding='utf-8') as f:
                logs = f.read()
                
            if "404" in logs or "URL" in logs:
                logger.info("Diagnóstico LLM: Conectividade rejeitada (404/URL). Possível corrupção de URL/Endpoints.")
                logger.info("Plano de Ação: Aplicar Patch Dinâmico (Expressões Regulares) no Código Fonte do Extractor...")
                
                script_path = os.path.join(BASE_DIR, 'src', 'agents', 'extractor', 'extractor.py')
                try:
                    with open(script_path, 'r', encoding='utf-8') as script_file:
                        code = script_file.read()
                        
                    # Detetar qualquer sufixo anómalo após "/posts" usando regex em vez de harcode 'X'
                    pattern = r'(url\s*=\s*"https://jsonplaceholder\.typicode\.com/posts)[^"]+(")'
                    if re.search(pattern, code):
                        logger.warning("Vulnerabilidade Encontrada: URL corrompida com terminação anómala detetada no source.")
                        # Remover qualquer sufixo corrompido, revertendo à forma base limpa
                        new_code = re.sub(pattern, r'\1\2', code)
                        
                        with open(script_path, 'w', encoding='utf-8') as script_file:
                            script_file.write(new_code)
                        
                        open(error_log_path, 'w').close()
                        logger.info("Auto-Cura Concluída: Patch regex universal injetado no código vivo!")
                        return True
                    else:
                        logger.warning("Falha 404 não pôde ser reparada. Nenhuma mutação detetada no código mapeado.")
                except Exception as e:
                    logger.error(f"O Módulo de Cura falhou a aplicar o patch: {e}")
                    
    logger.info("=== AUTO-CURA DECLINADA: O erro excede o escopo autonómo ===")
    return False

def main_loop():
    logger.info("==========================================================")
    logger.info("   SERVER ORQUESTRADOR TRIND-AI INICIADO (Modo Contínuo)  ")
    logger.info("==========================================================")
    
    ciclo = 1
    while True:
        logger.info(f"\n--- [INÍCIO DO CICLO ETL ORQUESTRADO #{ciclo}] ---")
        
        fluxo_saudavel = run_agent(r"src\agents\extractor\extractor.py", "Extractor")
        if fluxo_saudavel:
            fluxo_saudavel = run_agent(r"src\agents\transformer\transformer.py", "Transformer")
            if fluxo_saudavel:
                run_agent(r"src\agents\loader\loader.py", "Loader")
                
        logger.info(f"--- [FIM DO CICLO #{ciclo}]. O Motor adormecerá. Próxima Run em 5 minutos... ---")
        ciclo += 1
        
        try:
            time.sleep(300) 
        except KeyboardInterrupt:
            logger.info("\nIntervenção Humana Detetada (Ctrl+C). Orquestrador e Pipelines Desligados em Segurança.")
            break

if __name__ == "__main__":
    main_loop()
