from kubiya_sdk.tools import Arg
from .base import AWSCliTool
from kubiya_sdk.tools.registry import tool_registry

aws_cli_tool = AWSCliTool(
    name="aws_cli",
    description="Executes AWS CLI commands",
    content="aws {{ .command}}",
    args=[
        Arg(name="command",
            type="str",
            description="The AWS CLI command to execute. Do not use `AWS`, only enter its command.",
            required=True),
    ],
)

tool_registry.register("aws_cli", aws_cli_tool)
