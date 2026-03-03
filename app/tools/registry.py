from mcp.server.fastmcp import FastMCP
from app.services.search_service import perform_search
from app.services.email_service import send_email_service

def register_tools(mcp: FastMCP):

    @mcp.tool()
    async def web_search(query: str) -> str:
        """Search the web for up-to-date information."""
        try:
            return await perform_search(query)
        except Exception as e:
            return f"Error while searching: {str(e)}"

    @mcp.tool()
    async def send_email(to: str, subject: str, body: str) -> str:
        """
            Send an email to a recipient.

            Parameters:
            - to: recipient email address
            - subject: short email subject line
            - body: full message content

            Returns:
            Confirmation message after sending.
        """
        try:
            return await send_email_service(to, subject, body)
        except Exception as e:
            return f"Error while sending email: {str(e)}"