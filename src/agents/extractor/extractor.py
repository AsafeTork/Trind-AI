import os
import json
import logging
import sys
import urllib.request
from urllib.error import HTTPError, URLError

# Configuração dinâmica de caminhos estruturados
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
DATA_DIR = os.path.join(BASE_DIR, 'data')
os.makedirs(DATA_DIR, exist_ok=True)

logger = logging.getLogger("ExtractorAgent")
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(stream_handler)

def setup_error_log():
    error_handler = logging.FileHandler(os.path.join(DATA_DIR, 'error_extractor.log'), encoding='utf-8')
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(logging.Formatter('%(asctime)s - ERROR: %(message)s'))
    logger.addHandler(error_handler)

def extract_data():
    setup_error_log()
    url = "https://jsonplaceholder.typicode.com/posts"
    logger.info(f"A iniciar extração da API: {url}")
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Trind-AI/1.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            
            output_file = os.path.join(DATA_DIR, 'extracted_data.json')
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
                
            logger.info(f"Sucesso! {len(data)} registos foram guardados em '{output_file}'.")
            
    except HTTPError as e:
        logger.error(f"Falha na API: {e.code} - {e.reason}")
        sys.exit(1)  # Informa o Orquestrador que houve um Crash!
    except URLError as e:
        logger.error(f"Falha de Conectividade: {e.reason}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Erro inesperado: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    extract_data()
