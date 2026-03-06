from agentforge_core.config_loader import get_env_summary


def test_env_summary_returns_dict():
    result = get_env_summary()
    assert isinstance(result, dict)
    assert "REDIS_URL" in result
