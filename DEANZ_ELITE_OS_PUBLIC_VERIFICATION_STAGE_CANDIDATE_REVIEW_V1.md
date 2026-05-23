# Dean'z Elite OS Public Verification Stage Candidate Review v1

## Purpose

This document defines the first bounded candidate review for the
`public-verification-placeholder` job inside the `task-planner-foundation`
deployment workflow skeleton.

It exists to answer these questions after bounded image publication, bounded
rollout wiring, and the first ECS service baseline now exist:

- is the third disabled workflow job now reviewable for a later public
  verification enablement proposal?
- what exact evidence must remain intact before any live runtime verification
  discussion reopens?
- what actions remain blocked even if the public verification stage becomes a
  candidate?

This document does not:

- enable `public-verification-placeholder`
- run live public smoke tests
- mutate ALB, ECS, API Gateway, or DNS state
- hardcode production endpoint URLs
- change the Flask application contract

## Scope

This public-verification candidate review applies to:

- [DEANZ_ELITE_OS_FIRST_BOUNDED_ECR_IMAGE_PUBLICATION_RUN_V1.md](./DEANZ_ELITE_OS_FIRST_BOUNDED_ECR_IMAGE_PUBLICATION_RUN_V1.md)
- [DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_PATCH_V1.md](./DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_PATCH_V1.md)
- [DEANZ_ELITE_OS_FIRST_BOUNDED_ECS_ROLLOUT_RUN_V1.md](./DEANZ_ELITE_OS_FIRST_BOUNDED_ECS_ROLLOUT_RUN_V1.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_BASELINE_STANDUP_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_BASELINE_STANDUP_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)

It governs only the third-job public-verification review boundary.

## Candidate Job

The only workflow job in scope for this mission is:

- `public-verification-placeholder`

All earlier jobs remain outside scope:

- `push-image-placeholder`
- `ecs-rollout-placeholder`

## Candidate Review Objective

This review exists to decide whether `public-verification-placeholder`
currently remains:

- `public_verification_stage_blocked`
- `public_verification_stage_review_required`
- `public_verification_stage_candidate_ready`

This is still not a public-verification enablement action.

## Required Evidence

Before `public-verification-placeholder` may be considered a bounded candidate
for a later enablement proposal, the following must already exist and remain
intact.

### 1. Foundation Preservation

- [app.py](./app.py) remains unchanged
- the current Flask endpoint contract remains intact
- the container build verification workflow still exists

### 2. Upstream Runtime Truth

- the first bounded ECR image publication run completed
- immutable image tag
  `sha-dfc958a333b792f82c3feaaa4f543d323450938f` exists in ECR
- the ECS rollout stage patch exists
- the first bounded ECS rollout run is recorded honestly as blocked before
  baseline standup
- the ECS service baseline standup completed
- the `task-planner-foundation` ECS service baseline is steady at
  `desired=1`, `running=1`, `pending=0`

### 3. Workflow Boundary Preservation

- deployment workflow skeleton still exists
- `push-image-placeholder` remains the bounded image-publication job
- `ecs-rollout-placeholder` remains the bounded rollout job
- `public-verification-placeholder` still has `if: ${{ false }}`
- workflow-level permissions remain `contents: read`

### 4. Public Verification Governance Chain

- public runtime verification and release-gate contract exists
- immutable image promotion and ECS rollout contract exists
- ECS service runbook exists
- ECS runtime contract exists
- ECS baseline standup evidence exists

### 5. Source Hygiene

- no AWS credentials in source
- no OpenAI or model keys in source
- no live public verification commands exist in the workflow
- no committed production endpoint URLs exist in source for this stage
- no public-verification enablement flags are hidden in source

## Candidate Constraints

Even if the public verification stage becomes a candidate, the following must
remain true in this mission:

- `public-verification-placeholder` stays disabled
- no live public smoke test command is introduced
- no ALB, target-group, DNS, or API Gateway mutation is introduced
- no rollout or push-image behavior is widened
- no application code change may be bundled into public verification review
- release-gate posture remains subordinate to immutable image truth and
  rollback posture

## Review Outcomes

### 1. `public_verification_stage_blocked`

Required when:

- required evidence is missing
- the ECS baseline is absent or unstable
- release-gate posture is missing
- live public verification is proposed too early
- endpoint URLs or public-routing assumptions are smuggled into source

### 2. `public_verification_stage_review_required`

Allowed when:

- prerequisite evidence exists
- the job is still disabled
- upstream image, rollout, and baseline truth exist
- operator review is still required before any public-verification proposal
  reopens

### 3. `public_verification_stage_candidate_ready`

Allowed when:

- all required evidence exists
- `public-verification-placeholder` remains disabled
- upstream image publication, rollout, and ECS baseline truth are complete and
  verifiable
- future scope remains limited to `public-verification-placeholder`
- public verification remains subordinate to the release-gate contract

This outcome only allows a later mission to draft a public-verification
enablement proposal for this one job.

## Still-Forbidden Actions

Even after `public_verification_stage_candidate_ready`, the following remain
forbidden in this mission:

- enabling `public-verification-placeholder`
- committing live `curl`, `wget`, or equivalent smoke-test commands
- hardcoding public endpoint URLs in workflow source
- mutating ALB, target-group, DNS, or API Gateway state
- mutating `push-image-placeholder`
- mutating `ecs-rollout-placeholder`
- bundling application-code changes into public-verification review

## Canonical Planning Artifact

The non-secret planning artifact for this candidate review is:

- [`.github/public-verification-stage-candidate-review.template.json`](./.github/public-verification-stage-candidate-review.template.json)

That file is a planning artifact only.

It is not a workflow control plane and not an approval token.

## Source Boundary

Source may contain:

- candidate job name
- required evidence list
- blocked/review/ready outcomes
- explicit forbidden actions

Source must not contain:

- live public verification commands
- real public endpoint URLs
- real credentials
- hidden enablement flags

## Governance Rules

- the public-verification candidate review must stay limited to
  `public-verification-placeholder`
- candidate review must remain narrower than any later enablement proposal
- public verification may not advance ahead of immutable image, rollout, ECS
  baseline, and release-gate truth
- public verification remains subordinate to rollback and bounded manual review

## Explicit Non-Goals

This review does not:

- enable the public-verification job
- create live endpoint checks
- create AWS credentials
- create routing infrastructure
- change the Flask endpoint contract

## Paired Artifacts

- [DEANZ_ELITE_OS_ECS_SERVICE_BASELINE_STANDUP_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_BASELINE_STANDUP_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md)
- [`.github/public-verification-stage-candidate-review.template.json`](./.github/public-verification-stage-candidate-review.template.json)
- [DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_ENABLEMENT_PROPOSAL_V1.md](./DEANZ_ELITE_OS_PUBLIC_VERIFICATION_STAGE_ENABLEMENT_PROPOSAL_V1.md)
- [`.github/public-verification-stage-enablement-proposal.template.json`](./.github/public-verification-stage-enablement-proposal.template.json)

## Recommended Next Mission

The next bounded step after this review should be:

- `Public Verification Stage Enablement Proposal v1`

That mission must still remain third-job-only and must not enable live public
checks, widen earlier workflow jobs, or bypass release-gate and rollback
boundaries.
