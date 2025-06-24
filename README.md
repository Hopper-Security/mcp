# MCP Project (Hopper Security API Client)

## Overview

MCP (Master Control Program) is a client application for the Hopper Security API that provides access to security-related information about your codebase. It serves as a bridge between your applications and Hopper Security's platform, exposing various security resources through a simple interface.

The project uses the FastMCP framework to create a server that exposes resources for:

- **License Compliance**: Track open source licenses, compliance by project, and license policies
- **Vulnerability Management**: Monitor security vulnerabilities, their reachability, and SLA configurations
- **AI Usage Tracking**: Identify AI technologies used across your projects and fetch AI model metadata


## Configuration

The application requires the following configuration:

1. **JWT Token**: You need to set the `JWT` environment variable with a valid JWT token for authenticating with the Hopper Security API:
   ```bash
   export JWT=your_jwt_token_here
   ```

2. **API URL**: By default, the application connects to `https://api-main.prod.hopper.security`. If you need to use a different API endpoint, modify the `API_URL` in `config.py`.


## Available Resources

#### License Resources

- `mcp://licenseInventory`: List all effective open source licenses in your organization
- `mcp://licenseProjects`: Summarize license compliance by project
- `mcp://projectLicenseDetails/{project_id}`: Get detailed license issues for a specific project
- `mcp://licensePolicies`: List all license policies configured in your organization

#### Vulnerability Resources

- `mcp://vulnerabilityStats`: Get aggregated statistics about vulnerabilities across all projects
- `mcp://vulnerability.searchIssues`: Search for vulnerability issues across all projects
- `mcp://vulnerability.issueReachability/{projectId}/{issueId}`: Get reachability analysis for a specific vulnerability
- `mcp://slaConfig`: Get the SLA configuration for vulnerability resolution timeframes

#### AI Resources

- `mcp://aiApplications`: List all projects utilizing AI technologies
- `mcp://aiModelInfo/{provider}/{modelName}`: Fetch detailed metadata for a specific AI model


## License

This project is proprietary software owned by Hopper Security.

## Support

For questions or issues related to this project, please contact Hopper Security support.
