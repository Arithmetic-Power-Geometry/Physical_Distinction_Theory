from cycle119_sector_monotone_closure import audit, hidden_cost, safe_comp, unsafe_comp


def test_faithful_zero_set():
    assert hidden_cost([0, 0, 0]) == 0
    assert hidden_cost([0, 1, 0]) > 0


def test_safe_visible_inputs_remain_visible():
    x = ([2, -1], [0, 0])
    y = ([3, 4], [0, 0])
    assert hidden_cost(safe_comp(x, y)[1]) == 0


def test_extension_countermodel_would_violate_hidden_monotonicity():
    x = ([2], [0])
    y = ([3], [0])
    assert hidden_cost(unsafe_comp(x, y)[1]) == 36


def test_dimension_stress_audit():
    r = audit()
    assert r["trials"] == 1340
    assert r["safe_failures"] == 0
    assert r["unsafe_hidden_outputs"] > 0


def test_classification_guard():
    r = audit()
    assert r["classification"]["closure_theorem"] == "PROVED"
    assert r["classification"]["resource_principle_as_PDT_native"] == "OPEN"
    assert r["classification"]["abstract_mechanism_novelty"] == "IMPORTED/KNOWN"
