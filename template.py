import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s]: %(message)s:"
)

project_name = "karup"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/agents/__init__.py",
    f"src/{project_name}/agents/supervisor/__init__.py",
    f"src/{project_name}/agents/specialist/__init__.py",
    f"src/{project_name}/orchestrator/__init__.py",
    f"src/{project_name}/workflows/__init__.py",
    f"src/{project_name}/tools/__init__.py",
    f"src/{project_name}/tools/base.py",
    f"src/{project_name}/tools/registry.py",
    f"src/{project_name}/tools/schemas.py",
    f"src/{project_name}/tools/permissions.py",
    f"src/{project_name}/tools/executor.py",
    f"src/{project_name}/mcp/__init__.py",
    f"src/{project_name}/mcp/client.py",
    f"src/{project_name}/mcp/registry.py",
    f"src/{project_name}/mcp/schemas.py",
    f"src/{project_name}/adapters/__init__.py",
    f"src/{project_name}/adapters/google/__init__.py",
    f"src/{project_name}/adapters/microsoft/__init__.py",
    f"src/{project_name}/adapters/github/__init__.py",
    f"src/{project_name}/adapters/aws/__init__.py",
    f"src/{project_name}/adapters/linkedin/__init__.py",
    f"src/{project_name}/adapters/messaging/__init__.py",
    f"src/{project_name}/memory/__init__.py",
    f"src/{project_name}/memory/working.py",
    f"src/{project_name}/memory/episodic.py",
    f"src/{project_name}/memory/semantic.py",
    f"src/{project_name}/memory/preferences.py",
    f"src/{project_name}/memory/identity.py",
    f"src/{project_name}/memory/retrieval.py",
    f"src/{project_name}/memory/store.py",

    f"src/{project_name}/domain/__init__.py",
    f"src/{project_name}/domain/models.py",
    f"src/{project_name}/domain/schemas.py",
    f"src/{project_name}/domain/state.py",
    f"src/{project_name}/domain/commands.py",
    f"src/{project_name}/domain/events.py",
    f"src/{project_name}/domain/exceptions.py",

    f"src/{project_name}/clients/__init__.py",
    f"src/{project_name}/clients/llm/__init__.py",
    f"src/{project_name}/clients/llm/openai.py",
    f"src/{project_name}/clients/llm/bedrock.py",
    f"src/{project_name}/clients/llm/router.py",
    f"src/{project_name}/clients/vector/__init__.py",
    f"src/{project_name}/clients/vector/client.py",
    f"src/{project_name}/clients/storage/__init__.py",
    f"src/{project_name}/clients/storage/s3.py",
    f"src/{project_name}/clients/storage/dynamodb.py",

    f"src/{project_name}/api/__init__.py",
    f"src/{project_name}/api/routes.py",
    f"src/{project_name}/api/health.py",
    f"src/{project_name}/api/dependencies.py",


    f"src/{project_name}/prompts/__init__.py",

    f"src/{project_name}/security/__init__.py",
    f"src/{project_name}/security/guardrails.py",
    f"src/{project_name}/security/authentication.py",
    f"src/{project_name}/security/authorization.py",
    f"src/{project_name}/security/secrets.py",


    f"src/{project_name}/observability/__init__.py",
    f"src/{project_name}/observability/logging.py",
    f"src/{project_name}/observability/metrics.py",
    f"src/{project_name}/observability/tracing.py",
    f"src/{project_name}/observability/prometheus.py",
    f"src/{project_name}/observability/llm_metrics.py",


    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/http.py",
    f"src/{project_name}/utils/retry.py",
    f"src/{project_name}/utils/idempotency.py",
    f"src/{project_name}/utils/response.py",
    f"src/{project_name}/utils/time.py",


    "config/__init__.py",
    "config/settings.py",
    "config/config.yaml",
    "params.yaml",

 
    "deployment/lambda/chat/__init__.py",
    "deployment/lambda/chat/handler.py",
    "deployment/lambda/ingestion/__init__.py",
    "deployment/lambda/ingestion/handler.py",
    "deployment/lambda/scheduler/__init__.py",
    "deployment/lambda/scheduler/handler.py",

  
    "infra/main.tf",
    "infra/provider.tf",
    "infra/variables.tf",
    "infra/outputs.tf",
    "infra/terraform.tfvars",

   
    "infra/modules/networking/.gitkeep",
    "infra/modules/iam/.gitkeep",
    "infra/modules/ecs/.gitkeep",
    "infra/modules/ecr/.gitkeep",
    "infra/modules/lambda/.gitkeep",
    "infra/modules/s3/.gitkeep",
    "infra/modules/dynamodb/.gitkeep",
    "infra/modules/secrets/.gitkeep",
    "infra/modules/cloudwatch/.gitkeep",
    "infra/modules/monitoring/.gitkeep",

    
    "infra/environments/dev/.gitkeep",
    "infra/environments/prod/.gitkeep",

 
    "monitoring/prometheus/prometheus.yml",
    "monitoring/prometheus/recording_rules.yml",
    "monitoring/grafana/dashboards/.gitkeep",
    "monitoring/grafana/provisioning/.gitkeep",
    "monitoring/alerts/alert_rules.yml",


    "tests/unit/agents/__init__.py",
    "tests/unit/orchestrator/__init__.py",
    "tests/unit/workflows/__init__.py",
    "tests/unit/tools/__init__.py",
    "tests/unit/memory/__init__.py",
    "tests/unit/services/__init__.py",
    "tests/unit/domain/__init__.py",
    "tests/unit/security/__init__.py",

    "tests/integration/api/__init__.py",
    "tests/integration/aws/__init__.py",
    "tests/integration/google/__init__.py",
    "tests/integration/microsoft/__init__.py",
    "tests/integration/github/__init__.py",
    "tests/integration/mcp/__init__.py",

    "tests/e2e/workflows/__init__.py",
    "tests/e2e/agent/__init__.py",

    "tests/evaluation/datasets/.gitkeep",
    "tests/evaluation/agent_eval.py",
    "tests/evaluation/tool_eval.py",
    "tests/evaluation/regression.py",

    "tests/fixtures/__init__.py",

    "scripts/setup.sh",
    "scripts/test.sh",
    "scripts/lint.sh",
    "scripts/build.sh",
    "scripts/deploy.sh",
    "project.toml",
    "setup.py",
    "Dockerfile",
    ".dockerignore",
    ".gitignore",
    "README.md",
    "main.py",
    "app.py",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir = filepath.parent
    filename = filepath.name

    if filedir != Path("."):
        filedir.mkdir(parents=True, exist_ok=True)
        logging.info(
            f"Creating directory: {filedir} for file: {filename}"
        )

    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")