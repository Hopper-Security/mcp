from api import api_get

from mcp_instance import mcp


@mcp.resource("mcp://licenseInventory")
def list_effective_open_source_licenses() -> list:
    """
    Retrieves the full inventory of effective open source licenses in your organization.

    This resource returns all licenses detected across your tenant's codebase, including:
    - Custom and standard license identifiers
    - Full license names and reference links
    - Osi approved and fsfFree flags
    - Severity classification from your policy (e.g., APPROVED, POTENTIAL_RISK, DENIED)
    - Effective license objects resolved for your current configuration

    Useful for:
    - Understanding your organization's licensing footprint
    - List all licenses detected across your tenant's codebase

    Returns:
        A list of EffectiveOpenSourceLicense records representing all licenses in use
    """
    return api_get("/v1/licenses")


@mcp.resource("mcp://licenseProjects")
def summarize_license_compliance_by_project() -> list:
    """
    Retrieves license compliance statistics across all projects in your organization.

    This resource summarizes the current license status of each project, including:
    - Affected project information (projectId, repoName, moduleName, buildSystemType, isArchived, tags)
    - Issue stats counts grouped by severity (APPROVED, POTENTIAL_RISK, DENIED)

    Especially useful for:
    - Visualizing compliance at a project level
    - Prioritizing remediation based on license risk exposure
    - Tracking improvement over time for governance reporting

    Returns:
        A list of ProjectLicenseIssueStats for each scanned project
    """
    return api_get("/v1/licenses/projects/stats")


@mcp.resource("mcp://projectLicenseDetails/{project_id}")
def get_detailed_project_license_issues(project_id: int) -> dict:
    """
    Retrieves detailed license issues and dependencies for a specific project.

    This resource provides a deep view of the licensing landscape within a single project, including:
    - Affected project information (projectId, repoName, moduleName, buildSystemType, isArchived, tags)
    - All dependencies (direct and transitive)
    - Their associated licenses and severity classifications
    - Package metadata (e.g., package URL)

    Helpful for:
    - Auditing and remediating specific project license issues
    - Understanding transitive license risks
    - Preparing due diligence or legal disclosures

    Args:
        project_id (int): The unique ID of the project

    Returns:
        A ProjectLicenseIssues object with project metadata and detailed dependency license information
    """
    return api_get(f"/v1/licenses/projects/{project_id}")


@mcp.resource("mcp://licensePolicies")
def list_license_policies() -> list:
    """
    Retrieves all license policies configured in your organization.

    This includes:
    - License severity mappings (e.g., APPROVED, POTENTIAL_RISK, DENIED)
    - Rule definitions per policy
    - Policy groupings and their IDs

    Useful for:
    - Governance reviews and audits
    - Verify all policies
    - Ensuring consistent policy enforcement across modules
    - Building developer guidance or internal license rulebooks

    Returns:
        A list of TenantLicensePolicy objects
    """
    return api_get("/v1/licenses/policies")
