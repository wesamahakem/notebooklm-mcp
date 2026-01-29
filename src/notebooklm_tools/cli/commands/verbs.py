"""Verb-first CLI commands for NotebookLM Tools.

This module provides alternative command structure:
- nlm create notebook "Title"  (vs nlm notebook create "Title")
- nlm list notebooks           (vs nlm notebook list)
- nlm delete notebook <id>     (vs nlm notebook delete <id>)

Both command structures coexist for user flexibility.
"""

from typing import Optional

import typer

# Import existing command implementations
from notebooklm_tools.cli.commands.notebook import (
    create_notebook,
    list_notebooks,
    get_notebook,
    describe_notebook,
    rename_notebook,
    delete_notebook,
    query_notebook,
)
from notebooklm_tools.cli.commands.source import (
    list_sources,
    add_source,
    get_source,
    describe_source,
    get_source_content,
    delete_source,
    list_stale_sources,
    sync_sources,
)
from notebooklm_tools.cli.commands.studio import (
    studio_status,
    studio_delete,
    create_audio,
    create_video,
    create_report,
    create_infographic,
    create_slides,
    create_quiz,
    create_flashcards,
    create_data_table,
    create_mindmap,
)
from notebooklm_tools.cli.commands.research import (
    start_research,
    research_status,
    import_research,
)
from notebooklm_tools.cli.commands.chat import (
    configure_chat,
)
from notebooklm_tools.cli.commands.download import (
    download_audio,
    download_video,
    download_report,
    download_mind_map,
    download_slide_deck,
    download_infographic,
    download_data_table,
)
from notebooklm_tools.cli.commands.alias import (
    set_alias,
    get_alias,
    list_aliases,
    delete_alias,
)
from notebooklm_tools.cli.commands.config import (
    show_config,
    get_config_value,
    set_config_value,
)
from notebooklm_tools.cli.commands.skill import (
    install as skill_install,
    uninstall as skill_uninstall,
    list_tools as skill_list,
    show as skill_show,
)

# =============================================================================
# CREATE verb
# =============================================================================

create_app = typer.Typer(help="Create resources (notebooks, audio, video, etc)")


@create_app.command("notebook")
def create_notebook_verb(
    title: str = typer.Argument(..., help="Notebook title"),
) -> None:
    """Create a new notebook."""
    create_notebook(title)


@create_app.command("audio")
def create_audio_verb(
    notebook: str = typer.Argument(..., help="Notebook ID or alias"),
    length: Optional[str] = typer.Option(None, "--length", "-l", help="Audio length (short/medium)"),
    format_opt: Optional[str] = typer.Option(None, "--format", "-f", help="Audio format (mp3)"),
    confirm: bool = typer.Option(False, "--confirm", "-y", help="Skip confirmation prompt"),
) -> None:
    """Create an audio overview."""
    create_audio(notebook, length, format_opt, confirm)


@create_app.command("video")
def create_video_verb(
    notebook: str = typer.Argument(..., help="Notebook ID or alias"),
    style: Optional[str] = typer.Option(None, "--style", "-s", help="Video style"),
    format_opt: Optional[str] = typer.Option(None, "--format", "-f", help="Video format"),
    confirm: bool = typer.Option(False, "--confirm", "-y", help="Skip confirmation prompt"),
) -> None:
    """Create a video overview."""
    create_video(notebook, style, format_opt, confirm)


@create_app.command("report")
def create_report_verb(
    notebook: str = typer.Argument(..., help="Notebook ID or alias"),
    report_type: Optional[str] = typer.Option(None, "--type", "-t", help="Report type (briefing-doc/study-guide/blog)"),
    confirm: bool = typer.Option(False, "--confirm", "-y", help="Skip confirmation prompt"),
) -> None:
    """Create a report."""
    create_report(notebook, report_type, confirm)


@create_app.command("infographic")
def create_infographic_verb(
    notebook: str = typer.Argument(..., help="Notebook ID or alias"),
    orientation: Optional[str] = typer.Option(None, "--orientation", "-o", help="Orientation (landscape/portrait)"),
    detail: Optional[str] = typer.Option(None, "--detail", "-d", help="Detail level"),
    confirm: bool = typer.Option(False, "--confirm", "-y", help="Skip confirmation prompt"),
) -> None:
    """Create an infographic."""
    create_infographic(notebook, orientation, detail, confirm)


