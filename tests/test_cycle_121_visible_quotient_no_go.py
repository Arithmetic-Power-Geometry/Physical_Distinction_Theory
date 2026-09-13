from experiments.cycle_121_visible_quotient_no_go import (
    base_mul,
    extension_mul,
    lift,
    project,
    run,
    visible_resources,
)


def test_smallest_hidden_leak_witness():
    out = extension_mul(lift([1]), lift([1]))
    assert out == ([1], [1])
    assert project(out) == [1]


def test_projection_is_homomorphism():
    a = [2, -1, 3]
    b = [-2, 4, 0]
    assert project(extension_mul(lift(a), lift(b))) == base_mul(a, b)


def test_visible_resources_cannot_detect_extension():
    a = [1, -2, 0, 3]
    b = [2, 4, 5, -1]
    base = base_mul(a, b)
    ext = project(extension_mul(lift(a), lift(b)))
    assert visible_resources(base) == visible_resources(ext)


def test_associativity_explicit():
    x = lift([1, 2])
    y = lift([3, -1])
    z = lift([2, 4])
    assert extension_mul(extension_mul(x, y), z) == extension_mul(x, extension_mul(y, z))


def test_stress_audit():
    out = run()
    assert out["visible_transcript_checks"] == 3040
    assert out["visible_transcript_mismatches"] == 0
    assert out["associativity_failures"] == 0
    assert out["trials_with_hidden_leakage"] == 1472


def test_not_breakthrough_candidate():
    out = run()
    assert out["breakthrough_candidate"] is False
    assert "OPEN" in out["classification"]
