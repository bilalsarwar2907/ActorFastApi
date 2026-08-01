# verify

## Description
Use this skill after any code change, refactor, or new feature. Verifies the work is complete and safe.

## Procedure

1. Run `bash .claude/skills/verify/check.sh` — do not skip this step.
2. Read the output. It will report:
   - Test results (pass/fail + count)
   - Git diff summary (what changed)
   - Whether any test was weakened (assert removed, condition loosened, test skipped)
3. Report the result explicitly:
   - ✅ PASS — state which tests passed and confirm no tests were weakened
   - ❌ FAIL — state what failed and what needs fixing before this counts as done

## Rules
- "Done" is not "the code looks right." Done is this skill completing with a ✅ PASS.
- Never mark work complete if check.sh reports a failure.
- Never skip the diff check — green tests with weakened assertions are not a pass.
