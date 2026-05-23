# Dean'z Elite OS Push Image Stage GitHub OIDC Auth Shape Review v1

## Purpose

This document defines the first bounded GitHub OIDC auth-shape review for the
`push-image-placeholder` job inside the `task-planner-foundation` deployment
workflow skeleton.

It exists to answer these questions before any auth step is ever introduced:

- where may a future auth step appear?
- what permissions widening is acceptable for that single job?
- which OIDC trust fields must be referenced explicitly?
- what must still remain absent even after the auth shape is reviewed?

This document does not:

- add GitHub OIDC authentication to the workflow
- create AWS trust
- log in to ECR
- push an image
- change the Flask application contract

## Scope

This auth-shape review applies to:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PLACEHOLDER_BOUND_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PLACEHOLDER_BOUND_PATCH_V1.md)
- [DEANZ_ELITE_OS_GITHUB_OIDC_DEPLOYMENT_TRUST_CONTRACT_V1.md](./DEANZ_ELITE_OS_GITHUB_OIDC_DEPLOYMENT_TRUST_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_PROTECTED_DEPLOYMENT_ENVIRONMENT_APPROVAL_CONTRACT_V1.md](./DEANZ_ELITE_OS_PROTECTED_DEPLOYMENT_ENVIRONMENT_APPROVAL_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)

It governs only the exact future auth-step posture for the first disabled job.

## Auth Shape Review Objective

This review exists to decide whether the future auth step remains:

- `auth_shape_blocked`
- `auth_shape_review_required`
- `auth_shape_ready_for_placeholder_auth_patch`

This is still not a workflow patch action.

## Future Auth Step Placement

The only future auth step in scope is a single job-local auth step inside
`push-image-placeholder`.

It may appear only:

- inside `push-image-placeholder`
- before any future ECR login or push command
- after the job-level scope has already been reviewed

It must not appear in:

- `activation-gate-summary`
- `ecs-rollout-placeholder`
- `public-verification-placeholder`
- any other workflow file

## Future Permissions Shape

The future auth posture must remain job-scoped and minimal.

The only reviewed permissions widening allowed for a later patch is:

- `contents: read`
- `id-token: write`

This review does not authorize that change yet.

It only records that no broader permissions shape is acceptable for the first
auth step.

## Future Auth Step Inputs

The reviewed auth shape may reference only:

- a future deploy role assumption target derived from the OIDC trust contract
- an explicit AWS region value from a non-secret parameter source
- a deterministic role session name tied to this repo and job

The reviewed auth shape must not reference:

- `aws-access-key-id`
- `aws-secret-access-key`
- long-lived credentials in GitHub secrets
- wildcard trust subjects
- fork-based trust

## Required Upstream Evidence

Immediately before any future auth-placeholder patch is allowed to start, these
must still be true:

- `app.py` has no diff
- `push-image-placeholder` remains disabled
- the placeholder-bound patch remains intact
- GitHub OIDC deployment trust contract still matches this repo and `main`
- protected environment posture still remains `production` on `refs/heads/main`
- immutable tag posture remains `sha-<git-sha>`
- later jobs remain unchanged and disabled
- secrets posture remains clean

## Auth Shape Constraints

Even if the auth shape becomes review-ready, the following must remain absent:

- live `aws-actions/configure-aws-credentials` usage
- `aws ecr get-login-password`
- `docker login`
- `docker push`
- ECS task-definition registration
- ECS service update commands

The auth shape review must stop before any state-changing command enters source.

## Review Outcomes

### 1. `auth_shape_blocked`

Required when:

- permissions widen beyond `contents: read` and `id-token: write`
- static credentials are proposed
- trust posture no longer remains repo- and branch-bound
- later jobs are touched
- auth shape is bundled with ECR or ECS commands

### 2. `auth_shape_review_required`

Allowed when:

- the future shape is narrow enough
- the job remains disabled
- the future auth posture is still review-only
- operator review is still required before any auth-placeholder patch

### 3. `auth_shape_ready_for_placeholder_auth_patch`

Allowed when:

- the future auth step is confined to `push-image-placeholder`
- permissions shape remains minimal and job-scoped
- OIDC trust references remain explicit
- all upstream evidence still holds

This outcome still does not apply a patch.

## Still-Forbidden Actions

Even after `auth_shape_ready_for_placeholder_auth_patch`, the following remain
forbidden in this mission:

- enabling `push-image-placeholder`
- adding a live auth step
- adding ECR login
- adding image push behavior
- modifying later-stage jobs
- introducing static AWS credentials

## Canonical Planning Artifact

The non-secret planning artifact for this review is:

- [`.github/push-image-stage-github-oidc-auth-shape-review.template.json`](./.github/push-image-stage-github-oidc-auth-shape-review.template.json)

That file is a planning artifact only.

It is not a workflow control plane and not an auth token.

## Source Boundary

Source may contain:

- reviewed future auth-step placement
- reviewed future permission shape
- reviewed OIDC field expectations
- blocked/review/ready outcomes

Source must not contain:

- live auth steps
- credentials
- AWS-mutating commands
- a widened workflow outside the first job

## Governance Rules

- auth-shape review must remain downstream of the placeholder-bound patch
- auth-shape review must remain downstream of the OIDC trust contract
- auth-shape review must remain narrower than an actual auth-placeholder patch
- later jobs must stay blocked
- application code must remain untouched

## Explicit Non-Goals

This contract does not:

- patch the workflow
- enable any job
- create AWS trust
- create deployment automation
- change the Flask endpoint contract

## Paired Artifacts

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PLACEHOLDER_BOUND_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_PLACEHOLDER_BOUND_PATCH_V1.md)
- [DEANZ_ELITE_OS_GITHUB_OIDC_DEPLOYMENT_TRUST_CONTRACT_V1.md](./DEANZ_ELITE_OS_GITHUB_OIDC_DEPLOYMENT_TRUST_CONTRACT_V1.md)
- [`.github/push-image-stage-github-oidc-auth-shape-review.template.json`](./.github/push-image-stage-github-oidc-auth-shape-review.template.json)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_GITHUB_OIDC_AUTH_PLACEHOLDER_PATCH_V1.md)
- [`.github/push-image-stage-github-oidc-auth-placeholder-patch.template.json`](./.github/push-image-stage-github-oidc-auth-placeholder-patch.template.json)

## Recommended Next Mission

The next bounded step after this review should be:

- `Push Image Stage GitHub OIDC Auth Placeholder Patch v1`

That mission should remain disabled and non-deploying while recording the
future auth-step shape directly in the first job without introducing live
registry or deploy behavior.

## Warning

Do not treat this review as permission to add real GitHub OIDC auth.

It only defines the exact future auth posture a later placeholder-auth patch
must obey.
