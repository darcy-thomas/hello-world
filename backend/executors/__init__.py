"""Hello World node executor."""

from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)


class HelloWorldExecutor:
    """Executor for the Hello World node."""

    @staticmethod
    async def execute(inputs: Dict[str, Any], config: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the hello world node.

        Args:
            inputs: Input data (not used in this simple example)
            config: Node configuration (not used)

        Returns:
            Dictionary with the output message
        """
        logger.info("Executing Hello World node")

        # Simple output
        output = {
            "message": "Hello, World!",
            "status": "success"
        }

        logger.info("Hello World node completed successfully")
        return output
