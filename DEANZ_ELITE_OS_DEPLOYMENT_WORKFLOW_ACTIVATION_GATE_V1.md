# Dean'z Elite OS Deployment Workflow Activation Gate v1

## Purpose

This document defines the first bounded activation gate for introducing a real
AWS deployment workflow into the `task-planner-foundation` repository.

It exists to answer these questions before any workflow is allowed to push an
image or update ECS:

- which planning layers must already be complete?
- which runtime boundaries must already be frozen?
- which manual approvals must already exist?
- what exactly is still forbidden even if the gate is satisfied?

This document does not:

- create a deploy workflow
- push an image
- deploy anything
- add AWS credentials
- change the Flask application contract

## Scope

This gate applies to the existing AWS foundation planning chain:

- [DEANZ_ELITE_OS_ECS_RUNTIME_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECS_RUNTIME_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_RUNBOOK_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_RUNBOOK_V1.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_PARAMETERIZATION_ENVIRONMENT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_PARAMETERIZATION_ENVIRONMENT_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_ECS_SERVICE_IDENTITY_ACCESS_BOUNDARY_V1.md](./DEANZ_ELITE_OS_ECS_SERVICE_IDENTITY_ACCESS_BOUNDARY_V1.md)
- [DEANZ_ELITE_OS_GITHUB_OIDC_DEPLOYMENT_TRUST_CONTRACT_V1.md](./DEANZ_ELITE_OS_GITHUB_OIDC_DEPLOYMENT_TRUST_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md](./DEANZ_ELITE_OS_ECR_IMAGE_PROMOTION_ECS_REVISION_ROLLOUT_CONTRACT_V1.md)
- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md)

It governs only the decision to allow a future deploy workflow mission to
begin.

## Gate Objective

The activation gate decides whether the repo is ready for:

- `workflow_still_blocked`
- `workflow_review_required`
- `workflow_activation_allowed`

This is a planning and governance gate, not a deployment action.

## Required Preconditions

Before a deploy workflow may even be drafted, the following conditions must be
true:

### 1. Foundation Service Contract Preserved

- [app.py](./app.py) remains the foundation Flask service
- existing endpoints remain unchanged
- container port contract remains `8081`

### 2. Verification Bridge Exists

- `.github/workflows/container-build-verify.yml` exists
- the repo already has a non-deploying build/verify bridge

### 3. Runtime Planning Chain Exists

The following artifacts must already exist and remain source of truth:

- ECS runtime contract
- ECS service runbook
- ECS parameter and environment contract
- ECS identity and access boundary
- GitHub OIDC deployment trust contract
- ECR image promotion and ECS rollout contract
- public runtime verification and release-gate contract

### 4. Secrets Posture Is Clean

- no AWS credentials in source
- no OpenAI or model keys in source
- no live deployment secrets in workflows

### 5. Rollback Posture Is Defined

- previous revision rollback rule exists
- immutable image promotion rule exists
- release gate defines rollback-required outcomes

## Manual Approval Requirements

Even if the preconditions are satisfied, a deploy workflow remains blocked
unless these approvals exist outside automation:

- owner/operator approval to introduce deployment automation
- approval that OIDC trust boundaries are acceptable
- approval that release-gate and rollback posture are understood
- approval that live deployment is still scoped to this single foundation service

This mission records the need for those approvals. It does not create them.

## Activation Outcomes

### 1. `workflow_still_blocked`

Required when:

- any planning precondition is missing
- secrets posture is unsafe
- rollback posture is incomplete
- branch/repository trust remains undefined

### 2. `workflow_review_required`

Allowed when:

- planning chain exists
- preconditions are mostly satisfied
- manual approval evidence is still incomplete

### 3. `workflow_activation_allowed`

Allowed when:

- all planning contracts exist
- secrets posture is clean
- rollback and release-gate posture are explicit
- manual approval path is defined
- the intended workflow remains narrow and service-scoped

This outcome only allows the next mission to draft a workflow skeleton. It does
not authorize live deployment.

## Still-Forbidden Actions

Even with `workflow_activation_allowed`, the following remain out of scope for
this mission:

- committing AWS credentials
- creating live OIDC trust
- pushing to ECR
- updating ECS
- bypassing release-gate verification
- widening deployment to other services

## Canonical Planning Artifact

The non-secret planning artifact for this gate is:

- [aws/deployment-workflow-activation-gate.template.json](./aws/deployment-workflow-activation-gate.template.json)

That file is a planning artifact only.

It is not a workflow, not an approval system, and not a deploy manifest.

## Source Boundary

Source may contain:

- gate preconditions
- gate outcomes
- approval categories
- placeholder readiness flags

Source must not contain:

- real approval tokens
- production credentials
- live deploy commands in this mission

## Governance Rules

- workflow activation must remain downstream of all planning contracts
- workflow activation must remain narrower than deployment execution
- manual approval requirements must be explicit before automation is introduced
- the first workflow must remain service-scoped and reversible

## Explicit Non-Goals

This gate does not:

- create a workflow file
- create GitHub environment protection rules
- create AWS trust
- create AWS deploy roles
- change the Flask endpoint contract

## Paired Artifacts

- [DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md](./DEANZ_ELITE_OS_PUBLIC_RUNTIME_VERIFICATION_RELEASE_GATE_CONTRACT_V1.md)
- [GITHUB_ACTIONS_AWS_FOUNDATION_PLACEHOLDER_PLAN.md](./GITHUB_ACTIONS_AWS_FOUNDATION_PLACEHOLDER_PLAN.md)
- [aws/deployment-workflow-activation-gate.template.json](./aws/deployment-workflow-activation-gate.template.json)
- [DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_SKELETON_V1.md](./DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_SKELETON_V1.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)

## Follow-On Skeleton

This activation gate now pairs with the disabled workflow skeleton:

- [DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_SKELETON_V1.md](./DEANZ_ELITE_OS_DEPLOYMENT_WORKFLOW_SKELETON_V1.md)
- [`.github/workflows/deploy-foundation-skeleton.yml`](./.github/workflows/deploy-foundation-skeleton.yml)

The next non-deploying AWS step after that should be:

- `Protected Deployment Environment & Approval Contract v1`

## Warning

Do not treat this gate as permission to start live deployment.

It only governs whether a future workflow skeleton may be introduced.
