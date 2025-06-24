from api import api_get

from mcp_instance import mcp


@mcp.resource("mcp://aiApplications")
def list_ai_applications() -> list:
    """
    Retrieves all projects in your organization that are utilizing AI technologies.

    This resource provides a detailed inventory of AI model usage across your codebase,
    including:
    - Affected project information (projectId, repoName, moduleName, buildSystemType, isArchived, tags)
    - Model usage information (provider, model name, version, license)
    - File path and line number where the AI model is invoked
    - Direct source code links for traceability
    - Security classification of the usage (SAFE, REMOTE, UNSAFE)
    - Flags for potential insecure serialization (e.g. pickle usage)

    Use this to:
    - Track AI adoption and model integrations across teams
    - Support security audits and governance initiatives
    - Understand where and how AI is being applied in your ecosystem
    - Rapidly investigate security classifications and code impact

    Returns:
        A list of `ProjectAiModelUsage` records representing AI usage across projects.
    """
    return api_get("/v1/ai/usages")


@mcp.resource("mcp://aiModelInfo/{provider}/{modelName}")
def fetch_ai_model_metadata(provider: str, modelName: str) -> dict:
    """
    Fetches detailed metadata for a specific AI model provided by a given AI provider.

    This resource provides a detailed inventory of AI model usage across your codebase,
    including:
    - Model usage information (provider, model name, version, license)
    - File path and line number where the AI model is invoked
    - Direct source code links for traceability
    - Security classification of the usage (SAFE, REMOTE, UNSAFE)
    - Flags for potential insecure serialization (e.g. pickle usage)


    Use this to:
    - Perform deep inspection of model choices in your stack
    - Power internal model registries or explainability tools
    - Support security reviews for model-specific concerns

    Args:
        provider (str): The name of the AI provider (e.g., OPENAI, HUGGINGFACE, CLAUDE, GEMINI)
        modelName (str): The specific model name to inspect (e.g., gpt-4, llama-2-7b)

    Returns:
        A `ModelInfo` object describing the requested AI model in detail.
    """
    return api_get(f"/v1/ai/providers/{provider}/models?name={modelName}")