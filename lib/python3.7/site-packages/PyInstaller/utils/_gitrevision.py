#
# The content of this file will be filled in with meaningful data
# when creating an archive using `git archive` or by downloading an
# archive from github, e.g. from github.com/.../archive/develop.zip
#
rev = "5feb4167cc"     # abbreviated commit hash
commit = "5feb4167cc55c49cd25f408b6d4b253759a735b9"  # commit hash
date = "2020-05-22 12:00:50 +1000"   # commit date
author = "Ievgen Popovych <Jmennius@users.noreply.github.com>"
ref_names = "HEAD -> develop"  # incl. current branch
commit_message = """hooks: importlib_resources: Fix for modern versions (#4889)

Since 1.2.0 importlib_resources uses importlib.metadata to pick up
package version.
Since 1.3.1 there is a hidden import of `importlib_resources.trees`
(using __import__()).

It also looks like this hook used to set `excludedmodules` variable
which is not even a thing as far as I can tell
(likely meant `excludedimports`).

Tested with importlib_resources 1.5.0.

Fixes #4725
Signed-off-by: Ievgen Popovych <ievgenp@seetrue.ai>"""