@create_app.command("slides")
def create_slides_verb(
    notebook: str = typer.Argument(..., help="Notebook ID or alias"),
    length: Optional[str] = typer.Option(None, "--length", "-l", help="Length (short/medium/long)"),
    format_opt: Optional[str] = typer.Option(None, "--format", "-f", help="Format (pdf)"),
    confirm: bool = typer.Option(False, "--confirm", "-y", help="Skip confirmation prompt"),
) -> None:
    """Create a slide deck."""
    create_slides(notebook, length, format_opt, confirm)


@create_app.command("quiz")
def create_quiz_verb(
    notebook: str = typer.Argument(..., help="Notebook ID or alias"),
    difficulty: Optional[str] = typer.Option(None, "--difficulty", "-d", help="Difficulty (easy/medium/hard)"),
    quantity: Optional[str] = typer.Option(None, "--quantity", "-q", help="Number of questions"),
    confirm: bool = typer.Option(False, "--confirm", "-y", help="Skip confirmation prompt"),
) -> None:
    """Create a quiz."""
    create_quiz(notebook, difficulty, quantity, confirm)


@create_app.command("flashcards")
def create_flashcards_verb(
    notebook: str = typer.Argument(..., help="Notebook ID or alias"),
    difficulty: Optional[str] = typer.Option(None, "--difficulty", "-d", help="Difficulty level"),
    confirm: bool = typer.Option(False, "--confirm", "-y", help="Skip confirmation prompt"),
) -> None:
    """Create flashcards."""
    create_flashcards(notebook, difficulty, confirm)


@create_app.command("data-table")
def create_data_table_verb(
    notebook: str = typer.Argument(..., help="Notebook ID or alias"),
    description: str = typer.Argument(..., help="Description of the data table to create"),
    confirm: bool = typer.Option(False, "--confirm", "-y", help="Skip confirmation prompt"),
) -> None:
    """Create a data table."""
    create_data_table(notebook, description, confirm)


@create_app.command("mindmap")
def create_mindmap_verb(
    notebook: str = typer.Argument(..., help="Notebook ID or alias"),
    title: Optional[str] = typer.Option("Mind Map", "--title", "-t", help="Mind map title"),
    confirm: bool = typer.Option(False, "--confirm", "-y", help="Skip confirmation prompt"),
) -> None:
    """Create a mind map."""
    create_mindmap(notebook, title, confirm)


# =============================================================================
# LIST verb
# =============================================================================

list_app = typer.Typer(help="List resources (notebooks, sources, artifacts)")


@list_app.command("notebooks")
def list_notebooks_verb() -> None:
    """List all notebooks."""
    list_notebooks()


@list_app.command("sources")
def list_sources_verb(
    notebook: str = typer.Argument(..., help="Notebook ID or alias"),
    json_output: bool = typer.Option(False, "--json", help="Output as JSON"),
) -> None:
    """List sources in a notebook."""
    list_sources(notebook, json_output)


@list_app.command("artifacts")
def list_artifacts_verb(
    notebook: str = typer.Argument(..., help="Notebook ID or alias"),
    full: bool = typer.Option(False, "--full", "-a", help="Show all details"),
) -> None:
    """List all studio artifacts."""
    studio_status(notebook, full)


@list_app.command("aliases")
def list_aliases_verb() -> None:
    """List all aliases."""
    list_aliases()


