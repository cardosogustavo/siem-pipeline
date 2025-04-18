# Cloud Security Data Pipeline

Este projeto demonstra uma arquitetura de pipeline de dados para simulação de logs de eventos de segurança (SIEM) em nuvem, utilizando tecnologias modernas como Apache Kafka, Apache Spark, Docker, e Python.
O objetivo é aprender mais sobre as tecnologias citadas, machine learning e infraestrutura, além de fazer uma solução que pode ser usada em ambiente real.

## Visão Geral da Arquitetura

TODO: draw in excalidraw

## Estrutura de pastas

```
cloud-security-pipeline/
├── data/                         # Diretório que simula a origem dos dados (log gerado)
│
├── data_simulator/               # Módulo com lógica de geração de logs sintéticos
│   ├── __init__.py
│   └── simulator.py              # Função com Faker para criar logs
│
├── kafka_producer/               # Container responsável por enviar dados para o Kafka
│   ├── __init__.py
│   ├── kafka_producer.py         # Producer usando kafka-python
│   └── Dockerfile                # Define ambiente do producer
│
├── ml_model/                     # TODO: pasta contendo a lógica de ML para algoritmo aprender a classificar os dados em anomalia/não-anomalia
├── spark_streaming/              # Processamento em tempo real com Apache Spark
|   ├── checkpoint                # Pasta para o checkpoint da função de append do Spark
│   ├── spark_stream.py           # Script de leitura de dados Kafka → Parquet
│   ├── Dockerfile                # Dockerfile com dependências do PySpark
│   └── output/                   # Saída em formato Parquet
│       ├── parquet/              # Arquivos particionados gerados pelo Spark
│       │   ├── _spark_metadata/  # Controle interno do Spark (gerenciamento de stream)
│       │   └── part-*.parquet    # Partições reais com os dados
│
├── sqlite_loader/                # TODO: container para jogar os dados Parquet em um DB SQLite
|    ├── data/
|    ├── Dockerfile
|    ├── parquet_to_sqlite.py
├── docker-compose.yml            # Orquestração dos serviços (Kafka, Producer, Spark, etc)
├── README.md                     # Documentação do projeto para o GitHub
└── requirements.txt              # Dependências Python do projeto
```


## Tecnologias Utilizadas

Python - Lógica do gerador e processamento

Apache Kafka - Sistema de mensagens e transporte de eventos

Apache Spark - Processamento de stream em tempo real

Docker e Docker Compose - Empacotamento e orquestração

PySpark, Faker, kafka-python - Bibliotecas principais



## Principais Problemas Enfrentados (e Soluções)

Erro com dependências Ivy do Spark

> Solução: Criação de cache e instalação manual do ivy2 dentro do container

Problemas com PYTHONPATH e importações entre pastas

> Solução: Ajustes no ENV PYTHONPATH e estrutura do build

Kafka Producer: NoBrokersAvailable

> Solução: Configurar corretamente o hostname e portas entre os containers (em andamento)

Erro "basedir must be absolute" no spark-submit

> Solução: Usar caminhos absolutos dentro do container para o script Spark

Diretórios de output/checkpoint não encontrados

> Solução: Garantir que as pastas existam no container e sejam persistidas com volumes


## Como executar

Suba toda a stack:
`docker compose up --build`

Veja os logs de um container específico:
`sudo docker logs -f kafka_producer`

## Objetivos Finais

Simular uma arquitetura real de segurança para ingestão e análise de logs, com foco em escalabilidade, modularidade, observabilidade, processamento em tempo real.
Aprender na prática Machine Learning.
Aprofundar conhecimentos em infraestrutura, Spark e Kafka.


Em constante evolução — novas features como alertas e dashboard serão adicionadas em breve!
