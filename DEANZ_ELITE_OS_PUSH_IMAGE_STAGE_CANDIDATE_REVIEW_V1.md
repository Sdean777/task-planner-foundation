# Dean'z Elite OS Push Image Stage Candidate Review v1

## Purpose

This document defines the first bounded candidate review for the
`push-image-placeholder` job inside the `task-planner-foundation` deployment
workflow skeleton.

It exists to answer these questions before that job can even be proposed for
enablement:

- does the repo have enough bounded evidence to review the push-image stage?
- what exactly must already exist before the job is considered reviewable?
- what remains forbidden even if the stage becomes a candidate?

This document does not:

- enable the `push-image-placeholder` job
- add AWS authentication
- push an image to ECR
- change the Flask application contract

## Scope

This candidate review applies to:

- [DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ENABLEMENT_REVIEW_CONTRACT_V1.md](./DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ENABLEMENT_REVIEW_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_SKELETON_V1.md](./DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_SKELETON_V1.md)
- [DEANZ_ELITE_OS_PROTECTED_DEPLOYMENT_ENVIRONMENT_APPROVAL_CONTRACT_V1.md](./DEANZ_ELITE_OS_PROTECTED_DEPLOYMENT_ENVIRONMENT_APPROVAL_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_GITHUB_OIDC_DEPLOYMENT_TRUST_CONTRACT_V1.md](./DEANZ_ELITE_OS_GITHUB_OIDC_DEPLOYMENT_TRUST_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)

It governs only the first disabled job review boundary.

## Candidate Job

The only job in scope for this mission is:

- `push-image-placeholder`

All later-stage jobs remain outside scope:

- `ecs-rollout-placeholder`
- `public-verification-placeholder`

## Candidate Review Objective

This review exists to decide whether `push-image-placeholder` remains:

- `push_image_candidate_blocked`
- `push_image_candidate_review_required`
- `push_image_candidate_allowed_for_enablement_proposal`

This is still not a job-enable action.

## Required Evidence

Before `push-image-placeholder` may be considered a candidate, the following
must already exist:

### 1. Foundation Preservation

- [app.py](./app.py) remains unchanged
- existing endpoint contract remains intact
- container build verification workflow still exists

### 2. Workflow Governance Chain

- deployment workflow activation gate exists
- deployment workflow skeleton exists and remains disabled
- protected deployment environment contract exists
- deployment workflow enablement review contract exists

### 3. AWS Trust And Promotion Boundaries

- GitHub OIDC deployment trust contract exists
- ECR image promotion and ECS rollout contract exists
- immutable image tagging rule remains `sha-<git-sha>`

### 4. Secrets And Source Hygiene

- no AWS credentials in source
- no OpenAI or model keys in source
- no live deploy commands inserted into the job

## Candidate Constraints

Even if the stage becomes a candidate, the following must remain true:

- the job stays disabled in this mission
- no AWS authentication is added
- no ECR push commands are introduced
- no mutable-tag-only promotion path is allowed
- no other disabled job may be reviewed as part of this mission

## Review Outcomes

### 1. `push_image_candidate_blocked`

Required when:

- any required evidence is missing
- secrets posture is unsafe
- the workflow no longer remains service-scoped
- mutable tag or shortcut-based promotion is proposed

### 2. `push_image_candidate_review_required`

Allowed when:

- prerequisite evidence exists
- the stage is still disabled
- operator review is still required before any enablement proposal

### 3. `push_image_candidate_allowed_for_enablement_proposal`

Allowed when:

- all required evidence exists
- the stage remains disabled
- the proposed scope remains limited to image-push behavior only
- later jobs remain blocked

This outcome only allows a later mission to draft an enablement proposal for
this one job.

## Still-Forbidden Actions

Even after `push_image_candidate_allowed_for_enablement_proposal`, the
following remain forbidden in this mission:

- enabling `push-image-placeholder`
- adding `aws-actions/configure-aws-credentials`
- logging into ECR
- pushing any image
- enabling `ecs-rollout-placeholder`
- enabling `public-verification-placeholder`

## Canonical Planning Artifact

The non-secret planning artifact for this candidate review is:

- [`.github/push-image-stage-candidate-review.template.json`](./.github/push-image-stage-candidate-review.template.json)

That file is a planning artifact only.

It is not a workflow control plane and not an approval token.

## Source Boundary

Source may contain:

- candidate job name
- required evidence list
- blocked/review/candidate outcomes
- explicit forbidden actions

Source must not contain:

- live approval tokens
- real credentials
- hidden enablement flags

## Governance Rules

- the first candidate review must stay limited to `push-image-placeholder`
- candidate review must remain narrower than job enablement
- no later-stage job may advance ahead of this first candidate review
- image-push posture must remain subordinate to immutable tag and rollback rules

## Explicit Non-Goals

This contract does not:

- enable the push-image job
- create AWS trust
- create AWS credentials
- change the Flask endpoint contract

## Paired Artifacts

- [DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ENABLEMENT_REVIEW_CONTRACT_V1.md](./DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ENABLEMENT_REVIEW_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md)
- [`.github/push-image-stage-candidate-review.template.json`](./.github/push-image-stage-candidate-review.template.json)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ENABLEMENT_PROPOSAL_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ENABLEMENT_PROPOSAL_V1.md)
- [`.github/push-image-stage-enablement-proposal.template.json`](./.github/push-image-stage-enablement-proposal.template.json)

## Follow-On Proposal

This candidate review now pairs with the first single-job enablement proposal:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ENABLEMENT_PROPOSAL_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ENABLEMENT_PROPOSAL_V1.md)
- [`.github/push-image-stage-enablement-proposal.template.json`](./.github/push-image-stage-enablement-proposal.template.json)

The next bounded step after that should be:

- `Push Image Stage Controlled Patch Review v1`

## Warning

Do not treat this review as permission to enable the push-image job.

It only determines whether that single job is ready for a later enablement
proposal.
