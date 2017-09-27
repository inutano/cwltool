# Stubs for galaxy.tools.deps.resolvers.tool_shed_packages (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from .galaxy_packages import BaseGalaxyPackageDependencyResolver
from .resolver_mixins import UsesInstalledRepositoriesMixin

class ToolShedPackageDependencyResolver(BaseGalaxyPackageDependencyResolver, UsesInstalledRepositoriesMixin):
    resolver_type = ...  # type: str
    dependency_type = ...  # type: Any
    resolves_simple_dependencies = ...  # type: bool
    def __init__(self, dependency_manager, **kwds) -> None: ...
