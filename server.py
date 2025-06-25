from src.mcp_instance import mcp

# pylint: disable=unused-import
import src.licenses
import src.vulnerabilities
import src.ai
# pylint: enable=unused-import

if __name__ == "__main__":
    mcp.run()
