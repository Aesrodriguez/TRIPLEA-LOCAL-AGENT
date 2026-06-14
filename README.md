# TripleA Local Agent

> Agente de Inteligencia Artificial 100% local para automatización, auditoría de código, generación de documentación y asistencia al desarrollo de software.

---

# Objetivo

TripleA Local Agent es un proyecto diseñado para proporcionar un asistente de desarrollo completamente local, utilizando modelos ejecutados mediante Ollama, con capacidades de:

- Auditoría de proyectos
- Generación de código
- Refactorización
- Documentación automática
- Análisis de seguridad
- Optimización
- Automatización de tareas
- Integración con Git
- Memoria persistente
- Base de conocimiento empresarial

El objetivo es crear una plataforma comparable a asistentes comerciales, pero completamente bajo control local.

---

# Estado del Proyecto

Versión:

```
0.1.0-alpha
```

Estado:

```
En desarrollo
```

---

# Arquitectura

```
                    TripleA Local Agent

                           │

                    Interface Layer

                           │

          ┌────────────────┼────────────────┐

          │                │                │

       CLI/API          Future UI        External Tools

          │

          ▼

                 Core Application Layer

          │                │

          │                │

     Configuration      Memory Manager

          │

          ▼

                  LLM Communication Layer

                    Ollama Client

                           │

        localhost:11434

                           │

                  qwen2.5-coder

                           │

                  Future Models

                  - DeepSeek

                  - Llama

                  - Qwen

                  - Mistral

---

FileSystem Layer

- Read files

- Write files

- Search files

- Create files

- Create directories

- Project analysis

---

Future Layers

- Git Integration

- PostgreSQL Analysis

- Docker Analysis

- React Analysis

- Python Analysis

- Security Scanner

- Documentation Generator

- Unit Test Generator

- Knowledge Base

- Vector Database

- Semantic Search

- Agent Memory

- Autonomous Agents
```

---

# Estructura del Proyecto

```
TripleA-Local-Agent/

│

├── agents/

├── app/

├── config/

├── core/

├── data/

├── docs/

├── knowledge/

├── llm/

├── logs/

├── memory/

├── prompts/

├── scripts/

├── tests/

├── tools/

│

├── main.py

├── README.md

├── requirements.txt

└── .gitignore
```

---

# Funcionalidades Implementadas

## Etapa 1

- Estructura inicial del proyecto

## Etapa 2

- Configuración base

- requirements

- config.yaml

- entorno virtual

## Etapa 3

- Integración inicial con Ollama

## Etapa 4

- Herramientas FileSystem

- Lectura

- Escritura

- Creación

- Listado

## Etapa 5

Cliente profesional para Ollama

- Health Check

- List Models

- Generate

- Chat

- Manejo básico de errores

---

# Roadmap

## Etapa 6

Sistema de Memoria Persistente

### Funcionalidades

- Persistencia de conversaciones
- Persistencia de sesiones
- Almacenamiento de contexto
- Gestión de reglas
- Caché local
- Base para memoria semántica futura

## Etapa 7

- Base de conocimiento

## Etapa 8

- Prompt Engine

## Etapa 9

- Auditor Inteligente

## Etapa 10

- Editor Automático

## Etapa 11

- Git Integration

## Etapa 12

- Web UI

## Etapa 13+

- Semantic Search

- Vector Database

- Multi-Agent System

- Autonomous Tasks

- Enterprise Features

---

# Filosofía del Proyecto

Principios:

- SOLID

- Clean Code

- Clean Architecture

- DRY

- KISS

- Explicit is Better than Implicit

- Type Hints

- Modular Design

- Testable Code

- High Maintainability

---

# Tecnologías

- Python

- Ollama

- FastAPI

- Git

- YAML

- HTTPX

- Requests

- Rich

- Typer

---

# Licencia

Proyecto privado desarrollado para Triple A Construcciones.

Todos los derechos reservados.