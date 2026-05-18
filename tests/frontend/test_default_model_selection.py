from __future__ import annotations

from pathlib import Path


def test_frontend_prefers_backend_default_model_before_avatar_model() -> None:
    source = Path("apps/web/src/App.tsx").read_text(encoding="utf-8")
    assert "default_model?: string" in source
    assert "defaultModel?: string | null" in source

    default_idx = source.index("if (defaultModel && available.has(defaultModel)")
    current_idx = source.index("if (available.has(currentModel) && connected.has(currentModel))")
    avatar_idx = source.index("const avatarModel = initialAvatar?.model_type")
    assert default_idx < current_idx
    assert default_idx < avatar_idx

    assert "mo.default_model" in source
