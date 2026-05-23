# Dean'z Elite OS GitHub-Hosted Public Runtime Smoke Workflow Variable Baseline v1

## Purpose

This document records the bounded creation of the non-secret GitHub repository
variable required by the published `task-planner-foundation` hosted smoke
workflow.

It exists to answer these questions:

- what repository variable was established?
- what stable public runtime truth does it point to?
- did this mission widen workflow or AWS authority?
- what is the next honest hosted-dispatch step now that the variable exists?

This mission does not:

- change `app.py`
- modify `.github/workflows/public-runtime-smoke.yml`
- modify `.github/workflows/deploy-foundation-skeleton.yml`
- perform AWS mutation
- introduce secrets or credentials into source

## Scope

This variable-baseline mission applies to:

- [DEANZ_ELITE_OS_SECOND_BOUNDED_GITHUB_HOSTED_PUBLIC_RUNTIME_SMOKE_WORKFLOW_DISPATCH_RUN_V1.md](./DEANZ_ELITE_OS_SECOND_BOUNDED_GITHUB_HOSTED_PUBLIC_RUNTIME_SMOKE_WORKFLOW_DISPATCH_RUN_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_ROUTING_BASELINE_STANDUP_V1.md](./DEANZ_ELITE_OS_PUBLIC_ROUTING_BASELINE_STANDUP_V1.md)
- [`.github/workflows/public-runtime-smoke.yml`](./.github/workflows/public-runtime-smoke.yml)
- [`aws/github-hosted-public-runtime-smoke-workflow-variable-baseline.record.json`](./aws/github-hosted-public-runtime-smoke-workflow-variable-baseline.record.json)

It governs only the explicit repository-variable baseline needed for the next
bounded GitHub-hosted smoke dispatch.

## Variable Baseline Objective

The objective of this mission was to establish one explicit non-secret
repository variable boundary for the already-published hosted smoke workflow:

- variable name: `FOUNDATION_PUBLIC_BASE_URL`
- variable scope: GitHub repository variable
- variable value: the stable ALB-backed public runtime base URL
- verification method: `gh variable get FOUNDATION_PUBLIC_BASE_URL`

This keeps hosted smoke execution aligned with reviewed repository-backed
configuration instead of ad hoc dispatch-time inputs.

## Preflight Truth Used

This mission started from two already-established truths:

1. the second bounded hosted-dispatch run proved the workflow is published and
   repository-backed, but blocked because `FOUNDATION_PUBLIC_BASE_URL` was
   missing
2. the public routing baseline already established the stable non-secret base
   URL:
   `http://deanzelite-alb-2130825976.us-east-1.elb.amazonaws.com:8081`

Those truths meant the correct next step was not another hosted dispatch
attempt. It was the missing repository-variable baseline.

## Variable Baseline Established

The following repository-variable baseline is now in place:

- variable:
  `FOUNDATION_PUBLIC_BASE_URL`
- scope:
  GitHub repository variable
- value:
  `http://deanzelite-alb-2130825976.us-east-1.elb.amazonaws.com:8081`

The value is intentionally non-secret. It is the current stable public base URL
for the foundation runtime, not a credential or token.

Verification returned the stored value successfully through:

- `gh variable get FOUNDATION_PUBLIC_BASE_URL`

## Why This Was The Correct Mutation

The current hosted smoke workflow derives `PUBLIC_BASE_URL` from:

- `vars.FOUNDATION_PUBLIC_BASE_URL`

So the bounded hosted-dispatch chain must establish that repository-variable
boundary explicitly before retrying a real GitHub-hosted run.

This mission fixes the exact missing prerequisite without widening anything
else:

- no workflow trigger changed
- no permissions changed
- no deployment behavior changed
- no AWS runtime mutation happened

## Preserved Boundaries

This mission preserved the required boundaries:

- `app.py` stayed unchanged
- `.github/workflows/public-runtime-smoke.yml` stayed unchanged
- `.github/workflows/deploy-foundation-skeleton.yml` stayed unchanged
- no AWS credentials were added to source
- no OpenAI keys were added
- no AWS mutation happened in this mission

## Canonical Execution Record

The non-secret execution record for this mission is:

- [`aws/github-hosted-public-runtime-smoke-workflow-variable-baseline.record.json`](./aws/github-hosted-public-runtime-smoke-workflow-variable-baseline.record.json)

That file records the repository-variable mutation, the exact stored value, and
the next bounded mission.

## Recommended Next Mission

The next bounded step after this variable baseline should be:

- `Third Bounded GitHub-Hosted Public Runtime Smoke Workflow Dispatch Run v1`

That mission should retry one real repository-backed GitHub-hosted dispatch of
the published read-only smoke workflow now that both source publication and the
required repository-variable boundary are in place.

## Warning

Do not bypass this repository-variable boundary by inventing workflow inputs or
hardcoding runtime URLs in later hosted runs.

Use the published workflow and this repository-variable baseline together.
