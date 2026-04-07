import os
import json
import logging
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
DATA_DIR = os.path.join(BASE_DIR, 'data')
os.makedirs(DATA_DIR, exist_ok=True)

logger = logging.getLogger("TransformerAgent")
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(stream_handler)

def setup_error_log():
    error_handler = logging.FileHandler(os.path.join(DATA_DIR, 'error_transformer.log'), encoding='utf-8')
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(logging.Formatter('%(asctime)s - ERROR: %(message)s'))
    logger.addHandler(error_handler)

def transform_data():
    setup_error_log()
    
    input_path = os.path.join(DATA_DIR, 'extracted_data.json')
    output_path = os.path.join(DATA_DIR, 'transformed_data.json')
    
    logger.info(f"O Transformer foi acordado. A iniciar leitura de: {input_path}")
    
    if not os.path.exists(input_path):
        logger.error(f"ARQUIVO AUSENTE: Não foi encontrado o ficheiro {input_path}. Notificar Coordenador para acionar Extrator.")
        sys.exit(1)
        
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if not content.strip():
                raise ValueError("O ficheiro não tem conteúdo (tamanho 0).")
            data = json.loads(content)
            
        if not isinstance(data, list) or len(data) == 0:
            raise ValueError("O JSON foi carregado mas não contém formatação de lista ou está vazio.")
            
    except (json.JSONDecodeError, ValueError) as e:
        logger.error(f"CORRUPÇÃO DE DADOS: O ficheiro de input está corrompido ou vazio. Detalhes: {str(e)}")
        sys.exit(1)

    transformed = []
    for item in data:
        if 'id' in item and 'body' in item:
            transformed.append({
                'id': item['id'],
                'body_length': len(item['body'])
            })
            
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(transformed, f, indent=4, ensure_ascii=False)
        
    logger.info(f"Transformação concluída! {len(transformed)} registos agregados num esquema simplificado ({output_path}).")

if __name__ == "__main__":
    transform_data()
