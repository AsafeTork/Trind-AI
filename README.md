# Trind-AI 🧠🚀

> Uma arquitetura ETL resiliente impulsionada por Sistemas Multiagentes (SMA) e algoritmos de Auto-Cura.

O **Trind-AI** é um ecossistema infraestrutural desenhado para resolver a incontornável latência de manutenção causada pela "fragilidade estrutural" de pipelines de dados. Rompendo com o formato convencional de scripts estáticos e quebra frágil, esta arquitetura encadeia agentes contêinerizados capazes de agir com autonomia cirúrgica e curar-se algoritmicamente de anomalias inesperadas na rede.

---

## 🏗️ Arquitetura de Agentes

O pipeline distribui responsabilidades por três entidades sequenciais isoladas pela diretriz de um Cérebro Coordenador Central:

*   **📥 Agente Extrator**: Conecta-se a domínios web simulados (APIs), extraindo volumes de dados raw de forma determinística. Exposta estritamente à rede, levanta infrações drásticas (`sys.exit(1)`) perante anomalias externas (ex: `404 Not Found`).
*   **⚙️ Agente Transformador**: Atua como o fiscal de qualidade — valida a integridade JSON estrutural dos manifestos, impedindo progressão em payloads vazias. Purifica os registos convertendo blocos difusos (`body`) num modelo simplificado (`id` + contagem volumétrica `body_length`).
*   **📤 Agente Carregador**: Garante as chaves persistentes (UPSERTs) encapsuladas no motor motor de produção de `SQLite3`. É o agente fiador de estabilidade antes de emitir a telemetria JSON exposta para a interface visual local (`dashboard_data.js`).

---

## 🧬 O Diferencial: *Self-Healing* Dinâmico

Em ferramentas antiquadas de BI corporativo, a desidratação mínima numa URL ou alteração na Query paralisa a empresa inteira durante horas até o debugar ser completado. No **Trind-AI**, os agentes detêm propriedade de *Self-Healing*:

1.  **Deteção Cirúrgica**: Perante um *Crash* com erros críticos operacionais (`Return Código 1`), o Módulo LLM/Regex local é alertado e perscruta o registador de erros à procura de anomalias HTTP ou falhas catalogadas (`404` / `URL`).
2.  **Reparação Regenerativa**: Armado de Expressões Regulares de isolamento sintático, o *Orquestrador* injeta um Patch no próprio Código-Fonte Python de extração perante falhas conhecidas, expurgando sufixos e fragmentos corruptos de forma autônoma.
3.  **Reiniciação Autónoma**: Retoma instantânea e cíclica. O fluxo estático recupera vida organicamente e o sistema flui para estabilidade final sem requisitar permissão técnica manual à infraestrutura.

---

## 🛠️ Stack Técnica

*   **Agentes & Orquestração:** Python `3.x` Puro (Independente e focado em paralelismo assíncrono).
*   **Base de Dados:** Persistência em `SQLite3` adaptada a _pipelines_ operacionais e Data Storage resiliente.
*   **Monitorização (Sem Flutter CLI):** Core gráfico em **HTML5**, **JavaScript Assíncrono** e Componentização UX **Bootstrap**, garantindo o visual elegante _Client-Side_ (Offline Bypass Web CORS).

---

## 🚀 Como Rodar (Quick Start)

Este projeto reflete os princípios elementares de *Continuous Deployment* unipotente:

1. Clone o repositório para a sua máquina:
   ```bash
   git clone https://github.com/O-Seu-Usuario/trind-ai.git
   cd trind-ai
   ```

2. Dispare o Controlador Universal ETL em Background:
   ```bash
   python main_orchestrator.py
   ```

3. Exponha o Dashboard em tempo real:
   Como a arquitetura JavaScript consome passivamente a API local renderizada pelo Loader, não é necessário hostear *Live Server*. Limite-se a dar Duplo-Clique em `app/index.html` e maravilhe-se a observar em Monitor de Interface os 3 agentes Saudáveis de Data Streaming.
