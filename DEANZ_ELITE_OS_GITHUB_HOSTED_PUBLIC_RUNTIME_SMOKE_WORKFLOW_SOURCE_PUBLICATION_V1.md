# Dean'z Elite OS GitHub-Hosted Public Runtime Smoke Workflow Source Publication v1

## Purpose

This document records the bounded source-publication checkpoint required before
the `task-planner-foundation` read-only public runtime smoke workflow can be
truthfully executed through a repository-backed GitHub-hosted dispatch.

It exists to answer these questions:

- what source-state blocker prevented the first hosted smoke dispatch?
- what exact foundation artifact set must be published so the hosted workflow
  exists in repository truth?
- how can that source publication remain bounded and avoid runtime authority
  widening?

This mission does not:

- change the Flask endpoint contract
- widen workflow triggers or permissions
- add AWS authentication to source
- mutate ECS, ALB, or routing state
- treat local-only worktree files as published repository truth

## Scope

This source-publication mission applies to:

- [DEANZ_ELITE_OS_FIRST_BOUNDED_GITHUB_HOSTED_PUBLIC_RUNTIME_SMOKE_WORKFLOW_DISPATCH_RUN_V1.md](./DEANZ_ELITE_OS_FIRST_BOUNDED_GITHUB_HOSTED_PUBLIC_RUNTIME_SMOKE_WORKFLOW_DISPATCH_RUN_V1.md)
- [`.github/workflows/public-runtime-smoke.yml`](./.github/workflows/public-runtime-smoke.yml)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)
- [README.md](./README.md)
- [GITHUB_ACTIONS_AWS_FOUNDATION_PLACEHOLDER_PLAN.md](./GITHUB_ACTIONS_AWS_FOUNDATION_PLACEHOLDER_PLAN.md)
- [aws/github-hosted-public-runtime-smoke-workflow-source-publication.record.json](./aws/github-hosted-public-runtime-smoke-workflow-source-publication.record.json)

It governs only the bounded tracked-and-pushed source checkpoint needed for a
truthful later hosted-dispatch retry.

## Publication Objective

The objective of this mission is to establish one clean repository-backed
checkpoint that includes:

- the existing read-only smoke workflow source
- the smoke-automation doctrine chain
- the hosted-dispatch doctrine chain
- the current AWS foundation artifact set those chains depend on

The checkpoint must be:

- tracked
- committed
- pushed to `origin/main`
- clean enough that a later hosted dispatch runs published source rather than
  local-only worktree state

## Inspection Findings

The bounded preflight found three critical facts:

1. the repo is on `main` at local commit `6e926501b3ebee8e73e83fc8e445537d3a7a4494`
2. `origin/main` is still at `dfc958a333b792f82c3feaaa4f543d323450938f`
3. the current AWS foundation progression after `dfc958a` largely exists only
   as local untracked source state

That means the first hosted smoke dispatch was correctly blocked:

- GitHub cannot dispatch the local-only workflow chain truthfully
- the current smoke workflow path must first exist in tracked repository source
- the doctrine chain must not remain half-local if the hosted run is expected
  to prove current source truth

## Publication Boundary

This mission publishes the current bounded AWS foundation artifact set only.

Included publication surfaces:

- `README.md`
- `GITHUB_ACTIONS_AWS_FOUNDATION_PLACEHOLDER_PLAN.md`
- `BACKUP_CHECKPOINT_V1.md`
- `DEANZ_ELITE_OS_*.md`
- `.github/*.json`
- `.github/workflows/*.yml`
- `aws/*.json`

These are the current foundation docs, planning artifacts, execution records,
and workflows that define the repo's AWS foundation state.

This mission does not introduce new workflow behavior beyond source
publication. It publishes the already-created bounded chain.

## Preserved Runtime Boundaries

This source publication must preserve the following:

- no new `app.py` mutation in this mission
- no new workflow trigger widening in this mission
- no new workflow permission widening in this mission
- no new AWS mutation in this mission
- no credentials or secrets added to source

One important nuance remains explicit:

- the local branch already contained the earlier unpublished
  `Telemetry Runtime Identity Alignment` commit
- this mission publishes that existing branch lineage
- this mission does not create an additional `app.py` change itself

## Verification Standard

Before publication is accepted, the checkpoint must prove:

- workflow YAML parses
- JSON artifacts validate
- `git diff --check` is clean for the published files
- `app.py` has no new worktree diff in this mission
- the smoke workflow has no new worktree diff in this mission
- the deploy workflow has no new worktree diff in this mission
- a strict credential-pattern scan on the published files is clean

## Publication Outcome

This mission is successful when:

- the bounded artifact set is tracked
- one publication commit exists on top of the current local branch
- that commit is pushed to `origin/main`
- the smoke workflow chain now exists in repository-backed source truth

## Canonical Publication Record

The non-secret publication record for this mission is:

- [aws/github-hosted-public-runtime-smoke-workflow-source-publication.record.json](./aws/github-hosted-public-runtime-smoke-workflow-source-publication.record.json)

That file records the bounded publication checkpoint and the next mission.

## Recommended Next Mission

The next bounded step after this publication checkpoint should be:

- `Second Bounded GitHub-Hosted Public Runtime Smoke Workflow Dispatch Run v1`

That mission should retry one repository-backed hosted dispatch of the
existing read-only smoke workflow now that the source chain exists in tracked
and pushed repository state.
