# Dean'z Elite OS Push Image Stage Live-Enable Proposal v1

## Purpose

This document defines the refreshed bounded proposal for how the
`push-image-placeholder` job could be considered for a later live-enable patch
without advancing any later-stage deployment jobs.

It exists to answer these questions after the first-job placeholder stack and
live-enable candidate review are both complete:

- what is the exact minimal diff shape for a future live-enable attempt?
- what must remain unchanged while that future patch is only being proposed?
- what evidence must be rechecked immediately before any controlled patch
  review is allowed?

This document does not:

- enable the `push-image-placeholder` job
- add AWS authentication
- log in to ECR
- push an image
- change the Flask application contract

## Scope

This proposal applies only to:

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_CANDIDATE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_CANDIDATE_REVIEW_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_COMMAND_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_COMMAND_PLACEHOLDER_PATCH_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)

It governs only the exact proposal shape for the refreshed first-job
live-enable boundary.

## Proposal Objective

The proposal exists to define whether `push-image-placeholder` is:

- `live_enable_proposal_blocked`
- `live_enable_proposal_review_required`
- `live_enable_proposal_ready_for_controlled_patch_review`

This is still not a patch or an enablement action.

## Minimal Diff Shape

The refreshed live-enable proposal for `push-image-placeholder` must remain
narrow.

Allowed proposed diff shape:

1. change only the `push-image-placeholder` job
2. keep `ecs-rollout-placeholder` disabled
3. keep `public-verification-placeholder` disabled
4. keep the workflow trigger as `workflow_dispatch` only
5. keep the workflow service-scoped to `task-planner-foundation`
6. keep workflow-level permissions at `contents: read`

Any proposal that widens beyond that is out of scope.

## Proposed Patch Boundaries

If a later controlled patch-review mission is attempted, the proposal should
allow only:

- re-evaluating the `if: ${{ false }}` gate for `push-image-placeholder`
- a job-local `permissions` block no wider than `contents: read` plus
  `id-token: write`
- a single job-local auth-action step shape already defined by the existing
  placeholder chain
- a single job-local ECR-login command shape already defined by the existing
  placeholder chain
- a single job-local image-push shape subordinate to immutable
  `sha-<git-sha>` rollout identity
- explicit comments preserving later-job disablement

The proposal must not assume:

- ECS rollout changes
- public verification changes
- application-code changes
- workflow-level permission widening

## Commands That Must Remain Proposal-Bound

Even in the proposed future patch shape, these commands remain proposal-only
until a later mission explicitly authorizes them:

- `uses: aws-actions/configure-aws-credentials@v4`
- `aws ecr get-login-password`
- `docker login`
- `docker push`
- any command that mutates AWS state beyond first-job image publication scope

That means this mission may contain only:

- reviewed diff scope
- reviewed command ordering
- reviewed evidence and outcomes

not live state-changing workflow behavior.

## Recheck Evidence Before Any Controlled Patch Review

Immediately before a future controlled patch-review mission is allowed to
start, these must be rechecked:

- live-enable candidate review still allows `push-image-placeholder`
- `app.py` still has no diff
- protected environment posture still matches `production` / `main`
- GitHub OIDC trust boundary still matches repo, branch, audience, and
  environment posture
- immutable tag rule still requires `sha-<git-sha>`
- release-gate posture is still present
- secrets posture is still clean
- later jobs remain disabled
- workflow-level permissions remain `contents: read`

## Proposal Outcomes

### 1. `live_enable_proposal_blocked`

Required when:

- the proposed diff touches more than `push-image-placeholder`
- any later-stage job changes
- workflow-level permissions widen
- live AWS behavior is proposed without preserved boundaries
- secrets posture is unsafe

### 2. `live_enable_proposal_review_required`

Allowed when:

- the diff is narrow enough
- the job remains first in the sequence
- operator review is still required before any controlled patch review

### 3. `live_enable_proposal_ready_for_controlled_patch_review`

Allowed when:

- the proposed diff is limited to the first job
- later jobs remain disabled
- rollout identity remains immutable
- release-gate and trust posture remain intact
- all recheck evidence remains satisfied

This outcome still does not apply a patch.

## Still-Forbidden Actions

Even after `live_enable_proposal_ready_for_controlled_patch_review`, the
following remain forbidden in this mission:

- modifying `ecs-rollout-placeholder`
- modifying `public-verification-placeholder`
- enabling any job
- widening workflow-level permissions
- adding live AWS-mutating behavior to source
- bypassing immutable tag, rollback, or release-gate posture

## Canonical Planning Artifact

The non-secret planning artifact for this proposal is:

- [`.github/push-image-stage-live-enable-proposal.template.json`](./.github/push-image-stage-live-enable-proposal.template.json)

That file is a planning artifact only.

It is not a patch and not a workflow control plane.

## Source Boundary

Source may contain:

- proposed diff scope
- recheck evidence
- blocked/review/proposal-ready outcomes
- explicit forbidden actions

Source must not contain:

- live patch commands that mutate AWS
- credentials
- hidden enablement flags

## Governance Rules

- the live-enable proposal must remain downstream of the live-enable candidate review
- the proposal must remain narrower than actual job enablement
- later jobs must stay blocked
- application code must remain untouched

## Explicit Non-Goals

This contract does not:

- patch the workflow
- enable a job
- create AWS trust
- change the Flask endpoint contract

## Paired Artifacts

- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_CANDIDATE_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_CANDIDATE_REVIEW_V1.md)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_COMMAND_PLACEHOLDER_PATCH_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_ECR_LOGIN_COMMAND_PLACEHOLDER_PATCH_V1.md)
- [`.github/push-image-stage-live-enable-proposal.template.json`](./.github/push-image-stage-live-enable-proposal.template.json)
- [DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_CONTROLLED_PATCH_REVIEW_V1.md](./DEANZ_ELITE_OS_PUSH_IMAGE_STAGE_LIVE_ENABLE_CONTROLLED_PATCH_REVIEW_V1.md)
- [`.github/push-image-stage-live-enable-controlled-patch-review.template.json`](./.github/push-image-stage-live-enable-controlled-patch-review.template.json)

## Recommended Next Mission

The next bounded step after this proposal should be:

- `Push Image Stage Live-Enable Controlled Patch Review v1`

That mission should inspect the exact workflow diff for only the first job and
confirm that it remains within the reviewed trust, rollback, release-gate, and
immutability boundaries before any patch is applied.

## Warning

Do not treat this proposal as permission to patch the workflow.

It only defines the exact narrow shape a later controlled patch-review mission
must obey.
