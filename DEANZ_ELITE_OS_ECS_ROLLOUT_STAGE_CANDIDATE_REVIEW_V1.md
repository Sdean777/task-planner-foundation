# Dean'z Elite OS ECS Rollout Stage Candidate Review v1

## Purpose

This document defines the first bounded candidate review for the
`ecs-rollout-placeholder` job inside the `task-planner-foundation`
deployment workflow skeleton.

It exists to answer these questions after the first bounded ECR image
publication run completed:

- is the second disabled workflow job now reviewable for a later rollout-stage
  enablement proposal?
- what exact evidence must remain intact before any ECS mutation discussion
  reopens?
- what actions remain blocked even if the rollout stage becomes a candidate?

This document does not:

- enable `ecs-rollout-placeholder`
- register an ECS task definition
- update an ECS service
- enable `public-verification-placeholder`
- change the Flask application contract

## Scope

This rollout-stage candidate review applies to:

- [DEANZ_ELITE_OS_FIRST_BOUNDED_ECR_IMAGE_PUBLICATION_RUN_V1.md](./DEANZ_ELITE_OS_FIRST_BOUNDED_ECR_IMAGE_PUBLICATION_RUN_V1.md)
- [DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_ECS_RUNTIME_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECS_RUNTIME_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_RUNBOOK_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_RUNBOOK_V1.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_PARAMETERIZATION_ENVIRONMENT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_PARAMETERIZATION_ENVIRONMENT_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_IDENTITY_ACCESS_BOUNDARY_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_IDENTITY_ACCESS_BOUNDARY_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)

It governs only the second-job rollout-stage review boundary.

## Candidate Job

The only workflow job in scope for this mission is:

- `ecs-rollout-placeholder`

All other jobs remain outside scope:

- `push-image-placeholder`
- `public-verification-placeholder`

## Candidate Review Objective

This review exists to decide whether `ecs-rollout-placeholder` currently
remains:

- `rollout_stage_blocked`
- `rollout_stage_review_required`
- `rollout_stage_candidate_ready`

This is still not a rollout-enable action.

## Required Evidence

Before `ecs-rollout-placeholder` may be considered a bounded candidate for a
later enablement proposal, the following must already exist and remain intact.

### 1. Foundation Preservation

- [app.py](./app.py) remains unchanged
- the current Flask endpoint contract remains intact
- the container build verification workflow still exists

### 2. Image Publication Truth

- the first bounded ECR image publication run completed
- the immutable tag
  `sha-dfc958a333b792f82c3feaaa4f543d323450938f` is published
- the `main` mirror resolves to the same digest
- immutable SHA image truth remains authoritative for rollout input

### 3. Workflow Boundary Preservation

- deployment workflow skeleton still exists
- `push-image-placeholder` remains the only live-capable job
- `ecs-rollout-placeholder` still has `if: ${{ false }}`
- `public-verification-placeholder` still has `if: ${{ false }}`
- workflow-level permissions remain `contents: read`

### 4. Rollout Governance Chain

- ECS runtime contract exists
- ECS service runbook exists
- ECS service parameterization contract exists
- ECS identity and access boundary exists
- GitHub OIDC trust contract exists
- ECR image promotion and ECS rollout contract exists
- public runtime release-gate contract exists

### 5. Source Hygiene

- no AWS credentials in source
- no OpenAI or model keys in source
- no live `aws ecs register-task-definition` command in the workflow
- no live `aws ecs update-service` command in the workflow
- no live public verification commands in the workflow

## Candidate Constraints

Even if the rollout stage becomes a candidate, the following must remain true
in this mission:

- `ecs-rollout-placeholder` stays disabled
- no task-definition registration is introduced
- no ECS service update is introduced
- no public verification stage may advance
- no application code change may be bundled into rollout review
- immutable SHA image truth must remain the only approved rollout image input

## Review Outcomes

### 1. `rollout_stage_blocked`

Required when:

- required evidence is missing
- immutable image truth is not present
- ECS mutation behavior is proposed too early
- public verification is advanced prematurely
- app changes are bundled into the same rollout discussion

### 2. `rollout_stage_review_required`

Allowed when:

- prerequisite evidence exists
- the job is still disabled
- the image publication run completed
- operator review is still required before any rollout-stage proposal reopens

### 3. `rollout_stage_candidate_ready`

Allowed when:

- all required evidence exists
- `ecs-rollout-placeholder` remains disabled
- the bounded image publication run is complete and verifiable
- rollout truth remains bound to immutable SHA image identity
- `public-verification-placeholder` remains blocked

This outcome only allows a later mission to draft a rollout-stage enablement
proposal for this one job.

## Still-Forbidden Actions

Even after `rollout_stage_candidate_ready`, the following remain forbidden in
this mission:

- enabling `ecs-rollout-placeholder`
- invoking `aws ecs register-task-definition`
- invoking `aws ecs update-service`
- enabling `public-verification-placeholder`
- using `main` as rollout truth without immutable SHA linkage
- bundling application-code changes into rollout review

## Canonical Planning Artifact

The non-secret planning artifact for this candidate review is:

- [`.github/ecs-rollout-stage-candidate-review.template.json`](./.github/ecs-rollout-stage-candidate-review.template.json)

That file is a planning artifact only.

It is not a workflow control plane and not an approval token.

## Source Boundary

Source may contain:

- candidate job name
- required evidence list
- blocked/review/ready outcomes
- explicit forbidden actions

Source must not contain:

- live task-definition registration
- live ECS service updates
- real credentials
- hidden enablement flags

## Governance Rules

- the rollout-stage candidate review must stay limited to `ecs-rollout-placeholder`
- rollout-stage review must remain narrower than any later enablement proposal
- `public-verification-placeholder` may not advance ahead of rollout-stage review
- rollout identity must remain subordinate to immutable image truth and rollback posture

## Explicit Non-Goals

This review does not:

- enable the rollout job
- create AWS credentials
- create live ECS mutation behavior
- change the Flask endpoint contract

## Paired Artifacts

- [DEANZ_ELITE_OS_FIRST_BOUNDED_ECR_IMAGE_PUBLICATION_RUN_V1.md](./DEANZ_ELITE_OS_FIRST_BOUNDED_ECR_IMAGE_PUBLICATION_RUN_V1.md)
- [DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md)
- [`.github/ecs-rollout-stage-candidate-review.template.json`](./.github/ecs-rollout-stage-candidate-review.template.json)
- [DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_ENABLEMENT_PROPOSAL_V1.md](./DEANZ_ELITE_OS_ECS_ROLLOUT_STAGE_ENABLEMENT_PROPOSAL_V1.md)
- [`.github/ecs-rollout-stage-enablement-proposal.template.json`](./.github/ecs-rollout-stage-enablement-proposal.template.json)

## Recommended Next Mission

The next bounded step after this review should be:

- `ECS Rollout Stage Enablement Proposal v1`

That mission must stay second-job-only, preserve immutable SHA rollout truth,
and keep `public-verification-placeholder` disabled.

## Warning

Do not treat successful image publication as permission to mutate ECS.

Rollout review is now in scope, but live task-definition registration and ECS
service update behavior remain blocked.
