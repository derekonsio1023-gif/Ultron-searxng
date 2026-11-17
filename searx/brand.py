# SPDX-License-Identifier: AGPL-3.0-or-later
"""Implementations needed for a branding of SearXNG."""

# pylint: disable=too-few-public-methods

# Struct fields aren't discovered in Python 3.14
# - https://github.com/searxng/searxng/issues/5284
from __future__ import annotations

__all__ = ["SettingsBrand"]

import msgspec


class BrandCustom(msgspec.Struct, kw_only=True, forbid_unknown_fields=True):
    """Custom settings in the brand section."""

    links: dict[str, str] = {}
    """Custom entries in the footer of the WEB page: ``[title]: [link]``"""


class ThemeColors(msgspec.Struct, kw_only=True, forbid_unknown_fields=True):
    """Custom settings for theme colors in the brand section."""

    # --- Paleta NEON AZUL futurista (Ultron) ---
    theme_color_light: str = "#0066ff"        # Azul eléctrico principal (tema claro)
    background_color_light: str = "#f0f8ff"   # Azul hielo muy suave (AliceBlue)
    theme_color_dark: str = "#00d9ff"         # Cian neón brillante (tema oscuro)
    background_color_dark: str = "#0a0e1a"    # Azul espacial profundo
    theme_color_black: str = "#00d9ff"        # Cian neón (tema negro)
    background_color_black: str = "#000000"   # Negro puro


class SettingsBrand(msgspec.Struct, kw_only=True, forbid_unknown_fields=True):
    """Options for configuring brand properties.

    .. code:: yaml

       brand:
         issue_url: https://github.com/searxng/searxng/issues
         docs_url: https://docs.searxng.org
         public_instances: https://searx.space
         wiki_url: https://github.com/searxng/searxng/wiki

         custom:
           links:
             Uptime: https://uptime.searxng.org/history/example-org
             About: https://example.org/user/about.html
    """

    # --- URLs apuntando a tu fork "Ultron" ---
    issue_url: str = "https://github.com/derekonsio1023-gif/Ultron-searxng/issues"
    """If you host your own issue tracker change this URL."""

    docs_url: str = "https://docs.searxng.org"
    """If you host your own documentation change this URL."""

    public_instances: str = "https://searx.space"
    """If you host your own https://searx.space change this URL."""

    wiki_url: str = "https://github.com/derekonsio1023-gif/Ultron-searxng/searxng/wiki"
    """Link to your wiki (or ``false``)"""

    custom: BrandCustom = msgspec.field(default_factory=BrandCustom)
    """Optional customizing.

    .. autoclass:: searx.brand.BrandCustom
       :members:
    """

    pwa_colors: ThemeColors = msgspec.field(default_factory=ThemeColors)
    """Custom settings for PWA colors."""

    # new_issue_url is a hackish solution tailored for only one hoster (GH).  As
    # long as we don't have a more general solution, we should support it in the
    # given function, but it should not be expanded further.

    new_issue_url: str = "https://github.com/derekonsio1023-gif/Ultron-searxng/issues/new"
    """If you host your own issue tracker not on GitHub, then unset this URL.

    Note: This URL will create a pre-filled GitHub bug report form for an
    engine.  Since this feature is implemented only for GH (and limited to
    engines), it will probably be replaced by another solution in the near
    future.
    """
