from zope.interface import Interface
from plone.theme.interfaces import IDefaultPloneLayer

class IThemeSpecific(IDefaultPloneLayer):
    """theme-specific layer"""


class IEmSkinLayer(Interface):
    """Marker interface for browserlayer."""
