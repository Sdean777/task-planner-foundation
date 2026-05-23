# Dean'z Elite OS Second Bounded GitHub-Hosted Public Runtime Smoke Workflow Dispatch Run v1

## Purpose

This document records the second bounded attempt to execute the existing
read-only `task-planner-foundation` public runtime smoke workflow through a
repository-backed GitHub-hosted dispatch.

It exists to answer these questions:

- is the published smoke workflow now visible to GitHub-hosted Actions?
- are GitHub auth and workflow visibility now sufficient for a real hosted
  dispatch?
- does the workflow's required non-secret repository variable actually exist?
- was a safe bounded hosted dispatch actually possible?

This run does not:

- change `app.py`
- modify either workflow file
- invent workflow inputs that are missing from repository configuration
- treat a blocked preflight as a successful GitHub-hosted run

## Scope

This run applies to:

- [DEANZ_ELITE_OS_GITHUB_HOSTED_PUBLIC_RUNTIME_SMOKE_WORKFLOW_SOURCE_PUBLICATION_V1.md](./DEANZ_ELITE_OS_GITHUB_HOSTED_PUBLIC_RUNTIME_SMOKE_WORKFLOW_SOURCE_PUBLICATION_V1.md)
- [DEANZ_ELITE_OS_GITHUB_HOSTED_PUBLIC_RUNTIME_SMOKE_WORKFLOW_DISPATCH_CONTROLLED_RUN_REVIEW_V1.md](./DEANZ_ELITE_OS_GITHUB_HOSTED_PUBLIC_RUNTIME_SMOKE_WORKFLOW_DISPATCH_CONTROLLED_RUN_REVIEW_V1.md)
- [`.github/workflows/public-runtime-smoke.yml`](./.github/workflows/public-runtime-smoke.yml)
- [`aws/second-bounded-github-hosted-public-runtime-smoke-workflow-dispatch-run.record.json`](./aws/second-bounded-github-hosted-public-runtime-smoke-workflow-dispatch-run.record.json)

It governs only the second bounded hosted-dispatch execution attempt.

## Run Objective

The objective of this run was to execute one repository-backed GitHub-hosted
dispatch of the already-reviewed read-only smoke workflow while preserving the
established safety rules:

- the workflow must exist in tracked and pushed repository source
- GitHub auth must be valid
- the workflow must be visible remotely
- the required non-secret repository variable must exist before dispatch
- hosted smoke execution must remain read-only and separate from deployment
  authority

## Hosted Preflight Findings

The bounded hosted-dispatch preflight found four critical facts:

1. the repo is on `main` at pushed commit
   `ad3685e8008413267f85adea904038377bdc8bf0`
2. GitHub CLI authentication is valid outside the sandbox
3. the `Public Runtime Smoke` workflow is visible remotely
4. the required repository variable `FOUNDATION_PUBLIC_BASE_URL` does not
   exist

Observed GitHub state:

- `gh auth status` returned:
  - logged in to `github.com` account `Sdean777`
  - token scopes include `repo`
- `gh workflow list --limit 20` returned active workflow:
  - `Public Runtime Smoke`
- `gh variable get FOUNDATION_PUBLIC_BASE_URL` returned:
  - `variable FOUNDATION_PUBLIC_BASE_URL was not found`

## Why Hosted Dispatch Was Not Attempted

The current smoke workflow requires:

- `vars.FOUNDATION_PUBLIC_BASE_URL`

That variable is not present in the repository.

Proceeding anyway would have violated the repo's own rules:

- hosted smoke dispatch must use the explicit non-secret repository variable
  boundary
- the run must not invent missing inputs at dispatch time
- the workflow must not be forced into a guaranteed startup failure merely to
  claim execution happened
- bounded runs must stop honestly when a prerequisite is missing

So the correct execution result is a blocked run, not a failed dispatch.

## Execution Outcome

This run is recorded as:

- `github_hosted_smoke_dispatch_run_blocked_missing_foundation_public_base_url_variable`

No GitHub-hosted dispatch was executed.

Specifically:

- no `gh workflow run` was attempted
- no `gh run watch` was attempted
- no hosted workflow logs were produced
- no repository variable was created in this mission

## Why The Stop Was Correct

The current bounded hosted-dispatch chain assumes the published smoke workflow
can derive `PUBLIC_BASE_URL` from the non-secret repository variable
`FOUNDATION_PUBLIC_BASE_URL`.

That condition is not yet true for this repo configuration.

Attempting a dispatch now would not prove healthy hosted execution. It would
only prove that the workflow exits immediately on missing configuration, and
that is not the intended bounded run objective.

The correct next step is to establish the explicit repository-variable
baseline, then retry the hosted dispatch against that known input boundary.

## Preserved Boundaries

This run preserved the required boundaries:

- `app.py` stayed unchanged
- `.github/workflows/public-runtime-smoke.yml` stayed unchanged
- `.github/workflows/deploy-foundation-skeleton.yml` stayed unchanged
- no AWS credentials were added to source
- no OpenAI keys were added
- no hosted dispatch was attempted with missing configuration
- no AWS mutation happened in this mission

## Canonical Execution Record

The non-secret execution record for this run is:

- [`aws/second-bounded-github-hosted-public-runtime-smoke-workflow-dispatch-run.record.json`](./aws/second-bounded-github-hosted-public-runtime-smoke-workflow-dispatch-run.record.json)

That file records the published source state, the valid GitHub auth/workflow
visibility, the missing repository variable, and the next bounded mission.

## Recommended Next Mission

The next bounded step after this blocked run should be:

- `GitHub-Hosted Public Runtime Smoke Workflow Variable Baseline v1`

That mission should establish the non-secret repository variable
`FOUNDATION_PUBLIC_BASE_URL` for the published smoke workflow, then the hosted
dispatch can be retried honestly.

## Warning

Do not retry the hosted smoke dispatch by bypassing the repository-variable
boundary.

Establish the explicit GitHub repository-variable baseline first, then rerun
the bounded hosted dispatch against that known configuration.
