# Sharing API Implementation Plan

**Goal:** Enable programmatic sharing of notebooks via email and public link generation with granular control.

**Status:** Phase 2 (Implementation)

---

## Phase 1: RPC Discovery (COMPLETED)

We have identified the core RPCs from reference analysis.

**RPC Constants:**
- `RPC_SHARE_NOTEBOOK` = `QDyure` (Set visibility/public link)
- `RPC_GET_SHARE_STATUS` = `JFMDGd` (Get permissions/collaborators)

---

## Phase 2: Client Implementation (Next Level Architecture)

**Design Philosophy:**
- **Granular Methods:** Split operations into `get_share_status`, `add_collaborator`, `remove_collaborator`, `set_public_access`.
- **Strong Typing:** Use typed dictionaries/dataclasses for `ShareStatus` and `Collaborator`.
- **Async Native:** Fully async implementation consistent with our client architecture.

**File:** `src/notebooklm_tools/core/client.py`

**New Constants:**
```python
RPC_SHARE_NOTEBOOK = "QDyure"
RPC_GET_SHARE_STATUS = "JFMDGd"

# Role Constants
ROLE_VIEWER = 2
ROLE_EDITOR = 3
ROLE_OWNER = 1

# Access Levels
ACCESS_RESTRICTED = 1
ACCESS_PUBLIC = 2
```

**New Models (Internal Types):**
```python
@dataclass
class Collaborator:
    email: str
    role: int  # 2=Viewer, 3=Editor
    is_pending: bool
    photo_url: str | None

@dataclass
class ShareStatus:
    is_public: bool
    access_level: int
    collaborators: list[Collaborator]
    invite_link: str | None
```

**New Methods:**
```python
async def get_share_status(self, notebook_id: str) -> ShareStatus:
    """Fetch current sharing settings and collaborators."""
    # RPC: JFMDGd
    pass

async def set_public_access(self, notebook_id: str, is_public: bool) -> str | None:
    """Toggle public link access. Returns link if public."""
    # RPC: QDyure
    pass

async def add_collaborator(self, notebook_id: str, email: str, role: int = ROLE_VIEWER) -> bool:
    """Add a user by email."""
    # RPC: QDyure (with different params for user invite)
    pass

async def remove_collaborator(self, notebook_id: str, email: str) -> bool:
    """Remove a user."""
    # RPC: QDyure (remove operation)
    pass
```

---

## Phase 3: CLI & MCP Integration

**CLI Command:** `src/notebooklm_tools/cli/commands/share.py`
- `nlm share status <id>` -> Renders rich table of users.
- `nlm share invite <id> <email> --role editor`
- `nlm share public <id> --on/--off` -> Returns the public URL.

**MCP Tools:**
- `notebook_share_status(notebook_id)`
- `notebook_share_invite(notebook_id, email, role)`
- `notebook_share_public(notebook_id, is_public)`

---

## Next Steps

1.  **Add RPCs:** Update `RPC_NAMES` and constants in `client.py`.
2.  **Implement Client:** Add the methods with robust parsing logic.
3.  **Implement CLI:** Build the `share` command group.
4.  **Implement MCP:** Expose the tools.