@list_app.command("stale-sources")
def list_stale_sources_verb(
    notebook: str = typer.Argument(..., help="Notebook ID or alias"),
    json_output: bool = typer.Option(False, "--json", help="Output as JSON"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """List Drive sources that need syncing."""
    list_stale_sources(notebook, json_output, profile)


@list_app.command("skills")
def list_skills_verb() -> None:
    """List available skills and installation status."""
    skill_list()


# =============================================================================
# GET verb
# =============================================================================

get_app = typer.Typer(help="Get details about resources")


@get_app.command("notebook")
def get_notebook_verb(
    notebook: str = typer.Argument(..., help="Notebook ID or alias"),
    json_output: bool = typer.Option(False, "--json", help="Output as JSON"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Get notebook details."""
    get_notebook(notebook, json_output, profile)


@get_app.command("source")
def get_source_verb(
    source: str = typer.Argument(..., help="Source ID"),
    json_output: bool = typer.Option(False, "--json", help="Output as JSON"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Get source details."""
    get_source(source, json_output, profile)


@get_app.command("config")
def get_config_verb(
    key: str = typer.Argument(..., help="Configuration key (e.g. output.format)"),
) -> None:
    """Get configuration value."""
    get_config_value(key)


@get_app.command("alias")
def get_alias_verb(
    name: str = typer.Argument(..., help="Alias name"),
) -> None:
    """Get alias value."""
    get_alias(name)


# =============================================================================
# DELETE verb
# =============================================================================

delete_app = typer.Typer(help="Delete resources (notebooks, sources, artifacts)")


@delete_app.command("notebook")
def delete_notebook_verb(
    notebook: str = typer.Argument(..., help="Notebook ID or alias"),
    confirm: bool = typer.Option(False, "--confirm", "-y", help="Skip confirmation prompt"),
) -> None:
    """Delete a notebook permanently."""
    delete_notebook(notebook, confirm)


@delete_app.command("source")
def delete_source_verb(
    source: str = typer.Argument(..., help="Source ID"),
    notebook: Optional[str] = typer.Option(None, "--notebook", "-n", help="Notebook ID or alias"),
    confirm: bool = typer.Option(False, "--confirm", "-y", help="Skip confirmation prompt"),
) -> None:
    """Delete a source from notebook."""
    delete_source(source, notebook, confirm)


@delete_app.command("artifact")
def delete_artifact_verb(
    notebook: str = typer.Argument(..., help="Notebook ID or alias"),
    artifact: str = typer.Argument(..., help="Artifact ID"),
    confirm: bool = typer.Option(False, "--confirm", "-y", help="Skip confirmation prompt"),
) -> None:
    """Delete a studio artifact permanently."""
    studio_delete(notebook, artifact, confirm)


@delete_app.command("alias")
def delete_alias_verb(
    name: str = typer.Argument(..., help="Alias name"),
) -> None:
    """Delete an alias."""
    delete_alias(name)


# =============================================================================
# ADD verb (for sources)
# =============================================================================

add_app = typer.Typer(help="Add resources (sources to notebooks)")


@add_app.command("url")
def add_url_verb(
    notebook: str = typer.Argument(..., help="Notebook ID or alias"),
    url_arg: str = typer.Argument(..., help="URL to add"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Add a URL source to notebook."""
    add_source(notebook, url=url_arg, profile=profile)


@add_app.command("text")
def add_text_verb(
    notebook: str = typer.Argument(..., help="Notebook ID or alias"),
    text_arg: str = typer.Argument(..., help="Text content to add"),
    title: Optional[str] = typer.Option(None, "--title", help="Source title"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Add text source to notebook."""
    add_source(notebook, text=text_arg, title=title or "Pasted Text", profile=profile)


@add_app.command("drive")
def add_drive_verb(
    notebook: str = typer.Argument(..., help="Notebook ID or alias"),
    document_id: str = typer.Argument(..., help="Google Drive document ID"),
    title: Optional[str] = typer.Option(None, "--title", help="Source title"),
    doc_type: str = typer.Option("doc", "--type", help="Drive doc type: doc, slides, sheets, pdf"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Add a Google Drive source to notebook."""
    add_source(notebook, drive=document_id, title=title or f"Drive Document ({document_id[:8]}...)", doc_type=doc_type, profile=profile)


# =============================================================================
# RENAME verb
# =============================================================================

rename_app = typer.Typer(help="Rename resources")


@rename_app.command("notebook")
def rename_notebook_verb(
    notebook: str = typer.Argument(..., help="Notebook ID or alias"),
    title: str = typer.Argument(..., help="New title"),
) -> None:
    """Rename a notebook."""
    rename_notebook(notebook, title)


# =============================================================================
# STATUS verb
# =============================================================================

status_app = typer.Typer(help="Check status of resources")


@status_app.command("artifacts")
def status_artifacts_verb(
    notebook: str = typer.Argument(..., help="Notebook ID or alias"),
    full: bool = typer.Option(False, "--full", "-a", help="Show all details"),
) -> None:
    """Check status of studio artifacts."""
    studio_status(notebook, full)


@status_app.command("research")
def status_research_verb(
    notebook: str = typer.Argument(..., help="Notebook ID or alias"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Check status of research task."""
    research_status(notebook, profile)


# =============================================================================
# DESCRIBE verb
# =============================================================================

describe_app = typer.Typer(help="Get AI-generated descriptions and summaries")


@describe_app.command("notebook")
def describe_notebook_verb(
    notebook: str = typer.Argument(..., help="Notebook ID or alias"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Get AI-generated notebook summary with suggested topics."""
    describe_notebook(notebook, profile)


@describe_app.command("source")
def describe_source_verb(
    source: str = typer.Argument(..., help="Source ID"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Get AI-generated source summary with keywords."""
    describe_source(source, profile)


# =============================================================================
# QUERY verb (for chatting with notebooks)
# =============================================================================

query_app = typer.Typer(help="Chat with notebook sources")


@query_app.command("notebook")
def query_notebook_verb(
    notebook: str = typer.Argument(..., help="Notebook ID or alias"),
    question: str = typer.Argument(..., help="Question to ask"),
    conversation_id: Optional[str] = typer.Option(None, "--conversation-id", "-c", help="Conversation ID for follow-up questions"),
    source_ids: Optional[str] = typer.Option(None, "--source-ids", "-s", help="Comma-separated source IDs to query (default: all)"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Chat with notebook sources."""
    query_notebook(notebook, question, conversation_id, source_ids, profile)


# =============================================================================
# SYNC verb (for Drive sources)
# =============================================================================

sync_app = typer.Typer(help="Sync resources (Drive sources)")


@sync_app.command("sources")
def sync_sources_verb(
    notebook: str = typer.Argument(..., help="Notebook ID or alias"),
    source_ids: Optional[str] = typer.Option(None, "--source-ids", "-s", help="Comma-separated source IDs to sync (default: all stale)"),
    confirm: bool = typer.Option(False, "--confirm", "-y", help="Skip confirmation"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Sync Drive sources with latest content."""
    sync_sources(notebook, source_ids, confirm, profile)


# =============================================================================
# CONTENT verb (for getting raw source content)
# =============================================================================

content_app = typer.Typer(help="Get raw content from sources")


@content_app.command("source")
def content_source_verb(
    source: str = typer.Argument(..., help="Source ID"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Write content to file"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Get raw source content (no AI processing)."""
    get_source_content(source, output, profile)


# =============================================================================
# STALE verb (for listing stale Drive sources)
# =============================================================================

stale_app = typer.Typer(help="List stale resources that need syncing")


@stale_app.command("sources")
def stale_sources_verb(
    notebook: str = typer.Argument(..., help="Notebook ID or alias"),
    json_output: bool = typer.Option(False, "--json", help="Output as JSON"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """List Drive sources that need syncing."""
    list_stale_sources(notebook, json_output, profile)


# =============================================================================
# RESEARCH verb
# =============================================================================

research_app = typer.Typer(help="Research and discover sources")


@research_app.command("start")
def research_start_verb(
    query: str = typer.Argument(..., help="What to search for"),
    source: str = typer.Option("web", "--source", "-s", help="Where to search: web or drive"),
    mode: str = typer.Option("fast", "--mode", "-m", help="Research mode: fast (~30s, ~10 sources) or deep (~5min, ~40 sources, web only)"),
    notebook_id: Optional[str] = typer.Option(None, "--notebook-id", "-n", help="Add to existing notebook"),
    title: Optional[str] = typer.Option(None, "--title", "-t", help="Title for new notebook"),
    force: bool = typer.Option(False, "--force", "-f", help="Start new research even if one is already pending"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Start a research task to find new sources."""
    start_research(query, source, mode, notebook_id, title, force, profile)


@research_app.command("import")
def research_import_verb(
    notebook: str = typer.Argument(..., help="Notebook ID or alias"),
    source_ids: Optional[str] = typer.Option(None, "--source-ids", "-s", help="Comma-separated research source IDs to import (default: all)"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Import discovered sources into notebook."""
    import_research(notebook, source_ids, profile)


# =============================================================================
# CONFIGURE verb (for chat settings)
# =============================================================================

configure_app = typer.Typer(help="Configure settings")


@configure_app.command("chat")
def configure_chat_verb(
    notebook: str = typer.Argument(..., help="Notebook ID or alias"),
    goal: Optional[str] = typer.Option(None, "--goal", "-g", help="Chat goal"),
    style: Optional[str] = typer.Option(None, "--style", "-s", help="Chat style"),
    length: Optional[str] = typer.Option(None, "--length", "-l", help="Response length"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Configure chat settings for a notebook."""
    configure_chat(notebook, goal, style, length, profile)


# =============================================================================
# DOWNLOAD verb
# =============================================================================

download_app = typer.Typer(help="Download studio artifacts")


@download_app.command("audio")
def download_audio_verb(
    notebook: str = typer.Argument(..., help="Notebook ID or alias"),
    artifact_id: str = typer.Argument(..., help="Audio artifact ID"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output filename"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Download audio overview."""
    download_audio(notebook, artifact_id, output, profile)


@download_app.command("video")
def download_video_verb(
    notebook: str = typer.Argument(..., help="Notebook ID or alias"),
    artifact_id: str = typer.Argument(..., help="Video artifact ID"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output filename"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Download video overview."""
    download_video(notebook, artifact_id, output, profile)


@download_app.command("report")
def download_report_verb(
    notebook: str = typer.Argument(..., help="Notebook ID or alias"),
    artifact_id: str = typer.Argument(..., help="Report artifact ID"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output filename"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Download report."""
    download_report(notebook, artifact_id, output, profile)


@download_app.command("mind-map")
def download_mindmap_verb(
    notebook: str = typer.Argument(..., help="Notebook ID or alias"),
    artifact_id: str = typer.Argument(..., help="Mind map artifact ID"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output filename"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Download mind map."""
    download_mind_map(notebook, artifact_id, output, profile)


@download_app.command("slides")
def download_slides_verb(
    notebook: str = typer.Argument(..., help="Notebook ID or alias"),
    artifact_id: str = typer.Argument(..., help="Slide deck artifact ID"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output filename"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Download slide deck."""
    download_slide_deck(notebook, artifact_id, output, profile)


@download_app.command("infographic")
def download_infographic_verb(
    notebook: str = typer.Argument(..., help="Notebook ID or alias"),
    artifact_id: str = typer.Argument(..., help="Infographic artifact ID"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output filename"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Download infographic."""
    download_infographic(notebook, artifact_id, output, profile)


@download_app.command("data-table")
def download_data_table_verb(
    notebook: str = typer.Argument(..., help="Notebook ID or alias"),
    artifact_id: str = typer.Argument(..., help="Data table artifact ID"),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output filename"),
    profile: Optional[str] = typer.Option(None, "--profile", "-p", help="Profile to use"),
) -> None:
    """Download data table."""
    download_data_table(notebook, artifact_id, output, profile)


# =============================================================================
# SET verb (for aliases and config)
# =============================================================================

set_app = typer.Typer(help="Set values (aliases, config)")


@set_app.command("alias")
def set_alias_verb(
    name: str = typer.Argument(..., help="Alias name (e.g. 'my-notebook')"),
    value: str = typer.Argument(..., help="ID to alias"),
) -> None:
    """Set an alias for an ID."""
    set_alias(name, value)


@set_app.command("config")
def set_config_verb(
    key: str = typer.Argument(..., help="Configuration key (e.g. output.format)"),
    value: str = typer.Argument(..., help="Configuration value"),
) -> None:
    """Set configuration value."""
    set_config_value(key, value)


# =============================================================================
# SHOW verb (for displaying info)
# =============================================================================

show_app = typer.Typer(help="Show information")


@show_app.command("config")
def show_config_verb(
    json_output: bool = typer.Option(False, "--json", help="Output as JSON"),
) -> None:
    """Show all configuration."""
    show_config(json_output)


@show_app.command("aliases")
def show_aliases_verb() -> None:
    """Show all aliases."""
    list_aliases()


@show_app.command("skill")
def show_skill_verb() -> None:
    """Show NotebookLM skill content."""
    skill_show()


# =============================================================================
# INSTALL verb (for skills)
# =============================================================================

install_app = typer.Typer(help="Install resources (skills)")


@install_app.command("skill")
def install_skill_verb(
    tool: str = typer.Argument(..., help="Tool to install skill for (claude-code, opencode, gemini-cli, antigravity, codex, other)"),
    level: str = typer.Option("user", "--level", "-l", help="Install at user level (~/.config) or project level (./)"),
) -> None:
    """Install NotebookLM skill for an AI tool."""
    skill_install(tool, level)


# =============================================================================
# UNINSTALL verb (for skills)
# =============================================================================

uninstall_app = typer.Typer(help="Uninstall resources (skills)")


@uninstall_app.command("skill")
def uninstall_skill_verb(
    tool: str = typer.Argument(..., help="Tool to uninstall skill from"),
    level: str = typer.Option("user", "--level", "-l", help="Uninstall from user or project level"),
) -> None:
    """Remove installed NotebookLM skill."""
    skill_uninstall(tool, level)

