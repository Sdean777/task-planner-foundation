# Dean'z Elite OS Protected Deployment Environment & Approval Contract v1

## Purpose

This document defines the first bounded contract for the protected deployment
environment and manual approval posture that must exist before a real
deployment workflow can ever be enabled for `task-planner-foundation`.

It exists to answer these questions before any deploy stages are turned on:

- what is the intended protected environment name?
- which branch may target it?
- which manual approvals are required?
- what must still remain disabled even after environment protection exists?

This document does not:

- create a GitHub environment
- configure environment protection rules
- add live reviewers
- enable deployment jobs
- change the Flask application contract

## Scope

This contract applies to:

- [DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ACTIVATION_GATE_V1.md](./DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ACTIVATION_GATE_V1.md)
- [DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_SKELETON_V1.md](./DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_SKELETON_V1.md)
- [GITHUB_ACTIONS_AWS_FOUNDATION_PLACEHOLDER_PLAN.md](./GITHUB_ACTIONS_AWS_FOUNDATION_PLACEHOLDER_PLAN.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)

It governs only the future protected environment and approval boundary.

## Intended Protected Environment

The first protected environment should be:

- environment name: `production`

This remains a planning default, not an activated GitHub environment.

The first environment posture should be narrow:

- one environment only
- one service only
- one workflow family only
- no shared multi-service deployment target

## Branch-To-Environment Rule

The first protected environment should accept deployment intent only from:

- `refs/heads/main`

Current rule:

- no wildcard branches
- no tag-wide deployment authorization
- no fork-based environment access

## Manual Approval Categories

The first protected environment should require explicit human review across
these categories:

- owner/operator approval
- deployment-boundary approval
- rollback-and-release-gate approval
- service-scope approval

This contract records the categories only. It does not assign live reviewers.

## Intended Reviewer Posture

The first reviewer posture should be narrow:

- at least one named human reviewer later
- no self-approval by the workflow author unless explicitly approved later
- no bypass for routine pushes to `main`

That keeps the first deployment path deliberate.

## Required Preconditions Before Environment Protection Is Meaningful

The environment boundary should remain blocked unless these are already true:

- deployment workflow activation gate exists
- deployment workflow skeleton exists and remains disabled
- OIDC trust boundary exists
- rollout contract exists
- release-gate contract exists
- secrets posture remains clean

Environment protection without those prerequisites would be performative,
not safe.

## Still-Disabled Actions

Even after a protected environment exists, the following may still remain
disabled until a later mission explicitly enables them:

- ECR push job execution
- ECS rollout job execution
- public runtime verification execution
- any live AWS authentication

Creating the environment does not itself authorize deployment behavior.

## Source Boundary

Source may contain:

- intended environment name
- branch-to-environment rule
- approval categories
- placeholder reviewer posture

Source must not contain:

- real reviewer identities that were not explicitly approved for source
- approval tokens
- live environment secrets

## Canonical Planning Artifact

The non-secret planning artifact for this contract is:

- [`.github/protected-deployment-environment.template.json`](./.github/protected-deployment-environment.template.json)

That file is a planning artifact only.

It is not a live GitHub environment configuration and not an approval system.

## Governance Rules

- environment protection must remain downstream of the activation gate
- environment approval must remain narrower than workflow execution
- branch restrictions must remain explicit
- environment creation must not silently enable disabled jobs

## Explicit Non-Goals

This contract does not:

- create GitHub environment protection
- create required reviewers in GitHub
- enable deploy jobs
- enable AWS authentication
- change the Flask endpoint contract

## Paired Artifacts

- [DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ACTIVATION_GATE_V1.md](./DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ACTIVATION_GATE_V1.md)
- [DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_SKELETON_V1.md](./DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_SKELETON_V1.md)
- [`.github/protected-deployment-environment.template.json`](./.github/protected-deployment-environment.template.json)
- [DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ENABLEMENT_REVIEW_CONTRACT_V1.md](./DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ENABLEMENT_REVIEW_CONTRACT_V1.md)
- [`.github/deployment-workflow-enablement-review.template.json`](./.github/deployment-workflow-enablement-review.template.json)

## Follow-On Contract

This protected environment boundary now pairs with the enablement-review boundary:

- [DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ENABLEMENT_REVIEW_CONTRACT_V1.md](./DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_ENABLEMENT_REVIEW_CONTRACT_V1.md)
- [`.github/deployment-workflow-enablement-review.template.json`](./.github/deployment-workflow-enablement-review.template.json)

The next non-deploying AWS step after that should be:

- `Push Image Stage Candidate Review v1`

## Warning

Do not treat this contract as permission to enable deployment jobs.

It only defines the protected environment and approval boundary.
