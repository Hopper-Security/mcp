from api import api_get

from mcp_instance import mcp


@mcp.resource("mcp://vulnerabilityStats")
def get_vulnerabilities_stats() -> dict:
    """
    Retrieves aggregated statistics about vulnerabilities across all projects in the tenant's environment.

    Returns a comprehensive overview of the security posture including:
    - Total vulnerability count across all projects
    - Severity breakdown (Critical, High, Medium, Low)
    - Status metrics (New, In Progress, Resolved, Ignored)
    - Trend data showing historical vulnerability metrics
    - Top vulnerable projects list
    - Remediation metrics (average time to fix, remediation rate)

    This resource is useful for:
    - Generating executive dashboards showing overall security posture
    - Tracking vulnerability trends across the organization
    - Identifying projects requiring immediate security attention
    - Measuring effectiveness of security initiatives over time

    Returns:
        dict: A dictionary containing vulnerability statistics and metrics
    """
    return api_get("/v1/vulnerabilities/projects/stats")


@mcp.resource("mcp://vulnerability.searchIssues")
def search_vulnerability_issues() -> dict:
    """
    Retrieves detailed information about individual vulnerability issues across all projects.

    The returned data includes comprehensive details for each vulnerability:
    - Unique identifier and standard vulnerability ID (CVE, GHSA, etc.)
    - Affected project and package information
    - Severity rating and CVSS score
    - Detailed vulnerability description
    - Remediation status and suggested fix path
    - Reachability status and evidence
    - Detection dates and references

    This resource supports filtering by project, severity, status, CVE ID, affected package,
    and other parameters through the API endpoint.

    This resource is useful for:
    - Search for specific CVEs (e.g., to answer: "Am I impacted by CVE-123-456?")
    - Filter vulnerabilities by severity, affected package, or project (client-side)
    - Generate detailed vulnerability reports
    - Generating detailed vulnerability reports for security teams
    - Prioritizing remediation efforts based on severity and reachability
    - Tracking status of specific vulnerability issues
    - Performing targeted searches for specific types of vulnerabilities
    - Exporting vulnerability data for compliance reporting

    Returns:
        dict: A dictionary containing detailed vulnerability issues data
    """
    return api_get("/v1/vulnerabilities/issues")


@mcp.resource("mcp://vulnerability.issueReachability/{projectId}/{issueId}")
def get_vulnerability_reachability(projectId: int, issueId: int) -> dict:
    """
    Retrieves reachability analysis for a specific vulnerability issue in a given project.

    This analysis helps determine whether the vulnerable code path is actually reachable
    within the context of the project’s runtime, which can be used to prioritize triage and remediation.

    Args:
        projectId (int): The ID of the project.
        issueId (int): The ID of the vulnerability issue.

    This resource is useful for:
    - Showing evidence for reachable vulnerabilities(e.g., to answer: "Show me the evidence")


    Returns:
        dict: Reachability analysis result for the specific issue.
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
    - Setting up automated alerts for approaching SLA deadlines
    - Configuring reporting tools to highlight SLA violations
    - Establishing governance frameworks for security operations

    Returns:
        dict: A dictionary containing the SLA configuration parameters for the current tenant
    """
    return api_get("/v1/sla/config")
