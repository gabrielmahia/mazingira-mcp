from mazingira_mcp import server

_fn = lambda name: (getattr(server, name).fn if hasattr(getattr(server, name), "fn") else getattr(server, name))


def test_an_unknown_activity_is_an_error_not_the_construction_eia():
    r = _fn("nema_permit_guide")("space tourism", None)
    assert "error" in r and "construction" in r["valid_activities"] and "threshold" not in r
    assert "threshold" in _fn("nema_permit_guide")("construction", None)
