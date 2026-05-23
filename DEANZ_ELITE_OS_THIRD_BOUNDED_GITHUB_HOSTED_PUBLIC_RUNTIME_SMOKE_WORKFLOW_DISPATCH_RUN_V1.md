# Dean'z Elite OS Third Bounded GitHub-Hosted Public Runtime Smoke Workflow Dispatch Run v1

## Purpose

This document records the first successful repository-backed GitHub-hosted
dispatch of the published `task-planner-foundation` read-only smoke workflow
after both source publication and repository-variable baseline were established.

It exists to answer these questions:

- did the published GitHub-hosted smoke workflow now dispatch successfully?
- did the hosted run consume the explicit repository-variable boundary?
- what exact GitHub run and job completed?
- what should happen next now that hosted smoke execution is proven?

This mission does not:

- change `app.py`
- modify `.github/workflows/public-runtime-smoke.yml`
- modify `.github/workflows/deploy-foundation-skeleton.yml`
- mutate AWS runtime state
- publish the new success record back to repository source

## Scope

This third bounded hosted-dispatch run applies to:

- [DEANZ_ELITE_OS_GITHUB_HOSTED_PUBLIC_RUNTIME_SMOKE_WORKFLOW_SOURCE_PUBLICATION_V1.md](./DEANZ_ELITE_OS_GITHUB_HOSTED_PUBLIC_RUNTIME_SMOKE_WORKFLOW_SOURCE_PUBLICATION_V1.md)
- [DEANZ_ELITE_OS_GITHUB_HOSTED_PUBLIC_RUNTIME_SMOKE_WORKFLOW_VARIABLE_BASELINE_V1.md](./DEANZ_ELITE_OS_GITHUB_HOSTED_PUBLIC_RUNTIME_SMOKE_WORKFLOW_VARIABLE_BASELINE_V1.md)
- [`.github/workflows/public-runtime-smoke.yml`](./.github/workflows/public-runtime-smoke.yml)
- [`aws/third-bounded-github-hosted-public-runtime-smoke-workflow-dispatch-run.record.json`](./aws/third-bounded-github-hosted-public-runtime-smoke-workflow-dispatch-run.record.json)

It governs only the third bounded repository-backed hosted smoke dispatch.

## Run Objective

The objective of this run was to execute one real GitHub-hosted dispatch of the
already-published read-only smoke workflow while preserving the established
safety rules:

- workflow source must already be tracked and pushed
- GitHub auth must already be valid
- the workflow must be visible remotely
- `FOUNDATION_PUBLIC_BASE_URL` must already exist as a repository variable
- the hosted workflow must remain read-only and separate from deployment
  authority

## Hosted Preflight Findings

The hosted-dispatch preflight confirmed all required inputs were now in place:

1. GitHub CLI authentication is valid
2. the `Public Runtime Smoke` workflow is visible remotely
3. `FOUNDATION_PUBLIC_BASE_URL` exists as a repository variable
4. the variable value matches the established stable ALB-backed base URL

Observed GitHub state:

- `gh auth status`
  - logged in to `github.com` account `Sdean777`
- `gh workflow list --limit 20`
  - includes active workflow `Public Runtime Smoke`
- `gh variable get FOUNDATION_PUBLIC_BASE_URL`
  - returns:
    `http://deanzelite-alb-2130825976.us-east-1.elb.amazonaws.com:8081`

## Hosted Dispatch Executed

One real hosted dispatch was then executed:

- command:
  `gh workflow run public-runtime-smoke.yml --ref main`
- workflow:
  `Public Runtime Smoke`
- event:
  `workflow_dispatch`
- branch:
  `main`
- head SHA:
  `ad3685e8008413267f85adea904038377bdc8bf0`

The resulting GitHub-hosted run was:

- run id:
  `26319958797`
- run URL:
  `https://github.com/Sdean777/task-planner-foundation/actions/runs/26319958797`

## Run Outcome

The third bounded hosted-dispatch run completed successfully.

Recorded outcome:

- `github_hosted_smoke_dispatch_run_succeeded`

Authoritative GitHub run result:

- workflow status:
  `completed`
- workflow conclusion:
  `success`
- hosted job:
  `public-runtime-smoke`
- hosted job id:
  `77486908167`
- job conclusion:
  `success`

Step-level completion was also clean:

- `Set up job`
- `Show bounded smoke workflow posture`
- `Derive public base URL`
- `Run bounded public runtime smoke rounds`
- `Record bounded smoke automation outcome`
- `Complete job`

## Why This Success Matters

This run proves the current GitHub-hosted smoke path is no longer theoretical.

The repository now has:

- published read-only hosted smoke workflow source
- explicit non-secret repository-variable boundary
- successful GitHub-hosted dispatch evidence against the stable public base URL

That means the hosted smoke boundary is now operationally real, while still
remaining:

- read-only
- manually dispatched
- separate from deployment authority
- free of AWS credential material in source

## Preserved Boundaries

This mission preserved the required boundaries:

- `app.py` stayed unchanged
- `.github/workflows/public-runtime-smoke.yml` stayed unchanged
- `.github/workflows/deploy-foundation-skeleton.yml` stayed unchanged
- no AWS credentials were added to source
- no OpenAI keys were added
- no AWS mutation happened in this mission
- no workflow source publication happened in this mission

## Canonical Execution Record

The non-secret execution record for this hosted run is:

- [`aws/third-bounded-github-hosted-public-runtime-smoke-workflow-dispatch-run.record.json`](./aws/third-bounded-github-hosted-public-runtime-smoke-workflow-dispatch-run.record.json)

That file records the preflight truth, run id, job id, hosted conclusion, and
the next bounded mission.

## Recommended Next Mission

The next bounded step after this successful hosted run should be:

- `GitHub-Hosted Public Runtime Smoke Success Source Publication v1`

That mission should publish this successful hosted-run evidence and the current
updated doctrine chain as tracked repository source, so local documentation and
remote source truth converge again.

## Warning

Do not treat this successful hosted smoke run as permission to widen workflow
authority automatically.

The hosted smoke workflow remains read-only and separate from deployment or
rollback control.
