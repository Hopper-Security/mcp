from src.api import api_get

from src.mcp_instance import mcp


@mcp.resource("mcp://vulnerabilityStats")
def get_vulnerabilities_stats() -> dict:
    """

    Retrieves aggregated statistics about vulnerabilities across all projects in the tenant's environment.

    Returns a comprehensive overview of the security posture including:
    - Total vulnerability count across all projects
    - Severity breakdown (Critical, High, Medium, Low)
    - Project information (projectId, repoName, moduleName, buildSystemType, isArchived, tags)

    This resource is useful for:
    - Tracking vulnerability stats across the organization
    - Identifying projects requiring immediate security attention
    - Generating security posture dashboards

    Returns:
        A list of VulnerabilityProject objects, each containing project metadata and vulnerability statistics
    """
    return api_get("/v1/vulnerabilities/projects/stats")


@mcp.resource("mcp://vulnerability.searchIssues")
def search_vulnerability_issues() -> dict:
    """
    Retrieves detailed information about vulnerability issues across all projects.

    The returned data includes comprehensive details for each vulnerability:
    - Affected project information (projectId, repoName, moduleName, buildSystemType, isArchived, tags)
    - Unique identifier and standard vulnerability ID (CVE, GHSA, etc.)
    - Affected package information including version and dependency depth
    - Severity rating and CVSS score
    - EPSS score when available
    - Detailed vulnerability description and CWE types
    - Remediation status and suggested fix path
    - Reachability verdict (REACHABLE, UNREACHABLE, UNKNOWN, POTENTIALLY_REACHABLE)
    - Detection dates and issue tracking tickets

    This resource is useful for:
    - Searching for specific CVEs (e.g., to answer: "Am I impacted by CVE-123-456?")
    - Filtering vulnerabilities by severity, affected package, or project
    - Generating detailed vulnerability reports for security teams
    - Prioritizing remediation efforts based on severity and reachability
    - Tracking status of specific vulnerability issues
    - Exporting vulnerability data for compliance reporting

    Returns:
        A list of ProjectIssue objects containing detailed vulnerability data
    """
    return api_get("/v1/vulnerabilities/issues")


@mcp.resource("mcp://vulnerability.issueReachability/{projectId}/{issueId}")
def get_vulnerability_reachability(projectId: int, issueId: int) -> dict:
    """
    Retrieves reachability analysis for a specific vulnerability issue in a given project.

    This analysis helps determine whether the vulnerable code path is actually reachable
    within the context of the project's runtime, which can be used to prioritize triage and remediation.

    The returned data includes:
    - Evidence in the form of a call graph path when available
    - Method-level details with package names and method signatures
    - Source code links when available

    Args:
        projectId (int): The ID of the project containing the vulnerability
        issueId (int): The ID of the vulnerability issue to analyze

    This resource is useful for:
    - Determining if a vulnerability is exploitable in your specific codebase
    - Prioritizing remediation based on actual risk exposure
    - Showing evidence for reachable vulnerabilities
    - Understanding the exact code paths that lead to vulnerable methods

    Returns:
        ReachabilityAnalysis object containing verdict and evidence data
    """
    return api_get(f"/v1/vulnerabilities/projects/{projectId}/issues/{issueId}/reachability")


@mcp.resource("mcp://slaConfig")
def get_sla_config() -> dict:
    """
    Retrieves the Service Level Agreement (SLA) configuration for the current tenant.

    The SLA configuration defines the expected resolution timeframes (in days) for vulnerabilities
    based on their severity level (Critical, High, Medium, Low) and reachability status (Reachable, Unreachable).

    Returns a comprehensive configuration object containing:
    - criticalReachableDays: Maximum days to resolve Critical severity reachable vulnerabilities
    - highReachableDays: Maximum days to resolve High severity reachable vulnerabilities
    - mediumReachableDays: Maximum days to resolve Medium severity reachable vulnerabilities
    - lowReachableDays: Maximum days to resolve Low severity reachable vulnerabilities
    - criticalUnreachableDays: Maximum days to resolve Critical severity unreachable vulnerabilities
    - highUnreachableDays: Maximum days to resolve High severity unreachable vulnerabilities
    - mediumUnreachableDays: Maximum days to resolve Medium severity unreachable vulnerabilities
    - lowUnreachableDays: Maximum days to resolve Low severity unreachable vulnerabilities

    If no SLA configuration exists for the tenant, a default configuration with null values is returned.

    This resource is useful for:
    - Displaying SLA timeframes in vulnerability management dashboards
    - Calculating compliance metrics for vulnerability remediation
    - Configuring reporting tools to highlight SLA violations
    - Establishing governance frameworks for security operations

    Returns:
         A SlaConfig object containing the SLA configuration parameters for the current tenant
    """
    return api_get("/v1/sla/config")
