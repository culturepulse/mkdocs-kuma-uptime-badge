"""
Tests for the MkDocs Uptime Badge Plugin.
"""

from mkdocs.config.defaults import MkDocsConfig

from uptime_badge.plugin import UptimeBadgePlugin


def test_simple_case():
    """Test a simple badge replacement."""
    plugin = UptimeBadgePlugin()
    plugin.config = {'base_url': 'https://kuma.intra'}
    plugin.on_config(MkDocsConfig())
    
    markdown = "Check our status: {{uptime id=1}}"
    expected = "Check our status: ![status](https://kuma.intra/api/badge/1/status)"
    
    result = plugin.on_page_markdown(markdown)
    assert result == expected


def test_multiple_tags_per_page():
    """Test multiple badge replacements in a single page."""
    plugin = UptimeBadgePlugin()
    plugin.config = {'base_url': 'https://kuma.intra'}
    plugin.on_config(MkDocsConfig())
    
    markdown = """
# Status Page

Main service: {{uptime id=1}}
API: {{uptime id=2 type=uptime hours=24}}
Database: {{uptime id=3 type=ping hours=24}}
"""
    expected = """
# Status Page

Main service: ![status](https://kuma.intra/api/badge/1/status)
API: ![uptime](https://kuma.intra/api/badge/2/uptime/24)
Database: ![ping](https://kuma.intra/api/badge/3/ping/24)
"""
    
    result = plugin.on_page_markdown(markdown)
    assert result == expected


def test_missing_hours():
    """Test badge types that need hours but don't have them specified."""
    plugin = UptimeBadgePlugin()
    plugin.config = {'base_url': 'https://kuma.intra'}
    plugin.on_config(MkDocsConfig())
    
    markdown = "Uptime: {{uptime id=1 type=uptime}}"
    expected = "Uptime: ![uptime](https://kuma.intra/api/badge/1/uptime)"
    
    result = plugin.on_page_markdown(markdown)
    assert result == expected


def test_unsafe_characters_in_params():
    """Test handling of unsafe characters in parameters."""
    plugin = UptimeBadgePlugin()
    plugin.config = {'base_url': 'https://kuma.intra'}
    plugin.on_config(MkDocsConfig())
    
    markdown = 'Status: {{uptime id=1 upLabel="Service & API" downLabel="Down & Out"}}'
    expected = 'Status: ![status](https://kuma.intra/api/badge/1/status?upLabel=Service+%26+API&downLabel=Down+%26+Out)'
    
    result = plugin.on_page_markdown(markdown)
    assert result == expected


def test_badge_types_without_hours():
    """Test badge types that don't use hours parameter."""
    plugin = UptimeBadgePlugin()
    plugin.config = {'base_url': 'https://kuma.intra'}
    plugin.on_config(MkDocsConfig())
    
    markdown = """
Status: {{uptime id=1 type=status}}
Certificate: {{uptime id=2 type=cert-exp}}
"""
    expected = """
Status: ![status](https://kuma.intra/api/badge/1/status)
Certificate: ![cert-exp](https://kuma.intra/api/badge/2/cert-exp)
"""
    
    result = plugin.on_page_markdown(markdown)
    assert result == expected


def test_custom_base_url():
    """Test using a custom base URL."""
    plugin = UptimeBadgePlugin()
    plugin.config = {'base_url': 'https://custom.example.com'}
    plugin.on_config(MkDocsConfig())
    
    markdown = "Status: {{uptime id=1}}"
    expected = "Status: ![status](https://custom.example.com/api/badge/1/status)"
    
    result = plugin.on_page_markdown(markdown)
    assert result == expected


def test_no_match():
    """Test that markdown without uptime tags is returned unchanged."""
    plugin = UptimeBadgePlugin()
    plugin.config = {'base_url': 'https://kuma.intra'}
    plugin.on_config(MkDocsConfig())
    
    markdown = "# No uptime tags here\n\nJust regular markdown content."
    
    result = plugin.on_page_markdown(markdown)
    assert result == markdown


def test_quoted_values():
    """Test handling of quoted values in parameters."""
    plugin = UptimeBadgePlugin()
    plugin.config = {'base_url': 'https://kuma.intra'}
    plugin.on_config(MkDocsConfig())
    
    markdown = 'Label: {{uptime id=1 label="Response Time" labelSuffix="ms"}}'
    expected = 'Label: ![status](https://kuma.intra/api/badge/1/status?label=Response+Time&labelSuffix=ms)'
    
    result = plugin.on_page_markdown(markdown)
    assert result == expected


def test_missing_id():
    """Test that tags without an ID are left unchanged."""
    plugin = UptimeBadgePlugin()
    plugin.config = {'base_url': 'https://kuma.intra'}
    plugin.on_config(MkDocsConfig())
    
    markdown = "Invalid: {{uptime type=status}}"
    
    result = plugin.on_page_markdown(markdown)
    assert result == markdown