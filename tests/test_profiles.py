"""Tests for scientist profiles and evaluation."""

import pytest
from scientist_taste.config.profiles import ALL_PROFILES, get_profile, get_profiles_by_level
from scientist_taste.core.evaluator import TasteEvaluator


class TestProfiles:
    def test_all_profiles_exist(self):
        assert len(ALL_PROFILES) >= 10

    def test_get_profile(self):
        p = get_profile("einstein")
        assert p is not None
        assert p.name == "Albert Einstein"

    def test_get_by_level(self):
        classical = get_profiles_by_level("classical")
        assert len(classical) == 5
        nobel = get_profiles_by_level("nobel")
        assert len(nobel) == 5

    def test_all_have_axes(self):
        for p in ALL_PROFILES.values():
            assert len(p.axes) >= 3

    def test_weights_in_range(self):
        for p in ALL_PROFILES.values():
            for a in p.axes:
                assert 0.0 <= a.weight <= 1.0


class TestEvaluator:
    def test_single_evaluation(self):
        ev = TasteEvaluator().evaluate_single("unified geometric theory", "einstein")
        assert ev.scientist_name == "Albert Einstein"
        assert -1.0 <= ev.overall_score <= 1.0

    def test_group_evaluation(self):
        ge = TasteEvaluator().evaluate_group("physical intuition computation", level="classical")
        assert len(ge.evaluations) == 5
        assert ge.synthesis

    def test_unknown_scientist(self):
        ev = TasteEvaluator().evaluate_single("test", "nonexistent")
        assert ev.caveats
