# Distribution

This document describes how to build TexTools as a Blender extension zip and how the same process should run automatically from GitHub Actions when publishing a distribution release.

TexTools is packaged from the repository root. The root contains the extension manifest, `blender_manifest.toml`, and the registration entry point, `__init__.py`. Do not zip a parent folder by hand; use Blender's extension build command so the package layout and manifest are validated consistently.

## Release Inputs

Before building a distribution, check the release metadata and package contents.

- Update `version` in `blender_manifest.toml`.
- Confirm `blender_version_min` is correct for the release.
- Confirm the extension ID remains `textools` unless this is an intentional package identity change.
- Confirm bundled assets under `assets/` and bundled Python code under `vendor/` are needed and distributable.
- Run the operator/manual consistency checks used by the current development pass when operator documentation changes.
- Keep generated folders such as `dist/`, `__pycache__/`, and local Blender cache data out of the package.

## Local Build

From the repository root, validate the extension first:

```powershell
blender --command extension validate .
```

If Blender is not on `PATH`, call the installed executable directly:

```powershell
& "C:\Program Files\Blender Foundation\Blender 5.1\blender.exe" --command extension validate .
```

Build the extension zip into `dist/`:

```powershell
blender --command extension build --source-dir . --output-dir dist
```

By default, Blender names the zip from the manifest ID and version:

```text
dist/textools-<version>.zip
```

For an explicit output path, use:

```powershell
blender --command extension build --source-dir . --output-filepath dist/textools-1.6.2.zip
```

Use the manifest version in the filename. The explicit form is useful for release automation, but the default form is less error-prone during local builds.

## Local Verification

After building, install the zip into Blender 5 from disk.

1. Open Blender 5.
2. Go to **Edit > Preferences > Extensions**.
3. Remove any older TexTools installation.
4. Choose **Install from Disk** and select the zip from `dist/`.
5. Enable TexTools.
6. Open the UV Editor and confirm the TexTools sidebar appears.

For a quick command-line smoke test, import and register the extension in a Blender background session. The smoke test should verify that all documented `uv.textools_*` operators resolve after `register()` and then call `unregister()` before Blender exits.

## Release Checklist

Use this checklist before tagging a release.

- `blender_manifest.toml` has the release version.
- `README.md` and docs mention the correct supported Blender version.
- `docs/manual.md` matches the active operator list.
- `blender --command extension validate .` passes.
- `blender --command extension build --source-dir . --output-dir dist` creates one zip.
- The zip installs cleanly in Blender 5.
- Representative UV, texture, Color ID, mesh texture, and bake workflows have been smoke-tested.
- The git tag matches the manifest version, for example `v1.6.2` for `version = "1.6.2"`.

## GitHub Actions Release Flow

The repository should use GitHub Actions to build the extension zip and create a GitHub Release automatically. The workflow should live under `.github/workflows/`, typically as `.github/workflows/release.yml`.

Recommended trigger:

- `push` tags matching `v*`, such as `v1.6.2`.
- `workflow_dispatch` for manual release rebuilds.

Recommended job behavior:

1. Check out the repository.
2. Install or locate Blender 5 on the runner.
3. Validate the extension with `blender --command extension validate .`.
4. Build the zip with `blender --command extension build --source-dir . --output-dir dist`.
5. Upload the zip as a workflow artifact.
6. Create or update the GitHub Release for the tag.
7. Attach the generated zip to the Release.

Example workflow outline:

```yaml
name: Build Extension Release

on:
  push:
    tags:
      - "v*"
  workflow_dispatch:

permissions:
  contents: write

jobs:
  build-release:
    runs-on: windows-latest

    steps:
      - name: Check out repository
        uses: actions/checkout@v4

      - name: Install Blender 5
        # Use the project's chosen Blender setup action or a cached portable Blender install.
        # The runner must expose a `blender` command compatible with Blender's extension CLI.
        run: |
          echo "Install Blender 5 here"

      - name: Validate extension
        run: blender --command extension validate .

      - name: Build extension zip
        run: blender --command extension build --source-dir . --output-dir dist

      - name: Find package
        id: package
        shell: pwsh
        run: |
          $zip = Get-ChildItem dist -Filter "*.zip" | Select-Object -First 1
          if (-not $zip) { throw "No extension zip was created." }
          "path=$($zip.FullName)" >> $env:GITHUB_OUTPUT
          "name=$($zip.Name)" >> $env:GITHUB_OUTPUT

      - name: Upload package artifact
        uses: actions/upload-artifact@v4
        with:
          name: ${{ steps.package.outputs.name }}
          path: ${{ steps.package.outputs.path }}

      - name: Publish GitHub Release
        uses: softprops/action-gh-release@v2
        with:
          files: ${{ steps.package.outputs.path }}
          generate_release_notes: true
```

Replace the placeholder Blender installation step with the setup action used by the project. The important contract is that the workflow runs the same validation and build commands as the local process.

## Tagging And Publishing

For a normal release:

```powershell
git tag v1.6.2
git push origin v1.6.2
```

After the tag is pushed, GitHub Actions should build the zip and attach it to the GitHub Release. The Release asset is the distribution file users install through Blender's **Install from Disk** flow.

If a release build fails, delete or replace the failed Release asset only after fixing the source issue and rerunning the workflow. Do not hand-edit the zip contents after Blender builds them; fix the repository and rebuild.

## Expected Release Asset

Each release should publish one Blender extension zip built from the manifest. For version `1.6.2`, the default asset name is:

```text
textools-1.6.2.zip
```

The zip should contain the extension root files and folders needed by Blender, including `blender_manifest.toml`, `__init__.py`, `settings.py`, `operators/`, `utilities/`, `assets/`, `vendor/`, `LICENSE.txt`, and docs. The package should not contain `.git/`, local build outputs, or editor-specific workspace files.