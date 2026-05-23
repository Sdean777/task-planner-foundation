# Dean'z Elite OS Push Image Stage Live-Enable Candidate Review v1

## Purpose

This document defines the refreshed bounded live-enable candidate review for
the `push-image-placeholder` job inside the `task-planner-foundation`
deployment workflow skeleton.

It exists to answer these questions after the full first-job placeholder chain
is visible in source:

- is the first disabled job now constitutionally reviewable for a later
  live-enable proposal?
- what exact evidence must remain intact before any enablement discussion
  reopens?
- what still remains forbidden even if the job becomes live-enable-ready?

This document does not:

- enable `push-image-placeholder`
- add AWS authentication
- log in to ECR
- push an image
- widen workflow permissions
- change the Flask application contract

## Scope

This live-enable candidate review applies to:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_COMMAND_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_COMMAND_PLACEHOLDER_PATCH_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_OIDC_AUTH_ACTION_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_OIDC_AUTH_ACTION_PLACEHOLDER_PATCH_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PUSH_JOB_PERMISSION_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PUSH_JOB_PERMISSION_PLACEHOLDER_PATCH_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)

It governs only the refreshed first-job live-enable review boundary.

## Candidate Job

The only job in scope for this mission is:

- `push-image-placeholder`

All later-stage jobs remain outside scope:

- `ecs-rollout-placeholder`
- `public-verification-placeholder`

## Candidate Review Objective

This review exists to decide whether `push-image-placeholder` remains:

- `live_enable_blocked`
- `live_enable_review_required`
- `live_enable_candidate_ready`

This is still not a job-enable action.

## Required Evidence

Before `push-image-placeholder` may be considered a fresh live-enable
candidate, the following must already exist and remain intact:

### 1. Foundation Preservation

- [app.py](./app.py) remains unchanged
- the current Flask endpoint contract remains intact
- the container build verification workflow still exists

### 2. Workflow Boundary Preservation

- deployment workflow skeleton still exists
- `push-image-placeholder` still has `if: ${{ false }}`
- workflow-level permissions still remain `contents: read`
- `ecs-rollout-placeholder` remains disabled
- `public-verification-placeholder` remains disabled

### 3. First-Job Placeholder Chain Completion

- placeholder-bound patch remains intact
- GitHub OIDC auth placeholder patch remains intact
- ECR-login placeholder patch remains intact
- image-push placeholder patch remains intact
- push-job permission placeholder patch remains intact
- OIDC auth-action placeholder patch remains intact
- ECR-login command placeholder patch remains intact

### 4. Governance And Trust Boundaries

- protected deployment environment contract exists
- GitHub OIDC trust contract exists
- immutable image rollout contract still requires `sha-<git-sha>`
- public runtime verification and release-gate contract exists

### 5. Secrets And Source Hygiene

- no AWS credentials in source
- no OpenAI or model keys in source
- no live `uses: aws-actions/configure-aws-credentials@v4` in the workflow
- no live `aws ecr get-login-password` in the workflow
- no live `docker login` or `docker push` in the workflow

## Candidate Constraints

Even if the first job becomes a live-enable candidate, the following must
still remain true in this mission:

- the job stays disabled
- no AWS authentication is added
- no ECR login commands are introduced
- no image-push commands are introduced
- no later-stage job may advance
- no workflow-level permission widening is allowed

## Review Outcomes

### 1. `live_enable_blocked`

Required when:

- any required evidence is missing
- secrets posture is unsafe
- any live auth, login, or push behavior is proposed too early
- later-stage jobs are touched
- immutable image, rollback, or release-gate posture has drifted

### 2. `live_enable_review_required`

Allowed when:

- prerequisite evidence exists
- the job is still disabled
- the first-job placeholder chain is visible and bounded
- operator review is still required before any future live-enable proposal

### 3. `live_enable_candidate_ready`

Allowed when:

- all required evidence exists
- the job remains disabled
- the full first-job placeholder chain is intact
- the future scope remains limited to `push-image-placeholder`
- later jobs remain blocked

This outcome only allows a later mission to draft a refreshed live-enable
proposal for this one job.

## Still-Forbidden Actions

Even after `live_enable_candidate_ready`, the following remain forbidden in
this mission:

- enabling `push-image-placeholder`
- adding `aws-actions/configure-aws-credentials@v4`
- invoking `aws ecr get-login-password`
- invoking `docker login`
- invoking `docker push`
- enabling `ecs-rollout-placeholder`
- enabling `public-verification-placeholder`

## Canonical Planning Artifact

The non-secret planning artifact for this candidate review is:

- [`.github/push-image-stage-live-enable-candidate-review.template.json`](./.github/push-image-stage-live-enable-candidate-review.template.json)

That file is a planning artifact only.

It is not a workflow control plane and not an approval token.

## Source Boundary

Source may contain:

- candidate job name
- required evidence list
- blocked/review/ready outcomes
- explicit forbidden actions

Source must not contain:

- live approval tokens
- real credentials
- hidden enablement flags

## Governance Rules

- the refreshed live-enable candidate review must stay limited to `push-image-placeholder`
- candidate review must remain narrower than any future enablement proposal
- no later-stage job may advance ahead of this refreshed first-job review
- auth, login, and image-push posture remain subordinate to immutable tag, rollback, and release-gate rules

## Explicit Non-Goals

This contract does not:

- enable the push-image job
- create AWS trust
- create AWS credentials
- change the Flask endpoint contract

## Paired Artifacts

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_COMMAND_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_COMMAND_PLACEHOLDER_PATCH_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md)
- [`.github/push-image-stage-live-enable-candidate-review.template.json`](./.github/push-image-stage-live-enable-candidate-review.template.json)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_PROPOSAL_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_PROPOSAL_V1.md)
- [`.github/push-image-stage-live-enable-proposal.template.json`](./.github/push-image-stage-live-enable-proposal.template.json)

## Recommended Next Mission

The next bounded step after this review should be:

- `Push Image Stage Live-Enable Proposal v1`

That mission must still remain first-job-only and must not enable later jobs
or bypass the existing trust, rollback, and release-gate boundaries.

## Warning

Do not treat this review as permission to enable the push-image job.

It only determines whether the now-complete first-job placeholder stack is
stable enough for a later live-enable proposal.
