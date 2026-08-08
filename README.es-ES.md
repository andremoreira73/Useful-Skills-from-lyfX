

# Habilidades Útiles de lyfX

Una colección de habilidades y agentes de [Claude Code](https://claude.com/claude-code) desarrollados y probados en entornos reales en [lyfX.ai](https://lyfx.ai). Estos convierten a Claude en un agente especializado para flujos de trabajo específicos de negocios y desarrollo.

## ¿Qué son las habilidades?

Las habilidades son archivos `SKILL.md` que otorgan a Claude Code experiencia en un dominio. Coloca uno en `.claude/skills/` y Claude sabrá automáticamente cuándo y cómo usarlo. Sin configuración de API, sin complementos: solo un archivo markdown con instrucciones estructuradas.

Más información: [Documentación de Habilidades de Claude Code](https://code.claude.com/docs/en/skills)

## ¿Qué son los subagentes?

Los agentes son archivos markdown que definen subagentes especializados que Claude puede iniciar para tareas enfocadas. Coloca uno en `.claude/agents/` y Claude puede generarlo como un trabajador paralelo con su propia ventana de contexto, herramientas y habilidades. Los agentes son ideales para tareas como la revisión de código, donde deseas un revisor dedicado que no ensucie el contexto principal de tu conversación.

Más información: [Documentación de Subagentes de Claude Code](https://code.claude.com/docs/en/sub-agents#use-the-agents-command)

## Agentes Disponibles

### `code-reviewer`

Agente de revisión de código estructurada que verifica calidad, seguridad, salud del diseño y cumplimiento de convenciones. Comprende los principios de diseño fundamentales (Responsabilidad Única, DRY, Ley de Deméter, Abierto-Cerrado, etc.) y genera hallazgos categorizados (Crítico / Advertencia / Aprobado) con números de línea y sugerencias de corrección.

**Características:**

- Verificaciones generales de calidad (nombrado, duplicación, manejo de errores, secretos)
- Verificaciones específicas de Python (pistas de tipo, docstrings, administradores de contexto)
- Violaciones de principios de diseño basadas en _Software Design_ de Ronald Mak
- Estrategia para grandes bases de código utilizando la habilidad `/rlm` para escaneo paralelo
- Revisión de comandos CLI (cuando se combina con la habilidad `reviewing-cli-command`)

**Utilizado por:** La habilidad `/ai-dev-workflow` lanza este agente en el Paso 7 (Revisión de Código y Endurecimiento).

> **Atribución:** Basado en el agente code-reviewer del curso [Agent Skills with Anthropic](https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/) de DeepLearning.AI ([fuente](https://github.com/https-deeplearning-ai/sc-agent-skills-files/blob/main/L6/.claude/agents/code-reviewer.md)), modificado con verificaciones de salud de diseño, estrategia para grandes bases de código e integración de RLM. El repositorio original no especifica una licencia.

## Habilidades Disponibles

### `/market-research`

Realiza investigación de mercado estructurada con organización basada en proyectos. Guía a Claude a través de un flujo de trabajo de cuatro fases: validación del alcance, recopilación de datos, análisis y entregable final.

**Incluye:**

- SKILL.md -- flujo de trabajo y estructura del proyecto
- `references/methodology.md` -- formato del entregable, jerarquía de calidad de fuentes, estándares de citación, directrices de pronóstico
- `assets/brief_template.md` -- plantilla estructurada para definir el alcance de nuevos proyectos de investigación

**Lo que obtienes:** Documentos profesionales de investigación de mercado con citaciones en línea, niveles de calidad de fuentes y entregables estructurados (resumen ejecutivo, visión general del mercado, análisis de segmentos, tendencias).

### `/linkedin-posts`

Borra y perfecciona publicaciones de LinkedIn manteniendo tu voz auténtica. Gestiona el historial de versiones para que puedas iterar con Claude a través de diferentes sesiones.

**Incluye:**

- SKILL.md -- directrices de estilo, convención de versionado, flujo de trabajo

**Lo que obtienes:** Publicaciones que suenan como tú, no como una IA. Tono conversacional, estructura fácil de escanear, ganchos impulsados por la curiosidad. Cada borrador se versiona (v2, v3...) para que puedas rastrear las iteraciones.

### `/lyfx-corporate-design`

Directrices de diseño corporativo para lyfX.ai -- compartidas aquí como ejemplo de cómo codificar la identidad de marca en una habilidad. **Usa esto como inspiración para crear tu propia habilidad de diseño corporativo**, no como una plantilla para copiar directamente.

**Incluye:**

- SKILL.md -- paleta de colores, tipografía, jerarquía de texto, estilo de botones, variables CSS
- `assets/` -- variantes del logotipo (oscuro, blanco, favicon)

**Lo que obtienes:** Aplicación de marca consistente en todo el material visual que Claude crea: documentos, sitios web, presentaciones, diseños de UI.

### `/ai-dev-workflow`

Flujo de trabajo de desarrollo asistido por IA disciplinado con 7 pasos y 4 puertas de control humano. Hace que Claude actúe como un programador en par estructurado que aplica diseño *middle-out*, mantiene archivos de contexto vivos, ejecuta verificaciones de principios de diseño durante la descomposición e incluye un paso de endurecimiento de revisión de código antes de entregar.

Llevábamos trabajando así bastante tiempo, pero un [tweet de Eric Raymond](https://x.com/esrtweet/status/2019391670609940746) articuló el patrón tan bien que nos inspiró a formalizar nuestro flujo de trabajo en una habilidad reutilizable.

**Incluye:**

- SKILL.md -- flujo de trabajo de diseño *middle-out* con 7 pasos y 4 puertas de control humano
- `assets/design_notes_template.md` -- plantilla para la especificación de diseño dinámica
- `assets/code-reviewer-agent.md` -- plantilla empaquetada para el agente code-reviewer (usada en el Paso 7)
- `assets/reviewing-cli-command-skill.md` -- lista de verificación opcional de revisión de CLI para comandos Typer
- `references/plan_mode.md` -- guía de integración para el modo plan de Claude Code

**Lo que obtienes:** Sesiones de desarrollo estructuradas donde Claude redacta especificaciones, propone descomposiciones (validadas contra principios de diseño) e implementa un componente a la vez, deteniéndose en las puertas de control humano para validación. El Paso 7 ejecuta agentes de revisión de código en paralelo antes de entregar para capturar problemas transversales como consultas N+1, inconsistencias de nombrado y acoplamiento arquitectónico.

### `/rlm`

Procesa grandes bases de código (más de 100 archivos) utilizando el patrón Recursive Language Model (Modelo de Lenguaje Recursivo). En lugar de leer cada archivo en el contexto (lo que provoca degradación del contexto), esta habilidad orquesta subagentes paralelos que manejan una porción pequeña de la base de código y regresan con resúmenes.

**Incluye:**

- SKILL.md -- el protocolo RLM (Indexar, Mapear, Reducir) con modos Nativo y Estricto
- `scripts/rlm.py` -- script auxiliar para indexar, buscar y dividir archivos en fragmentos

**Lo que obtienes:** La capacidad de analizar, revisar o buscar bases de código completas sin degradar la calidad de razonamiento de Claude. Funciona bien junto con el agente `code-reviewer` para revisiones de código a gran escala.

> **Aviso de licencia:** Esta habilidad está adaptada de [rlm-skill de BowTiedSwan](https://github.com/BowTiedSwan/rlm-skill), que actualmente no especifica una licencia. Hemos atribuido el trabajo original y adaptado la implementación para el sistema de herramientas de Claude Code. Si usas esta habilidad, ten en cuenta que el estado de la licencia aguas arriba no está resuelto. Animamos a BowTiedSwan a agregar una licencia de código abierto explícita a su repositorio.

## Instalación

### Instalar habilidades

Copia cualquier carpeta de habilidad en el directorio `.claude/skills/` de tu proyecto:

```bash
cp -r skills/market-research /path/to/your/project/.claude/skills/
```

O en tus habilidades globales para usar en todos los proyectos:

```bash
cp -r skills/market-research ~/.claude/skills/
```

### Instalar agentes

Copia los archivos de agentes en tu directorio global `.claude/agents/`:

```bash
mkdir -p ~/.claude/agents
cp agents/code-reviewer.md ~/.claude/agents/
```

### Alternativa con enlaces simbólicos

Si prefieres mantenerte sincronizado con este repositorio:

```bash
git clone https://github.com/andremoreira73/Useful-Skills-from-lyfX.git
ln -s $(pwd)/Useful-Skills-from-lyfX/skills/market-research ~/.claude/skills/market-research
ln -s $(pwd)/Useful-Skills-from-lyfX/agents/code-reviewer.md ~/.claude/agents/code-reviewer.md
```

## Personalización

Estas habilidades y agentes están diseñados para adaptarse a tu flujo de trabajo:

- **market-research**: Edita `references/methodology.md` para que coincida con tu formato de entregables y preferencias de fuentes. Personaliza `assets/brief_template.md` para tu alcance de investigación.
- **linkedin-posts**: Actualiza las directrices de estilo en SKILL.md para que coincidan con tu voz y tono.
- **lyfx-corporate-design**: Reemplaza toda la habilidad con los colores, fuentes y activos de tu propia marca.
- **ai-dev-workflow**: Ajusta las puertas de control humano, el formato de especificación de componentes, la lista de principios de diseño o las convenciones de archivos del proyecto en SKILL.md para que coincidan con el ritmo de desarrollo de tu equipo. La plantilla empaquetada `code-reviewer-agent.md` puede personalizarse con criterios de revisión específicos del proyecto.
- **rlm**: Ajusta `EXCLUDE_DIRS` en `scripts/rlm.py` para que coincida con la estructura de directorios de tu proyecto. Ajusta `chunk_size` según las necesidades de tu ventana de contexto.
- **code-reviewer**: Agrega verificaciones específicas del proyecto, ajusta los principios de diseño relevantes para tu base de código o agrega secciones específicas de lenguaje además de Python.

## Acerca de lyfX.ai

[lyfX.ai](https://lyfx.ai) es una empresa de datos e IA con profunda experiencia en estas áreas, particularmente para aplicaciones en la fabricación. Creamos estas habilidades para agilizar nuestros propios flujos de trabajo empresariales con Claude Code, y las compartimos con la esperanza de que otros las encuentren útiles.

## Licencia

MIT -- úsalo como desees.
