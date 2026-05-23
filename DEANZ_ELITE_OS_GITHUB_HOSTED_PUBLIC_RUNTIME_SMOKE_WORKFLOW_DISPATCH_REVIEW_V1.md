# Dean'z Elite OS GitHub-Hosted Public Runtime Smoke Workflow Dispatch Review v1

## Purpose

This document defines the first bounded review layer for repository-backed
hosted execution of the already-proven read-only public runtime smoke workflow
for the `task-planner-foundation` service.

It exists to answer these questions:

- is the current read-only smoke workflow now stable enough for GitHub-hosted
  dispatch review?
- what exact hosted-dispatch boundaries must remain intact before any
  repository-backed run is attempted?
- which trigger, permission, and authority expansions remain forbidden even if
  hosted dispatch becomes a candidate?

This review does not:

- run a GitHub-hosted workflow dispatch
- modify `.github/workflows/public-runtime-smoke.yml`
- modify `.github/workflows/deploy-foundation-skeleton.yml`
- add AWS authentication or mutation commands
- change the Flask endpoint contract

## Scope

This review applies to:

- [DEANZ_ELITE_OS_FIRST_BOUNDED_PUBLIC_RUNTIME_SMOKE_AUTOMATION_RUN_V1.md](./DEANZ_ELITE_OS_FIRST_BOUNDED_PUBLIC_RUNTIME_SMOKE_AUTOMATION_RUN_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_SMOKE_AUTOMATION_PATCH_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_SMOKE_AUTOMATION_PATCH_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md)
- [`.github/workflows/public-runtime-smoke.yml`](./.github/workflows/public-runtime-smoke.yml)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)
- [`.github/github-hosted-public-runtime-smoke-workflow-dispatch-review.template.json`](./.github/github-hosted-public-runtime-smoke-workflow-dispatch-review.template.json)

It governs only the hosted-dispatch review boundary for the existing separate
read-only smoke workflow.

## Review Objective

This review exists to decide whether GitHub-hosted smoke dispatch currently
remains:

- `hosted_dispatch_blocked`
- `hosted_dispatch_review_required`
- `hosted_dispatch_candidate_ready`

This is still not a hosted workflow run mission.

## Required Evidence

Before any later hosted-dispatch proposal may reopen, the following must
already exist and remain intact.

### 1. Smoke Workflow Preservation

- [`.github/workflows/public-runtime-smoke.yml`](./.github/workflows/public-runtime-smoke.yml)
  exists in source
- the smoke workflow remains `workflow_dispatch` only
- the smoke workflow keeps workflow-level permissions at `contents: read`
- the smoke workflow still derives its base URL from
  `vars.FOUNDATION_PUBLIC_BASE_URL`
- the smoke workflow remains read-only and observational
- the smoke workflow still performs the proven endpoint checks only
- the smoke workflow still writes summary-only outcomes

### 2. Stable Runtime Truth

- the stable non-secret ALB base URL still exists
- the bounded public runtime remains steady on the accepted ECS revision
- telemetry runtime identity remains aligned to `AWS ECS Fargate`
- the second bounded public verification run completed honestly
- the post-deploy public runtime smoke tests completed cleanly
- the first bounded public runtime smoke automation run completed as `stable`

### 3. Hosted Dispatch Separation

- GitHub-hosted dispatch remains separate from deployment authority
- `.github/workflows/deploy-foundation-skeleton.yml` remains unchanged in this
  review
- hosted dispatch remains manual and repository-backed only
- hosted dispatch does not gain rollback, rollout, or routing authority
- hosted dispatch does not become a hidden deployment controller

### 4. Source Hygiene

- no AWS credentials in source
- no OpenAI or model keys in source
- no hardcoded live public base URL in workflow source
- no hidden trigger widening in source
- no bundled image publication or ECS rollout logic in the smoke workflow

## Candidate Constraints

Even if hosted dispatch becomes a candidate, the following must remain true in
this mission:

- no hosted workflow dispatch is executed
- no workflow file is modified
- no deploy workflow mutation is introduced
- no schedule, `workflow_run`, `push`, or `pull_request` trigger is added
- no workflow permission widening is introduced
- no repository variable mutation is introduced
- no approval or environment boundary is bypassed

## Review Outcomes

### 1. `hosted_dispatch_blocked`

Required when:

- the smoke workflow no longer remains read-only
- stable ALB-backed smoke evidence is missing
- the workflow no longer uses the non-secret repository variable boundary
- hosted dispatch is proposed as deployment or rollback authority
- trigger or permission widening appears before a proposal mission

### 2. `hosted_dispatch_review_required`

Allowed when:

- stable read-only smoke evidence exists
- the workflow is still bounded correctly
- repository-backed hosted execution still needs exact proposal narrowing
- the execution surface is not yet specific enough for a proposal mission

### 3. `hosted_dispatch_candidate_ready`

Allowed when:

- the smoke workflow exists and remains read-only
- the workflow is still `workflow_dispatch` only
- workflow-level permissions remain `contents: read`
- the stable ALB base URL remains non-secret and intact
- the local-equivalent smoke-automation run already proved the workflow logic
  without drift
- hosted dispatch remains separate from deployment authority
- source hygiene remains intact

This outcome only allows a later proposal mission. It does not authorize a
hosted workflow dispatch by itself.

## Still-Forbidden Actions

Even after `hosted_dispatch_candidate_ready`, the following remain forbidden
in this mission:

- running the GitHub-hosted workflow dispatch
- modifying `.github/workflows/public-runtime-smoke.yml`
- modifying `.github/workflows/deploy-foundation-skeleton.yml`
- adding schedule, `workflow_run`, `push`, or `pull_request` triggers
- widening workflow permissions beyond `contents: read`
- adding AWS auth or mutation commands
- hardcoding the live public base URL into workflow source
- introducing rollback or remediation authority

## Canonical Planning Artifact

The non-secret planning artifact for this review is:

- [`.github/github-hosted-public-runtime-smoke-workflow-dispatch-review.template.json`](./.github/github-hosted-public-runtime-smoke-workflow-dispatch-review.template.json)

That file is a planning artifact only.

It is not a workflow run and not an approval token.

## Governance Rules

- hosted smoke dispatch must remain narrower than deployment workflows
- hosted smoke dispatch must remain read-only
- hosted smoke dispatch must remain repository-backed and manual
- hosted smoke dispatch outcomes must remain observational, not mutational
- deployment authority must stay in the deployment workflow chain, not the
  smoke workflow chain

## Explicit Non-Goals

This review does not:

- run a GitHub-hosted workflow dispatch
- create a new workflow file
- change deployment approvals
- add rollback behavior
- change the Flask endpoint contract

## Paired Artifacts

- [DEANZ_ELITE_OS_FIRST_BOUNDED_PUBLIC_RUNTIME_SMOKE_AUTOMATION_RUN_V1.md](./DEANZ_ELITE_OS_FIRST_BOUNDED_PUBLIC_RUNTIME_SMOKE_AUTOMATION_RUN_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_SMOKE_AUTOMATION_PATCH_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_SMOKE_AUTOMATION_PATCH_V1.md)
- [`.github/github-hosted-public-runtime-smoke-workflow-dispatch-review.template.json`](./.github/github-hosted-public-runtime-smoke-workflow-dispatch-review.template.json)

## Recommended Next Mission

The next bounded step after this review should be:

- `GitHub-Hosted Public Runtime Smoke Workflow Dispatch Proposal v1`

That mission should define the exact repository-backed hosted execution
boundary for the existing read-only smoke workflow without widening triggers,
permissions, or deployment authority.
