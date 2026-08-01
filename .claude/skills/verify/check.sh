#!/bin/bash
# ActorFastApi — Verification Gates
# Runs after any code change. All three gates must pass.

set -e
PASS=true

echo "========================================"
echo "  ActorFastApi Verification"
echo "========================================"

# GATE 1: Run tests
echo ""
echo "[ GATE 1 ] Running test suite..."
if python -m pytest tests/test_actors.py -v; then
  echo "✅ Tests passed"
else
  echo "❌ Tests FAILED"
  PASS=false
fi

# GATE 2: Show diff
echo ""
echo "[ GATE 2 ] Git diff (what changed)..."
git diff HEAD~1 --stat 2>/dev/null || git diff --cached --stat 2>/dev/null || echo "(no committed diff — showing working tree)" && git diff --stat
echo ""
git diff HEAD~1 -- "*.py" 2>/dev/null || git diff -- "*.py"

# GATE 3: Check for weakened tests
echo ""
echo "[ GATE 3 ] Checking for weakened tests..."
DIFF=$(git diff HEAD~1 -- tests/ 2>/dev/null || git diff -- tests/)

WEAKENED=false
if echo "$DIFF" | grep -E "^\-.*assert" > /dev/null 2>&1; then
  echo "⚠️  WARNING: assert statement removed from tests"
  WEAKENED=true
fi
if echo "$DIFF" | grep -E "^\-.*def test_" > /dev/null 2>&1; then
  echo "⚠️  WARNING: test function removed"
  WEAKENED=true
fi
if echo "$DIFF" | grep -E "^\+.*pytest.mark.skip" > /dev/null 2>&1; then
  echo "⚠️  WARNING: test marked as skip"
  WEAKENED=true
fi

if [ "$WEAKENED" = false ]; then
  echo "✅ No tests weakened"
else
  echo "❌ Tests were weakened — this is not a clean pass"
  PASS=false
fi

# FINAL VERDICT
echo ""
echo "========================================"
if [ "$PASS" = true ]; then
  echo "  ✅ VERIFICATION PASSED — safe to proceed"
else
  echo "  ❌ VERIFICATION FAILED — do not mark as done"
fi
echo "========================================"
