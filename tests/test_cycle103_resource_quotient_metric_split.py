import cycle103_resource_quotient_metric_split as c103


def test_smallest_no_canonical_section_witness():
    w = c103.no_canonical_section_witness()
    assert w["ambient_dimension"] == 2
    assert w["qT_equals_q"] is True
    assert w["section_is_fixed"] is False


def test_exact_dimension_balance_all_required_dimensions():
    rows = c103.coordinate_dimension_ledger()
    assert {r["n"] for r in rows} == set(c103.DIMS)
    assert all(r["balance_ok"] for r in rows)


def test_random_metric_split():
    out = c103.random_metric_split_audit(trials=100, seed=17)
    assert out["violations_gt_1e-9"] == 0


def test_record_recoverability():
    out = c103.record_recoverability_audit(trials=100, seed=23)
    assert out["violations_gt_1e-12"] == 0


def test_generate_boundary_and_no_breakthrough():
    out = c103.generate()
    assert out["breakthrough_candidate"] is False
    assert out["results"]["quotient_only_reverse_embedding"]["status"].startswith("FALSIFIED")
    assert out["results"]["metric_split"]["status"].startswith("PROVED")
