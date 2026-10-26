# O2 component compute profile for POWDER

A minimal compute allocation for operator-managed O2 component assessments.

## Resources

- One Emulab d430.
- Standard Ubuntu 22.04 image: `emulab-ops/UBUNTU22-64-STD`.
- No radios, spectrum, experiment-network links, shared VLANs or extra public IPs.

## Use

Import `https://github.com/fkerem/fors-o2-component-r1.git` as a repository-backed
POWDER profile and select tag `profile-r1`. The root `profile.py` describes the
allocation. Record the resolved commit shown by the portal before proceeding.

Wait until the node is ready and POWDER's repository-checkout startup service
shows **Finished**. The checkout places this minimal repository in
`/local/repository`. This profile installs no O2 application and starts no tests.
Application setup and any assessment are separate operator actions.

See the [POWDER profile documentation](https://docs.powderwireless.net/creating-profiles.html)
for repository import and experiment creation.
