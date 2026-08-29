# V5.1 infrastructure contracts

These files are protected course infrastructure:

- `importer-policy.json` is the one shared public-tree and ZIP policy used by the validator, deterministic packager, and phone importer.
- `site-manifest.schema.json` is the closed V5.1 public manifest contract. Unknown fields are rejected.
- `starter-tree.sha256` allows starter-mode CI only for the byte-exact reviewed neutral shell.
- `form-environment.template.txt` lists form and Turnstile variables without containing a credential.
- `infrastructure-version.json` identifies the infrastructure, workflow, manifest, policy, and business-assets contract versions.
- `ACTIVATION_REHEARSAL.md` covers account-dependent checks that local tests cannot prove.

Do not weaken a file, media, CSP, approval, privacy, or size rule to make one student package pass. Fix the public output, optimize the asset, or move approved heavy media to a proper delivery host.

The GitHub workflows pin official actions to full release commit SHAs verified for V5.1. Treat dependency update pull requests as infrastructure changes: review the upstream release, rerun local tests, and repeat the activation rehearsal before merging.
