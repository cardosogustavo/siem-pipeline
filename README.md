# Cloud Security Data Pipeline

Este projeto demonstra uma arquitetura de pipeline de dados para simulação de logs de eventos de segurança (SIEM) em nuvem, utilizando tecnologias modernas como Apache Kafka, Apache Spark, Docker, e Python.
O objetivo é aprender mais sobre as tecnologias citadas, machine learning e infraestrutura, além de fazer uma solução que pode ser usada em ambiente real.

## Visão Geral da Arquitetura

TODO: draw in excalidraw

## Estrutura de pastas (TODO: organizar a apresentação)

`cloud-security-pipeline/
├── data/                         # Local onde os dados serão armazenados
├── data_simulator/               # Gerador de logs sintéticos com Faker
│   └── simulator.py              # Função de geração de logs
├── kafka_producer/               # Producer Kafka em Python
│   ├── kafka_producer.py
│   └── Dockerfile
├── spark_streaming/              # Processamento em tempo real com Spark
│   ├── spark_stream.py
│   └── Dockerfile
├── docker-compose.yml            # Orquestração dos containers`


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
