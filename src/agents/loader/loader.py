import os
import json
import sqlite3
import logging
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
DATA_DIR = os.path.join(BASE_DIR, 'data')
os.makedirs(DATA_DIR, exist_ok=True)

logger = logging.getLogger("LoaderAgent")
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(stream_handler)

def load_data():
    input_path = os.path.join(DATA_DIR, 'transformed_data.json')
    db_path = os.path.join(DATA_DIR, 'production_database.db')
    js_output_path = os.path.join(DATA_DIR, 'dashboard_data.js')
    
    logger.info("O Loader foi acordado. A conectar à DB SQLite e gerar dados UI...")
    
    if not os.path.exists(input_path):
        logger.error(f"Falha Crítica: Fonte de dados desapareceu ({input_path}).")
        sys.exit(1)
        
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS analytics_data (
                id INTEGER PRIMARY KEY,
                body_length INTEGER
            )
        ''')
        
        for item in data:
            cursor.execute('''
                INSERT OR REPLACE INTO analytics_data (id, body_length)
                VALUES (?, ?)
            ''', (item['id'], item['body_length']))
            
        conn.commit()
        conn.close()
        
        # O dashboard usa isto para contornar problemas de CORS no clique direto do ficheiro html
        with open(js_output_path, 'w', encoding='utf-8') as f:
            f.write(f"const trindAiStats = {{ status: 'SAUDÁVEL', records: {len(data)}, updatedAt: new Date().toLocaleString() }};\n")
            f.write(f"const trindAiData = {json.dumps(data)};\n")
            
        logger.info(f"{len(data)} registos persistidos na BD {db_path} e exportados para o UI.")
        logger.info("CARGA FINALIZADA: Sistema Trind-AI operando em 100%")
        
    except Exception as e:
        logger.error(f"Erro inesperado durante a carga de dados: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    load_data()
